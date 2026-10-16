from PIL import Image
im=Image.open('_src/orig/logo-aton-Photoroom-768x512.png').convert('RGBA')
a=im.getchannel('A'); bb=a.point(lambda v:255 if v>20 else 0).getbbox()
w=Image.new('RGBA',im.size,(255,255,255,0)); w.putalpha(a); w=w.crop(bb); w.save('img/logo-aton.png')
al=w.getchannel('A'); H=al.height
rows=[al.crop((0,y,al.width,y+1)).getextrema()[1] for y in range(H)]
cut=next(y for y in range(int(H*.45),H) if rows[y]<25)
sy=w.crop((0,0,w.width,cut)); sy=sy.crop(sy.getchannel('A').getbbox()); sy.save('img/sygnet.png')
wm=w.crop((0,cut,w.width,H)); wm=wm.crop(wm.getchannel('A').point(lambda v:255 if v>20 else 0).getbbox()); wm.save('img/napis-aton.png')
print(w.size,sy.size,wm.size)
ic=Image.new('RGBA',(180,180),(7,7,8,255)); s=sy.copy(); s.thumbnail((140,140)); ic.alpha_composite(s,((180-s.width)//2,(180-s.height)//2)); ic.convert('RGB').save('apple-touch-icon.png')
ic.resize((48,48),Image.LANCZOS).save('favicon.png')
