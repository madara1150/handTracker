import os

def get_filenames():
    filenames = []
    for filename in os.listdir("data"):
        filenames.append(os.path.join("data", filename))
    return filenames

def create_floder(name):
    os.makedirs(f"data/{name}")

def create_floder_crop(name):
    os.makedirs(f"crop/{name}")

def check_folders():
    folders = os.listdir("data/")
    folders.sort()
    labels_dict = {int(folder): folder for folder in folders}
    return labels_dict

def get_fileCrop():
    filenames = []
    for filename in os.listdir("crop"):
        filenames.append(filename)
    return filenames