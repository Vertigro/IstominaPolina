from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (200,200), color=('#CCFFFF'))
im.show()
font = ImageFont.truetype('C:/142/Roboto-Black.ttf', size=18)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (100, 100),
    'Текст 18px',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
im.show()
