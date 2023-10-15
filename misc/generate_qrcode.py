import tkinter as tk
from tkinter import ttk
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from tkinter import messagebox

class DataEntryForm:
    def __init__(self, master):
        self.master = master
        master.title("Data Entry Form")

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_address = tk.Label(master, text="Address:")
        self.label_address.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.entry_address = tk.Entry(master)
        self.entry_address.grid(row=1, column=1, padx=10, pady=10)

        self.print_button = tk.Button(master, text="Print", command=self.print_data)
        self.print_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.barcode_button = tk.Button(master, text="Generate Barcode", command=self.generate_barcode)
        self.barcode_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.qrcode_button = tk.Button(master, text="Generate QR Code", command=self.generate_qrcode)
        self.qrcode_button.grid(row=4, column=0, columnspan=2, pady=10)

    def print_data(self):
        name = self.entry_name.get()
        address = self.entry_address.get()

        if name and address:
            print("Name:", name)
            print("Address:", address)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def generate_barcode(self):
        name = self.entry_name.get()
        if name:
            code = Code128(name, writer=ImageWriter(), add_checksum=False)
            filename = f"barcode_{name}.png"
            code.save(filename)
            messagebox.showinfo("Barcode Generated", f"Barcode saved as {filename}")
        else:
            messagebox.showerror("Error", "Please enter a name before generating a barcode.")

    def generate_qrcode(self):
        name = self.entry_name.get()
        if name:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(name)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            filename = f"qrcode_{name}.png"
            img.save(filename)
            messagebox.showinfo("QR Code Generated", f"QR Code saved as {filename}")
        else:
            messagebox.showerror("Error", "Please enter a name before generating a QR code.")


def main():
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()


if __name__ == "__main__":
    main()
