n = int(3)
k = int(1)
spisok =["привет", "привет2", "привет3" ]
def f(spisok):
    return f
l = ('ghbdtn')
for i in range(3):
    from PIL import Image, ImageDraw, ImageFont

    im = Image.new('RGB', (200,200), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Windows/Fonts/Book Antiqua/ANTQUAB.TTF', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
            (100,100),
        l ,
        font=font,    
        fill=('#1C0606')
        )
    im.show()
    if k == 1:
        from PIL import Image
        im = Image.new('RGB', (200,200), color=('#FAACAC'))
        im.save('C:/прорамма/картинка.jpg')
    k = k + 1
    if k == 2:
        from PIL import Image
        im = Image.new('RGB', (200,200), color=('#FAACAC'))
        im.save('C:/прорамма/картинка1.jpg')
    if k == 3:
        from PIL import Image
        im == Image.new('RGB', (200,200), color=('#FAACAC'))
        im.save('C:/прорамма/картинка3.jpg')
