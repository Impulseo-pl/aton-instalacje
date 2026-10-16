# Jednorazowa łatka CSS: ekran ładowania, przejścia, odsłanianie przy przewijaniu
f = 'assets/styles.css'
s = open(f, encoding='utf8').read()
L = s.split('\n')
start = [i for i, l in enumerate(L) if l.startswith('.hero-sygnet{')][0]
end = [i for i, l in enumerate(L) if l.startswith('@keyframes swiatlo')][0]
L[start:end + 1] = ['''.hero-sygnet{display:block;width:150px;height:auto;margin:0 auto 22px;overflow:visible;
  fill:none;stroke:#fff;stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round;
  filter:drop-shadow(0 0 6px rgba(255,255,255,.9)) drop-shadow(0 0 18px rgba(255,255,255,.45))}
.hero-napis{width:230px;margin:0 auto 48px;filter:drop-shadow(0 0 10px rgba(255,255,255,.7)) drop-shadow(0 0 22px rgba(255,255,255,.35))}''']
s = '\n'.join(L)

def rep(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b, 1)

rep('.btn{display:inline-block;', '.btn{display:inline-block;background-image:linear-gradient(#fff,#fff)!important;background-repeat:no-repeat!important;background-size:0% 100%!important;background-position:left center!important;\n  ')
rep('transition:background .35s,color .35s,box-shadow .35s}', 'transition:background-size .55s cubic-bezier(.65,0,.35,1),color .4s,box-shadow .4s}')
rep('.btn:hover{background:#fff;color:var(--czern);', '.btn:hover{background-size:100% 100%!important;color:var(--czern);')
rep('.top{position:fixed;top:0;left:0;right:0;z-index:50;transition:background .35s,border-color .35s;',
    '.top{position:fixed;top:0;left:0;right:0;z-index:50;transition:background .5s,border-color .5s,transform .6s cubic-bezier(.22,1,.36,1);')
rep('.spis{position:sticky;top:79px;', '.spis{position:sticky;top:79px;transition:top .6s cubic-bezier(.22,1,.36,1);')
rep('.menu a{text-decoration:none;font-size:16px;color:rgba(255,255,255,.82);transition:color .3s,text-shadow .3s}',
    '.menu a{text-decoration:none;font-size:16px;color:rgba(255,255,255,.82);transition:color .3s,text-shadow .3s;position:relative}\n'
    '.menu a:not(.menu-tel)::after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:1px;background:#fff;transform:scaleX(0);transition:transform .5s cubic-bezier(.22,1,.36,1)}\n'
    '.menu a:not(.menu-tel):hover::after,.menu a[aria-current]::after{transform:scaleX(1)}')

RUCH = '''/* ================= ruch ================= */
:root{--ease:cubic-bezier(.22,1,.36,1)}
html.lenis,html.lenis body{height:auto}
html.lenis{scroll-behavior:auto}
.lenis.lenis-stopped{overflow:hidden}
.top.schowany{transform:translateY(-100%)}
html.bez-naglowka .spis{top:0}

/* ekran ładowania – rysowany sygnet ATON */
.loader{display:none}
html.js.pierwszy .loader{display:flex}
.loader{position:fixed;inset:0;z-index:200;background:var(--czern);flex-direction:column;align-items:center;justify-content:center;
  transition:opacity 1.1s var(--ease),visibility 1.1s}
.loader::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 46%,rgba(255,255,255,.08),transparent 42%);opacity:0;animation:ld-poswiata 2.4s .8s var(--ease) forwards}
.loader-sygnet{width:150px;height:auto;overflow:visible;fill:none;stroke:#fff;stroke-width:2;stroke-linejoin:round;stroke-linecap:round;position:relative;
  animation:ld-blask 1.2s ease-out 1.6s forwards;transition:transform 1.2s var(--ease)}
.loader-sygnet *{stroke-dasharray:1;stroke-dashoffset:1}
.loader-sygnet .s-kolo{animation:ld-rysuj 1.5s var(--ease) .15s forwards}
.loader-sygnet .s-znak{animation:ld-rysuj .4s var(--ease) 1.45s forwards}
.loader-sygnet .s-tr{animation:ld-rysuj 1.1s cubic-bezier(.65,0,.35,1) .55s forwards}
.loader-sygnet .s-tr2{animation:ld-rysuj .8s cubic-bezier(.65,0,.35,1) 1.05s forwards}
.loader-napis{width:200px;margin-top:30px;opacity:0;clip-path:inset(0 50% 0 50%);filter:blur(6px);
  animation:ld-napis 1.1s var(--ease) 1.5s forwards;position:relative}
.loader-linia{display:block;width:120px;height:1px;margin-top:34px;background:rgba(255,255,255,.18);position:relative;overflow:hidden}
.loader-linia::after{content:"";position:absolute;inset:0;background:#fff;transform:scaleX(0);transform-origin:left;animation:ld-linia 2.3s cubic-bezier(.65,0,.35,1) .2s forwards}
@keyframes ld-rysuj{to{stroke-dashoffset:0}}
@keyframes ld-blask{to{filter:drop-shadow(0 0 6px rgba(255,255,255,.9)) drop-shadow(0 0 18px rgba(255,255,255,.45))}}
@keyframes ld-napis{to{opacity:1;clip-path:inset(0 0 0 0);filter:blur(0) drop-shadow(0 0 10px rgba(255,255,255,.6))}}
@keyframes ld-linia{to{transform:scaleX(1)}}
@keyframes ld-poswiata{to{opacity:1}}
html.gotowe .loader{opacity:0;visibility:hidden;pointer-events:none}
html.gotowe .loader-sygnet{transform:scale(1.08)}

/* zasłona przy przejściach między podstronami */
.zaslona{position:fixed;inset:0;z-index:150;background:var(--czern);pointer-events:none;opacity:0;transition:opacity .8s var(--ease)}
html.js:not(.gotowe):not(.pierwszy) .zaslona{opacity:1}
html.wyjscie .zaslona{opacity:1;transition-duration:.45s;pointer-events:auto}

/* tło: powolne wejście */
html.js .noc{transform:scale(1.1);transition:transform 3.2s var(--ease)}
html.js.gotowe .noc{transform:none}

/* hero: elementy wchodzą po kolei */
html.js .hero-in>*,html.js .hero-pasek{opacity:0;transform:translateY(26px);transition:opacity 1.3s var(--ease),transform 1.5s var(--ease)}
html.js .hero-in>:nth-child(1){transform:scale(.92)}
html.js.gotowe .hero-in>*,html.js.gotowe .hero-pasek{opacity:1;transform:none}
html.js .hero-in>:nth-child(2){transition-delay:.12s}
html.js .hero-in>:nth-child(3){transition-delay:.24s}
html.js .hero-in>:nth-child(4){transition-delay:.36s}
html.js .hero-in>:nth-child(5){transition-delay:.5s}
html.js .hero-pasek{transition-delay:.7s}
html.js .hero-sygnet *{stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 1.6s cubic-bezier(.65,0,.35,1)}
html.js.gotowe .hero-sygnet *{stroke-dashoffset:0}
html.js.pierwszy .hero-sygnet *{transition-duration:0s}

/* nagłówki podstron */
html.js .naglowek .t,html.js .naglowek .podtytul{opacity:0;transform:translateY(24px);transition:opacity 1.2s var(--ease) .15s,transform 1.4s var(--ease) .15s}
html.js .naglowek .podtytul{transition-delay:.3s}
html.js.gotowe .naglowek .t,html.js.gotowe .naglowek .podtytul{opacity:1;transform:none}

/* odsłanianie przy przewijaniu */
html.js .rv{opacity:0;transform:translateY(34px);transition:opacity 1.1s var(--ease),transform 1.3s var(--ease);transition-delay:var(--d,0s)}
html.js .rv.widac{opacity:1;transform:none}
html.js .rv-foto{clip-path:inset(14% 0 14% 0);transition:clip-path 1.4s var(--ease);transition-delay:var(--d,0s)}
html.js .rv-foto img{transform:scale(1.18);transition:transform 1.8s var(--ease),filter .5s;transition-delay:var(--d,0s)}
html.js .rv-foto.widac{clip-path:inset(0 0 0 0)}
html.js .rv-foto.widac img{transform:none}
html.js .t.rv{letter-spacing:10px;transition:opacity 1.1s var(--ease),transform 1.3s var(--ease),letter-spacing 1.6s var(--ease)}
html.js .t.rv.widac{letter-spacing:4px}
html.js .t-lewo.rv.widac{letter-spacing:3px}
@media (max-width:640px){html.js .t.rv.widac{letter-spacing:3px}html.js .t-lewo.rv.widac{letter-spacing:2px}}

'''
rep('@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}html{scroll-behavior:auto}}',
    RUCH + '@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}html{scroll-behavior:auto}\n'
    '  html.js .rv,html.js .hero-in>*,html.js .hero-pasek,html.js .naglowek .t,html.js .naglowek .podtytul{opacity:1!important;transform:none!important}\n'
    '  html.js .rv-foto{clip-path:none!important}html.js .rv-foto img{transform:none!important}\n'
    '  .loader-sygnet *,.hero-sygnet *{stroke-dashoffset:0!important}.loader-napis{opacity:1;clip-path:none;filter:none}}')
open(f, 'w', encoding='utf8').write(s)
print('ok')
