# -*- coding: utf-8 -*-
"""Generator dema ATON. Uruchom: python _src/build.py (z katalogu aton-instalacje)."""
import os, json, re, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://impulseo-pl.github.io/aton-instalacje/'
IMG = os.path.join(ROOT, 'img')
TEL, TELH = '+48 697 296 018', '+48697296018'
MAIL = 'biuro@e-aton.pl'

# ---------- obrazy ----------
def variants(name):
    out = []
    for f in os.listdir(IMG):
        m = re.fullmatch(re.escape(name) + r'-(\d+)\.webp', f)
        if m:
            w, h = Image.open(os.path.join(IMG, f)).size
            out.append((int(m.group(1)), f, w, h))
    if not out:
        raise SystemExit('brak obrazu ' + name)
    return sorted(out)

def pic(p, name, alt, sizes='(max-width: 800px) 100vw, 50vw', lazy=True, cls=''):
    v = variants(name)
    small, big = v[0], v[-1]
    srcset = ', '.join(f'{p}img/{f} {w}w' for _, f, w, h in v)
    a = (f'<img src="{p}img/{big[1]}" srcset="{srcset}" sizes="{sizes}" '
         f'width="{big[2]}" height="{big[3]}" alt="{html.escape(alt)}"')
    if lazy: a += ' loading="lazy" decoding="async"'
    if cls: a += f' class="{cls}"'
    return a + '>'

def full(name):
    return variants(name)[-1][1]

def landscape(name):
    v = variants(name)[-1]
    return v[2] > v[3]

# ---------- realizacje (zdjęcia ze strony aton-instalacje.pl) ----------
KAT = [
    ('odgromowe', 'Instalacje odgromowe'),
    ('elektryczne', 'Instalacje elektryczne'),
    ('rozdzielnice', 'Rozdzielnice'),
    ('fotowoltaika', 'Fotowoltaika i magazyny energii'),
]
FOTY = [
    ('odgromowe', 'odgrom-attyka-dach-plaski', 'Zwody poziome na attyce dachu płaskiego'),
    ('odgromowe', 'odgrom-iglica-dach-skosny', 'Iglica odgromowa na kalenicy dachu skośnego'),
    ('odgromowe', 'odgrom-wsporniki-karpiowka', 'Przewód odgromowy na wspornikach – dachówka karpiówka'),
    ('odgromowe', 'odgrom-wsporniki-karpiowka-2', 'Połączenie krzyżowe zwodów na dachu z karpiówki'),
    ('odgromowe', 'odgrom-przy-panelach-pv', 'Zwód poprowadzony przy panelach fotowoltaicznych na dachu płaskim'),
    ('odgromowe', 'odgrom-zwod-attyka', 'Maszt odgromowy przy attyce, dach płaski z otoczakami'),
    ('odgromowe', 'odgrom-maszt-dach-plaski', 'Maszt odgromowy na dachu płaskim'),
    ('odgromowe', 'odgrom-maszt-podstawa', 'Maszt na betonowej podstawie wolnostojącej'),
    ('odgromowe', 'odgrom-dach-plaski-zwod', 'Instalacja odgromowa dachu płaskiego z wyłazem'),
    ('elektryczne', 'elektr-stan-surowy', 'Okablowanie domu w stanie surowym'),
    ('elektryczne', 'elektr-przepust-scienny', 'Przepust przewodów zasilających przez ścianę'),
    ('elektryczne', 'elektr-zlacze-rozlacznik', 'Złącze z rozłącznikiem głównym'),
    ('elektryczne', 'elektr-opisane-przewody', 'Opisane przewody przed podłączeniem rozdzielnicy'),
    ('elektryczne', 'elektr-puszka-opis-obwodu', 'Puszka z oznaczeniem obwodu i złączkami'),
    ('rozdzielnice', 'rozdz-natynkowa-przepiecia-2', 'Rozdzielnica natynkowa z ochroną przeciwprzepięciową'),
    ('rozdzielnice', 'rozdz-natynkowa-przepiecia', 'Rozdzielnica natynkowa – rzędy aparatów modułowych'),
    ('rozdzielnice', 'rozdz-szafa-gotowa', 'Rozdzielnica wysoka po montażu'),
    ('rozdzielnice', 'rozdz-gesta-zabudowa', 'Rozdzielnica z opisanymi obwodami'),
    ('rozdzielnice', 'rozdz-podtynkowa-montaz', 'Rozdzielnica podtynkowa w trakcie montażu'),
    ('rozdzielnice', 'rozdz-szafa-montaz', 'Szafa rozdzielcza w trakcie zabudowy'),
    ('rozdzielnice', 'rozdz-sciana-stan-surowy', 'Rozdzielnice na ścianie w stanie surowym'),
    ('rozdzielnice', 'rozdz-sciana-stan-surowy-2', 'Obudowy rozdzielnic przed tynkowaniem'),
    ('rozdzielnice', 'rozdz-wiazka-przewodow', 'Wiązka przewodów wprowadzona do rozdzielnicy'),
    ('fotowoltaika', 'pv-farma-gruntowa-2', 'Instalacja fotowoltaiczna na konstrukcji gruntowej'),
    ('fotowoltaika', 'pv-farma-gruntowa', 'Konstrukcja gruntowa – widok z boku'),
    ('fotowoltaika', 'pv-farma-gruntowa-3', 'Panele na konstrukcji gruntowej'),
    ('fotowoltaika', 'pv-falownik-konstrukcja', 'Falownik zamontowany pod konstrukcją paneli'),
    ('fotowoltaika', 'pv-falownik-solax', 'Falownik hybrydowy SolaX z rozdzielnicą AC/DC'),
    ('fotowoltaika', 'pv-falownik-solax-2', 'Falownik SolaX po uruchomieniu'),
    ('fotowoltaika', 'pv-magazyn-energii', 'Magazyn energii – moduły bateryjne'),
    ('fotowoltaika', 'pv-falownik-magazyn-huawei', 'Falownik Huawei z magazynem energii'),
    ('fotowoltaika', 'pv-dongle-huawei', 'Moduł komunikacyjny Huawei do monitoringu w aplikacji'),
    ('fotowoltaika', 'pv-rozlacznik-dc', 'Rozłącznik DC i przyłącza falownika'),
    ('fotowoltaika', 'pv-przepieciowka-wtyk', 'Ograniczniki przepięć i złącze komunikacyjne'),
    ('fotowoltaika', 'pv-zlacza-dc', 'Złącza DC falownika'),
    ('fotowoltaika', 'pv-wyswietlacz-falownika', 'Wyświetlacz falownika – praca w trybie normalnym'),
]
ALT = {n: a for _, n, a in FOTY}
def ile(k): return sum(1 for x in FOTY if x[0] == k)

# ---------- oferta ----------
OFERTA = [
    dict(id='instalacje-elektryczne', k='Elektryka', t='Instalacje elektryczne',
         krotko='Okablowanie domów i budynków od stanu surowego do montażu osprzętu. Każdy przewód opisany.',
         kafel='elektr-opisane-przewody',
         lead='Instalacja, której po wykończeniu nie widać, a która przez lata po prostu działa. Zaczynamy od rozmowy o tym, jak będziecie korzystać z domu, a kończymy na opisanej rozdzielnicy i protokole pomiarów.',
         tekst=['Rozplanowanie gniazd, łączników i punktów świetlnych robimy razem z inwestorem na rzutach domu – tak, żeby gniazdo nie wylądowało za szafą, a włącznik po złej stronie drzwi. Obwody dzielimy według pomieszczeń i odbiorników, z zapasem na to, co dojdzie za kilka lat.',
                'W stanie surowym prowadzimy okablowanie, osadzamy puszki i wprowadzamy przewody do rozdzielnicy. Każdy przewód i każda puszka dostaje opis obwodu – widać to na zdjęciach z naszych budów. Po tynkach wracamy na montaż osprzętu i oświetlenia.'],
         zakres=['rozplanowanie punktów elektrycznych na rzutach', 'okablowanie w stanie surowym, puszki, przepusty',
                 'zasilanie od złącza do rozdzielnicy', 'obwody siłowe: płyta indukcyjna, pompa ciepła, ładowarka samochodu',
                 'montaż gniazd, łączników i oświetlenia', 'opis obwodów i pomiary odbiorcze'],
         foty=['elektr-stan-surowy', 'elektr-przepust-scienny', 'elektr-zlacze-rozlacznik', 'elektr-opisane-przewody', 'elektr-puszka-opis-obwodu']),
    dict(id='smart-home', k='Smart home', t='Automatyka i smart home',
         krotko='Oświetlenie, rolety, ogrzewanie i energia sterowane z jednego miejsca – zaplanowane już w stanie surowym.',
         kafel=None,
         lead='Inteligentny dom zaczyna się od przewodów, nie od aplikacji. Jeśli okablowanie zaplanujemy na etapie budowy, sterowanie można potem rozbudowywać bez kucia ścian.',
         tekst=['Dobieramy system do inwestycji i budżetu: od sterowania oświetleniem i roletami, przez ogrzewanie w strefach, po sceny („wyjście z domu”, „noc”, „kino”) wywoływane jednym przyciskiem albo z telefonu.',
                'Automatykę łączymy z instalacją fotowoltaiczną i magazynem energii, żeby dom korzystał z prądu wtedy, gdy jest najtańszy albo własny. Szafę automatyki projektujemy razem z rozdzielnicą – czytelnie opisaną, z miejscem na rozbudowę.'],
         zakres=['projekt automatyki razem z instalacją elektryczną', 'sterowanie oświetleniem, roletami i bramą',
                 'ogrzewanie strefowe i harmonogramy', 'sceny i sterowanie z telefonu',
                 'okablowanie sieci LAN i punkty Wi-Fi', 'zarządzanie energią z PV i magazynu'],
         foty=[]),
    dict(id='fotowoltaika-magazyny-energii', k='Fotowoltaika i magazyny', t='Fotowoltaika i magazyny energii',
         krotko='Instalacje dachowe i gruntowe, falowniki hybrydowe, magazyny energii z monitoringiem w aplikacji.',
         kafel='pv-farma-gruntowa-2',
         lead='Montujemy instalacje fotowoltaiczne na dachach i na konstrukcjach gruntowych, a do istniejących systemów dokładamy magazyny energii.',
         tekst=['W naszych realizacjach pracują falowniki hybrydowe SolaX i Huawei z magazynami energii. Falownik, zabezpieczenia AC/DC i magazyn montujemy jako jeden uporządkowany zestaw – z rozłącznikami, ochroną przeciwprzepięciową i opisem.',
                'Po uruchomieniu podłączamy moduł komunikacyjny, więc produkcję, zużycie i stan magazynu widać w aplikacji. Przy dachu z instalacją odgromową układamy panele tak, żeby zachować odstępy od zwodów.'],
         zakres=['instalacje dachowe i na konstrukcji gruntowej', 'falowniki hybrydowe i sieciowe',
                 'magazyny energii, także do istniejących instalacji', 'zabezpieczenia AC/DC i ochrona przeciwprzepięciowa',
                 'monitoring pracy w aplikacji', 'zgłoszenie instalacji do operatora sieci'],
         foty=['pv-farma-gruntowa-2', 'pv-falownik-solax', 'pv-magazyn-energii', 'pv-falownik-magazyn-huawei', 'pv-falownik-konstrukcja', 'pv-rozlacznik-dc']),
    dict(id='rozdzielnice-dokumentacja', k='Rozdzielnice', t='Rozdzielnice i dokumentacja',
         krotko='Rozdzielnice natynkowe i podtynkowe z ochroną przeciwprzepięciową, opisem obwodów i schematem.',
         kafel='rozdz-natynkowa-przepiecia-2',
         lead='Rozdzielnica to miejsce, do którego elektryk wraca po latach. Budujemy je tak, żeby każdy – także ktoś spoza naszej firmy – wiedział, co jest czym.',
         tekst=['Montujemy rozdzielnice natynkowe, podtynkowe i wysokie szafy dla domów, lokali i budynków usługowych. Aparaty układamy w logiczne rzędy, przewody prowadzimy w korytkach, a każdy obwód dostaje opis na aparacie i w dokumentacji.',
                'Standardem jest ochrona przeciwprzepięciowa i wyłączniki różnicowoprądowe dobrane do obwodów. Po zakończeniu przekazujemy schemat rozdzielnicy, opis obwodów i protokoły pomiarów.'],
         zakres=['rozdzielnice natynkowe, podtynkowe i szafy wolnostojące', 'ochrona przeciwprzepięciowa',
                 'zabezpieczenia nadprądowe i różnicowoprądowe', 'opis aparatów i obwodów',
                 'schemat jednokreskowy rozdzielnicy', 'modernizacja starych rozdzielnic'],
         foty=['rozdz-natynkowa-przepiecia-2', 'rozdz-szafa-gotowa', 'rozdz-gesta-zabudowa', 'rozdz-podtynkowa-montaz', 'rozdz-natynkowa-przepiecia', 'rozdz-wiazka-przewodow']),
    dict(id='instalacje-odgromowe', k='Odgromowe', t='Instalacje odgromowe',
         krotko='Zwody, maszty i uziemienia na dachach płaskich i skośnych, także przy fotowoltaice.',
         kafel='odgrom-attyka-dach-plaski',
         lead='Ochrona odgromowa na dachach płaskich z attyką, na dachówce, blasze i przy instalacjach fotowoltaicznych.',
         tekst=['Na dachach płaskich prowadzimy zwody po attyce i stawiamy maszty na podstawach betonowych, które nie naruszają pokrycia. Na dachach skośnych montujemy przewody na wspornikach dobranych do pokrycia – inne pod karpiówkę, inne pod blachę.',
                'Gdy na dachu są panele, maszty ustawiamy tak, żeby panele znalazły się w strefie ochronnej, z zachowaniem odstępów separacyjnych. Instalację kończymy pomiarem rezystancji uziemienia i protokołem.'],
         zakres=['zwody poziome na dachach płaskich i attykach', 'maszty i iglice odgromowe',
                 'wsporniki dobrane do pokrycia dachu', 'ochrona instalacji fotowoltaicznych',
                 'przewody odprowadzające i uziemienie', 'pomiar rezystancji uziemienia'],
         foty=['odgrom-attyka-dach-plaski', 'odgrom-iglica-dach-skosny', 'odgrom-wsporniki-karpiowka', 'odgrom-przy-panelach-pv', 'odgrom-maszt-podstawa', 'odgrom-maszt-dach-plaski']),
    dict(id='pomiary-odbiory', k='Pomiary', t='Pomiary i odbiory',
         krotko='Pomiary odbiorcze nowych instalacji i okresowe kontrole z protokołami.',
         kafel='rozdz-szafa-gotowa',
         lead='Pomiar to dowód, że instalacja jest bezpieczna. Wykonujemy go po każdej naszej realizacji i jako osobną usługę – przy odbiorze domu, sprzedaży mieszkania czy okresowej kontroli.',
         tekst=['Prawo budowlane (art. 62) wymaga, żeby instalację elektryczną i piorunochronną budynku sprawdzać co najmniej raz na 5 lat. Pomiary są też potrzebne przy odbiorze nowej instalacji i często przy ubezpieczeniu domu.',
                'Każdy pomiar kończymy protokołem z wynikami i listą ewentualnych usterek – z informacją, co trzeba poprawić i dlaczego.'],
         zakres=['ciągłość przewodów ochronnych', 'rezystancja izolacji', 'impedancja pętli zwarcia',
                 'działanie wyłączników różnicowoprądowych', 'rezystancja uziemienia i instalacji odgromowej', 'protokoły pomiarowe'],
         foty=[]),
]

# ---------- FAQ ----------
FAQ = [
    ('Od czego zacząć instalację elektryczną w domu jednorodzinnym?',
     'Od rozmowy i rzutów domu. Zanim powstanie pierwsza bruzda, ustalamy, gdzie stoją meble, gdzie będzie telewizor, kuchnia i biurko, jakie urządzenia potrzebują osobnych obwodów i czy planujecie smart home, fotowoltaikę albo ładowarkę samochodu. Z tego powstaje rozplanowanie punktów, na którym pracujemy na budowie.'),
    ('Czy smart home trzeba zaplanować już na etapie budowy?',
     'Najlepiej tak. W stanie surowym da się poprowadzić przewody do rolet, czujników i szafy automatyki bez kucia. Systemy bezprzewodowe można dołożyć później, ale przewodowa podstawa daje więcej możliwości i mniej awarii.'),
    ('Czy instalacja odgromowa jest obowiązkowa w domu jednorodzinnym?',
     'Nie zawsze. O potrzebie ochrony decyduje ocena ryzyka według normy PN-EN 62305. Warto ją przeprowadzić przy domach w otwartym terenie, wyższych budynkach i wszędzie tam, gdzie na dachu jest fotowoltaika.'),
    ('Czy do istniejącej fotowoltaiki można dołożyć magazyn energii?',
     'Zwykle tak. Przy falowniku hybrydowym magazyn podłącza się bezpośrednio. Przy zwykłym falowniku sieciowym stosuje się rozwiązanie z osobnym falownikiem bateryjnym. Po oględzinach instalacji mówimy, która droga ma sens.'),
    ('Jak często trzeba robić pomiary instalacji elektrycznej?',
     'Według art. 62 Prawa budowlanego instalację elektryczną i piorunochronną budynku sprawdza się co najmniej raz na 5 lat. Pomiar robi się też po wykonaniu nowej instalacji, po większej przeróbce i często na potrzeby ubezpieczyciela.'),
    ('Co dostanę po zakończeniu prac?',
     'Działającą instalację, opisaną rozdzielnicę, schemat i protokoły pomiarów. Gdy za kilka lat coś będzie trzeba zmienić, Ty albo inny elektryk od razu zobaczycie, który obwód za co odpowiada.'),
    ('Ile kosztuje instalacja elektryczna?',
     'To zależy od metrażu, liczby punktów, zabezpieczeń i tego, czy w grę wchodzi automatyka. Wycenę przygotowujemy po rozmowie i obejrzeniu projektu – rzetelną, z rozpisanym zakresem, bez kwot „od”.'),
]

KROKI = [
    ('Analiza potrzeb', 'Rozmawiamy o domu, sposobie korzystania z niego i planach na przyszłość. Oglądamy projekt albo budynek.'),
    ('Projekt', 'Rozplanowanie punktów, podział na obwody, dobór zabezpieczeń i systemów. Wycena z rozpisanym zakresem.'),
    ('Wykonanie', 'Okablowanie, rozdzielnica, montaż urządzeń. Na budowie zostawiamy porządek i opisane przewody.'),
    ('Uruchomienie', 'Konfiguracja automatyki, falownika i magazynu. Pokazujemy, jak wszystko obsługiwać.'),
    ('Dokumentacja', 'Schemat rozdzielnicy, opis obwodów i protokoły pomiarów – komplet na lata.'),
]

NAV = [('', 'Home'), ('o-nas/', 'O nas'), ('oferta/', 'Oferta'), ('realizacje/', 'Realizacje'), ('kontakt/', 'Kontakt')]

ORG = {
    "@type": "Electrician",
    "@id": BASE + "#firma",
    "name": "ATON – instalacje elektryczne, smart home",
    "alternateName": "ATON",
    "description": "Instalacje elektryczne, automatyka i smart home, fotowoltaika z magazynami energii, rozdzielnice, instalacje odgromowe oraz pomiary elektryczne.",
    "url": BASE,
    "logo": BASE + "img/logo-aton.png",
    "image": BASE + "img/og.jpg",
    "telephone": TELH,
    "email": MAIL,
    "knowsAbout": ["instalacje elektryczne", "smart home", "automatyka budynkowa", "fotowoltaika",
                   "magazyny energii", "rozdzielnice elektryczne", "instalacje odgromowe", "pomiary elektryczne"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Oferta", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": o['t'], "url": BASE + 'oferta/#' + o['id']}} for o in OFERTA]},
}

# ---------- szablon ----------
def head(p, title, desc, path, extra_ld=None):
    ld = [dict(ORG, **{"@context": "https://schema.org"})]
    if extra_ld: ld += extra_ld
    lds = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}img/og.jpg">
<meta name="theme-color" content="#070708">
<link rel="icon" href="{p}favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Roboto:wght@500&display=swap">
<link rel="preload" as="image" href="{p}img/noc-1536.webp" imagesrcset="{p}img/noc-900.webp 900w, {p}img/noc-1536.webp 1536w" imagesizes="100vw">
<link rel="stylesheet" href="{p}assets/styles.css">
{lds}
</head>'''

def header(p, cur):
    links = ''.join(
        f'<a href="{p}{u}"{" aria-current=\"page\"" if u == cur else ""}>{n}</a>' for u, n in NAV)
    return f'''<body>
<div class="noc" aria-hidden="true"></div>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="top">
  <div class="top-in">
    <a class="znak" href="{p}" aria-label="ATON – strona główna"><img src="{p}img/napis-aton.png" width="237" height="50" alt="ATON"></a>
    <nav class="menu" id="menu" aria-label="Menu główne">{links}<a class="menu-tel" href="tel:{TELH}">{TEL}</a></nav>
    <button class="burger" aria-controls="menu" aria-expanded="false" aria-label="Menu"><span></span><span></span></button>
  </div>
</header>
<main id="tresc">'''

def footer(p):
    oferta = ''.join(f'<li><a href="{p}oferta/#{o["id"]}">{o["t"]}</a></li>' for o in OFERTA)
    strony = ''.join(f'<li><a href="{p}{u}">{n}</a></li>' for u, n in NAV)
    return f'''</main>
<footer class="stopka">
  <div class="wrap stopka-gora">
    <div>
      <img class="stopka-logo" src="{p}img/logo-aton.png" width="237" height="234" alt="ATON" loading="lazy">
      <p>Instalacje elektryczne, smart home</p>
    </div>
    <div><h2>Oferta</h2><ul>{oferta}</ul></div>
    <div><h2>Strona</h2><ul>{strony}</ul></div>
    <div><h2>Kontakt</h2><ul><li><a href="tel:{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
  </div>
  <div class="wrap stopka-dol">
    <span>E-mail: <a href="mailto:{MAIL}">{MAIL}</a></span>
    <span>Telefon: <a href="tel:{TELH}">{TEL}</a></span>
    <span>© 2026 ATON. Wszelkie prawa zastrzeżone.</span>
  </div>
</footer>
<div class="lb" id="lb" hidden><button class="lb-x" aria-label="Zamknij">×</button><button class="lb-p" aria-label="Poprzednie">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="Następne">›</button></div>
<script src="{p}assets/app.js" defer></script>
</body>
</html>'''

def faq_html(items):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def crumbs_ld(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "ATON", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": name, "item": BASE + path}]}

def form_html(id_='f'):
    opcje = ''.join(f'<option>{o["t"]}</option>' for o in OFERTA)
    return f'''<form class="form" id="{id_}" novalidate>
  <div class="pola">
    <label>Imię i nazwisko<input name="imie" autocomplete="name" required></label>
    <label>Telefon<input name="tel" type="tel" autocomplete="tel" required></label>
    <label>E-mail<input name="email" type="email" autocomplete="email"></label>
    <label>Czego dotyczy zapytanie<select name="temat"><option>Wybierz</option>{opcje}<option>Coś innego</option></select></label>
    <label>Miejscowość inwestycji<input name="miejsce" autocomplete="address-level2"></label>
    <label>Etap inwestycji<select name="etap"><option>Wybierz</option><option>Projekt / przed budową</option><option>Stan surowy</option><option>Budynek wykończony</option><option>Modernizacja istniejącej instalacji</option></select></label>
    <label class="szer">Wiadomość<textarea name="msg" rows="5" placeholder="Np. dom 160 m², stan surowy zamknięty, interesuje nas instalacja z przygotowaniem pod smart home."></textarea></label>
  </div>
  <label class="zgoda"><input type="checkbox" required> Zgadzam się na kontakt w sprawie zapytania.</label>
  <button class="btn" type="submit">Wyślij zapytanie</button>
  <p class="form-info" role="status"></p>
</form>'''

def kontakt_blok(p):
    return f'''<section class="sekcja" id="kontakt">
  <div class="wrap kontakt-uklad">
    <div class="szklo kontakt-dane">
      <h2 class="t t-lewo">Porozmawiajmy o inwestycji</h2>
      <p>Opisz krótko, co budujesz albo co chcesz zmienić. Oddzwonimy, dopytamy o szczegóły i umówimy się na oględziny lub rozmowę nad projektem.</p>
      <a class="neon-link" href="tel:{TELH}"><span>Telefon</span>{TEL}</a>
      <a class="neon-link" href="mailto:{MAIL}"><span>E-mail</span>{MAIL}</a>
    </div>
    <div class="szklo">{form_html()}</div>
  </div>
</section>'''

def page_title(t, sub=''):
    s = f'<p class="podtytul">{sub}</p>' if sub else ''
    return f'<section class="naglowek"><div class="wrap"><h1 class="t">{t}</h1>{s}</div></section>'

def write(path, content):
    fp = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(content)

# ---------- HOME ----------
def home():
    p = ''
    pasek = ''.join(f'<a href="oferta/#{o["id"]}">{o["t"]}</a>' for o in OFERTA)
    kafle = ''
    for o in OFERTA:
        if o['kafel']:
            im = pic(p, o['kafel'], ALT.get(o['kafel'], o['t']), sizes='(max-width: 700px) 100vw, (max-width: 1100px) 50vw, 400px')
        else:
            im = f'<img src="img/noc-900.webp" width="900" height="600" alt="Nowoczesny dom z oświetleniem sterowanym automatyką" loading="lazy" class="kadr-dom">'
        kafle += f'''<a class="kafel" href="oferta/#{o['id']}">
  <div class="kafel-foto">{im}</div>
  <div class="kafel-tekst"><h3>{o['t']}</h3><p>{o['krotko']}</p><span class="wiecej">Szczegóły</span></div>
</a>'''
    okladki = {'odgromowe': 'odgrom-iglica-dach-skosny', 'elektryczne': 'elektr-zlacze-rozlacznik',
               'rozdzielnice': 'rozdz-szafa-gotowa', 'fotowoltaika': 'pv-magazyn-energii'}
    kat = ''.join(f'''<a class="kat" href="realizacje/#{k}">
  <div class="kat-foto">{pic(p, okladki[k], ALT[okladki[k]], sizes='(max-width: 700px) 50vw, 300px')}</div>
  <h3>{n}</h3><span>{ile(k)} zdjęć</span></a>''' for k, n in KAT)
    kroki = ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in KROKI)
    title = 'ATON – instalacje elektryczne, smart home, fotowoltaika i magazyny energii'
    desc = 'Instalacje elektryczne, automatyka i smart home, fotowoltaika z magazynami energii, rozdzielnice, instalacje odgromowe i pomiary. Od projektu po dokumentację. Tel. 697 296 018.'
    return head(p, title, desc, '', [faq_ld(FAQ)]) + header(p, '') + f'''
<section class="hero">
  <div class="hero-in">
    <img class="hero-sygnet" src="img/sygnet.png" width="162" height="155" alt="">
    <img class="hero-napis" src="img/napis-aton.png" width="237" height="50" alt="ATON">
    <h1>Nowoczesna technologia w eleganckiej formie</h1>
    <p class="hero-sub">Instalacje elektryczne, automatyka i inteligentne systemy dla wymagających inwestycji.</p>
    <div class="przyciski"><a class="btn" href="kontakt/">Skontaktuj się</a><a class="btn btn-cichy" href="realizacje/">Zobacz realizacje</a></div>
  </div>
  <nav class="hero-pasek" aria-label="Obszary działalności">{pasek}</nav>
</section>

<section class="sekcja">
  <div class="wrap">
    <h2 class="t">O nas</h2>
    <div class="dwa-panele">
      <div class="szklo panel-duzy"><p>ATON to pasja do technologii ukryta w precyzyjnych instalacjach. Wierzymy, że nowoczesna elektryka powinna być niewidzialnym sercem domu — bezpiecznym i gotowym na wyzwania przyszłości.</p></div>
      <div class="szklo">
        <p>Od lat dostarczamy rozwiązania dla najbardziej wymagających inwestycji, łącząc wiedzę inżynierską z wyjątkową dbałością o estetykę wykonania.</p>
        <hr>
        <h3 class="maly">Nasza filozofia</h3>
        <p>Projektujemy komfort i spokój ducha naszych klientów, opierając się na komponentach najwyższej klasy.</p>
        <a class="link" href="o-nas/">Więcej o nas</a>
      </div>
    </div>
  </div>
</section>

<section class="sekcja">
  <div class="wrap">
    <h2 class="t">Oferta</h2>
    <p class="wstep">Realizujemy inwestycje kompleksowo: od analizy potrzeb i projektu, po wykonanie, uruchomienie oraz dokumentację. Projektujemy i wykonujemy instalacje, które mają działać niezauważalnie — bezpiecznie, stabilnie i estetycznie.</p>
    <div class="kafle">{kafle}</div>
  </div>
</section>

<section class="sekcja pelna">
  <div class="wrap">
    <h2 class="t">Realizacje</h2>
    <p class="wstep">Zdjęcia z naszych budów – bez retuszu i bez aranżacji. Tak wyglądają instalacje, zanim zakryje je tynk.</p>
    <div class="katy">{kat}</div>
    <p class="srodek"><a class="btn" href="realizacje/">Wszystkie realizacje</a></p>
  </div>
</section>

<section class="sekcja">
  <div class="wrap">
    <div class="porzadek">
      <div class="porzadek-foto">
        {pic(p, 'elektr-puszka-opis-obwodu', ALT['elektr-puszka-opis-obwodu'], sizes='(max-width: 800px) 50vw, 300px')}
        {pic(p, 'rozdz-gesta-zabudowa', ALT['rozdz-gesta-zabudowa'], sizes='(max-width: 800px) 50vw, 400px')}
      </div>
      <div class="szklo">
        <h2 class="t t-lewo">Porządek, który zostaje na lata</h2>
        <p>Na zdjęciu obok jest zwykła puszka z jednej z naszych budów. Ma opis obwodu, uporządkowane złączki i przewody przycięte na równo. Nikt tego nie zobaczy po tynkowaniu – ale zobaczy to elektryk, który za dziesięć lat będzie szukał usterki.</p>
        <p>Tak samo budujemy rozdzielnice: aparaty w logicznych rzędach, opis każdego obwodu, schemat w dokumentacji. To jest ta „dbałość o estetykę wykonania”, o której piszemy.</p>
      </div>
    </div>
  </div>
</section>

<section class="sekcja">
  <div class="wrap">
    <h2 class="t">Jak pracujemy</h2>
    <ol class="kroki szklo">{kroki}</ol>
  </div>
</section>

<section class="sekcja">
  <div class="wrap waski">
    <h2 class="t">Najczęstsze pytania</h2>
    <div class="faq">{faq_html(FAQ)}</div>
  </div>
</section>
''' + kontakt_blok(p) + footer(p)

# ---------- OFERTA ----------
def oferta():
    p = '../'
    spis = ''.join(f'<a href="#{o["id"]}">{o["k"]}</a>' for o in OFERTA)
    sekcje = ''
    for i, o in enumerate(OFERTA):
        zakres = ''.join(f'<li>{z}</li>' for z in o['zakres'])
        tekst = ''.join(f'<p>{t}</p>' for t in o['tekst'])
        if o['foty']:
            foty = ''.join(
                f'<a class="fot" href="{p}img/{full(n)}" data-cap="{html.escape(ALT[n])}">{pic(p, n, ALT[n], sizes="(max-width: 800px) 50vw, 300px")}</a>'
                for n in o['foty'])
            galeria = f'<div class="mur">{foty}</div>'
        elif o['id'] == 'smart-home':
            galeria = f'<figure class="foto-szer"><img src="{p}img/noc-1536.webp" width="1536" height="1024" alt="Nowoczesny dom wieczorem – oświetlenie sterowane automatyką" loading="lazy"><figcaption>Zdjęcie poglądowe</figcaption></figure>'
        else:
            galeria = ''
        sekcje += f'''<section class="usluga" id="{o['id']}">
  <div class="wrap">
    <div class="usluga-gora{' odwr' if i % 2 else ''}">
      <div class="szklo">
        <h2 class="t t-lewo">{o['t']}</h2>
        <p class="lead">{o['lead']}</p>
        {tekst}
      </div>
      <div class="szklo zakres">
        <h3 class="maly">Zakres</h3>
        <ul>{zakres}</ul>
        <a class="btn" href="{p}kontakt/?temat={o['id']}">Zapytaj o wycenę</a>
      </div>
    </div>
    {galeria}
  </div>
</section>'''
    title = 'Oferta – instalacje elektryczne, smart home, fotowoltaika, odgromowe | ATON'
    desc = 'Instalacje elektryczne w domach, automatyka i smart home, fotowoltaika z magazynami energii, rozdzielnice, instalacje odgromowe, pomiary i odbiory. Zakres prac i zdjęcia z realizacji.'
    return head(p, title, desc, 'oferta/', [crumbs_ld('Oferta', 'oferta/')]) + header(p, 'oferta/') + page_title('Oferta', 'Realizujemy inwestycje kompleksowo: od analizy potrzeb i projektu, po wykonanie, uruchomienie oraz dokumentację. Jeśli nie widzisz tu dokładnie tego, czego potrzebujesz — skontaktuj się z nami. Dobierzemy rozwiązanie do Twojej inwestycji.') + f'''
<nav class="spis" aria-label="Obszary oferty"><div class="wrap">{spis}</div></nav>
{sekcje}
''' + kontakt_blok(p) + footer(p)

# ---------- REALIZACJE ----------
def realizacje():
    p = '../'
    filtry = '<button class="on" data-k="*">Wszystkie</button>' + ''.join(
        f'<button data-k="{k}">{n}</button>' for k, n in KAT)
    foty = ''.join(
        f'<a class="fot" data-k="{k}" href="{p}img/{full(n)}" data-cap="{html.escape(a)}">{pic(p, n, a, sizes="(max-width: 600px) 50vw, (max-width: 1000px) 33vw, 300px")}<span>{a}</span></a>'
        for k, n, a in FOTY)
    title = 'Realizacje – instalacje elektryczne, rozdzielnice, odgromowe, fotowoltaika | ATON'
    desc = 'Zdjęcia z naszych budów: instalacje odgromowe, okablowanie domów, rozdzielnice, fotowoltaika z falownikami SolaX i Huawei oraz magazyny energii.'
    return head(p, title, desc, 'realizacje/', [crumbs_ld('Realizacje', 'realizacje/')]) + header(p, 'realizacje/') + page_title('Nasze realizacje', 'Zdjęcia robione telefonem na budowie, w trakcie i po zakończeniu prac. Kliknij, żeby powiększyć.') + f'''
<section class="sekcja pelna galeria-sekcja">
  <div class="wrap">
    <div class="filtry" role="toolbar" aria-label="Filtr kategorii">{filtry}</div>
    <div class="mur mur-duzy" id="mur">{foty}</div>
  </div>
</section>
''' + kontakt_blok(p) + footer(p)

# ---------- O NAS ----------
def onas():
    p = '../'
    kroki = ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in KROKI)
    title = 'O nas – ATON, instalacje elektryczne i smart home'
    desc = 'ATON to pasja do technologii ukryta w precyzyjnych instalacjach. Instalacje elektryczne, automatyka, fotowoltaika – z dbałością o estetykę wykonania i pełną dokumentacją.'
    return head(p, title, desc, 'o-nas/', [crumbs_ld('O nas', 'o-nas/')]) + header(p, 'o-nas/') + page_title('O nas') + f'''
<section class="sekcja sekcja-bliska">
  <div class="wrap">
    <div class="dwa-panele">
      <div class="szklo panel-duzy"><p>ATON to pasja do technologii ukryta w precyzyjnych instalacjach. Wierzymy, że nowoczesna elektryka powinna być niewidzialnym sercem domu — bezpiecznym i gotowym na wyzwania przyszłości.</p></div>
      <div class="szklo">
        <p>Od lat dostarczamy rozwiązania dla najbardziej wymagających inwestycji, łącząc wiedzę inżynierską z wyjątkową dbałością o estetykę wykonania.</p>
        <hr>
        <h3 class="maly">Nasza filozofia</h3>
        <p>Projektujemy komfort i spokój ducha naszych klientów, opierając się na komponentach najwyższej klasy.</p>
      </div>
    </div>
  </div>
</section>

<section class="sekcja">
  <div class="wrap">
    <div class="rzad">
      <div class="rzad-foto">{pic(p, 'rozdz-natynkowa-przepiecia-2', ALT['rozdz-natynkowa-przepiecia-2'])}</div>
      <div class="szklo">
        <h2 class="t t-lewo">Niewidzialne serce domu</h2>
        <p>Dobrą instalację elektryczną poznaje się po tym, że się o niej nie myśli. Światło włącza się tam, gdzie sięga ręka, bezpiecznik nie wybija przy czajniku i piekarniku naraz, a rolety same opuszczają się wieczorem.</p>
        <p>Żeby tak było, myślimy o instalacji razem z inwestorem: o meblach, o tym, kto gdzie pracuje, co dojdzie za kilka lat – pompa ciepła, ładowarka, magazyn energii. Zapas na przyszłość kosztuje na etapie budowy niewiele, a później oszczędza kucia ścian.</p>
      </div>
    </div>
    <div class="rzad odwr">
      <div class="rzad-foto">{pic(p, 'pv-falownik-magazyn-huawei', ALT['pv-falownik-magazyn-huawei'])}</div>
      <div class="szklo">
        <h2 class="t t-lewo">Komponenty najwyższej klasy</h2>
        <p>Pracujemy na sprawdzonym sprzęcie od producentów, którzy dają serwis i aktualizacje na lata. W naszych realizacjach fotowoltaicznych pracują m.in. falowniki hybrydowe SolaX i Huawei z magazynami energii.</p>
        <p>Rozdzielnice wyposażamy w ochronę przeciwprzepięciową i zabezpieczenia dobrane do obwodów, a nie „takie, jakie były w hurtowni”. Wybór sprzętu zawsze uzasadniamy w wycenie.</p>
      </div>
    </div>
    <div class="rzad">
      <div class="rzad-foto">{pic(p, 'elektr-opisane-przewody', ALT['elektr-opisane-przewody'])}</div>
      <div class="szklo">
        <h2 class="t t-lewo">Dokumentacja, nie domysły</h2>
        <p>Każdy przewód opisujemy jeszcze w stanie surowym. Po zakończeniu prac zostawiamy schemat rozdzielnicy, opis obwodów i protokoły pomiarów.</p>
        <p>To zabezpiecza Ciebie – przy odbiorze, przy ubezpieczeniu, przy sprzedaży domu – i każdego elektryka, który kiedyś będzie przy tej instalacji pracował.</p>
      </div>
    </div>
  </div>
</section>

<section class="sekcja">
  <div class="wrap">
    <h2 class="t">Jak pracujemy</h2>
    <ol class="kroki szklo">{kroki}</ol>
  </div>
</section>
''' + kontakt_blok(p) + footer(p)

# ---------- KONTAKT ----------
def kontakt():
    p = '../'
    title = 'Kontakt – ATON, instalacje elektryczne | tel. 697 296 018'
    desc = 'Zadzwoń: +48 697 296 018 lub napisz: biuro@e-aton.pl. Wycena instalacji elektrycznej, smart home, fotowoltaiki, magazynu energii lub instalacji odgromowej.'
    return head(p, title, desc, 'kontakt/', [crumbs_ld('Kontakt', 'kontakt/')]) + header(p, 'kontakt/') + page_title('Kontakt') + f'''
<section class="sekcja sekcja-bliska">
  <div class="wrap kontakt-uklad">
    <div class="szklo kontakt-dane">
      <a class="neon-link duzy" href="tel:{TELH}"><span>Telefon</span>{TEL}</a>
      <a class="neon-link duzy" href="mailto:{MAIL}"><span>E-mail</span>{MAIL}</a>
      <hr>
      <h2 class="maly">Co warto przygotować przed rozmową</h2>
      <ul class="lista">
        <li>projekt domu albo rzuty pomieszczeń (może być zdjęcie z telefonu)</li>
        <li>etap budowy i planowany termin prac</li>
        <li>listę urządzeń, które mają się pojawić: pompa ciepła, płyta, ładowarka, klimatyzacja</li>
        <li>czy myślisz o smart home, fotowoltaice albo magazynie energii</li>
      </ul>
    </div>
    <div class="szklo">
      <h2 class="t t-lewo">Formularz kontaktowy</h2>
      {form_html('fk')}
    </div>
  </div>
</section>
''' + footer(p)

# ---------- pliki pomocnicze ----------
def extras():
    urls = ['', 'o-nas/', 'oferta/', 'realizacje/', 'kontakt/']
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         ''.join(f'  <url><loc>{BASE}{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(
        f'User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {BASE}sitemap.xml\n')

write('', home())
write('oferta', oferta())
write('realizacje', realizacje())
write('o-nas', onas())
write('kontakt', kontakt())
extras()
print('ok')
