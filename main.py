import os 
import shutil

#######################
desktop_dir = os.path.dirname(os.path.realpath(__file__))
#######################

png_dir = desktop_dir + "/png_folder/"
txt_dir = desktop_dir + "/txt_folder/"
video_dir = desktop_dir + "/video_folder/"
documents_dir = desktop_dir + "/documents_folder/"

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
        if file.endswith(".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"):
            if not os.path.exists(png_dir):
                os.mkdir(png_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, png_dir)
            print(f"Moving {file} ...")

def video_filesclean():
    files_on_desktop = os.listdir(desktop_dir)
    for file in files_on_desktop:
        if file.endswith(".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"):
            if not os.path.exists(video_dir):
                os.mkdir(video_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, video_dir)
            print(f"Moving {file} ...")

def documents_filesclean():
    files_on_desktop = os.listdir(desktop_dir)
    for file in files_on_desktop:
        if file.endswith(".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"):
            if not os.path.exists(documents_dir):
                os.mkdir(documents_dir)
            file_dir = desktop_dir + "/" + file
            shutil.move(file_dir, documents_dir)
            print(f"Moving {file} ...")

    
if __name__ == "__main__":
    txt_filesclean()
    png_filesclean()
    video_filesclean()