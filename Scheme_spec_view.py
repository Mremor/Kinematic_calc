from tkinter import *


class SchemeSpecView:
    def __init__(self, root, width, height, scheme_spec_img, title="    Условные обозначения схемы нагружения",
                 resizeble=(False, False), icon=None):
        self.root = Toplevel(root)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+50")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)
        self.width = width
        self.height = height
        self.scheme_spec_img = scheme_spec_img
        self.run_spec()




    def run_spec(self):
        self.scheme_spec_frame = Frame(self.root, bg="#704404", width=self.width, height=self.height)
        self.scheme_spec_label = Label(self.scheme_spec_frame, image=self.scheme_spec_img)
        self.scheme_spec_label.image = self.scheme_spec_img

        self.scheme_spec_frame.place(x=0, y=0)
        self.scheme_spec_label.pack()










