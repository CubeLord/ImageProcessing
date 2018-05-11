import numpy as np
import cv2
import pprint
import ImageProcessingFunctions as IP

sprite_height = 16
sprite_width = 16
Tilecolors = []
Mapcolors = []


def TestTiles():
    print("Printing Tile Image...")
    tiles = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")
    #tiles = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")
    print("Image Shape is:")
    pprint.pprint(tiles.shape)
    IP.draw('Tiles', IP.enlarge(tiles, 3))

    #print("Printing Map...")
    map = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\ZeldaOverworldMapQ1BGcroped.png")
    #draw("Map", map)
    #print(map.shape)


    #REMOVING BLACK LINE ON THE LEFT OF IMAGE
    i = 0
    while(map[0,i][0] == 0 and map[0,i][2] == 0 and map[0,i][2] == 0):
        i+=1

    x = i
    newMap = np.zeros((map.shape[0],map.shape[1]-x,3), np.uint8)

    newMap = map[0:map.shape[0],x:map.shape[1]]
    #draw("NEW Map", newMap)
    print("new map shape:")
    print(newMap.shape)

    cv2.imwrite("OverworldCroped.png", newMap)



    dict = {}
    dict, Tilecolors = IP.defSprites(dict, "C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Overworld Tiles.png")

    print("TileColors length is: ", len(Tilecolors))
    print("TileColors are (BGR format): ")
    pprint.pprint( Tilecolors)
    IP.drawColors("Tilecolors", Tilecolors)

    print("Loading Map colors:")
    Mapcolors = IP.getColors(map)

    print("MapColors length is: ", len(Mapcolors))
    print("MapColors are (BGR format): ")
    pprint.pprint( Mapcolors)
    IP.drawColors("Mapcolors", Mapcolors)
    
    #print("Listing Tiles...")
    #print("Press ESC to skip")
    #IP.drawDict()


    #FOR CHECKING WHETHER IT CANT FIND A CIRTAIN COLOR
    #cantFind = []
    #for i in range(len(dict)):
    #    dict[i], cantFind = IP.fixColors(dict[i], cantFind, Tilecolors, Mapcolors)
    #print(cantFind)
    #drawDict()




    #TESTING ALL COLORS INSIDE TILES
    #print("Processing folowing Images:")
    #cantFind = []
    #oldTiles = IP.copyImg(IP.drawColors("OLD",Tilecolors))
    #tmp, cantFind = IP.fixColors(IP.drawColors("NEW", Tilecolors), cantFind, Tilecolors, Mapcolors)
    #newTiles = IP.copyImg(tmp)
    #newTilecolors = []
    #newTilecolors = IP.getColors(newTiles)

    #print("OLD:")
    #pprint.pprint(Tilecolors)

    #print("NEW:")
    #pprint.pprint(newTilecolors)

    #while(1):
    #    IP.draw("OLD TILES",enlarge(oldTiles, 5))
    #    IP.draw("NEW TILES",enlarge(newTiles, 5))

    #CHECKING FIXCOLORS ON THE TILECOLORS
    #cantFind = []
    #tmp, cantFind = IP.fixColors(tiles, cantFind, Tilecolors, Mapcolors)
    #IP.draw("Tiles after Fixed color", IP.enlarge(tmp, 3))

    #TileColorsAfterFix = []
    #TileColorsAfterFix = IP.getColors(tmp)
    #print("TileColors Before\n")
    #pprint.pprint(Tilecolors)
    #print("TileColors After\n")
    #pprint.pprint(TileColorsAfterFix)


    #FOR TESTING INDIVIDUAL SPRITES IN THE DICTIONARY
    i = 0
    cantFind = []
    while(i < 144):
        sprite = IP.copyImg(dict[i])   
        sprite, cantFind = IP.fixColors(sprite, cantFind, Tilecolors, Mapcolors)
        dict[i] = IP.copyImg(sprite)
        i +=1

    #after this dictionary is FINAL

    Ftiles = IP.createFinalTiles(dict)
    print("MAP COLORS ARE:")
    pprint.pprint(Mapcolors)
    print("FINALTILES COLORS ARE:")
    FTcolors = IP.getColors(Ftiles)
    pprint.pprint(FTcolors)
    FTcolorsImg = IP.drawColors("Final Tiles Colors", FTcolors)

    #IP.FillMatrix(dict, newMap)
    print("PRINTING COLORS OF FINAL TILES IN FORM OF MATRIX:")
    

    Ftiles = cv2.imread("FinalTilesUpdated0.png")
    FTcolors = IP.getColors(Ftiles)
    matrix = IP.FillMatrixColor(FTcolors, Ftiles)
    IP.draw("FinalTiles",IP.enlarge(Ftiles,5))

    #Ading the tiles that appear only on the map to the Tiles image
    #Ftiles = IP.createFinalTiles(dict)
    #cv2.imwrite("FinalTilesUpdated.png",Ftiles)
    #IP.drawDict(dict)

    #REDEFINING THE MATRIX TO MATCH NEEDS:
    #each list is oen sprite
    Smatrix = []
    for i in range(162):
        Smatrix.append([])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Smatrix[j//16 + 18*(i//16)].append(matrix[i][j])
    
    print("\nCORRECTED MATRIX\n")
    for i in range(len(Smatrix)):
        print(Smatrix[i])

    genSprite = np.zeros((16,16,3), np.uint8)
    for x in range(len(Smatrix)):  
       for i in range(16):
            for j in range(16):
                genSprite[i][j] = FTcolors[Smatrix[x][i*16 + j]]
       IP.draw("genSprite",IP.enlarge(genSprite, 10))


def TestLinkSprites():
    link  = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Link.png")
    IP.draw("Link", IP.enlarge(link, 1))
    ##REMOVING DESCRIPTIONS ON THE LEFT AND BOTTOM OF IMAGE, ALSO ONE EXTRA LINE OF PIXELS ON TOP
    x = 159
    y = 80
    clink = np.zeros((link.shape[0]-y,link.shape[1]-x,3), np.uint8)
    clink = link[1:link.shape[0] - y,x:link.shape[1]]

    IP.draw("croped Link", IP.enlarge(clink, 2))
    dict = {}
    Tilecolors = []
    dict, Tilecolors =  IP.defLinkSprites(dict,clink, Tilecolors)
    dict = IP.filterDict(dict)
    IP.drawDict(dict)
    pprint.pprint(Tilecolors)
    colorImg = IP.drawColors("Link colors", Tilecolors)
    #cv2.imwrite("OverworldCroped.png", newMap)

    #GetlinkColors -> Matrix and colorcodes extracted
    LinkTiles = IP.createFinalTiles(dict)
    IP.draw("LinkTiles", IP.enlarge(LinkTiles, 5))
    cv2.imwrite("LinkColors.png", IP.enlarge(colorImg, 5))
    matrix = IP.FillMatrixColor(Tilecolors, LinkTiles)

#fixing matrix to be as needed, each row is one sprite
    Smatrix = []
    for i in range(162):
        Smatrix.append([])

    for i in range(16*2):
        for j in range(len(matrix[0])):
            Smatrix[j//16 + 18*(i//16)].append(matrix[i][j])
    
    print("\nCORRECTED MATRIX\n")
    for i in range(len(Smatrix)):
        print(Smatrix[i])

    genSprite = np.zeros((16,16,3), np.uint8)
    for x in range(len(Smatrix)):  
       for i in range(16):
            for j in range(16):
                genSprite[i][j] = Tilecolors[Smatrix[x][i*16 + j]]
       IP.draw("genSprite",IP.enlarge(genSprite, 10))

def TestItemSprites():
    items = cv2.imread("NES - The Legend of Zelda - TreasuresNEW.png")
    items = items[0:items.shape[0]-208, 0:items.shape[1]]
    IP.draw("Items and Icons", IP.enlarge(items, 5))
    odict = {0:8, 1:8,  2:10, 3:16, 4:8}
    dict = {0:8, 1:8, 2:8, 3:16, 4:8, 5:10, 6:14, 7:8, 8:8, 9:8, 10:8, 11:8, 12:8, 13:9, 14:7, 15:8, 16:10, 17:6, 18:9, 19:7}
    
    spritesDict = {}
    #p = countDict(dict, 8)
    #sprite = items[0:16, 0+p:14+p]
    #IP.draw("sprite", IP.enlarge(sprite, 10))
    for i in range(len(dict)):
        spritesDict[i] = items[0:16, countDict(dict, i):dict[i]]
    #IP.drawDict(spritesDict)
    
    return

def countDict(dict, l):
    br = 0
    for i in range(len(dict)):
        br += dict[i]
    return br

#TestTiles()
TestLinkSprites()
#TestItemSprites()

#TODO: MAKE A MATRIX FOR THE ORIGINAL MAP TILES, A MATRIX FOR THE COLORS, AND EXTRACT THE COLORS IN SOME WAY
#EXTRACT THE DUNGEON TILES
#EXTRACT COLORS AND MATRIX FOR LINK SPRITES