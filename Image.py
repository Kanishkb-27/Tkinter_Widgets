import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()

root.title("Tkinter Image Example")

# Load image with PIL

image = Image.open("istockphoto-460682111-612x612.jpg")

# Resize (optional)

image = image.resize((300, 200))

# Convert to Tkinter format

photo = ImageTk.PhotoImage(image)

# Display image

label = tk.Label(root, image=photo)

label.pack()

root.mainloop()