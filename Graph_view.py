from PIL import Image as PilImage
from PIL import ImageTk

from tkinter import *
from tkinter.ttk import Notebook

class GraphView:
    def __init__(self, root, width, height, moment_inert_dev, title="    Условные обозначения схемы нагружения",
                 resizeble=(False, False), icon=None):
        self.root = Toplevel(root)
        self.value = float(moment_inert_dev)
        self.moment_dev_list = [1.1, 1.3, 1.6, 2.0, 2.5, 3.0, 4.0, 5.0]
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+50")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)

        self.orig_img1 = PilImage.open(r"Data\Graph_103_760x1080.png")
        self.orig_img2 = PilImage.open(r"Data\Graph_104_760x1080.png")
        self.orig_img3 = PilImage.open(r"Data\Graph_105_760x1080.png")
        self.orig_img4 = PilImage.open(r"Data\Graph_106_760x1080.png")
        self.orig_img5 = PilImage.open(r"Data\Graph_107_760x1080.png")
        self.orig_img6 = PilImage.open(r"Data\Graph_108_760x1080.png")
        self.orig_img7 = PilImage.open(r"Data\Graph_109_760x1080.png")
        self.orig_img8 = PilImage.open(r"Data\Graph_110_760x1080.png")

        self.graph_103_img = ImageTk.PhotoImage(self.orig_img1)
        self.graph_104_img = ImageTk.PhotoImage(self.orig_img2)
        self.graph_105_img = ImageTk.PhotoImage(self.orig_img3)
        self.graph_106_img = ImageTk.PhotoImage(self.orig_img4)
        self.graph_107_img = ImageTk.PhotoImage(self.orig_img5)
        self.graph_108_img = ImageTk.PhotoImage(self.orig_img6)
        self.graph_109_img = ImageTk.PhotoImage(self.orig_img7)
        self.graph_110_img = ImageTk.PhotoImage(self.orig_img8)

        self.draw_notebook()
        self.tab_choise()
        self.tabs_control.bind("<<NotebookTabChanged>>", self.tab_changed)

        self.zoomcycle = 0
        self.zimg_id = None

        self.root.bind("<MouseWheel>", self.zoomer)


    def tab_changed(self, event):
        self.tab_current = self.tabs_control.select()
        if self.tab_current[-1] == "e":
            self.orig_img = self.orig_img1
            self.canvas = self.tab_1_canv
        elif self.tab_current[-1] == "2":
            self.orig_img = self.orig_img2
            self.canvas = self.tab_2_canv
        elif self.tab_current[-1] == "3":
            self.orig_img = self.orig_img3
            self.canvas = self.tab_3_canv
        elif self.tab_current[-1] == "4":
            self.orig_img = self.orig_img4
            self.canvas = self.tab_4_canv
        elif self.tab_current[-1] == "5":
            self.orig_img = self.orig_img5
            self.canvas = self.tab_5_canv
        elif self.tab_current[-1] == "6":
            self.orig_img = self.orig_img6
            self.canvas = self.tab_6_canv
        elif self.tab_current[-1] == "7":
            self.orig_img = self.orig_img7
            self.canvas = self.tab_7_canv
        elif self.tab_current[-1] == "8":
            self.orig_img = self.orig_img8
            self.canvas = self.tab_8_canv

    def draw_notebook(self):
        self.tabs_control = Notebook(self.root, height=100, width=30, padding=(0, 10, 0, 0))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="√(J2/J1)= 1.1", underline=0)
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="√(J2/J1)= 1.3", underline=1)
        self.tab_3 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_3, text="√(J2/J1)= 1.6", underline=1)
        self.tab_4 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_4, text="√(J2/J1)= 2.0", underline=1)
        self.tab_5 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_5, text="√(J2/J1)= 2.5", underline=1)
        self.tab_6 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_6, text="√(J2/J1)= 3.0", underline=1)
        self.tab_7 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_7, text="√(J2/J1)= 4.0", underline=1)
        self.tab_8 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_8, text="√(J2/J1)= 5.0", underline=1)
        self.tab_filling()

    def tab_filling(self):
        self.tab_1_canv = Canvas(self.tab_1, width=760, height=1080, background="white")
        self.tab_2_canv = Canvas(self.tab_2, width=760, height=1080, background="white")
        self.tab_3_canv = Canvas(self.tab_3, width=760, height=1080, background="white")
        self.tab_4_canv = Canvas(self.tab_4, width=760, height=1080, background="white")
        self.tab_5_canv = Canvas(self.tab_5, width=760, height=1080, background="white")
        self.tab_6_canv = Canvas(self.tab_6, width=760, height=1080, background="white")
        self.tab_7_canv = Canvas(self.tab_7, width=760, height=1080, background="white")
        self.tab_8_canv = Canvas(self.tab_8, width=760, height=1080, background="white")

        self.tab_1_canv.create_image(0, 0, image=self.graph_103_img, anchor="nw")
        self.tab_2_canv.create_image(0, 0, image=self.graph_104_img, anchor="nw")
        self.tab_3_canv.create_image(0, 0, image=self.graph_105_img, anchor="nw")
        self.tab_4_canv.create_image(0, 0, image=self.graph_106_img, anchor="nw")
        self.tab_5_canv.create_image(0, 0, image=self.graph_107_img, anchor="nw")
        self.tab_6_canv.create_image(0, 0, image=self.graph_108_img, anchor="nw")
        self.tab_7_canv.create_image(0, 0, image=self.graph_109_img, anchor="nw")
        self.tab_8_canv.create_image(0, 0, image=self.graph_110_img, anchor="nw")

        self.tabs_control.pack(fill=BOTH, expand=1)
        self.tab_1_canv.pack()
        self.tab_2_canv.pack()
        self.tab_3_canv.pack()
        self.tab_4_canv.pack()
        self.tab_5_canv.pack()
        self.tab_6_canv.pack()
        self.tab_7_canv.pack()
        self.tab_8_canv.pack()

        self.tab_1_canv.bind("<Motion>", self.crop)
        self.tab_2_canv.bind("<Motion>", self.crop)
        self.tab_3_canv.bind("<Motion>", self.crop)
        self.tab_4_canv.bind("<Motion>", self.crop)
        self.tab_5_canv.bind("<Motion>", self.crop)
        self.tab_6_canv.bind("<Motion>", self.crop)
        self.tab_7_canv.bind("<Motion>", self.crop)
        self.tab_8_canv.bind("<Motion>", self.crop)

    def zoomer(self, event):
        if (event.delta > 0):
            if self.zoomcycle != 4: self.zoomcycle += 1
        elif (event.delta < 0):
            if self.zoomcycle != 0: self.zoomcycle -= 1
        self.crop(event)

    def crop(self, event):
        if self.zimg_id: self.canvas.delete(self.zimg_id)
        if (self.zoomcycle) != 0:
            x, y = event.x, event.y
            if self.zoomcycle == 1:
                tmp = self.orig_img.crop((x-45, y-30, x+45, y+30))
            elif self.zoomcycle == 2:
                tmp = self.orig_img.crop((x-30, y-20, x+30, y+20))
            elif self.zoomcycle == 3:
                tmp = self.orig_img.crop((x-15, y-10, x+15, y+10))
            elif self.zoomcycle == 4:
                tmp = self.orig_img.crop((x-6, y-4, x+6, y+4))
            size = 300, 200
            self.zimg = ImageTk.PhotoImage(tmp.resize(size))
            self.zimg_id = self.canvas.create_image(event.x, event.y, image=self.zimg)

    def tab_choise(self):
        self.val_moment_list = self.nearest(self.moment_dev_list, self.value)
        self.ind_moment_list = self.moment_dev_list.index(self.val_moment_list)
        if self.ind_moment_list == 0:
            self.tabs_control.select(self.tab_1)
        if self.ind_moment_list == 1:
            self.tabs_control.select(self.tab_2)
        if self.ind_moment_list == 2:
            self.tabs_control.select(self.tab_3)
        if self.ind_moment_list == 3:
            self.tabs_control.select(self.tab_4)
        if self.ind_moment_list == 4:
            self.tabs_control.select(self.tab_5)
        if self.ind_moment_list == 5:
            self.tabs_control.select(self.tab_6)
        if self.ind_moment_list == 6:
            self.tabs_control.select(self.tab_7)
        if self.ind_moment_list == 7:
            self.tabs_control.select(self.tab_8)

    def nearest(self, lst, value):
        return min(lst, key=lambda x: abs(x - value))
