import os

def get_filenames():
    filenames = []
    for filename in os.listdir("image"):
        filenames.append(os.path.join("image", filename))
    return filenames

def create_floder(name):
    os.makedirs(f"img/{name}")