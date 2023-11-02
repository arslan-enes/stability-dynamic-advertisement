from PIL import Image, ImageDraw, ImageFont

def create_rectangle(image, x1, y1, x2, y2, color):
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([x1, y1, x2, y2], fill=color, radius=20, width=0)

def create_text(image, x, y, text, size, color):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/times.ttf", size)
    draw.text((x, y), text, fill=color, font=font)

WIDTH = 2160
HEIGHT = 2160

RECTANGLE_COLOR = "#21313c"
PAGE_COLOR = "#ffffff"

new_image = Image.new('RGB', (WIDTH, HEIGHT), color = PAGE_COLOR)

create_rectangle(new_image, 100, -50, WIDTH-100, 20, RECTANGLE_COLOR)
create_rectangle(new_image, 100, HEIGHT-20, WIDTH-100, HEIGHT+50, RECTANGLE_COLOR)

new_image.paste(Image.open('base_images/coffecup.png'), (573, 400))
new_image.paste(Image.open('logos/coffe-logo.png').resize((256,256)),(952, 100))

create_text(new_image, 420, 1500, "Coffee Coffee Coffee", 150, RECTANGLE_COLOR)

create_rectangle(new_image, 573, 1800, 573+1024, 2000, RECTANGLE_COLOR)
create_text(new_image, 593, 1850, "Every cup is a masterpiece!  >", 80, PAGE_COLOR)

new_image.save('pil_color.png')
