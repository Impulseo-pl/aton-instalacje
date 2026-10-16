from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    pg=b.new_page(viewport={'width':1440,'height':900})
    for s in ['o-nas','oferta','realizacje','kontakt']:
        pg.goto('https://aton-instalacje.pl/'+s+'/',wait_until='networkidle'); pg.wait_for_timeout(1200)
        pg.screenshot(path=f'orig_{s}.png',full_page=True)
    b.close()
