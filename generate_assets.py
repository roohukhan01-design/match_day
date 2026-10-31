from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
p=Path('assets');p.mkdir(exist_ok=True)
def draw_icon(size,transparent=False):
 im=Image.new('RGBA',(size,size),(0,0,0,0) if transparent else (8,25,30,255))
 d=ImageDraw.Draw(im)
 k=size/1024
 if not transparent:d.rounded_rectangle((42*k,42*k,982*k,982*k),radius=220*k,fill=(15,116,82,255))
 d.ellipse((200*k,200*k,824*k,824*k),fill='white')
 d.polygon([(512*k,342*k),(645*k,439*k),(594*k,600*k),(430*k,600*k),(379*k,439*k)],fill=(9,59,64,255))
 for x,y in [(512,250),(740,430),(655,710),(365,710),(280,430)]:
  d.line((512*k,512*k,x*k,y*k),fill=(9,59,64,255),width=max(2,int(24*k)))
 return im
draw_icon(1024).save(p/'icon-only.png')
draw_icon(1024,True).save(p/'icon-foreground.png')
Image.new('RGBA',(1024,1024),(8,25,30,255)).save(p/'icon-background.png')
for name,bg in [('splash.png',(242,247,247,255)),('splash-dark.png',(7,13,18,255))]:
 im=Image.new('RGBA',(2732,2732),bg)
 logo=draw_icon(760);im.alpha_composite(logo,((2732-760)//2,(2732-760)//2))
 im.save(p/name)
print('Generated MatchDay build assets')
