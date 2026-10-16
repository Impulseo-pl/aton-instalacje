import sys
from playwright.sync_api import sync_playwright
path,w,h,ys=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),[int(x) for x in sys.argv[4].split(',')]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    pg=b.new_page(viewport={'width':w,'height':h},is_mobile=w<700,has_touch=w<700)
    pg.goto('http://127.0.0.1:8124/aton-instalacje/'+path+'?team=1',wait_until='networkidle')
    for y in ys:
        pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(2600 if y==0 else 500)
        pg.screenshot(path=f'_src/vp_{(path.strip("/") or "home")}_{w}_{y}.png')
    b.close()
