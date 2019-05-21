import itertools
from contextlib import contextmanager
import cStringIO
from PIL import Image, ImageDraw

LENGTH=4096
STEP=1

def get_input(x, y):
    return itertools.product(xrange(x), xrange(y))


def get_xy():
    # map NxN squares at a time
    for q in xrange(0, LENGTH, STEP):
        for z in xrange(0, LENGTH, STEP):
            for x in xrange(STEP):
                for y in xrange(STEP):
                    yield (q + x, z + y)


def get_rbg(r, b, g):
    return r, b, g


def do_draw(xy, draw):
    for r in xrange(255):
        for g in xrange(255):
            for b in xrange(255):
                try:
                    xy_p = xy.next()
                except StopIteration:
                    return
                draw.point(xy_p, (r, g, b))


if __name__ == '__main__':
    print len(list(get_xy()))
    im = Image.new("RGB", (LENGTH, LENGTH))
    draw = ImageDraw.Draw(im)

    xy = get_xy()

    do_draw(xy, draw)
    del draw

    # write to stdout
with open("test.png", "w") as f:
    im.save(f, "PNG")
