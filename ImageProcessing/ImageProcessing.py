import numpy as np
import cv2
import pprint

#siva boja izmedju spritova je [192, 192, 192]

sprite_height = 16
sprite_width = 16
Tilecolors = []
Mapcolors = []

#def draw(img):
#	while(1):
#		cv2.imshow('img',img)
#		k = cv2.waitKey(33)
#		if k == 27:
#			cv2.destroyAllWindows()
#			break
#		elif k == -1:
#			continue
#		else:
#			print(k)


def draw(name, img):
    #img    - the image you want to draw
    cv2.imshow(name,img)
    k  = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return k

def enlarge(img, x, height, width):
    #img    - the image you want to enlarge
    #x      - how many times you want to enlarge it

    Enlarged = np.zeros((height*x,width*x,3), np.uint8)

    for i in range(height):
        for j in range(width):
            for ii in range(x):
                for jj in range(x):
                    b = img[i, j]
                    Enlarged[x*i+ii,x*j+jj] = b

    return Enlarged

def defSprites(dict):
    #dict - dictionary to which to write
    tiles = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")
    global Tilecolors
    x = 0
    y = 0
    br = 0
    while(y <8):
        while(x < 18):
            dict[br] = np.zeros((sprite_height,sprite_width,3), np.uint8)
            for i in range(16):
                for j in range(16):
                    dict[br][i,j] = tiles[i+1+y+y*16,j+1+x*16+x]
                    rememberColor(dict[br][i,j], Tilecolors);
            br = br + 1
            x = x+1
        x = 0
        y = y+1
    return dict

def rememberColor(c, colors):
    for i in range(len(colors)):
        if colors[i][0] == c[0] and colors[i][1] == c[1] and colors[i][2] == c[2]:
             return colors
    colors.append(c)
    return colors

def getColors(img, shape, colors):
    height = shape[0] 
    width = shape[1]
    for i in range(height):
        for j in range(width):
            rememberColor(img[i,j], colors)
    return colors

def drawColors(name, colors):
    colorImage = np.zeros((16,16*len(colors),3), np.uint8)
    for i in range(16):
        for j in range(16*len(colors)):
            colorImage[i,j]=colors[j//16]

    draw(name, enlarge(colorImage, 5, 16, 16*len(colors)))
    return colorImage


def drawDict():
    for i in range(len(dict)):
        if draw('Dictionary', enlarge(dict[i], 10, 16, 16)) == 27:
            return None

def compare(sprite1, sprite2):
    for i in range(sprite_height):
        for j in range(sprite_width):
            if sprite1[i,j][0] != sprite2[i,j][0] and sprite1[i,j][1] != sprite2[i,j][1] and sprite1[i,j][2] != sprite2[i,j][2]:
                print("Values are sprite1: [{},{},{}] and sprite2: [{},{},{}]".format(sprite1[i,j][0],sprite1[i,j][1],sprite1[i,j][2],sprite2[i,j][0],sprite2[i,j][1],sprite2[i,j][2]))
                return False
    return True


def copyImg(img):
    copy = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            copy[i,j]=img[i,j]
    return copy

cantFind = []
def fixColors(sprite):
    global Tilecolors
    global Mapcolors
    #drawColors("Map colors", Mapcolors)
    global cantFind
    for i in range(sprite.shape[0]):
        for j in range(sprite.shape[1]):
            if (sprite[i,j][0] == Tilecolors[0][0] and sprite[i,j][1] == Tilecolors[0][1] and sprite[i,j][2] == Tilecolors[0][2]) or (sprite[i,j][0] == Tilecolors[8][0] and sprite[i,j][1] == Tilecolors[8][1] and sprite[i,j][2] == Tilecolors[8][2]):
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[1][k]

            elif sprite[i,j][0] == Tilecolors[1][0] and sprite[i,j][1] == Tilecolors[1][1] and sprite[i,j][2] == Tilecolors[1][2]:
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[0][k]

            elif sprite[i,j][0] == Tilecolors[2][0] and sprite[i,j][1] == Tilecolors[2][1] and sprite[i,j][2] == Tilecolors[2][2]:
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[2][k]

            elif (sprite[i,j][0] == Tilecolors[3][0] and sprite[i,j][1] == Tilecolors[3][1] and sprite[i,j][2] == Tilecolors[3][2]) or (sprite[i,j][0] == Tilecolors[7][0] and sprite[i,j][1] == Tilecolors[7][1] and sprite[i,j][2] == Tilecolors[7][2]):
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[3][k]

            elif sprite[i,j][0] == Tilecolors[4][0] and sprite[i,j][1] == Tilecolors[4][1] and sprite[i,j][2] == Tilecolors[4][2]:
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[4][k]

            elif sprite[i,j][0] == Tilecolors[5][0] and sprite[i,j][1] == Tilecolors[5][1] and sprite[i,j][2] == Tilecolors[5][2]:
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[5][k]

            elif sprite[i,j][0] == Tilecolors[6][0] and sprite[i,j][1] == Tilecolors[6][1] and sprite[i,j][2] == Tilecolors[6][2]:
                for k in range(3):
                    sprite[i,j][k] = Mapcolors[6][k]
            else:
                print("Can't find color:", sprite[i,j])
                if (str(sprite[i,j][0]) + " " + str(sprite[i,j][1]) + " " + str(sprite[i,j][2])) not in cantFind:
                    cantFind.append(str(sprite[i,j][0]) + " " + str(sprite[i,j][1]) + " " + str(sprite[i,j][2]))
    return sprite

print("Printing Tile Image...")
tiles = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")
#tiles = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")
print("Image Shape is:")
pprint.pprint(tiles.shape)
draw('Tiles', tiles)

#print("Printing Map...")
test = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\ZeldaOverworldMapQ1BGcroped.png")
#draw("Map", test)
print(test.shape)

dict = {}
defSprites(dict)

print("TileColors length is: ", len(Tilecolors))
print("TileColors are (BGR format): ")
pprint.pprint( Tilecolors)
drawColors("Tilecolors", Tilecolors)

print("Loading Map colors:")
Mapcolors = getColors(test, test.shape , Mapcolors)

print("MapColors length is: ", len(Mapcolors))
print("MapColors are (BGR format): ")
pprint.pprint( Mapcolors)
drawColors("Mapcolors", Mapcolors)

#print("Listing Tiles...")
#print("Press ESC to skip")
#drawDict()

tsprite = np.zeros((sprite_height,sprite_width,3), np.uint8)
y = 0
x = 0
offsetx = 7
offsety = 0
for i in range(16):
    for j in range(16):
        tsprite[i,j] = test[i+offsety+y*16,j+x*16+offsetx]
        #test[i+offsety+y*16,j+x*16+offsetx] = [255,255,255]        #proveri MapColors

#FOR CHECKING WHETHER IT CANT FIND A CIRTAIN COLOR
#for i in range(len(dict)):
#    dict[i] = fixColors(dict[i])
#print(cantFind)
#drawDict()


#TESTING ALL COLORS INSIDE TILES
#print("Processing folowing Images:")
#oldTiles = copyImg(drawColors("OLD",Tilecolors))
#newTiles = copyImg(fixColors(drawColors("NEW", Tilecolors)))
#newTilecolors = []
#newTilecolors = getColors(newTiles, newTiles.shape, newTilecolors)

#print("OLD:")
#pprint.pprint(Tilecolors)

#print("NEW:")
#pprint.pprint(newTilecolors)

#while(1):
#    draw("OLD TILES",enlarge(oldTiles, 10, oldTiles.shape[0], oldTiles.shape[1]))
#    draw("NEW TILES",enlarge(newTiles, 10, newTiles.shape[0], newTiles.shape[1]))

#FOR TESTING INDIVIDUAL SPRITES IN THE DICTIONARY
#i = 0
#while(i < 144):
#    stone = copyImg(dict[i])   
#    stone = fixColors(stone)
#    print("Result of compare [{}]:".format(i))
#    print(compare(stone, dict[i]))

#    draw("after fix", enlarge(stone, 10, stone.shape[0], stone.shape[1]))
#    draw("original", enlarge(dict[i], 10, dict[i].shape[0], dict[i].shape[1]))
#    i +=1

