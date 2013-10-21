from gimpfu import *
import gimp

def create_txt_img(text, file):
    img = gimp.Image(768,768,RGB)
    bg = gimp.Layer(img, "BG", 768, 768, 1, 0, 0)
    img.add_layer(bg)
    gimp.set_foreground(100, 100, 100)
    textlayer=pdb.gimp_text_fontname(
				img,
				None, #layer,
				200,
				-20,
				text,
				-1,   #border
				True, #anitalias
				288,   #size
				0, #GIMP_PIXELS
				'Sans Bold')
    textlayer.add_alpha()
    xcffile = file + ".xcf"
    pdb.gimp_file_save(img, textlayer, xcffile, xcffile)
    pdb.gimp_image_scale(img, 64, 64)
    xcffile = file + "_64.xcf"
    pdb.gimp_file_save(img, textlayer, xcffile, xcffile)
    newlayer = img.merge_visible_layers(0)
    pngfile = file + ".png"
    pdb.file_png_save(img, newlayer, pngfile, pngfile, 1, 0, 0, 0, 0, 0, 0)

for d in ("Ich", "Du", "er"):
    create_txt_img(d, d)
