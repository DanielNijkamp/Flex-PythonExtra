from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background1.jpg")


breedte = achtergrond.width
hoogte = achtergrond.height


lettertype = ImageFont.truetype("impact.ttf", 50)


tekengebied = ImageDraw.Draw(achtergrond)

tekst_breedte = 609
tekst_hoogte = 46

tekst_X = (breedte - tekst_breedte)/2
tekst_Y = (hoogte - tekst_hoogte)/2


tekst = "On my way to find syntax error"
tekengebied.multiline_text((tekst_X,tekst_Y), tekst, font=lettertype, fill=(255,255,255))

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))




achtergrond.show()



