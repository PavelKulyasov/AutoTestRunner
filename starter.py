from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename, askopenfile
from os import path, makedirs, startfile, system, listdir, remove, rmdir
import add_label as al

class Starter(Frame):

    tests_to_start = [0]

    def __init__(self, parent):
        self.menu = Frame(master=parent)
        self.menu.grid(column=0, row=1, sticky=W)
        self.row_number = 2
        self.parent = parent
        self.buttons_menu()

    def add_test(self):
        filetypes = (("Python файл", "*.py"),
                     ("Любой", "*"))
        filepath = askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)

        filename = self.ready_path(filepath)
        self.tests_to_start.append(filename)
        if filename:
            panel = al.AddLabel(path.basename(filename), self.row_number)
            panel.grid(column=0, row=self.row_number, sticky=W)
            self.row_number += 1

    def start_test(self):
        if len(self.tests_to_start) > 1:
            for test in self.tests_to_start[1:]:
                system(test)
        
    def ready_path(self, filepath):

        path_name = filepath.replace('/', '\\') if '/' in filepath else filepath
        return path_name

    def buttons_menu(self):
        self.btn_add = Button(master=self.menu, text="Добавить тест", command=self.add_test)
        self.btn_add.grid(column=0, row=1, padx=5, sticky=W)

        self.btn_start = Button(master=self.menu, text="Fire!!!", command=self.start_test)
        self.btn_start.grid(column=1, row=1, padx=5, sticky=W)

if __name__ == '__main__':
    root = Tk()
    root.geometry("200x100+300+300")
    app = Starter(root)
    root.mainloop() 