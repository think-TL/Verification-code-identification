from PIL import Image
im = Image.open("3.png")
imgry = im.convert('L')

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else :
         table.append(1)

out = imgry.point(table,'1')
out.show()