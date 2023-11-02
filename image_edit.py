from PIL import Image, ImageDraw, ImageFont

def _create_rectangle(image, x1, y1, x2, y2, color):
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([x1, y1, x2, y2], fill=color, radius=20, width=0)

def _create_text(image, x, y, text, size, color):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/times.ttf", size)
    draw.text((x, y), text, fill=color, font=font)

def edit_advertisement(base_image, color, company_logo, punchline, button_text):
    
    WIDTH = 2160
    HEIGHT = 2160

    RECTANGLE_COLOR = color
    PAGE_COLOR = "#ffffff"

    BUTTON_TEXT = button_text.rjust(25)
    PUNCHLINE = punchline.rjust(20)


    new_image = Image.new('RGB', (WIDTH, HEIGHT), color = PAGE_COLOR)

    _create_rectangle(new_image, 100, -50, WIDTH-100, 20, RECTANGLE_COLOR)
    _create_rectangle(new_image, 100, HEIGHT-20, WIDTH-100, HEIGHT+50, RECTANGLE_COLOR)

    new_image.paste(Image.open(base_image), (573, 400))
    new_image.paste(Image.open(company_logo).resize((256,256)),(952, 100))

    _create_text(new_image, 420, 1500, PUNCHLINE, 150, RECTANGLE_COLOR)

    _create_rectangle(new_image, 573, 1800, 573+1024, 2000, RECTANGLE_COLOR)
    _create_text(new_image, 593, 1850, BUTTON_TEXT, 80, PAGE_COLOR)

    # new_image.save('pil_color.png')

    return new_image
