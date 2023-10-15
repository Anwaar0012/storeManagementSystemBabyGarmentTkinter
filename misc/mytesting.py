import tkinter as tk
from tkinter import ttk
from fpdf import FPDF
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from tkinter import messagebox
from PIL import Image, ImageTk
# from barcode import Code128
# from barcode.writer import ImageWriter

class DataEntryForm:
    def __init__(self, master):
        self.master = master
        master.title("Simple Form with PDF, Barcode, and QR Code")

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_city = tk.Label(master, text="City:")
        self.label_city.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.entry_city = tk.Entry(master)
        self.entry_city.grid(row=1, column=1, padx=10, pady=10)

        self.print_button = tk.Button(master, text="Print PDF", command=self.print_pdf)
        self.print_button.grid(row=2, column=0, columnspan=2, pady=10)

    def print_pdf(self):
        name = self.entry_name.get()
        city = self.entry_city.get()

        if name and city:
            pdf = FPDF()
            pdf.add_page()

            # Add text to PDF
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"City: {city}", ln=True, align='L')

            # Generate barcode and add to PDF
            barcode_filename = f"barcode_{name}.png"
            code128 = Code128(name, writer=ImageWriter())
            code128.save(barcode_filename)
            pdf.image(barcode_filename, x=10, y=pdf.get_y() + 10, w=50)

            # Generate QR code and add to PDF
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(f"Name: {name}\nCity: {city}")
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_filename = f"qrcode_{name}.png"
            qr_img.save(qr_filename)
            pdf.image(qr_filename, x=70, y=pdf.get_y() + 10, w=50)

            # Save PDF
            pdf_output_filename = f"data_details_{name}.pdf"
            pdf.output(pdf_output_filename)

            messagebox.showinfo("PDF Generated", f"PDF with details saved as {pdf_output_filename}")

            # Display barcode and QR code images
            barcode_img = Image.open(barcode_filename)
            barcode_img = barcode_img.resize((100, 50), Image.ANTIALIAS)
            barcode_img = ImageTk.PhotoImage(barcode_img)

            qr_img = Image.open(qr_filename)
            qr_img = qr_img.resize((100, 100), Image.ANTIALIAS)
            qr_img = ImageTk.PhotoImage(qr_img)

            barcode_label = tk.Label(self.master, text="Barcode")
            barcode_label.grid(row=3, column=0, pady=10)
            barcode_display = tk.Label(self.master, image=barcode_img)
            barcode_display.image = barcode_img
            barcode_display.grid(row=4, column=0, pady=10)

            qr_label = tk.Label(self.master, text="QR Code")
            qr_label.grid(row=3, column=1, pady=10)
            qr_display = tk.Label(self.master, image=qr_img)
            qr_display.image = qr_img
            qr_display.grid(row=4, column=1, pady=10)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

def main():
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()

