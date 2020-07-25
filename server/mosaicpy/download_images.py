import os
from PIL import Image

def scrape_and_clean_images(username, password, tags):
    scrape_images(username, password, tags)
    clean_to_squares()
    scale_images()
    

def scrape_images(username, password, tags):
    """scapes images from instagram by user specification"""
    print(username, password, tags)
    for i in range(len(tags)):
        # here maybe update task status
        os.system("instagram-scraper " + tags[i]["tag"] + " -u " + username + " -p " + password + " -t image -d ./img/pics")


def scale_images():
    size = 50, 50
    in_dir = "./img/pics/"
    out_dir = "./img/pics/small/"
    for in_file in os.listdir(in_dir):
        out_file = os.path.splitext(in_file)[0]
        if in_file != out_file:
            try:
                im = Image.open(in_dir + in_file)
                im.thumbnail(size)
                im.save(out_dir + out_file + ".jpg", "JPEG")
            except IOError:
                print("cannot create thumbnail for '%s'" % in_file)


def clean_to_squares():
    to_remove = []
    folder = "./img/pics/"
    for filename in os.listdir(folder):
        if (filename.split(".")[-1].lower == "jpg"):
            image = Image.open(folder+filename)
            width, height = image.size
            if(width != height):
                remove_img(folder + filename)
                to_remove.append(True)
            else:
                continue
    
    print(to_remove)


def remove_img(path):
    os.remove(path)

def get_files_no_dirs(path):
    files = []
    all_content = os.listdir(path)
    for elem in all_content:
        if (len(elem.split(".")) > 1):
            files.append(elem)
    return files