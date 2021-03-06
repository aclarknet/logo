# Via https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#

# Fonts via https://github.com/python-pillow/Pillow/tree/master/Tests/fonts

import os
import sys

from PIL import Image, ImageDraw, ImageFont

# create an image
def create_image(filename):
    """
    Create image
    """

    out = Image.new("RGBA", (600, 600), (0, 0, 0, 0))
    # get a font
    fnt = ImageFont.truetype(filename, 100)
    print(filename)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # https://www.geeksforgeeks.org/python-pil-imagedraw-draw-rectangle/
    w, h = 500, 50
    shape = [(40, 40), (w - 10, h - 10)]
    # d.rectangle(shape, fill=(255, 255, 255, 0), outline="white")

    # draw multiline text
    # White text
    # d.multiline_text((15, -15), "ACLARKNET", font=fnt, fill=(255, 255, 255))
    # Black text
    d.multiline_text((20, 220), "ACLARK.NET", font=fnt, fill=(0, 0, 0))

    fontname = filename.split(".")[0]  # Remove file extension
    out.save("logo_NotoSans-Regular.png", "PNG")


if __name__ == "__main__":

    # files = [f for f in os.listdir(".") if f.endswith("ttf")]
    # for filename in files:

    create_image("NotoSans-Regular.ttf")
