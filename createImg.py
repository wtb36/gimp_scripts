from gimpfu import *
import gimp

def create_txt_img(text, file):
    img = gimp.Image(768,768,RGB)
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

for d in ("Ich", "Du", "er"):
    create_txt_img(d, d)
