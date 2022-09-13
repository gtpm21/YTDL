from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import pytube.exceptions
import logging                  
import os 

#Functions
def select_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)
    else:
        path_label.config(text=DOWNLOAD_FOLDER)

def download_file():
    if link_field.get():
        video_url = link_field.get()
    else:
        messagebox.showerror('Error', 'Please provide a viable link!')

    path = path_label.cget('text')

    try:
        logging.info("Requesting video data")
        video_title = str(YouTube(video_url).title)
    except pytube.exceptions.RegexMatchError:
        raise ValueError(f"Video URL {video_url} does not exist")
    except pytube.exceptions.VideoPrivate:
        raise ValueError(f"Video URL {video_url} is private")
    except pytube.exceptions.MembersOnly:
        raise ValueError(f"Video URL {video_url} is Members Only")
    except pytube.exceptions.RecordingUnavailable:
        raise ValueError(f"Video URL {video_url} does not have a recording for the livestream")
    except pytube.exceptions.VideoUnavailable:
        raise ValueError(f"Video URL {video_url} does not have an available video")
    except pytube.exceptions.LiveStreamError:
        raise ValueError(f"Video URL {video_url} is a livestream and cannot be downloaded")

    logging.info("Checking if ouput file already exists")
    if os.path.exists(os.path.join(path, video_title)):
        logging.info(f"Found existing output file, exiting download() and returning 'File {os.path.join(path, video_title)} already exists'")
        return f"File {os.path.join(path, video_title)} already exists"

    print(f"Downloading {video_title} to {path}")
    YouTube(video_url).streams.get_highest_resolution().download(output_path=path)

#main window
root = Tk()
title = root.title('Youtube Downloader')
window_height = 500
window_width = 500
root.resizable(False, False)

#main window position
MyLeftPos = (root.winfo_screenwidth() - window_height) / 2
myTopPos = (root.winfo_screenheight() - window_width) / 2
root.geometry( "%dx%d+%d+%d" % (window_height, window_width, MyLeftPos, myTopPos))

#canvas
canvas = Canvas(root)
canvas.pack(expand=True, fill=BOTH)

#image logo
logo_img = PhotoImage(file='images\youtube-logo-png-46020.png')
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image = logo_img)

#link field
link_field = Entry(root, width=50)
link_label = Label(root, text='Paste Download Link: ', font=('Arial', 16))

#select path
if os.name == "nt":
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
else:  # PORT: For *Nix systems
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
    
path_label_propmt = Label(root, text='Selected Path To Save File: ', font=('Arial', 16))
path_label = Label(root, text=DOWNLOAD_FOLDER, font=('Arial', 14))
select_btn = Button(root, text='Select', command=select_path)

#buttons
dl_btn = Button(root, text='Download!',  command=download_file)

#add widgets to window
canvas.create_window(250, 220, window=link_label)
canvas.create_window(250, 250, window=link_field)
canvas.create_window(250, 300, window=path_label_propmt)
canvas.create_window(250, 330, window=path_label)
canvas.create_window(250, 400, window=select_btn)
canvas.create_window(250, 450, window=dl_btn)


root.mainloop()
