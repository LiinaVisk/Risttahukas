from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import math

class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 800
        self.__height = 700
        self.default_font = font.Font(family="Verdana", size=16)

        self.title("Risttahukas")
        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        self.create_frame_widgets()

        self.bind("<Return>", lambda event: self.send_click())
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="lime", height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg="yellow")
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        lbl_height = Label(self.top_frame, text="Sisesta kõrgus:", font=self.default_font)
        lbl_height.grid(row=1, column=0, padx=5, pady=5)

        self.height_entry = Entry(self.top_frame, font=self.default_font)
        self.height_entry.grid(row=2, column=0, padx=5, pady=5)
        self.height_entry.focus()

        lbl_length = Label(self.top_frame, text="Sisesta pikkus:", font=self.default_font)
        lbl_length.grid(row=3, column=0, padx=5, pady=5)

        self.length_entry = Entry(self.top_frame, font=self.default_font)
        self.length_entry.grid(row=4, column=0, padx=5, pady=5)

        lbl_width = Label(self.top_frame, text="Sisesta laius:", font=self.default_font)
        lbl_width.grid(row=5, column=0, padx=5, pady=5)

        self.width_entry = Entry(self.top_frame, font=self.default_font)
        self.width_entry.grid(row=6, column=0, padx=5, pady=5)

        btn_send = Button(self.top_frame, text="Arvuta", font=self.default_font, command=self.send_click)
        btn_send.grid(row=7, column=0, padx=5, pady=5)

        self.text_box = Text(self.bottom_frame, font=self.default_font, state=DISABLED)
        scrollbar = Scrollbar(self.bottom_frame, orient="vertical")
        scrollbar.config(command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

    def on_close(self):
        if messagebox.askokcancel("Lähed ?", "Kas said vajaliku abi ?"):
            self.destroy()

    def send_click(self):
        try:
            height = float(self.height_entry.get())
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())

            # Kontrolli, kas sisestatud väärtused on positiivsed
            if height <= 0 or length <= 0 or width <= 0:
                messagebox.showwarning("Vigane sisestus", "Palun sisestage positiivsed väärtused.")
                return
        except ValueError:
            messagebox.showwarning("Vigane sisestus", "Palun sisestage numbrilised väärtused.")
            return

        diagonal = self.controller.model.calculate_diagonal(height, length, width)
        surface_area = self.controller.model.calculate_surface_area(height, length, width)
        volume = self.controller.model.calculate_volume(height, length, width)

        input_data = f"Risttahuka kõrgus on {height}, laius on {length} ja pikkus on {width}"
        result_text = f"{input_data}\nDiagonaal: {diagonal:.2f}\nTäis pindala: {surface_area:.2f}\nRuumala: {volume:.2f}"
        self.display_results(result_text)

        if self.controller.model.game_over:
            self.height_entry["state"] = "disabled"
            self.length_entry["state"] = "disabled"
            self.width_entry["state"] = "disabled"

    def display_results(self, result_text):
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, END)  # Remove previous text
        self.text_box.insert(END, result_text)
        self.text_box.config(state="disabled")

