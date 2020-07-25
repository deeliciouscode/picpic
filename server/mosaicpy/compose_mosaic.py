from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import os, sys, shutil
import math
import getpass
from colormath.color_objects import LabColor, XYZColor, sRGBColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_conversions import convert_color


def compose_and_safe_mosaic(id):
    imgBig = "./img/pics/"+id
    subImgs = get_sub_imgs()
    matches = checkBestColor(imgBig, subImgs)
    drawPicture(matches, 80, 50)


def checkBestColor(imgBig, subImgs):
    "takes the meta image and returns "
    listMetaColor = getColorList(imgBig)

    subImgsAvgColor = []
    for i in range(len(subImgs)):
        avgCol = getAvgColor(subImgs[i])
        imgUrl = subImgs[i]
        tempTpl = (avgCol, imgUrl)
        subImgsAvgColor.append(tempTpl)

    listPicsMatched = matchPicToPixlByColor(listMetaColor, subImgsAvgColor)

    return listPicsMatched

def getColorList(img):
    "takes a path to an image and gives back a list of all the single pixel-colors in order"
    sizeMeta = 80,80
    imgB = Image.open(img)
    imgB.thumbnail(sizeMeta)
    pixels = imgB.load() # this is not a list, nor is it list()'able
    width, height = imgB.size
    print("###############", width, height)
    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    
    #tupl = [(i,i,i) for i in all_pixels]

    return all_pixels

def getAvgColor(img):
    "takes a path to an image and gives back the average color of that image"
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

def matchPicToPixlByColor(pxlList, picList):
    "matches the pixel-colors of the meta image to the average color of the small pictures"
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

def turnToLabColors(pixelList):
    "takes a list of rgb values and returns a list of lab colors (to compare colors)"
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

def drawPicture(subPics, factorMeta, factorSub):
    "draws the image based on the smallPics provided and the user defined factor"
    openImgs = []
    for filename in os.listdir("./img/pics/small"):
        opn = (filename, Image.open("./img/pics/small/"+filename))
        openImgs.append(opn)

    #print(openImgs)
    #images = map(Image.open, subPics)

    width, height = (factorMeta*factorSub, factorMeta*factorSub)
    
    new_im = Image.new('RGB', (width, height))

    x_offset = 0
    y_offset = 0

    for im in range(factorMeta):
        for jim in range(factorMeta):
            try:
                rightPic = chooseRight(subPics[im + jim * factorSub], openImgs)
                new_im.paste(rightPic[1], (x_offset,y_offset))
                x_offset += factorSub
            except IndexError as ie:
                print(ie)
                continue
            
        y_offset += factorSub
        x_offset = 0
    
    new_im.save('./img/final/final.jpg')

def chooseRight(pixelToBeFilled, openPicsTupelList):
    "takes a pixel and all possible pictures and returns the matching image for that pixel"
    justName = pixelToBeFilled.split("/")[-1]
    for i in range(len(openPicsTupelList)):
        if (justName in openPicsTupelList[i][0]):
            #print(openPicsTupelList[i])
            return openPicsTupelList[i]
        else:
            continue

def get_sub_imgs():
    "returns a list of all small images in './pics/small/'"
    sub_imgs = []
    for filename in os.listdir("./img/pics/small"):
        sub_imgs.append("./img/pics/small/"+filename)
    return sub_imgs