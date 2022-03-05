# from tkinter import *
# from tkinter.filedialog import askopenfilename, askopenfile
# import add_label as al


# class Test(Frame):

#     def __init__(self):
#         pass


#     def add_test(self):
        # filetypes = (("Python файл", "*.py"),
        #              ("Любой", "*"))
        # filepath = askopenfilename(title="Открыть файл", initialdir="/",
        #                               filetypes=filetypes)
        # filename = filepath.split("/")                    
        # filename = askopenfile(filetypes=['.jpeg', '.jpg', '.png', '.gif',
        #                                                '.tiff', '.tif', '.bmp'])              
        # if filename:
        #     print(filename)
            # panel = al.AddLabel(filename[-1])
            # panel.grid(column=1, row=2, sticky=W)

import os

print(os.listdir())