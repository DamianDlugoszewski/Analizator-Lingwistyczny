"""
TkInter - Dialog Window https://docs.python.org/3/library/tk.html
"""

import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog
import analyzer


class App:
    def __init__(self, root):
        root.title("Analizator lingiwstyczny")
        root.geometry("500x300")
        root.resizable(width=False, height=False)
        self.filepath_open = tk.StringVar()
        self.check1_value = tk.IntVar()
        self.check2_value = tk.IntVar()
        self.radio1_value = tk.IntVar()
        self.radio2_value = tk.IntVar()
        self.filepath_save = tk.StringVar()

        label1 = tk.Label(root)
        font = tkfont.Font(size=14)
        label1["font"] = font
        label1["justify"] = "center"
        label1["text"] = "Analizator lingiwstyczny"
        label1.place(x=160, y=0, width=200, height=30)

        button1 = tk.Button(root)
        font = tkfont.Font(size=10)
        button1["font"] = font
        button1["justify"] = "center"
        button1["text"] = "Otwórz"
        button1.place(x=220, y=40, width=70, height=25)
        button1["command"] = lambda: self.open_file()

        label2 = tk.Label(root)
        font = tkfont.Font(size=11)
        label2["font"] = font
        label2["justify"] = "center"
        label2["text"] = "Co analizujemy?"
        label2.place(x=200, y=80, width=110, height=25)

        checkbox1 = tk.Checkbutton(root)
        font = tkfont.Font(size=10)
        checkbox1["font"] = font
        checkbox1["justify"] = "center"
        checkbox1["text"] = "Słowa"
        checkbox1.place(x=200, y=100, width=110, height=25)
        checkbox1["variable"] = self.check1_value
        checkbox1["offvalue"] = 0
        checkbox1["onvalue"] = 1

        checkbox2 = tk.Checkbutton(root)
        font = tkfont.Font(size=10)
        checkbox2["font"] = font
        checkbox2["justify"] = "center"
        checkbox2["text"] = "Litery"
        checkbox2.place(x=200, y=120, width=108, height=25)
        checkbox2["variable"] = self.check2_value
        checkbox2["offvalue"] = 0
        checkbox2["onvalue"] = 1

        label3 = tk.Label(root)
        font = tkfont.Font(size=11)
        label3["font"] = font
        label3["justify"] = "center"
        label3["text"] = "Sortowanie"
        label3.place(x=200, y=150, width=110, height=25)

        radio1 = tk.Radiobutton(root)
        font = tkfont.Font(size=10)
        radio1["font"] = font
        radio1["justify"] = "center"
        radio1["text"] = "Znak"
        radio1.place(x=110, y=180, width=85, height=25)
        radio1["variable"] = self.radio1_value
        radio1["value"] = 0

        radio2 = tk.Radiobutton(root)
        font = tkfont.Font(size=10)
        radio2["font"] = font
        radio2["justify"] = "center"
        radio2["text"] = "Ilość wystąpień"
        radio2.place(x=128, y=200, width=110, height=25)
        radio2["variable"] = self.radio1_value
        radio2["value"] = 1

        radio3 = tk.Radiobutton(root)
        font = tkfont.Font(size=10)
        radio3["font"] = font
        radio3["justify"] = "center"
        radio3["text"] = "Rosnąco"
        radio3.place(x=300, y=180, width=85, height=25)
        radio3["variable"] = self.radio2_value
        radio3["value"] = 0

        radio4 = tk.Radiobutton(root)
        font = tkfont.Font(size=10)
        radio4["font"] = font
        radio4["justify"] = "center"
        radio4["text"] = "Malejąco"
        radio4.place(x=300, y=200, width=85, height=25)
        radio4["variable"] = self.radio2_value
        radio4["value"] = 1

        button2 = tk.Button(root)
        ft = tkfont.Font(size=10)
        button2["font"] = ft
        button2["justify"] = "center"
        button2["text"] = "Zapisz"
        button2.place(x=220, y=240, width=70, height=25)
        button2["command"] = lambda: self.save_file()

        label4 = tk.Label(root)
        ft = tkfont.Font(size=6)
        label4["font"] = ft
        label4["justify"] = "center"
        label4["text"] = "by Damian Długoszewski"
        label4.place(x=160, y=270, width=190, height=30)

        radio1.select()
        radio2.deselect()
        radio3.select()
        radio4.deselect()

    def open_file(self):
        """Otwórz plik aby przeanalizować tekst"""
        self.filepath_open = filedialog.askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )

    def save_file(self):
        """Wskaż plik, do którego ma zostać zapisana analiza tekstu"""
        self.filepath_save = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        analyzer.start(self.filepath_open,
                       self.check1_value.get(),
                       self.check2_value.get(),
                       self.radio1_value.get(),
                       self.radio2_value.get(),
                       self.filepath_save)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
