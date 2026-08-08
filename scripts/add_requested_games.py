from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import hashlib, math, random

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'covers_webp'; OUT.mkdir(exist_ok=True)
# title, filename, genre, year, status, tags
GAMES=[
("An Eggstremely Hard Game","An_Eggstremely_Hard_Game","Казуальные",2026,"planned",["coop"]),
("Crushed In Time","Crushed_In_Time","Головоломки",2026,"done",["coop"]),
("BOKURA: planet","BOKURA_planet","Головоломки",2025,"planned",["coop"]),
("Cuphead","Cuphead","Экшены",2017,"planned",["coop"]),
("Biped 2","Biped_2","Головоломки",2025,"planned",["coop"]),
("MOUSE: P.I. For Hire","MOUSE_PI_For_Hire","Экшены",2026,"planned",[]),
("The Stanley Parable: Ultra Deluxe","The_Stanley_Parable_Ultra_Deluxe","Приключения",2022,"planned",[]),
("Resident Evil HD Remaster","Resident_Evil_HD_Remaster","Хоррор",2015,"planned",[]),
("Resident Evil 2","Resident_Evil_2","Хоррор",2019,"planned",[]),
("Resident Evil 3","Resident_Evil_3","Хоррор",2020,"planned",[]),
("Resident Evil 4","Resident_Evil_4","Хоррор",2023,"planned",[]),
("Resident Evil 7 biohazard","Resident_Evil_7","Хоррор",2017,"planned",[]),
("Resident Evil Village","Resident_Evil_Village","Хоррор",2021,"planned",[]),
("Resident Evil Code: Veronica Remake","Resident_Evil_Code_Veronica_Remake","Хоррор",2027,"planned",[]),
("A Plague Tale: Innocence","A_Plague_Tale_Innocence","Приключения",2019,"planned",[]),
("The Quarry","The_Quarry","Хоррор",2022,"done",[]),
("Trine","Trine","Приключения",2009,"done",["coop"]),
("Trine 2","Trine_2","Приключения",2011,"done",["coop"]),
("BrokenLore: FOLLOW","BrokenLore_FOLLOW","Хоррор",2025,"planned",[]),
("Creepy Tale 2","Creepy_Tale_2","Приключения",2021,"done",[]),
("Creepy Tale 3: Ingrid Penance","Creepy_Tale_3","Приключения",2023,"done",[]),
("Creepy Tale: Some Other Place","Creepy_Tale_Some_Other_Place","Приключения",2024,"done",[]),
("Strange Horticulture","Strange_Horticulture","Головоломки",2022,"done",[]),
("Strange Antiquities","Strange_Antiquities","Головоломки",2025,"planned",[]),
("Directive 8020","Directive_8020","Хоррор",2026,"planned",[]),
("Devil May Cry","Devil_May_Cry","Экшены",2001,"playing",[]),
("Cat Quest II","Cat_Quest_II","Приключения",2019,"planned",["coop"]),
("Beyond: Two Souls","Beyond_Two_Souls","Приключения",2013,"playing",[]),
("Brothers: A Tale of Two Sons Remake","Brothers_Remake","Приключения",2024,"planned",["coop"]),
("Quarantine Zone: The Last Check","Quarantine_Zone","Симуляторы",2026,"done",[]),
("Still Wakes the Deep","Still_Wakes_the_Deep","Хоррор",2024,"planned",[]),
("Call of Cthulhu","Call_of_Cthulhu","Хоррор",2018,"done",[]),
("Planet of Lana","Planet_of_Lana","Приключения",2023,"planned",[]),
("Pathologic 3","Pathologic_3","Приключения",2026,"planned",[]),
("Tails Noir","Tails_Noir","Приключения",2021,"planned",[]),
("Heavy Rain","Heavy_Rain","Приключения",2010,"planned",[]),
("HAAK","HAAK","Экшены",2022,"planned",[]),
("TUNIC","TUNIC","Приключения",2022,"planned",[]),
("Slender Threads","Slender_Threads","Приключения",2025,"planned",[]),
("Bum Simulator","Bum_Simulator","Симуляторы",2023,"planned",[]),
("Outlast 2","Outlast_2","Хоррор",2017,"planned",[]),
("Sherlock Holmes: Crimes and Punishments","Sherlock_Holmes_Crimes_and_Punishments","Приключения",2014,"planned",[]),
("The Witcher 3: Wild Hunt","The_Witcher_3_Wild_Hunt","Ролевые",2015,"planned",[]),
]

def font(size,bold=False):
    p='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p,size)

def cover(title, slug, genre, year):
    W,H=600,800; seed=int(hashlib.sha1(title.encode()).hexdigest()[:8],16); r=random.Random(seed)
    palettes=[((12,10,30),(111,65,175)),((8,27,36),(18,126,130)),((38,12,20),(178,44,64)),((25,22,8),(191,137,35)),((9,27,17),(50,125,75))]
    a,b=palettes[seed%len(palettes)]
    im=Image.new('RGB',(W,H)); px=im.load()
    for y in range(H):
      t=y/(H-1)
      for x in range(W):
        glow=max(0,1-math.hypot(x-W*.62,y-H*.43)/(W*.75))*.28
        px[x,y]=tuple(int(a[i]*(1-t*.45-glow)+b[i]*(t*.55+glow)) for i in range(3))
    d=ImageDraw.Draw(im,'RGBA')
    for _ in range(55):
      x,y=r.randrange(W),r.randrange(H); rr=r.randrange(1,7)
      d.ellipse((x-rr,y-rr,x+rr,y+rr),fill=(220,190,255,r.randrange(18,80)))
    # Character portrait, softly blended into each game-coloured world.
    av=Image.open(ROOT/'assets/avatar-320.jpg').convert('RGB').resize((510,510),Image.Resampling.LANCZOS)
    av=ImageEnhance.Color(av).enhance(.72)
    mask=Image.new('L',av.size,0); md=ImageDraw.Draw(mask); md.ellipse((-50,-20,560,600),fill=230); mask=mask.filter(ImageFilter.GaussianBlur(28))
    im.paste(av,(90,165),mask)
    d=ImageDraw.Draw(im,'RGBA'); d.rectangle((0,0,W,190),fill=(5,4,15,205)); d.rectangle((0,620,W,H),fill=(5,4,15,220))
    d.line((40,174,560,174),fill=(*b,230),width=3)
    # Fit wrapped exact title.
    words=title.split(); lines=[]; cur=''
    f=font(50,True)
    for w in words:
      test=(cur+' '+w).strip()
      if d.textbbox((0,0),test,font=f)[2] > 520 and cur: lines.append(cur); cur=w
      else: cur=test
    lines.append(cur)
    while len(lines)>3:
      f=font(f.size-3,True); lines=[]; cur=''
      for w in words:
       test=(cur+' '+w).strip()
       if d.textbbox((0,0),test,font=f)[2]>530 and cur: lines.append(cur); cur=w
       else: cur=test
      lines.append(cur)
    total=len(lines)*(f.size+3); yy=(180-total)//2
    for line in lines:
      box=d.textbbox((0,0),line,font=f,stroke_width=2); x=(W-(box[2]-box[0]))//2
      d.text((x,yy),line,font=f,fill=(247,241,255),stroke_width=3,stroke_fill=(8,4,18)); yy+=f.size+3
    d.text((42,675),genre.upper(),font=font(20,True),fill=(*b,255))
    d.text((42,714),str(year),font=font(34,True),fill=(255,255,255,235))
    d.text((558,720),'L',font=font(58,True),anchor='rs',fill=(215,183,255,115))
    im.save(OUT/f'{slug}.webp','WEBP',quality=87,method=6)

if __name__ == '__main__':
    for g in GAMES:
        cover(g[0],g[1],g[2],g[3])
    print(f'Generated {len(GAMES)} covers')
