import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    for w,h,n in [(1440,900,'orig_1440.png'),(390,844,'orig_390.png')]:
        pg=b.new_page(viewport={'width':w,'height':h})
        pg.goto(sys.argv[1],wait_until='networkidle'); pg.wait_for_timeout(1500)
        pg.screenshot(path=n,full_page=True)
    b.close()
