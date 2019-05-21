import itertools
from contextlib import contextmanager
import cStringIO
from PIL import Image, ImageDraw

def get_input(x, y):
    return itertools.product(xrange(x), xrange(y))


with open("test.png", "w") as f:
    LENGTH=4096
    im = Image.new("RGB", (LENGTH, LENGTH))

    inp = get_input(LENGTH, LENGTH)

    for r in xrange(255):
        for b in xrange(255):
            for g in xrange(255):
                x, y = inp.next()
                im.putpixel((x, y), (r, b, g))

    # write to stdout
    im.save(f, "PNG")
