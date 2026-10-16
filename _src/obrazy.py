# Przygotowanie obrazów dema ATON: python _src/obrazy.py (z katalogu aton-instalacje)
import os
from PIL import Image, ImageOps, ImageChops
S='_src/real/'; O='img/'
M={
 'odgrom-attyka-dach-plaski':'WhatsApp-Image-2025-12-28-at-20.30.13-1.jpeg',
 'odgrom-iglica-dach-skosny':'WhatsApp-Image-2025-12-28-at-20.30.13-2.jpeg',
 'odgrom-wsporniki-karpiowka':'WhatsApp-Image-2025-12-28-at-20.30.13-3.jpeg',
 'odgrom-wsporniki-karpiowka-2':'WhatsApp-Image-2025-12-28-at-20.30.13-4.jpeg',
 'odgrom-przy-panelach-pv':'WhatsApp-Image-2025-12-28-at-20.30.13-5.jpeg',
 'odgrom-zwod-attyka':'WhatsApp-Image-2025-12-28-at-20.30.13-6.jpeg',
 'odgrom-maszt-dach-plaski':'WhatsApp-Image-2025-12-28-at-20.30.13-7.jpeg',
 'odgrom-maszt-podstawa':'WhatsApp-Image-2025-12-28-at-20.30.13-8.jpeg',
 'odgrom-dach-plaski-zwod':'WhatsApp-Image-2025-12-28-at-20.30.13.jpeg',
 'elektr-zlacze-rozlacznik':'IMG_4062.jpg',
 'elektr-stan-surowy':'IMG_3818.jpg',
 'elektr-przepust-scienny':'IMG_3806.jpg',
 'elektr-opisane-przewody':'IMG_3343.jpg',
 'elektr-puszka-opis-obwodu':'IMG_3451.jpg',
 'rozdz-natynkowa-przepiecia':'IMG_6630-1.jpg',
 'rozdz-natynkowa-przepiecia-2':'IMG_6629-1.jpg',
 'rozdz-podtynkowa-montaz':'IMG_4058.jpg',
 'rozdz-szafa-montaz':'IMG_3654-1.jpg',
 'rozdz-sciana-stan-surowy':'IMG_3653.jpg',
 'rozdz-szafa-gotowa':'IMG_3479-1.jpg',
 'rozdz-gesta-zabudowa':'IMG_2435.jpg',
 'rozdz-sciana-stan-surowy-2':'2.jpg',
 'rozdz-wiazka-przewodow':'1.jpg',
 'pv-falownik-konstrukcja':'IMG_3808.jpg',
 'pv-farma-gruntowa':'IMG_3809.jpg',
 'pv-farma-gruntowa-2':'IMG_3810.jpg',
 'pv-farma-gruntowa-3':'IMG_3811.jpg',
 'pv-falownik-solax':'IMG_4973.jpg',
 'pv-falownik-solax-2':'IMG_4974.jpg',
 'pv-magazyn-energii':'IMG_4975.jpg',
 'pv-wyswietlacz-falownika':'IMG_2441-2.jpg',
 'pv-zlacza-dc':'IMG_2465.jpg',
 'pv-przepieciowka-wtyk':'IMG_2500.jpg',
 'pv-rozlacznik-dc':'IMG_2504.jpg',
 'pv-falownik-magazyn-huawei':'IMG_2909.jpg',
 'pv-dongle-huawei':'IMG_2910.jpg',
}
for n,f in M.items():
    im=ImageOps.exif_transpose(Image.open(S+f)).convert('RGB')
    for w in (640,1200):
        if w>im.width and w!=640: w=im.width
        r=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
        r.save(f'{O}{n}-{w}.webp',quality=78,method=6)
bg=Image.open('_src/orig/bg.png').convert('RGB')
for w in (900,1536): bg.resize((w,round(bg.height*w/bg.width)),Image.LANCZOS).save(f'{O}noc-{w}.webp',quality=80,method=6)
bg.resize((1200,800)).save(O+'og.jpg',quality=82)
# logo: czarne na białym -> białe z alfą
lg=Image.open('_src/orig/aton-logo-png-2.png').convert('RGBA')
bgw=Image.new('RGBA',lg.size,'white'); bgw.alpha_composite(lg); g=bgw.convert('L')
a=ImageOps.invert(g)
white=Image.new('RGBA',lg.size,(255,255,255,0)); white.putalpha(a)
bb=a.point(lambda v:255 if v>40 else 0).getbbox(); white=white.crop(bb); white.save(O+'logo-aton.png')
# podział na sygnet i napis: szukamy pustego pasa poziomego
al=white.getchannel('A'); rows=[max(al.crop((0,y,al.width,y+1)).getdata()) for y in range(al.height)]
gap=[y for y in range(al.height) if rows[y]<30 and y>al.height*0.4]
cut=gap[0]
sy=white.crop((0,0,white.width,cut)); sy=sy.crop(sy.getchannel('A').getbbox()); sy.save(O+'sygnet.png')
wm=white.crop((0,cut,white.width,white.height)); wm=wm.crop(wm.getchannel('A').getbbox()); wm.save(O+'napis-aton.png')
print('logo',white.size,'sygnet',sy.size,'napis',wm.size)
# favicon / apple
ic=Image.new('RGBA',(180,180),(7,7,8,255)); s=sy.copy(); s.thumbnail((140,140)); ic.alpha_composite(s,((180-s.width)//2,(180-s.height)//2)); ic.convert('RGB').save('apple-touch-icon.png')
ic.resize((48,48),Image.LANCZOS).save('favicon.png')
