pip install Pillow
n = int()
while n != 10:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new ('RGB', (200,200), color=('#FAACAC'))
    # Создаем объект со шрифтом
    font = ImageFont.truetype('D:/Roboto-Black.ttf', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
     (100, 100),
        'Текст 18px',
        # Добавляем шрифт к изображению
        font=font,
        fill='#1C0606')
        # Ширина и высота
    im.size
    # Ширина
    im.width
    # Высота
    im.height
    im.show()
    im.save('D:/new_pic.jpg')