#!/usr/bin/env python

# http://www.pythonware.com/library/pil/handbook/image.htm

from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + "-thumbnail" + ext, "JPEG")
