from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    pg=b.new_page(viewport={'width':1440,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.goto('http://127.0.0.1:8124/aton-instalacje/?team=1',wait_until='commit')
    t=[400,1100,1700,2300,2900,3600,5200]; prev=0; fr=[]
    for ms in t:
        pg.wait_for_timeout(ms-prev); prev=ms
        n=f'_src/ld_{ms}.png'; pg.screenshot(path=n); fr.append(n)
    W=Image.new('RGB',(360*4,225*2))
    for i,n in enumerate(fr): W.paste(Image.open(n).resize((360,225)),((i%4)*360,(i//4)*225))
    W.save('_src/ld_sheet.png')
    print('lenis', pg.evaluate('document.documentElement.className'))
    # przewiń całą stronę i sprawdź, czy wszystko się odsłoniło
    h=pg.evaluate('document.body.scrollHeight')
    for y in range(0,h,500): pg.mouse.wheel(0,500); pg.wait_for_timeout(120)
    pg.wait_for_timeout(1800)
    print('rv niewidoczne:',pg.evaluate("document.querySelectorAll('.rv:not(.widac),.rv-foto:not(.widac)').length"))
    pg.screenshot(path='_src/ld_dol.png')
    pg.mouse.wheel(0,-900); pg.wait_for_timeout(1500); pg.screenshot(path='_src/ld_gora.png')
    # przejście na podstronę
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(500)
    pg.click('.menu a[href="oferta/"]'); pg.wait_for_timeout(200); pg.screenshot(path='_src/tr_1.png')
    pg.wait_for_load_state('load'); pg.wait_for_timeout(250); pg.screenshot(path='_src/tr_2.png')
    pg.wait_for_timeout(1500); pg.screenshot(path='_src/tr_3.png')
    print('loader na podstronie:',pg.is_visible('.loader'), pg.url)
    print('errors',errs); b.close()
