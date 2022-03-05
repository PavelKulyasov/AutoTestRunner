from tkinter import *
from tkinter.filedialog import askdirectory


class AddLabel(Frame):
    
    def __init__(self, name, number):
        super(AddLabel, self).__init__()
        self.number = number
        self.colortext = None
        if self.number % 2 == 0:
            self.colortext = "#37DE6A"
        else:
            self.colortext = "#FF9540"
        self.marker(name)

    def choose_path_compare(self):
        directory = askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            path_name = directory.replace('/', '\\') if '/' in directory else directory
            self.btn_compare.grid_forget()
            self.lbl_path_compare = Label(self, text=f"{path_name}")
            self.lbl_path_compare.grid(column=2, row=1, padx=5)

    def marker(self, text):

        self.lbl_text = Label(self, text=text, background=f'{self.colortext}', borderwidth="5", )
        self.lbl_text.grid(column=0, row=1, padx=5)

        self.btn_compare = Button(self, text="Файлы для сравнения", command=self.choose_path_compare)
        self.btn_compare.grid(column=1, row=1, padx=5)
