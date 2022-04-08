# filename crop_image
from PIL import Image

colors_to_replace = [
    (112, 98, 43, 255),
    (213, 173, 22, 255),
    (199, 163, 25, 255),
    (226, 183, 20, 255),
    (116, 101, 42, 255),
    (211, 172, 23, 255)
    ]

colors = set()

def crop(path):
    img = Image.open(path)
    # img = img.crop((1290, 310, 2620, 790))
    img = img.crop((1290, 330, 2600, 820))
    img = img.convert("RGBA")
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            colors.add(pixdata[x, y])
            if pixdata[x, y] in colors_to_replace:
            # if pixdata[x, y][0] > 100 and pixdata[x, y][2] < 50:
                pixdata[x, y] = (50, 52, 55, 255)
    img.save("cropped.png", format="png")
    return "cropped.png"
