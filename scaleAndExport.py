from gimpfu import *
import gimp
import os
import sys

def resize_and_export(filename, size):
    # Remove extension (.xcf).
    fn = filename[0:-4]
    pdb.gimp_message(fn)
    # Open file.
    img = pdb.gimp_file_load(filename, filename, run_mode=RUN_NONINTERACTIVE)
    # Get first layer.
    ly = img.layers[0]
    # Scale image to size x size.
    pdb.gimp_image_scale(img, size, size)
    # Merge visible layers.
    newlayer = img.merge_visible_layers(0)
    # Save as png.
    pngfile = "%s_%s.png" % (fn, size)
    pdb.file_png_save(img, newlayer, pngfile, pngfile, 1, 0, 0, 0, 0, 0, 0)

pwd = os.getcwdu()
files = os.listdir(pwd)
for f in files:
    if f.endswith('.xcf'):
        resize_and_export(os.path.join(pwd, f), 64)
