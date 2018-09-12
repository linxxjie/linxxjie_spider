import random
from PIL import Image, ImageFont, ImageDraw

width = 80
height = 40

# 字体
font = ImageFont.truetype('D:\\workplace\\web\\FURUNO_ FS1570-NBDP\\font\\common.ttf', 28)

# 颜色
image = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)
for t in range(4):
    num = random.randint(0, 9)
    draw.text((20*t, 10), str(num), font=font, fill=(44, 187, 15))

image.save('E:\spider\image\yanzhengma.jpg')