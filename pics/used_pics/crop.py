#!/home/dee/anaconda3/bin/python3.6

import os
import Image
import numpy as np


picList = os.listdir('.')



def cleanList(pics):
    toDel = []
    for i in range(len(pics)):
        if ".png" not in pics[i]:
            toDel.append(i)

    for i in range(len(toDel)):
        del pics[toDel[i]-i]
    
    return pics

cleanedList = cleanList(picList)

for i in range(len(cleanedList)):
    image = Image.open(cleanedList[i])
    image.load()

    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

    image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

    new_image = Image.fromarray(image_data_new)
    new_image.save(cleanedList[i])