from tkinter import *
from PIL import ImageTk, Image

display = Tk()
frame = Frame(display, width=300,height=300)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame,bg='white', width=300, height=300)
coordinates = 20, 50, 210, 230
#arc = canvas.create_arc(coordinates, start=0, extent=359, fill="orange")
#arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
#arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")

fBullet = ImageTk.PhotoImage(file = "fBullet.png")

label = Label(display, image=fBullet)
label.pack()


# file = PhotoImage(file = "fBullet.png")
# image = canvas.create_image(150, 150, image=file)

canvas.pack(expand = True, fill = BOTH)
 
display.mainloop()