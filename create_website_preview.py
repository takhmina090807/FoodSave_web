from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

W,H=1500,810
OUT=Path('/Users/tahmina/Documents/Food Save/foodsave_website_preview.png')
photo=Image.open('/Users/tahmina/Documents/Food Save/public/images/restaurant-produce.png').convert('RGB')
canvas=Image.new('RGB',(W,H),'#f8f7f1')
d=ImageDraw.Draw(canvas)

def font(path,size): return ImageFont.truetype(path,size)
SANS='/System/Library/Fonts/Supplemental/Arial.ttf'
SANS_B='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
SERIF='/System/Library/Fonts/Supplemental/Georgia.ttf'
SERIF_B='/System/Library/Fonts/Supplemental/Georgia Bold.ttf'
# soft outer frame
for y in range(H):
    pass
# demo strip
d.rectangle((0,0,W,44),fill='#e7ede3')
d.text((W//2,22),'DEMO SITE  ·  Partner listings, offers and prices shown are examples',font=font(SANS_B,15),fill='#496750',anchor='mm')
# header
d.rectangle((0,44,W,134),fill='#f8f7f1')
d.line((0,133,W,133),fill='#e5e5db',width=2)
# brand mark
d.ellipse((78,70,119,111),fill='#174d3a')
d.ellipse((91,77,111,100),fill='#eaf0e8')
d.polygon([(91,98),(109,82),(104,104),(94,105)],fill='#eaf0e8')
d.text((132,90),'foodsave',font=font(SANS_B,30),fill='#174d3a',anchor='lm')
d.text((266,90),'.',font=font(SANS_B,30),fill='#82a581',anchor='lm')
nav=['Home','Explore Food','Nearby Map','Our Impact','For Restaurants','Delivery Partners','About Us']
x=470
for i,label in enumerate(nav):
    ff=font(SANS_B if i==0 else SANS,16)
    d.text((x,90),label,font=ff,fill='#174d3a' if i==0 else '#617067',anchor='lm')
    x+=d.textlength(label,font=ff)+28
# basket button
bbox=(1330,67,1450,113)
d.rounded_rectangle(bbox,radius=23,fill='#fffdf8',outline='#d6ddd3',width=2)
d.text((1390,90),'Basket',font=font(SANS_B,16),fill='#174d3a',anchor='mm')
# hero image crop
img=ImageOps.fit(photo,(596,455),method=Image.Resampling.LANCZOS,centering=(.55,.5))
mask=Image.new('L',(596,455),0); md=ImageDraw.Draw(mask); md.rounded_rectangle((0,0,595,454),radius=36,fill=255)
canvas.paste(img,(824,205),mask)
d=ImageDraw.Draw(canvas)
d.rectangle((824,570,1420,660),fill='#173b2c')
d.text((855,612),'TODAY’S GOODNESS, RESCUED.',font=font(SANS_B,15),fill='#ffffff',anchor='lm')
# floating offer badge
d.rounded_rectangle((785,260,1060,335),radius=12,fill='#fffdf8',outline='#ebe8df',width=1)
d.ellipse((803,279,838,314),fill='#f8eadc')
d.text((820,297),'%',font=font(SANS_B,19),fill='#be7840',anchor='mm')
d.text((852,283),'Up to 50% off',font=font(SANS_B,16),fill='#314b3a')
d.text((852,307),'on good food today',font=font(SANS,13),fill='#829087')
# hero text left
d.text((105,215),'GOOD FOOD. BETTER FUTURE.',font=font(SANS_B,14),fill='#69816f')
d.line((105,246,144,246),fill='#8aab8f',width=2)
d.text((105,279),'Save food.',font=font(SERIF,64),fill='#20392d')
d.text((105,346),'Save money.',font=font(SERIF,64),fill='#6f9679')
copy=['Discover fresh meals from your favourite local','restaurants at better prices. Eat well, waste less,','and make a difference.']
for i,line in enumerate(copy): d.text((107,443+i*31),line,font=font(SANS,19),fill='#69766e')
# buttons
d.rounded_rectangle((105,555,282,612),radius=6,fill='#174d3a')
d.text((193,584),'Explore meals',font=font(SANS_B,17),fill='#ffffff',anchor='mm')
d.text((310,584),'Become a partner',font=font(SANS_B,16),fill='#174d3a',anchor='lm')
# search band
d.rounded_rectangle((105,682,1420,756),radius=8,fill='#fffefa',outline='#edede5',width=2)
d.ellipse((118,703,144,729),outline='#4f7359',width=3)
d.line((139,725,151,737),fill='#4f7359',width=3)
d.text((184,705),'Find something good',font=font(SANS_B,15),fill='#465b4d')
d.text((184,733),'Search meals, restaurants or neighbourhoods',font=font(SANS,13),fill='#8b958b')
d.line((760,696,760,742),fill='#e4e5dc',width=2)
d.text((800,705),'NEARBY',font=font(SANS_B,11),fill='#9aa399')
d.text((800,733),'Dubai, UAE  ·  demo location',font=font(SANS_B,15),fill='#475b4b')
# frame border
frame=ImageDraw.Draw(canvas)
frame.rounded_rectangle((1,1,W-2,H-2),radius=6,outline='#dcded5',width=2)
canvas.save(OUT,optimize=True)
print(OUT)
