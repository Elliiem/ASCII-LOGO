from PIL import Image,ImageDraw
# Open Files
# ------------------------------- #
Out = open('Out.txt', 'r')
Color = open("color.txt", "r")
Size = open("Size.txt", "r")
# ------------------------------- #

# Get Colors
# --------------------------------------- #
ColorList = []
for line in Color:
    ColorRow = line.split("|")
    ColorRow.pop(-1)
    for x in range(0,len(ColorRow)):
        ColorRow[x] = ColorRow[x].split(".")
    ColorList.append(ColorRow)
# --------------------------------------- #

# Get Chars
# -------------------------------- #
LineList = []
for line in Out:
    line = line.replace("\n", "")
    LineList.append(line)
# -------------------------------- #

# Pillow Image
# ------------------------------------------------------------------------ #
width = int(Size.readline())
height = int(Size.readline())
Img = Image.new("RGB", (6*width-5, 10*height-23), color=(100,100,100))
d = ImageDraw.Draw(Img)
# ------------------------------------------------------------------------ #

def DrawText(Row,Pixel,char,colour):
    d.text(((Pixel-1)*6, (Row - 1) * 10-3), char, fill=colour)

def GetCharTXT(Row, Pixel):
    if Pixel >= width - 1:
        Pixel = width - 2
    Line = LineList[Row - 1]
    List = Line.split("|")
    List.pop(-1)
    return List[Pixel]

for Row in range(1, height):
    color = ColorList[Row-1]
    print(Row)
    for Pixel in range(1, width-1):
        r = int(color[Pixel][0])
        g = int(color[Pixel][1])
        b = int(color[Pixel][2])
        DrawText(Row, Pixel, GetCharTXT(Row, Pixel),(r,g,b))

Img.save("Bild.png")