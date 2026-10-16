(function(){
  /* menu */
  var top=document.querySelector('.top'),btn=document.querySelector('.burger'),menu=document.getElementById('menu');
  function sc(){top.classList.toggle('scroll',window.scrollY>40)}
  sc();window.addEventListener('scroll',sc,{passive:true});
  btn.addEventListener('click',function(){var o=menu.classList.toggle('open');btn.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''});
  menu.addEventListener('click',function(e){if(e.target.tagName==='A'){menu.classList.remove('open');btn.setAttribute('aria-expanded',false);document.body.style.overflow=''}});

  /* filtr realizacji */
  var mur=document.getElementById('mur'),filtry=document.querySelectorAll('.filtry button');
  function filtruj(k){
    filtry.forEach(function(b){b.classList.toggle('on',b.dataset.k===k)});
    mur.querySelectorAll('.fot').forEach(function(f){f.classList.toggle('ukryte',k!=='*'&&f.dataset.k!==k)});
  }
  if(mur){
    filtry.forEach(function(b){b.addEventListener('click',function(){filtruj(b.dataset.k);history.replaceState(null,'',b.dataset.k==='*'?location.pathname:'#'+b.dataset.k)})});
    var h=location.hash.slice(1);if(h&&document.querySelector('.filtry [data-k="'+h+'"]'))filtruj(h);
  }

  /* lightbox */
  var lb=document.getElementById('lb'),lbi=lb.querySelector('img'),lbc=lb.querySelector('figcaption'),lista=[],idx=0;
  function pokaz(i){idx=(i+lista.length)%lista.length;var a=lista[idx];lbi.src=a.getAttribute('href');lbi.alt=a.dataset.cap;lbc.textContent=a.dataset.cap}
  document.addEventListener('click',function(e){
    var a=e.target.closest('a.fot');if(!a)return;e.preventDefault();
    lista=Array.prototype.filter.call(a.parentNode.querySelectorAll('a.fot'),function(x){return !x.classList.contains('ukryte')});
    pokaz(lista.indexOf(a));lb.hidden=false;document.body.style.overflow='hidden';lb.querySelector('.lb-x').focus();
  });
  function zamknij(){lb.hidden=true;document.body.style.overflow=''}
  lb.querySelector('.lb-x').onclick=zamknij;
  lb.querySelector('.lb-p').onclick=function(){pokaz(idx-1)};
  lb.querySelector('.lb-n').onclick=function(){pokaz(idx+1)};
  lb.addEventListener('click',function(e){if(e.target===lb)zamknij()});
  document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')zamknij();if(e.key==='ArrowLeft')pokaz(idx-1);if(e.key==='ArrowRight')pokaz(idx+1)});
  var tx=0;lb.addEventListener('touchstart',function(e){tx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){var d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>50)pokaz(idx+(d<0?1:-1))});

  /* spis oferty – podświetlenie bieżącej sekcji */
  var spis=document.querySelectorAll('.spis a');
  if(spis.length&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){spis.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+x.target.id)})}})},{rootMargin:'-40% 0px -55% 0px'});
    document.querySelectorAll('.usluga').forEach(function(s){io.observe(s)});
  }

  /* formularz – w demie otwiera wiadomość e-mail */
  document.querySelectorAll('form.form').forEach(function(f){
    var t=new URLSearchParams(location.search).get('temat');
    if(t){var el=document.querySelector('.spis a[href="#'+t+'"]'),txt=null;
      document.querySelectorAll('.stopka a[href$="#'+t+'"]').forEach(function(a){txt=a.textContent});
      if(txt)Array.prototype.forEach.call(f.temat.options,function(o){if(o.text===txt)o.selected=true})}
    f.addEventListener('submit',function(e){
      e.preventDefault();var info=f.querySelector('.form-info');
      if(!f.imie.value.trim()||!f.tel.value.trim()){info.textContent='Podaj imię i numer telefonu – oddzwonimy.';return}
      if(!f.querySelector('.zgoda input').checked){info.textContent='Zaznacz zgodę na kontakt.';return}
      var body='Imię i nazwisko: '+f.imie.value+'\nTelefon: '+f.tel.value+'\nE-mail: '+f.email.value+'\nTemat: '+f.temat.value+'\nMiejscowość: '+f.miejsce.value+'\nEtap: '+f.etap.value+'\n\n'+f.msg.value;
      location.href='mailto:biuro@e-aton.pl?subject='+encodeURIComponent('Zapytanie ze strony – '+f.temat.value)+'&body='+encodeURIComponent(body);
      info.textContent='Dziękujemy. Otwieramy Twój program pocztowy z gotową wiadomością.';
    });
  });
})();
(function(){try{if(String(location.protocol).indexOf('http')!==0)return;try{if(/[?&#]team=1/.test(location.search+location.hash)){localStorage.setItem('nb_team','1');}}catch(e){}try{if(localStorage.getItem('nb_team')==='1')return;}catch(e){}if((document.referrer||'').indexOf('crm-newbeginning')>-1)return;try{if(navigator.webdriver)return;}catch(e){}try{if(/^https?:\/\/(kris20032|impulseo-pl)\.github\.io\/?$/i.test(document.referrer||''))return;}catch(e){}if(sessionStorage.getItem('_dv'))return;sessionStorage.setItem('_dv','1');var seg=(location.pathname.split('/').filter(Boolean)[0])||'';var base=location.origin+(seg?('/'+seg):'');var ua='';try{ua=(navigator.userAgent||'').slice(0,300);}catch(e){}var EP='https://zngfubfinbojfgaxdrbf.supabase.co/rest/v1/demo_views';var KEY='sb_publishable_MWwoyGlSCWnJ4awtOPF0ow_ZVS0Y8qK';function send(g){try{fetch(EP,{method:'POST',keepalive:true,headers:{'Content-Type':'application/json','apikey':KEY,'Authorization':'Bearer '+KEY,'Prefer':'return=minimal'},body:JSON.stringify({demo_url:base,page:location.pathname,referrer:(document.referrer||null),user_agent:(ua||null),ip:(g&&g.ip)||null,country:(g&&g.cc)||null,city:(g&&g.city)||null})}).catch(function(){});}catch(e){}}var done=false;function once(g){if(done)return;done=true;send(g);}try{var t=setTimeout(function(){once(null);},1500);fetch('https://ipwho.is/?fields=ip,success,country_code,city',{cache:'no-store'}).then(function(r){return r.json();}).then(function(d){clearTimeout(t);once(d&&d.success!==false?{ip:d.ip,cc:d.country_code,city:d.city}:null);}).catch(function(){clearTimeout(t);once(null);});}catch(e){once(null);}}catch(e){}})();
