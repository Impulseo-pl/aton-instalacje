import json,re,urllib.request,os
d={p['slug']:p for p in json.load(open('pages.json',encoding='utf8'))}
s=d['realizacje']['content']['rendered']; s=re.sub(r'(?s)<style.*?</style>','',s)
for m in re.finditer(r'(?i)<h[1-6][^>]*>(.*?)</h|<span[^>]*elementor-heading[^>]*>(.*?)<|(INSTALACJE ODGROMOWE|INSTALACJE ELEKTRYCZNE|Rozdzielnice|MAGAZYNY ENERGII)|uploads/2025/12/([^"\s]+?)(?:-\d+x\d+)?\.(jpe?g)',s):
    print(m.group(1) or m.group(2) or m.group(3) or m.group(4)+'.'+m.group(5))
urls=sorted(set(re.sub(r'-\d+x\d+(\.jpe?g)$',r'\1',u) for u in re.findall(r'https://aton-instalacje.pl/wp-content/uploads/2025/12/[^"\s]+?\.jpe?g',s)))
os.makedirs('real',exist_ok=True)
for u in urls:
    f='real/'+u.rsplit('/',1)[1]
    if not os.path.exists(f):
        urllib.request.urlretrieve(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}).full_url,f) if False else open(f,'wb').write(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read())
print(len(urls))
