from PIL import Image
import os
Config = []
Conf = open("Config.txt","r")
for lines in Conf:
    parameter = (lines.split(":"))[1]
    Config.append(parameter)
Config[1] = Config[1].split(",")
print(Config[1])
for x in range(0,len(Config[1])):
    List = Config[1]
    List[x] = List[x].replace('"', "")
    List[x] = List[x].replace("\n", "")
Config[1] = List
print(Config[1])

Big = int(Config[0])
size = [round(50 * Big), round(25 * Big)]
Size = open("Size.txt", "w")
# Img
# ---------------------------------------#
NameList = os.listdir("./")


for x in NameList:
    if x.__contains__(".png") and x != "Bild.png":
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






CharList = Config[1]
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
    Out.write("|")
    for x in RowList:
        Out.write(x + "|")
    Out.write("\n")

def WriteColor (ColorList):
    Color.write("|")
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
        PixelBrightness = GetBrightness(px[Pixel, Row])
        if PixelBrightness < min:
            min = PixelBrightness
        if PixelBrightness > max:
            max = PixelBrightness
if max-min !=0:
 mult = 255 / (max - min)
else:
 mult = 1
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
