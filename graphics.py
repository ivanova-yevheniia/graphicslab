from PIL import Image, ImageDraw

with open("DS2.txt", "r") as fl:
    data = fl.readlines()
    xy = []
    for line in data:
        x, y = line.split(" ")
        xy.append(int(y))
        xy.append(540 - int(x))

    fl.close()
print(xy)
canvas = Image.new("RGB", (960, 540), (255, 255, 255))

dr = ImageDraw.Draw(canvas)
dr.point(xy, fill=0)

canvas.show()
canvas.save("IMAGE", "PNG")
