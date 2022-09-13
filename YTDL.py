from tkinter import *
from tkinter import filedialog
from pytube import YouTube

#Functions
def select_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)
    else:
        path_label.config(text='Select Path To Save File: ')

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget('text')
    YouTube(get_link).streams.get_highest_resolution().download(output_path=user_path)

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
path_label = Label(root, text='Select Path To Save File: ', font=('Arial', 16))
select_btn = Button(root, text='Select', command=select_path)

#buttons
dl_btn = Button(root, text='Download!',  command=download_file)

#add widgets to window
canvas.create_window(250, 220, window=link_label)
canvas.create_window(250, 250, window=link_field)
canvas.create_window(250, 300, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 400, window=dl_btn)


root.mainloop()
