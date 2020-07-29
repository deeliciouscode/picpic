from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import os, sys, shutil
import math
import getpass
from colormath.color_objects import LabColor, XYZColor, sRGBColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_conversions import convert_color

img_path = "./server/img/pics/"
final_path = './server/img/final/'
factorMeta = 100 # TODO
factorSub = 30

def compose_and_safe_mosaic(id):
    imgBig = createMetaImg(id)
    subImgs = get_sub_imgs()
    matches = checkBestColor(imgBig, subImgs)
    drawPicture(matches, imgBig, id)
    

def createMetaImg(img):
    sizeMeta = factorMeta, factorMeta
    meta_img = Image.open(img_path+img)
    meta_img.thumbnail(sizeMeta)
    meta_img.save(img_path+"meta/meta.jpg")
    return img_path+"meta/meta.jpg"

def checkBestColor(imgBig, subImgs):
    "takes the meta image and returns ..."
    listMetaColor = getColorList(imgBig)

    subImgsAvgColors = []
    for i in range(len(subImgs)):
        avgCol = getAvgColor(subImgs[i])
        imgUrl = subImgs[i]
        tempTpl = (avgCol, imgUrl)
        subImgsAvgColors.append(tempTpl)

    listPicsMatched = matchPicToPixelByColor(listMetaColor, subImgsAvgColors)

    return listPicsMatched

def matchPicToPixelByColor(pxlList, picList):
    "matches the pixel-colors of the meta image to the average color of the small pictures"
    pxlListLab = turnToLabColors(pxlList)
    picListLab = turnToLabColors(picList)
    matches = []
    for i in range(len(pxlListLab)):        
        clsMI = 1000000000.0
        closestMatch = None
        for j in range(len(picListLab)):
            delta_e = delta_e_cie1976(pxlListLab[i], picListLab[j][0])
            if(delta_e < clsMI):
                closestMatch = picListLab[j][1]
                clsMI = delta_e
        matches.append((pxlList[i],closestMatch))  
    return matches

def getColorList(img):
    "takes a path to an image and gives back a list of all the single pixel-colors in order"
    imgB = Image.open(img)
    pixels = imgB.load() # this is not a list, nor is it list()'able
    width, height = imgB.size
    imgB.close()
    # print("###############", width, height)
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

def turnToLabColors(pixelList):
    "takes a list of rgb values and returns a list of lab colors (to compare colors)"
    if (type(pixelList[0][0]) != tuple):
        labColorList = []
        for i in range(len(pixelList)):
            rgb = sRGBColor(pixelList[i][0], pixelList[i][1], pixelList[i][2], is_upscaled = True)
            lab = convert_color(rgb, LabColor)
            labColorList.append(lab)
        
        # print(len(pixelList))
        # print(len(labColorList))
        return labColorList
    else:
        labColorList = []
        for i in range(len(pixelList)):
            rgb = sRGBColor(pixelList[i][0][0], pixelList[i][0][1], pixelList[i][0][2], is_upscaled = True)
            lab = convert_color(rgb, LabColor)
            labColorList.append((lab, pixelList[i][1]))
        
        # print(len(pixelList))
        # print(len(labColorList))
        return labColorList

# TODO: use actual image width / height for the big image!
def drawPicture(subPics, imgBig, id):
    "draws the image based on the smallPics provided and the user defined factor"
    all_imgs = []
    for filename in os.listdir(img_path+"small"):
        opn = (filename, (img_path+"small/"+filename))
        all_imgs.append(opn)

    meta = Image.open(imgBig)
    meta_w, meta_h = meta.size
    meta.close()    

    width, height = (meta_w*factorSub, meta_h*factorSub)
    
    new_im = Image.new('RGB', (width, height))

    x_offset = 0
    y_offset = 0

    for i in range(meta_w):
        for j in range(meta_h):
            try:
                img = Image.open(subPics[i*meta_h+j][1])
                new_im.paste(img, (x_offset,y_offset))
                img.close()
                y_offset += factorSub
            except IndexError as ie:
                print(ie)
                continue
            
        x_offset += factorSub
        y_offset = 0
    
    print(final_path+"final-"+id)
    new_im.save(final_path+"final-"+id)

def get_sub_imgs():
    "returns a list of all small images in './pics/small/'"
    sub_imgs = []
    for filename in os.listdir(img_path+"small"):
        sub_imgs.append(img_path+"small/"+filename)
    return sub_imgs


# For faster testing
if(__name__ == "__main__"):
    img_path = "../img/pics/"
    final_path = '../img/final/'
    # need to insert a valid id there
    compose_and_safe_mosaic("93570058_695880524501632_5334775039256825243_n.jpg")