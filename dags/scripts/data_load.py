import os

def load_data():
    # Access data and model
    print("Accessing data and model...")
    path_to_folder = "dataset/brain_tumor_dataset"
    no_tumor_img = os.listdir(path=os.path.join(path_to_folder, 'no'))
    yes_tumor_img = os.listdir(path=os.path.join(path_to_folder, 'yes'))