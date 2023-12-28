import os 
import shutil

#######################
desktop_dir = "C:/Users/basti/OneDrive/Desktop"
#######################

png_dir = desktop_dir + "/png_folder/"
txt_dir = desktop_dir + "/txt_folder/"
jpg_dir = desktop_dir + "/jpg_folder/"

def txt_filesclean():
    files_on_desktop = os.listdir(desktop_dir)
    for file in files_on_desktop:
        if file.endswith(".txt"):
            if not os.path.exists(txt_dir):
                os.mkdir(txt_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, txt_dir)
            print(f"Moving {file} ...")
        
def png_filesclean():
    files_on_desktop = os.listdir(desktop_dir)
    for file in files_on_desktop:
        if file.endswith(".png"):
            if not os.path.exists(png_dir):
                os.mkdir(png_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, png_dir)
            print(f"Moving {file} ...")

def jpg_filesclean():
    files_on_desktop = os.listdir(desktop_dir)
    for file in files_on_desktop:
        if file.endswith(".jpg"):
            if not os.path.exists(jpg_dir):
                os.mkdir(jpg_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, jpg_dir)
            print(f"Moving {file} ...")

    
if __name__ == "__main__":
    txt_filesclean()
    png_filesclean()
    jpg_filesclean()