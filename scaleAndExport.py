from gimpfu import *
import gimp
import os
import sys

def resize_and_export(filename, size):
    fn = filename[0:-4]
    pdb.gimp_message(fn)
    img = pdb.gimp_file_load(filename, filename, run_mode=RUN_NONINTERACTIVE)
    #pdb.gimp_message(img.layers)
    ly = img.layers[0]
    #pdb.gimp_by_color_select(ly, gimpcolor.RGB(254, 254, 254), 0, CHANNEL_OP_REPLACE, False, False, 0, False)
    #pdb.gimp_edit_clear(ly)
    xcffile = "%s_%s.xcf" % (fn, size)
    #pdb.gimp_file_save(img, ly, xcffile, xcffile)

    pdb.gimp_image_scale(img, size, size)
    #xcffile = "%s_%s.xcf" % (fn, size)
    #pdb.gimp_file_save(img, ly, xcffile, xcffile)
    newlayer = img.merge_visible_layers(0)
    pngfile = "%s_%s.png" % (fn, size)
    pdb.file_png_save(img, newlayer, pngfile, pngfile, 1, 0, 0, 0, 0, 0, 0)

pwd = os.getcwdu()
files = os.listdir(pwd)
for f in files:
    if f.endswith('.xcf'):
        resize_and_export(os.path.join(pwd, f), 64)
