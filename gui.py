from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from cartoonify import *

top = tk.Tk()
top.geometry('400x400')
top.title("Cartooner")
top.configure(background='white')
label=Label(top, background='#CDCDCD', font=('Ubuntu', 20, 'bold'))

upload = Button(top, text="Make A Cartoon", command=upload(), padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('Ubuntu', 10, 'bold'))
upload.pack(side=TOP, pady=50)

save_img = Button(top, text="Save Image", command=save(resized6, ImagePath), padx=50, pady=5)
save_img.configure(background='#364156', foreground='white', font=('Ubuntu', 10, 'bold'))
save_img.pack(side=TOP, pady=50)

top.mainloop()