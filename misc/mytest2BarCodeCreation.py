import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from barcode import Code128
from barcode.writer import ImageWriter
import qrcode

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

            # Save PDF
            pdf_output_filename = f"data_details_{name}.pdf"
            pdf.output(pdf_output_filename)

            messagebox.showinfo("PDF Generated", f"PDF with details saved as {pdf_output_filename}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

def main():
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
