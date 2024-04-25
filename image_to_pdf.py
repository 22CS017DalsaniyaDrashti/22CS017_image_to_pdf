import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("400x200")  # Increased size
        
        # Create title label
        self.title_label = tk.Label(root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Create labels
        self.label = tk.Label(root, text="Select an Image:")
        self.label.pack(pady=5)

        # Create buttons
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=5)

    def select_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    def convert_to_pdf(self):
        if not hasattr(self, 'filepath'):
            return

        # Open the image
        image = Image.open(self.filepath)
        
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Calculate aspect ratio
        aspect_ratio = image.height / image.width
        # Set maximum width for the PDF
        max_width = 200  # You can adjust this value
        
        # Resize the image to fit within the width
        new_width = min(image.width, max_width)
        new_height = int(new_width * aspect_ratio)
        image = image.resize((new_width, new_height))

        # Save image to PDF
        pdf.image(self.filepath, 0, 0, new_width, new_height)
        pdf_output_path = self.filepath.replace('.jpg', '.pdf').replace('.jpeg', '.pdf').replace('.png', '.pdf')
        pdf.output(pdf_output_path)

        # Inform user about successful conversion
        messagebox.showinfo("Success", "Conversion completed! PDF saved as {}".format(pdf_output_path))

# Create the main application window
root = tk.Tk()
app = ImageToPDFConverter(root)
root.mainloop()

