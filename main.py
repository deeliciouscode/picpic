#!/home/dee/anaconda3/bin/python3.6
import os
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import os, sys, shutil
import math
import getpass
from colormath.color_objects import LabColor, XYZColor, sRGBColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_conversions import convert_color


photosFrom = []
fileEnding = "jpg"
tempFolders = ['./picsProcessed', './picsProcessed/small', './pics', './pics/small','./metaImg', './metaImg/small']

print("wie möchten Sie skalieren? Ganze Zahl zwischen 8 und 160")
tempFactor = input()

# print("u want the Pic in Colorful? (y/n)")
# colorfulDeter = input()
# if(colorfulDeter == "y" or colorfulDeter == "Y"):
#     colorful = True
# else:
#     colorful = False


print("how many pics? (dont take more than 1000 Dude)")
maxNumPhotos = int(input())

try:
    tempFactor = int(tempFactor)
except:
    print("Das war ungültig. Es wird auf 128 skaliert")
    tempFactor = 128

if(tempFactor > 160):
    tempFactor = 160
elif(tempFactor <= 16):
    tempFactor = 16
else:
    toSubs = tempFactor % 8
    tempFactor -= toSubs
factor = tempFactor
size = factor, factor



def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

def scrapeImages():
    
    moreUsers = True

    print("Von wem möchen Sie alles die Photos herunter laden?")

    while (moreUsers):
        lastUser = input()
        if (lastUser == ""):
            moreUsers = False
            break
        else:
            photosFrom.append(lastUser)
            print("Von wem noch? 'Enter' für niemanden mehr")
    
    if(len(photosFrom) != 0):
        maxProAcc = round(maxNumPhotos / len(photosFrom))
    else:
        maxProAcc = maxNumPhotos

    print("Ihr Username?")
    username = input()

    password = getpass.getpass('Ihr Password: ')

    for i in range(len(photosFrom)):
        os.system("instagram-scraper " + photosFrom[i] + " -m " + str(maxProAcc) + " -u " + username + " -p " + password + " -t image -d ./pics")


def blackandwhitethem():
    for filename in os.listdir("./pics"):
        if(filename.split(".")[-1] == "jpg"):
            black_and_white("./pics/"+filename, "./picsProcessed/"+filename)
        else:
            continue

def safeInDirec(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    color_image.save(output_image_path)


def deterFileFormat(filepath):
    fileFormat = filepath.split(".")[-1]
    return fileFormat

def loadAndSafeMetaImage():
    print("what should be your Meta/Main Image? Provide File Path")
    metaFp = input()
    fileEnding = deterFileFormat(metaFp)
    safeInDirec(metaFp, "./metaImg/metaimg."+fileEnding)


def scaleImgsToFactor(direcIn, direcOut):
    for infile in os.listdir(direcIn):
        outfile = os.path.splitext(infile)[0]
        if infile != outfile:
            try:
                im = Image.open(direcIn + infile)
                im.thumbnail(size)
                im.save(direcOut + outfile + ".jpg", "JPEG")
            except IOError:
                print("cannot create thumbnail for '%s'" % infile)

def getSmallImgs():
    listSmallImgs = []
    for filename in os.listdir("./pics/small"):
        listSmallImgs.append("./pics/small/"+filename)
    return listSmallImgs

def getMetaImg():
    metaImgPath = "./metaImg/small/metaimg.jpg"
    return metaImgPath

def getColorList(img):
    imgB = Image.open(img)
    pixels = imgB.load() # this is not a list, nor is it list()'able
    width, height = imgB.size

    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    
    #tupl = [(i,i,i) for i in all_pixels]

    return all_pixels    


def getAvgColor(img):
    listMetaCol = getColorList(img)
    
    r, g, b = (0, 0, 0)

    for i in range(len(listMetaCol)):
        r += listMetaCol[i][0]
        g += listMetaCol[i][1]
        b += listMetaCol[i][2]

    r = r / len(listMetaCol)
    g = g / len(listMetaCol)
    b = b / len(listMetaCol)
    return (r, g, b)


def matchPicToPixlByBrightness(pxlList, picList):   
    closestMatches = []
    for i in range(len(pxlList)):
        clsMI = 256.0
        for j in range(len(picList)):
            diff = abs(pxlList[i] - picList[j][0])
            if(diff < clsMI):
                closestMatch = picList[j][1]
                clsMI = diff

        closestMatches.append(closestMatch)
        
    return closestMatches


def turnToLabColors(pixelList):
    if (type(pixelList[0][0]) != tuple):
        labColorList = []
        for i in range(len(pixelList)):
            rgb = sRGBColor(pixelList[i][0], pixelList[i][1], pixelList[i][2], is_upscaled = True)
            lab = convert_color(rgb, LabColor)
            labColorList.append(lab)
        
        print(len(pixelList))
        print(len(labColorList))
        return labColorList
    else:
        labColorList = []
        for i in range(len(pixelList)):
            rgb = sRGBColor(pixelList[i][0][0], pixelList[i][0][1], pixelList[i][0][2], is_upscaled = True)
            lab = convert_color(rgb, LabColor)
            labColorList.append((lab, pixelList[i][1]))
        
        print(len(pixelList))
        print(len(labColorList))
        return labColorList

def matchPicToPixlByColor(pxlList, picList):
    pxlListLab = turnToLabColors(pxlList)
    picListLab = turnToLabColors(picList)

    closestMatches = []
    for i in range(len(pxlListLab)):        
        clsMI = 1000000.0
        for j in range(len(picListLab)):
            delta_e = delta_e_cie1976(pxlListLab[i], picListLab[j][0])
            if(delta_e < clsMI):
                closestMatch = picListLab[j][1]
                clsMI = delta_e

        closestMatches.append(closestMatch)
    
    print(len(closestMatches))
        
    
    return closestMatches



def checkBestColor(imgBig, subImgs):
    
    listMetaColor = getColorList(imgBig)

    subImgsAvgColor = []
    for i in range(len(subImgs)):
        avgCol = getAvgColor(subImgs[i])
        imgUrl = subImgs[i]
        tempTpl = (avgCol, imgUrl)
        subImgsAvgColor.append(tempTpl)

    listPicsMatched = matchPicToPixlByColor(listMetaColor, subImgsAvgColor)

    return listPicsMatched



def chooseRight(pixelToBeFilled, openPicsTupelList):
    justName = pixelToBeFilled.split("/")[-1]
    for i in range(len(openPicsTupelList)):
        if (justName in openPicsTupelList[i][0]):
            #print(openPicsTupelList[i])
            return openPicsTupelList[i]
        else:
            continue



def drawPicture(subPics, factor):
    
    openImgs = []
    for filename in os.listdir("./pics/small"):
        opn = (filename, Image.open("./pics/small/"+filename))
        openImgs.append(opn)

    #print(openImgs)
    #images = map(Image.open, subPics)

    width, height = (factor*factor, factor*factor)
    
    new_im = Image.new('RGB', (width, height))

    x_offset = 0
    y_offset = 0

    for im in range(factor):
        for jim in range(factor):
            try:
                rightPic = chooseRight(subPics[im + jim * factor], openImgs)
                new_im.paste(rightPic[1], (x_offset,y_offset))
                x_offset += factor
            except IndexError as ie:
                continue
            
        y_offset += factor
        x_offset = 0

    print("What should your image be called like? just the name, no file endings!")
    nameImg = input()
    print("Where do you want to save it? provide path to folder")
    saveIn = input()
    
    if (saveIn[-1] == "/"):
        new_im.save(saveIn+nameImg+'.jpg')
    else:
        new_im.save(saveIn+"/"+nameImg+'.jpg')
 


def delUnused(foldPaths):
    for i in range(len(foldPaths)):
        folder = foldPaths[i]
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)



def createFolders(folderPaths):
    for i in range(len(folderPaths)):
        path = folderPaths[i]        
        os.makedirs(path, exist_ok=True)   
        os.makedirs(path, exist_ok=True)
        os.makedirs(path, exist_ok=True)
        os.makedirs(path, exist_ok=True)
        os.makedirs(path, exist_ok=True)

def remove_img(path, img_name):
    os.remove(path + '/' + img_name)
    # check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        #return True
        pass

def cleanToSquares(folder):
    listWeg = []

    for filename in os.listdir(folder):
        tempImg = Image.open("./pics/small/"+filename)
        pixelsTemp = tempImg.load()
        width, height = tempImg.size
        if(width != height):
            remove_img(folder, filename)
            listWeg.append(True)
        else:
            continue
        
    print(len(listWeg))



createFolders(tempFolders)

scrapeImages()

blackandwhitethem()
loadAndSafeMetaImage()

cleanToSquares("./pics/small/")

scaleImgsToFactor("./metaImg/", "./metaImg/small/")
scaleImgsToFactor("./pics/", "./pics/small/")

imgBig = getMetaImg()
subImgs = getSmallImgs()

bestFitsInOrder = checkBestColor(imgBig, subImgs)

drawPicture(bestFitsInOrder, factor)

delUnused(tempFolders)

# robbie.exe banksy _naropinosa henriettaharris tays_hipsdontlie