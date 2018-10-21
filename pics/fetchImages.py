#!/home/dee/anaconda3/bin/python3.6

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Blue Flower, Red Flower, Yellow Flower, Green Flower, orange Flower, white flower, black flower","limit":50,"print_urls":True,"format":"png"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images