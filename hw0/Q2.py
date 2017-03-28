from PIL import Image
img = Image.open("a.png")
img2 = img.rotate(180)
img2.save("img2.png")
