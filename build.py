#!/usr/bin/env python3
import os, json

def cells(folder, title, ratio):
    fs=sorted(os.listdir(folder))
    return ''.join(f'<button class="cell" style="aspect-ratio:{ratio}" data-src="{folder}/{f}" data-set="{title}" data-i="{i}"><img src="{folder}/{f}" loading="lazy" alt=""></button>' for i,f in enumerate(fs)), len(fs)

carousels=sorted([d for d in os.listdir('cs') if d.startswith('carousel-')], key=lambda d:int(d.split('-')[1]))
names={
'carousel-1-presentation':'презентация','carousel-2-images':'образы','carousel-3-colors':'цвета',
'carousel-4-details':'детали','carousel-5-mixes':'миксы','carousel-6-photosession':'фотосессия',
'carousel-7-colors':'три цвета','carousel-8-fabric':'фактура','carousel-9-morning':'утро дома',
'carousel-10-lookbook':'ракурсы','carousel-11-constructor':'конструктор','carousel-12-scenes':'три сцены',
'carousel-13-stilllife':'натюрморт','carousel-14-layouts':'без модели'}
sec=[]
for d in carousels:
    n=int(d.split('-')[1]); title=names.get(d,d)
    c,k=cells('cs/'+d,f'Карусель {n} · {title}','4/5')
    sec.append(f'<section class="sec"><h3>Карусель {n} · {title} <span>{k}</span></h3><div class="grid">{c}</div></section>')
sc,sk=cells('cs/stories-1-layouts','Сторис · лайауты','9/16')
pc,pk=cells('photo','Фотосессия · блондинка','4/5')
html=f'''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>WOOGEE SUITE — для Леры</title>
<style>
:root{{--paper:#f6f3ec;--ink:#191814;--muted:#7b756b;--line:#e5dfd2}}
*{{box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
header{{padding:22px 16px 8px}}
h1{{font-size:26px;margin:0 0 4px;letter-spacing:-.02em}}
.sub{{color:var(--muted);font-size:14px}}
.hint{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 14px;font-size:14px;color:#4a453d;margin-top:12px}}
.hint b{{color:var(--ink)}}
nav.menu{{position:sticky;top:0;z-index:20;background:var(--paper);display:flex;gap:6px;padding:10px 16px;border-bottom:1px solid var(--line);overflow-x:auto}}
nav.menu a{{flex:0 0 auto;background:#ece7db;color:var(--ink);text-decoration:none;padding:8px 14px;border-radius:999px;font-size:13px;font-weight:600}}
.sec{{padding:6px 16px 16px}}
h2{{font-size:20px;margin:18px 16px 6px}}
h3{{font-size:14px;margin:14px 0 8px;font-weight:600}}
h3 span{{color:var(--muted);font-weight:400;font-size:12px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}}
.grid.s{{grid-template-columns:repeat(4,1fr)}}
.cell{{padding:0;border:0;background:#e9e3d6;border-radius:8px;overflow:hidden;cursor:pointer}}
.cell img{{width:100%;height:100%;object-fit:cover;display:block}}
#lb{{position:fixed;inset:0;background:#0f0e0c;display:none;z-index:50;flex-direction:column}}
#lb.on{{display:flex}}
#lb .top{{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;color:#f3eee3;font-size:13px}}
#lb .close{{background:rgba(255,255,255,.12);border:0;color:#fff;font-size:20px;width:40px;height:40px;border-radius:50%}}
#lb .stage{{flex:1;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:0 6px}}
#lb img{{max-width:100%;max-height:100%;object-fit:contain}}
#lb .bottom{{padding:12px 14px 26px;color:#cfc7b8;font-size:12px;text-align:center}}
#lb nav{{position:absolute;top:50%;width:100%;display:flex;justify-content:space-between;pointer-events:none}}
#lb nav button{{pointer-events:auto;background:rgba(255,255,255,.12);border:0;color:#fff;font-size:24px;width:44px;height:64px;border-radius:12px;margin:0 8px}}
footer{{padding:10px 16px 40px;color:var(--muted);font-size:12px}}
</style></head><body>
<header>
  <h1>WOOGEE SUITE</h1>
  <div class="sub">{len(carousels)} каруселей · сторис · фотосессия</div>
  <div class="hint"><b>Сохранить в «Фото»:</b> тап на кадр → удерживай палец → «Сохранить в Фото».</div>
</header>
<nav class="menu"><a href="#carousels">Карусели</a><a href="#stories">Сторис</a><a href="#photo">Фотосессия</a></nav>
<h2 id="carousels">Карусели</h2>
{''.join(sec)}
<h2 id="stories">Сторис · лайауты</h2>
<section class="sec"><div class="grid s">{sc}</div></section>
<h2 id="photo">Фотосессия</h2>
<section class="sec"><div class="grid">{pc}</div></section>
<footer>Черновики на утверждение. Не опубликовано.</footer>
<div id="lb"><div class="top"><span id="lbt"></span><button class="close" onclick="closeLb()">✕</button></div>
<div class="stage"><img id="lbi" src="" alt=""></div>
<nav><button onclick="step(-1)">‹</button><button onclick="step(1)">›</button></nav>
<div class="bottom">удерживай картинку → «Сохранить в Фото»</div></div>
<script>
let cur=0,list=[];
function openLb(src,setName,i){{
  const all=[...document.querySelectorAll('.cell')]; list=all.map(c=>c.dataset.src);
  cur=all.findIndex(c=>c.dataset.src===src);
  document.getElementById('lbi').src=src;
  document.getElementById('lbt').textContent=setName+' · '+(i+1)+' из '+all.filter(c=>c.dataset.set===setName).length;
  document.getElementById('lb').classList.add('on');
}}
function step(d){{ cur=(cur+d+list.length)%list.length; document.getElementById('lbi').src=list[cur]; }}
function closeLb(){{ document.getElementById('lb').classList.remove('on'); }}
document.addEventListener('click',e=>{{const c=e.target.closest('.cell'); if(c) openLb(c.dataset.src,c.dataset.set,parseInt(c.dataset.i));}});
document.addEventListener('keydown',e=>{{if(e.key==='Escape') closeLb(); if(e.key==='ArrowRight') step(1); if(e.key==='ArrowLeft') step(-1);}});
</script></body></html>'''
open('index.html','w').write(html)
print('ok', len(carousels), sk, pk, len(html))
