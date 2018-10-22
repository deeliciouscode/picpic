#!/home/dee/anaconda3/bin/python3.6
import os
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import os, sys, shutil
import math
import getpass


photosFrom = []
fileEnding = "jpg"
factor = 128
metaWidth = 1080
metaHeight = 1080
size = factor, factor
tempFolders = ['./picsProcessed', './pics', './metaImg', './metaImg/small', './picsProcessed/small']


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

    print("Ihr Username?")
    username = input()

    password = getpass.getpass('Ihr Password: ')

    for i in range(len(photosFrom)):
        os.system("instagram-scraper " + photosFrom[i] + " -u " + username + " -p " + password + " -t image -d ./pics")


def blackandwhitethem():
    for filename in os.listdir("./pics"):
        if(filename.split(".")[-1] == "jpg"):
            black_and_white("./pics/"+filename, "./picsProcessed/"+filename)
        else:
            continue

def deterFileFormat(filepath):
    fileFormat = filepath.split(".")[-1]
    return fileFormat

def loadAndBWMetaImage():
    print("what should be your Meta/Main Image? Provide File Path")
    metaFp = input()
    fileEnding = deterFileFormat(metaFp)
    black_and_white(metaFp, "./metaImg/metaimg."+fileEnding)


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
    for filename in os.listdir("./picsProcessed/small"):
        listSmallImgs.append("./picsProcessed/small/"+filename)
    return listSmallImgs

def getMetaImg():
    metaImgPath = "./metaImg/small/metaimg.jpg"
    return metaImgPath

def getPxlBr(img):
    imgB = Image.open(img)
    pixels = imgB.load() # this is not a list, nor is it list()'able
    width, height = imgB.size

    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    
    tupl = [(i,i,i) for i in all_pixels]

    metaImgBrList = []

    for i in range(len(tupl)):
        metaImgBrList.append(getBrightness(tupl[i]))

    return metaImgBrList

def getAvgBrightness(img):
    listMetaBr = getPxlBr(img)
    return sum(listMetaBr) / len(listMetaBr)

def getBrightness(pixel):
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    brtn = (0.2126*R + 0.7152*G + 0.0722*B)
    return brtn

def matchPicToPixl(pxlList, picList):
    
    
    closestMatches = []
    for i in range(len(pxlList)):
        clsMI = 256.0
        for j in range(len(picList)):
            diff = abs(pxlList[i] - picList[j][0])
            if(diff < clsMI):
                closestMatch = picList[j][1]
                clsMI = diff

        closestMatches.append(closestMatch)
        
    #print(closestMatches[100])

    return closestMatches


def checkBestLucid(imgBig, subImgs):
    
    listMetaBr = getPxlBr(imgBig)

    subImgsBrightness = []

    for i in range(len(subImgs)):
        avgBr = getAvgBrightness(subImgs[i])
        imgUrl = subImgs[i]
        tempTpl = (avgBr, imgUrl)
        subImgsBrightness.append(tempTpl)
   
    #print(subImgsBrightness)

    listPicsMatched = matchPicToPixl(listMetaBr, subImgsBrightness)

    return listPicsMatched

def chooseRight(pixelToBeFilled, openPicsTupelList):
    justName = pixelToBeFilled.split("/")[-1]
    for i in range(len(openPicsTupelList)):
        if (justName in openPicsTupelList[i][0]):
            #print(openPicsTupelList[i])
            return openPicsTupelList[i]
        else:
            continue

def drawPicture(subPics):
    
    openImgs = []
    for filename in os.listdir("./picsProcessed/small"):
        opn = (filename ,Image.open("./picsProcessed/small/"+filename))
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


createFolders(tempFolders)

scrapeImages()

blackandwhitethem()
loadAndBWMetaImage()

scaleImgsToFactor("./metaImg/", "./metaImg/small/")
scaleImgsToFactor("./picsProcessed/", "./picsProcessed/small/")

imgBig = getMetaImg()
subImgs = getSmallImgs()

bestFitsInOrder = checkBestLucid(imgBig, subImgs)

drawPicture(bestFitsInOrder)

delUnused(tempFolders)

#os.makedirs(path, exist_ok=True) (to create folder)