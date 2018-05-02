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
    IP.FillMatrixColor(FTcolors, Ftiles)
    IP.draw("FinalTiles",IP.enlarge(Ftiles,5))

    #Ading the tiles that appear only on the map to the Tiles image
    #Ftiles = IP.createFinalTiles(dict)
    #cv2.imwrite("FinalTilesUpdated.png",Ftiles)
    #IP.drawDict(dict)

def TestLinkSprites():
    link  = cv2.imread("C:\\Users\\Milorad Markovic\\Downloads\\NES - Zelda 1 Textures\\Export from Gimp\\NES - The Legend of Zelda - Link.png")
    IP.draw("Link", IP.enlarge(link, 1))
    ##REMOVING BLACK LINE ON THE LEFT OF IMAGE
    x = 159
    y =80

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
    IP.FillMatrixColor(Tilecolors, LinkTiles)


#TestTiles()
TestLinkSprites()


#TODO: MAKE A MATRIX FOR THE ORIGINAL MAP TILES, A MATRIX FOR THE COLORS, AND EXTRACT THE COLORS IN SOME WAY
#EXTRACT THE DUNGEON TILES
#EXTRACT COLORS AND MATRIX FOR LINK SPRITES