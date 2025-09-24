from pil import image, imagedraw, imagefont

img - image.open(your_image.png)
d = imagedraw.draw(img)

font = imagefont.truetype("dejavusansmono.ttf", 24)

txt = "the new date of birth"
pos = (the position of the date of birth in the image)

d.rectangle([pos, (pos[0] + 160, pos[1] + 28)], fill=(235, 228, 203))
d.text(pos, txt, font=fnt, fill="black")

img.save("newimage.png")
