from PIL import Image, ImageFilter

img = Image.open("pikachu.jpg")
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert("L")
crooked = filtered_img.rotate(180)
resized = filtered_img.resize((300,300))
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
filtered_img.save("sharpen.png", 'png')
region.show()
