"""Export one study week's Notion source into a short-lived Actions artifact."""
import hashlib, json, os, re, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path
ROOT = '3c4917c0e64080a3b421ef822477e0cd'
WEEK = int(os.environ.get('STUDY_WEEK_NUMBER', '13'))
OUT = Path('notion-week-export')
TOKEN = os.environ['NOTION_API_KEY']
CACHE, RECORDS = {}, {}
def compact(s): return str(s).replace('-', '')
def req(method, path, body=None):
    for attempt in range(5):
        time.sleep(.36)
        r = urllib.request.Request('https://api.notion.com/v1' + path,
            data=json.dumps(body).encode() if body is not None else None,
            headers={'Authorization':'Bearer '+TOKEN,'Notion-Version':'2025-09-03','Content-Type':'application/json'}, method=method)
        try:
            with urllib.request.urlopen(r, timeout=60) as response: return json.load(response)
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(min(20, 2**attempt+1)); continue
            raise RuntimeError(f'Notion {method} {path.split("?")[0]}: HTTP {e.code}') from None
    raise RuntimeError('Notion retry limit')
def get(kind, identity):
    key = kind, compact(identity)
    if key not in CACHE: CACHE[key] = req('GET', f'/{kind}/{identity}')
    return CACHE[key]
def paged(path, body=None):
    cursor = None
    while True:
        query = dict(body or {}, page_size=100)
        if cursor: query['start_cursor'] = cursor
        result = req('POST', path, query) if body is not None else req('GET', path+'?'+urllib.parse.urlencode(query))
        yield from result.get('results', [])
        cursor = result.get('next_cursor')
        if not result.get('has_more'): break
def rich(items): return ''.join(x.get('plain_text',x.get('text',{}).get('content','')) for x in items)
def title(page):
    for p in page.get('properties',{}).values():
        if p.get('type') == 'title': return rich(p.get('title',[]))
    return rich(page.get('title',[])) or 'Untitled'
def under_study(item):
    for _ in range(16):
        if compact(item.get('id','')) == ROOT: return True
        p = item.get('parent',{}); k = p.get('type')
        endpoint = {'page_id':'pages','database_id':'databases','data_source_id':'data_sources','block_id':'blocks'}.get(k)
        if not endpoint: return False
        if compact(p[k]) == ROOT: return True
        item = get(endpoint,p[k])
    return False
def props(page):
    out = {}
    for name,p in page.get('properties',{}).items():
        k = p.get('type'); v = p.get(k)
        if k in ('title','rich_text'): out[name] = rich(v or [])
        elif k in ('select','status'): out[name] = (v or {}).get('name')
        elif k in ('people','multi_select'): out[name] = [x.get('name','') for x in v or []]
        elif k in ('date','number','checkbox'): out[name] = v
    return out
def safe(s): return re.sub(r'[<>:"/\\|?*\x00-\x1f]','_',s).strip(' .')[:150] or 'attachment'
def download(file,rec,source):
    url = file.get(file.get('type'),{}).get('url','')
    parsed = urllib.parse.urlparse(url); host = (parsed.hostname or '').lower()
    if parsed.scheme != 'https' or not host.endswith(('.notion.so','.notion.com','.amazonaws.com','.notion-static.com')):
        rec['external_files'].append({'name':file.get('name',''),'url':url,'source':source}); return None
    name = safe(file.get('name') or urllib.parse.unquote(Path(parsed.path).name))
    folder = OUT/compact(rec['id']); folder.mkdir(parents=True,exist_ok=True)
    target = folder/name
    if target.exists(): target = folder/(safe(source[-12:])+'_'+name)
    digest = hashlib.sha256(); size = 0
    try:
        r = urllib.request.Request(url,headers={'User-Agent':'study-assignment-export'})
        with urllib.request.urlopen(r,timeout=90) as response, target.open('wb') as out:
            while chunk := response.read(1024*1024):
                size += len(chunk)
                if size > 95*1024*1024: raise RuntimeError('Attachment too large')
                digest.update(chunk); out.write(chunk)
    except Exception as e:
        target.unlink(missing_ok=True)
        raise RuntimeError(f'Attachment failed: {name} ({type(e).__name__})') from None
    item = dict(name=name,path=target.relative_to(OUT).as_posix(),bytes=size,sha256=digest.hexdigest(),source=source)
    rec['files'].append(item); return item
def database(identity,parent):
    for source in get('databases',identity).get('data_sources',[]):
        for page in paged(f'/data_sources/{source["id"]}/query',{}):
            if not page.get('archived') and not page.get('in_trash'): export(page,parent)
def blocks(identity,rec,depth=0):
    if depth > 12: raise RuntimeError('Unexpected nesting depth')
    lines = []
    for b in paged(f'/blocks/{identity}/children'):
        k = b['type']; d = b.get(k,{}); text = rich(d.get('rich_text',[]))
        if k == 'child_page':
            export(get('pages',b['id']),rec['id']); lines.append('[하위 페이지: '+d.get('title','')+']')
        elif k == 'child_database':
            database(b['id'],rec['id']); lines.append('[과제 데이터베이스: '+d.get('title','')+']')
        elif k in ('file','pdf','image','audio','video'):
            item = download(d,rec,b['id'])
            if item: lines.append(f'[{item["name"]}]({item["path"]})')
            if d.get('caption'): lines.append(rich(d['caption']))
        elif k == 'table_row': lines.append('| '+' | '.join(rich(c) for c in d.get('cells',[]))+' |')
        elif k == 'code': lines.append(chr(96)*3+d.get('language','')+'\n'+text+'\n'+chr(96)*3)
        elif k == 'equation': lines.append('$$'+d.get('expression','')+'$$')
        elif k in ('bookmark','embed','link_preview'): lines.append(d.get('url',''))
        elif text:
            prefix = {'heading_1':'# ','heading_2':'## ','heading_3':'### ','bulleted_list_item':'- ','numbered_list_item':'1. ','quote':'> '}.get(k,'')
            lines.append(prefix+text)
        if b.get('has_children') and k not in ('child_page','child_database'): lines.extend(blocks(b['id'],rec,depth+1))
    return lines
def export(page,parent=None):
    identity = compact(page['id'])
    if identity in RECORDS: return
    rec = dict(id=page['id'],title=title(page),url=page.get('url'),last_edited_time=page.get('last_edited_time'),parent_id=parent,properties=props(page),files=[],external_files=[])
    RECORDS[identity] = rec
    for name,p in page.get('properties',{}).items():
        if p.get('type') == 'files':
            for f in p.get('files',[]): download(f,rec,name)
    rec['text'] = '\n\n'.join(blocks(page['id'],rec))
    print(json.dumps(dict(title=rec['title'],files=len(rec['files']),text_characters=len(rec['text'])),ensure_ascii=False))

diagnostics = {'root_id': ROOT, 'searches': {}, 'root_children': []}
try:
    root_page = get('pages', ROOT)
    diagnostics['root_title'] = title(root_page)
    for b in paged(f'/blocks/{ROOT}/children'):
        k = b['type']; d = b.get(k,{})
        item = {'id': b['id'], 'type': k, 'has_children': b.get('has_children',False)}
        if k in ('child_page','child_database'): item['title'] = d.get('title','')
        elif k in ('link_to_page',): item['target'] = d
        elif d.get('rich_text'): item['text'] = rich(d['rich_text'])[:300]
        diagnostics['root_children'].append(item)
except RuntimeError as e:
    diagnostics['root_error'] = str(e)
matches = {}
pattern = re.compile(rf'(?i)(?<![a-z0-9])w[\s_-]*0?{WEEK}(?!\d)|(?<!\d){WEEK}\s*주차')
for query in (f'w{WEEK}',f'{WEEK}주차',str(WEEK)):
    rows = []
    for page in paged('/search',{'query':query,'filter':{'property':'object','value':'page'}}):
        row = {'id':page['id'],'title':title(page),'parent':page.get('parent'),'in_trash':page.get('in_trash',False)}
        try: row['under_study'] = under_study(page)
        except RuntimeError as e: row['scope_error'] = str(e)
        rows.append(row)
        if pattern.search(title(page)) and not page.get('in_trash') and row.get('under_study'): matches[compact(page['id'])] = page
    diagnostics['searches'][query] = rows
OUT.mkdir(exist_ok=True)
(OUT/'diagnostics.json').write_text(json.dumps(diagnostics,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(diagnostics,ensure_ascii=False,indent=2))
for page in matches.values(): export(page)
(OUT/'manifest.json').write_text(json.dumps(dict(week=WEEK,root_id=ROOT,matched_pages=len(matches),records=list(RECORDS.values())),ensure_ascii=False,indent=2),encoding='utf-8')
if not RECORDS: print(f'No W{WEEK} pages exported; see discovery diagnostics.')
print(f'Exported {len(RECORDS)} pages and {sum(len(x["files"]) for x in RECORDS.values())} attachments.')
