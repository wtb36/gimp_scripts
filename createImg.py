from gimpfu import *
import gimp

base_size = 768
xoffset = 48
yoffset = 192

xoffset1 = 48
yoffset1 = 32

xoffset2 = 48
yoffset2 = (base_size - yoffset1) / 2 - 20

xoffsetVc = 410
yoffsetVc = -20

def create_text_layer(img, text, xo, yo, fontsize = 288):
    textlayer=pdb.gimp_text_fontname(
				img,
				None, #layer,
				xo,
				yo,
				text,
				-1,   #border
				True, #anitalias
				fontsize,   #size
				0, #GIMP_PIXELS
				'Sans Bold')
    textlayer.add_alpha()
    textlayer.resize(base_size - (xo if xo > 0 else 0), base_size - (yo if yo > 0 else 0), xo if xo < 0 else 0, yo if yo < 0 else 0)
    return textlayer


def create_txt_img(text1, text2, isVc, file, size=64):
    img = gimp.Image(base_size, base_size, RGB)
    bg = gimp.Layer(img, "BG", base_size, base_size, 1, 0, 0)
    img.add_layer(bg)

    gimp.set_foreground(200, 200, 200)
    if isVc:
        textlayer = create_text_layer(img,"0190361480376248", 0, 0, 72)
        textlayer = create_text_layer(img,"0190361483028370", 0, 80, 72)
        textlayer = create_text_layer(img,"0190361048291837", 0, 160, 72)
        textlayer = create_text_layer(img,"0190361381023847", 0, 240, 72)
        textlayer = create_text_layer(img,"0190361183940283", 0, 320, 72)
        textlayer = create_text_layer(img,"0190361467502374", 0, 400, 72)
        textlayer = create_text_layer(img,"0190361193849387", 0, 480, 72)
        textlayer = create_text_layer(img,"0190361402837463", 0, 560, 72)
        textlayer = create_text_layer(img,"0190361203476283", 0, 640, 72)
        textlayer = create_text_layer(img,"0190361203476283", 0, 720, 72)

    gimp.set_foreground(0, 97, 160)

    if text2:
	textlayer = create_text_layer(img, text1, xoffset1, yoffset1)
        textlayer = create_text_layer(img, text2, xoffset2, yoffset2)
    else:
	textlayer = create_text_layer(img, text1, xoffset, yoffset)


    if isVc:
        gimp.set_foreground(100, 100, 100)
        textlayer = create_text_layer(img, "VC", xoffsetVc, yoffsetVc, 216)
	pdb.gimp_layer_set_opacity(textlayer, 70)

    bg.resize(base_size, base_size, 0, 0)
    img.resize(base_size, base_size, 0, 0)

    xcffile = file + ".xcf"
    pdb.gimp_file_save(img, textlayer, xcffile, xcffile)

    pdb.gimp_image_scale(img, size, size)
    xcffile = "%s_%s.xcf" % (file, size)
    pdb.gimp_file_save(img, textlayer, xcffile, xcffile)
    newlayer = img.merge_visible_layers(0)
    pngfile = "%s_%s.png" % (file, size)
    pdb.file_png_save(img, newlayer, pngfile, pngfile, 1, 0, 0, 0, 0, 0, 0)

el1 = ( "Account", "Currency", "Curve", "Location", "Portfolio", "Scenario", "Tenant", "Usage", "Variable")
vc1 = ( "Account", "Currency", "Variable")
vc2 = ( ("Cost", "Type"), ("Curve", "Group"), ("Discount", "Curve"), ("Discount", "Type"), ("Exchange", "Rate"), ("Future", "Cost"), ("Future", "Rental"), ("Vacancy", "Duration"))
el2 = ( ("Cost", "Type"), ("Curve", "Group"), ("Discount", "Object"), ("Discount", "Type"), ("Exchange", "Rate"), ("Future", "Cost"), ("Future", "Rental"), ("Real", "Estate"), ("Vacancy", "Duration"))

for d in (el1):
    file = "el_" + d[0].lower() + d[1:]
    create_txt_img(d, None, False, file)
    create_txt_img(d, None, False, file, 32)

for (d1, d2) in (el2):
    file = "el_" + d1[0].lower() + d1[1:] + d2
    create_txt_img(d1, d2, False, file)
    create_txt_img(d1, d2, False, file, 32)

for d in (vc1):
    file = "vc_" + d[0].lower() + d[1:]
    create_txt_img(d, None, True, file)
    create_txt_img(d, None, True, file, 32)

for (d1, d2) in (vc2):
    file = "vc_" + d1[0].lower() + d1[1:] + d2
    create_txt_img(d1, d2, True, file)
    create_txt_img(d1, d2, True, file, 32)
