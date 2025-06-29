import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def convert_to_sketch(img_path):
    image = cv2.imread(img_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
    return sketch

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        sketch = convert_to_sketch(file_path)
        output_path = os.path.splitext(file_path)[0] + "_sketch.jpg"
        cv2.imwrite(output_path, sketch)
        messagebox.showinfo("Success", f"Pencil sketch saved as:\n{output_path}")
        show_result(output_path)

def show_result(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    result_label.config(image=img_tk)
    result_label.image = img_tk

# Set up the GUI
root = tk.Tk()
root.title("Pencil Sketch Converter")
root.geometry("400x450")
root.resizable(False, False)

title_label = tk.Label(root, text="Pencil Sketch Converter", font=("Arial", 16))
title_label.pack(pady=10)

btn = tk.Button(root, text="Select Image", command=select_image, font=("Arial", 12))
btn.pack(pady=10)

result_label = tk.Label(root)
result_label.pack(pady=10)

root.mainloop()
