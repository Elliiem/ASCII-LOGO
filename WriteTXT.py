from PIL import Image
import os

Big = 1.5
size = [round(50 * Big), round(25 * Big)]
Size = open("Size.txt", "w")

NameList = os.listdir("./")
PNG = 0
for x in NameList:
    if x.__contains__(".png"):
        print(x)
        PNG = x
        break
Img = Image.open(PNG)
Img = Img.resize(size)
width = Img.size[0]
height = Img.size[1]
Size.write(str(width)+"\n")
Size.write(str(height))
px = Img.load()
# ---------------------------------------#

# TXT
# ---------------------------------------#
Out = open("Out.txt", "w+")
Color = open("color.txt", "w+")
# ---------------------------------------#


# Kinda Normal CharList = ["░","▒","▓","█"]
# Kunst CharList = ["□","▤","▒","▓","▧","▩","▣"]
# Funktioniert CharList = ["█","▉","▊","▋","▌","▍","▎","▏",":"]
CharList = [" "," "," ",";", "c", "o", "0", "A"]
#CharList = ["=","="]
CharList.reverse()

divisor = 255 / (len(CharList) - 1)


def GetBrightness(Pixel):
    R = Pixel[0]
    G = Pixel[1]
    B = Pixel[2]
    Brightness = (R + G + B) / 3
    return Brightness


def GetChar(Brightness):
    Brightness -= min
    Brightness *= mult
    x = round(Brightness / divisor)
    return CharList[x]


def WriteToTxT(RowList):
    for x in RowList:
        Out.write(x + "|")
    Out.write("\n")

def WriteColor (ColorList):
    for x in ColorList:
        Color.write(str(x[0])+".")
        Color.write(str(x[1]) + ".")
        Color.write(str(x[2]))
        Color.write("|")
    Color.write("\n")









# Get mult
# ------------------------------#
max = 0
min = 255
for Row in range(1, height):
    for Pixel in range(1, width):
        print(px[Pixel, Row])
        PixelBrightness = GetBrightness(px[Pixel, Row])
        if PixelBrightness < min:
            min = PixelBrightness
        if PixelBrightness > max:
            max = PixelBrightness
mult = 255 / (max - min)
# ------------------------------#

# Txt File Out.txt
# -------------------------------#
for Row in range(1, height):
    RowList = []
    ColorRow = []
    for Pixel in range(1, width):
        PixelBrightness = GetBrightness(px[Pixel, Row])
        RowList += GetChar(PixelBrightness)
        ColorRow += [px[Pixel,Row]]
    WriteToTxT(RowList)
    WriteColor(ColorRow)
# -------------------------------#
