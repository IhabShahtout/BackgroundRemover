import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import cv2
import numpy as np
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("800x600")
        self.style = ttk.Style(theme="cosmo")

        # Buttons Frame
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.TOP, pady=10, fill=tk.X)

        # Load Image
        self.load_button = ttk.Button(
            self.button_frame,
            text="Load Image",
            command=self.load_image,
            bootstyle=PRIMARY
        )
        self.load_button.pack(side=tk.LEFT, padx=10)

        # Remove Background
        self.remove_bg_button = ttk.Button(
            self.button_frame,
            text="Remove Background",
            command=self.remove_background,
            bootstyle=SUCCESS
        )
        self.remove_bg_button.pack(side=tk.LEFT, padx=10)

        # Save Image
        self.save_button = ttk.Button(
            self.button_frame,
            text="Save Image",
            command=self.save_image,
            bootstyle=INFO
        )
        self.save_button.pack(side=tk.LEFT, padx=10)

        # Quality Control
        self.quality_control_frame = ttk.Frame(self.root)
        self.quality_control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.quality_label = ttk.Label(
            self.quality_control_frame,
            text="Quality (JPEG 1-100 / PNG 0-9):"
        )
        self.quality_label.pack(side=tk.LEFT)

        self.quality_value = tk.IntVar(value=95)
        self.quality_scale = ttk.Scale(
            self.quality_control_frame,
            from_=1,
            to=100,
            variable=self.quality_value,
            orient=tk.HORIZONTAL,
            length=200,
            command=self.update_quality_display
        )
        self.quality_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        self.quality_display = ttk.Label(
            self.quality_control_frame,
            text=f"Quality: {self.quality_value.get()}"
        )
        self.quality_display.pack(side=tk.LEFT, padx=10)

        # Image Display
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(side=tk.TOP, pady=20, fill=tk.BOTH, expand=True)

        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Attribution
        self.attribution_label = ttk.Label(
            self.root,
            text="Developed by: Eng Ihab Shahtout",
            font=("Arial", 10),
            bootstyle=SECONDARY
        )
        self.attribution_label.pack(side=tk.BOTTOM, pady=10)

        # Image storage
        self.original_image = None
        self.processed_image = None

    def update_quality_display(self, *args):
        self.quality_display.config(text=f"Quality: {self.quality_value.get()}")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image)

    def display_image(self, image):
        display_image = image.copy()
        display_image.thumbnail((700, 500))
        photo = ImageTk.PhotoImage(display_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def remove_background(self):
        if self.original_image:
            self.processed_image = remove(self.original_image)
            self.display_image(self.processed_image)
        else:
            messagebox.showwarning("No Image", "Please load an image first.")

    def save_image(self):
        if self.processed_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG Files", "*.png"),
                    ("JPEG Files", "*.jpg;*.jpeg"),
                    ("All Files", "*.*")
                ]
            )
            if file_path:
                file_extension = os.path.splitext(file_path)[1].lower()
                quality = self.quality_value.get()
                if file_extension == ".png":
                    compress_level = int(quality * 0.09)
                    compress_level = max(0, min(compress_level, 9))
                    self.processed_image.save(file_path, compress_level=compress_level)
                    messagebox.showinfo("Success", "Image saved successfully as PNG!")
                elif file_extension in [".jpg", ".jpeg"]:
                    try:
                        background = Image.new("RGB", self.processed_image.size, (255, 255, 255))
                        background.paste(self.processed_image, mask=self.processed_image.split()[3])
                        background.save(file_path, format='JPEG', quality=quality)
                        messagebox.showinfo(
                            "Success",
                            f"Image saved successfully as JPEG with quality {quality}!"
                        )
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to save as JPEG: {e}")
                else:
                    messagebox.showwarning("Unsupported Format", "Please choose a supported format (PNG, JPG).")
        else:
            messagebox.showwarning("No Processed Image", "Please process an image first.")


if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = BackgroundRemoverApp(root)
    root.mainloop()
