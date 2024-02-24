import os

def get_filenames():
    filenames = []
    for filename in os.listdir("data"):
        filenames.append(os.path.join("data", filename))
    return filenames

def create_floder(name):
    os.makedirs(f"data/{name}")