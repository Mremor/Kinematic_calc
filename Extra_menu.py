from tkinter import *
from tkinter import messagebox as mb
#from tkinter import filedialog as fd

from Ring_search import RingSearch
from Force_hydro import ForceHydro
from Wall_thickness import WallThickness
from Threaded_connect import ThreadedConnect
from Ear_calc import Ear
from Bottom_thickness import BottomThickness
from Hydra_at_down import HydraAtDown
from PDF_view import PDFViewer




class AdvanceMenu:
    def __init__(self, parent, width, height, title=" ", resizeble=(False, False), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)
        self.ring_list_AMG = [(3, 5, 1.4), (3, 7, 1.9), (4, 8, 1.9), (6, 9, 1.9), (6.5, 9.5, 1.9), (7, 10, 1.9),
                          (7.5, 10.5, 1.9),
                          (8, 11, 1.9), (7, 11, 2.5), (7.5, 11.5, 2.5), (9, 12, 1.9), (8, 12, 2.5),
                          (9.5, 12.5, 1.9),
                          (10, 13, 1.9), (9, 13, 2.5), (11, 14, 1.9), (10, 14, 2.5), (12, 15, 1.9),
                          (11, 15, 2.5),
                          (10, 15, 3.0), (13, 16, 1.9), (12, 16, 2.5), (11, 16, 3.0), (13.5, 16.5, 1.9),
                          (14, 17, 1.9),
                          (13, 17, 2.5), (12, 17, 3.0), (15, 18, 1.9), (14, 18, 2.5), (13, 18, 3.0),
                          (16, 19, 1.9),
                          (15, 19, 2.5), (14, 19, 3.0), (17, 20, 1.9), (16, 20, 2.5), (15, 20, 3.0),
                          (14, 20, 3.6),
                          (18, 21, 1.9), (17, 21, 2.5), (19, 22, 1.9), (18, 22, 2.5), (17, 22, 3.0),
                          (16, 22, 3.6),
                          (20, 23, 1.9), (19, 23, 2.5), (20, 24, 2.5), (19, 24, 3.0), (18, 24, 3.6),
                          (21, 25, 2.5),
                          (20, 25, 3.0), (19, 25, 3.6), (22, 26, 2.5), (20, 26, 3.6), (23, 27, 2.5),
                          (22, 27, 3.0),
                          (21, 27, 3.6), (24, 28, 2.5), (23, 28, 3.0), (22, 28, 3.6), (25, 29, 2.5),
                          (24, 29, 3.0),
                          (26, 30, 2.5), (25, 30, 3.0), (24, 30, 3.6), (27, 31, 2.5), (25, 31, 3.6),
                          (29, 32, 1.9),
                          (28, 32, 2.5), (27, 32, 3.0), (26, 32, 3.6), (29, 33, 2.5), (28, 33, 3.0),
                          (29, 34, 2.5),
                          (28, 34, 3.6), (30, 35, 3.0), (29, 35, 3.6), (32, 36, 2.5), (30, 36, 3.6),
                          (32, 37, 3.0),
                          (35, 38, 1.9), (34, 38, 2.5), (32, 38, 3.6), (30, 38, 4.6), (37, 40, 1.9),
                          (36, 40, 2.5),
                          (35, 40, 3.0), (34, 40, 3.6), (32, 40, 4.6), (38, 41, 1.9), (37, 41, 2.5),
                          (36, 41, 3.0),
                          (35, 41, 3.6), (38, 42, 2.5), (38, 42, 3.0), (36, 42, 3.6), (34, 42, 4.6),
                          (35, 43, 4.6),
                          (40, 44, 2.5), (36, 44, 4.6), (40, 45, 3.0), (39, 45, 3.6), (37, 45, 4.6),
                          (40, 46, 3.6),
                          (38, 47, 4.6), (42, 48, 3.6), (40, 48, 4.6), (46, 50, 2.5), (45, 50, 3.0),
                          (44, 50, 3.6),
                          (42, 50, 4.6), (45, 51, 3.6), (46, 52, 3.6), (45, 53, 4.6), (48, 54, 3.6),
                          (50, 55, 3.0),
                          (49, 55, 3.6), (47, 55, 4.6), (50, 56, 3.6), (48, 56, 4.6), (52, 58, 3.6),
                          (50, 58, 4.6),
                          (55, 60, 3.0), (54, 60, 3.6), (52, 60, 4.6), (50, 60, 5.8), (55, 61, 3.6),
                          (56, 62, 3.6),
                          (54, 62, 4.6), (58, 63, 3.0), (57, 63, 3.6), (55, 63, 4.6), (60, 64, 2.5),
                          (58, 64, 3.6),
                          (60, 65, 3.0), (59, 65, 3.6), (57, 65, 4.6), (55, 65, 5.8), (60, 66, 3.6),
                          (62, 68, 3.6),
                          (60, 68, 4.6), (63, 69, 3.6), (65, 70, 3.0), (64, 70, 3.6), (62, 70, 4.6),
                          (65, 71, 3.6),
                          (63, 71, 4.6), (66, 72, 3.6), (64, 72, 4.6), (65, 73, 4.6), (63, 73, 5.8),
                          (68, 74, 3.6),
                          (70, 75, 2.5), (70, 75, 3.0), (69, 75, 3.6), (67, 75, 4.6), (65, 75, 5.8),
                          (70, 76, 3.6),
                          (71, 77, 3.6), (72, 78, 3.6), (70, 78, 4.6), (75, 80, 2.5), (75, 80, 3.0),
                          (74, 80, 3.6),
                          (72, 80, 4.6), (70, 80, 5.8), (75, 81, 3.6), (76, 82, 3.6), (74, 82, 4.6),
                          (75, 83, 4.6),
                          (79, 85, 3.6), (77, 85, 4.6), (75, 85, 5.8), (80, 86, 3.6), (78, 86, 4.6),
                          (82, 88, 3.6),
                          (80, 88, 4.6), (85, 90, 3.0), (84, 90, 3.6), (82, 90, 4.6), (80, 90, 5.8),
                          (88, 92, 3.0),
                          (86, 92, 3.6), (85, 92, 4.6), (85, 92, 5.8), (88, 94, 3.6), (90, 95, 3.0),
                          (90, 96, 3.6),
                          (92, 98, 2.5), (92, 98, 3.6), (90, 98, 4.6), (95, 100, 2.5), (94, 100, 3.6),
                          (92, 100, 4.6),
                          (90, 100, 5.8), (95, 101, 3.6), (96, 102, 3.6), (95, 102, 4.6), (92, 102, 5.8),
                          (98, 104, 3.6),
                          (98, 105, 4.6), (95, 105, 5.8), (100, 108, 4.6), (105, 110, 3.0), (104, 110, 3.6),
                          (102, 110, 4.6),
                          (100, 110, 5.8), (105, 112, 4.6), (102, 112, 5.8), (108, 114, 3.6), (110, 115, 2.5),
                          (110, 115, 3.6), (108, 110, 4.6), (100, 110, 5.8), (110, 118, 4.6), (114, 120, 3.6),
                          (112, 120, 4.6), (110, 120, 5.8), (115, 122, 4.6), (118, 124, 3.6), (120, 125, 3.0),
                          (118, 125, 4.6), (115, 125, 5.8), (120, 128, 4.6), (125, 130, 3.6), (122, 130, 4.6),
                          (120, 130, 5.8), (130, 135, 3.6), (125, 135, 4.6), (125, 135, 5.8), (125, 138, 7.5),
                          (130, 140, 3.6), (130, 140, 4.6), (130, 140, 5.8), (128, 140, 7.5), (140, 145, 3.0),
                          (140, 145, 3.6), (135, 145, 5.8), (145, 150, 3.0), (140, 150, 4.6), (140, 150, 5.8),
                          (145, 155, 5.8), (150, 160, 3.6), (150, 160, 4.6), (150, 160, 5.8), (145, 160, 8.5),
                          (160, 165, 3.6), (155, 165, 4.6), (160, 170, 5.8), (165, 175, 5.8), (175, 180, 3.6),
                          (170, 180, 5.8), (175, 185, 3.6), (175, 185, 5.8), (170, 185, 8.5), (180, 190, 4.6),
                          (180, 190, 5.8), (185, 195, 5.8), (190, 200, 4.6), (190, 200, 5.8), (195, 205, 5.8),
                          (200, 210, 4.6), (200, 210, 5.8), (195, 210, 8.5), (200, 215, 8.5), (210, 220, 4.6),
                          (210, 220, 5.8), (220, 225, 3.6), (220, 230, 4.6), (220, 230, 5.8), (225, 235, 5.8),
                          (220, 235, 8.5), (230, 240, 5.8), (235, 245, 5.8), (245, 250, 3.6), (240, 250, 4.6),
                          (240, 250, 5.8), (235, 250, 8.5), (250, 255, 3.6), (245, 255, 5.8), (250, 260, 5.8),
                          (260, 270, 5.8), (265, 275, 5.8), (270, 280, 5.8), (280, 290, 5.8), (290, 300, 5.8),
                          (290, 305, 5.8)]
        self.ring_list_NGJ = [(12, 15, 1.9), (12, 16, 2.5), (12, 17, 3.0), (14, 18, 2.5), (16, 21, 3.0), (17, 20, 1.9),
                          (17, 21, 2.5), (20, 25, 3.0), (20, 26, 3.6), (21, 25, 2.5), (22, 26, 2.5), (24, 28, 2.5),
                          (26, 29, 1.9), (26, 30, 2.5), (26, 32, 3.6), (30, 36, 3.6), (30, 38, 4.6), (34, 40, 3.6),
                          (36, 42, 3.6), (38, 42, 3.0), (39, 45, 3.6), (40, 46, 3.6), (46, 50, 2.5), (50, 56, 3.6),
                          (52, 58, 3.6), (54, 60, 3.6), (57, 63, 4.6), (66, 72, 3.6), (72, 80, 4.6), (75, 85, 5.8)]
        self.ring_set = IntVar()


        self.draw_widgets()
        self.grab_focus()

    # Взятие фокуса дочерним окном
    def grab_focus(self):
        self.root.focus_set()
        self.root.wait_window()


    # Ввод виджетов
    def draw_widgets(self):
        self.draw_menu()
        self.background_img = PhotoImage(file= r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)


    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, font=("GOST Type BU", 11, "bold"), background="#73c0f4",
                             foreground="#e6eff3", tearoff=0)
        calc_hydro_menu = Menu(menu_bar, font=("GOST Type BU", 11, "bold"), background="#73c0f4",
                               foreground="#e6eff3", tearoff=0)
        instrument_menu = Menu(menu_bar, font=("GOST Type BU", 11, "bold"), background="#73c0f4",
                             foreground="#e6eff3", tearoff=0)

        info_menu = Menu(menu_bar, font=("GOST Type BU", 11, "bold"), background="#73c0f4",
                             foreground="#e6eff3", tearoff=0)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Расчет гидроцилиндров", menu=calc_hydro_menu)
        menu_bar.add_cascade(label="Инструменты", menu=instrument_menu)
        menu_bar.add_cascade(label="Справка", menu=info_menu)

        # Команды меню Файл
        file_menu.add_command(label="Открыть", command=self.pdf_v)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.exit)

        # Команды меню Расчет
        calc_hydro_menu.add_command(label="Усилие гидроцилиндра", command=self.force_calc)
        calc_hydro_menu.add_command(label="Толщина стенки гильзы", command=self.wall_thickness)
        calc_hydro_menu.add_command(label="Резьбовые соединения", command=self.threaded_connections)
        calc_hydro_menu.add_command(label="Расчет проушины", command=self.ear_calc)
        calc_hydro_menu.add_command(label="Определение толщины днища", command=self.bottom_thickness_calc)
        calc_hydro_menu.add_command(label="Расчет на прочность и устойчивость", command=self.hydra_at_down_calc)

        # Команды меню Инструменты
        ring_set_menu = Menu(instrument_menu, tearoff=0)
        ring_set_menu.add_radiobutton(label="Набор для масла АМГ (В-14)", font=("GOST Type BU", 11, "bold"),
                                      background="#73c0f4", foreground="#e6eff3", value=1, variable=self.ring_set,
                                      command=self.preset_set_for_AMG)
        ring_set_menu.add_radiobutton(label="Набор для масла НГЖ (ИРП-1377)", font=("GOST Type BU", 11, "bold"),
                                      background="#73c0f4", foreground="#e6eff3", value=2, variable=self.ring_set,
                                      command=self.preset_set_for_NGJ)
        instrument_menu.add_cascade(label="Выбор уплотнительных колец", menu=ring_set_menu)


        # Команды меню Справка
        info_menu.add_command(label="О приложении", command=self.show_info)
        self.root.configure(menu=menu_bar)


    def pdf_v(self):
        self.start_def_ring_gost(self.root, 875, 700, eq=True, title="   Просмотр PDF документов ")

    def start_def_ring_gost(self, root, width, height, title, eq, resizeble=(False, False), icon=r"Data\PDF_ico.ico"):
        PDFViewer(root, width, height, eq, title, resizeble, icon)

    def show_info(self):
        mb.showinfo("Информация", f"Лучшее графическое приложение на свете")

    def exit(self):
        choice = mb.askyesno("  Выход", "Ты хочешь выйти ?")
        if choice:
            self.root.destroy()


    def preset_set_for_AMG(self):
        self.label.destroy()
        ring_list = self.ring_list_AMG
        self.start_ring_search(self.root, self.label, ring_list)

    def preset_set_for_NGJ(self):
        self.label.destroy()
        ring_list = self.ring_list_NGJ
        self.start_ring_search(self.root, self.label, ring_list)


    def force_calc(self):
        self.label.destroy()
        self.start_force_calc(self.root, self.label, self.ring_list_AMG, self.ring_list_NGJ)

    def wall_thickness(self):
        self.label.destroy()
        self.start_wall_thickness_calc(self.root, self.label)

    def threaded_connections(self):
        self.label.destroy()
        self.start_threaded_connections_calc(self.root, self.label)

    def ear_calc(self):
        self.label.destroy()
        self.start_ear_calc(self.root, self.label)

    def bottom_thickness_calc(self):
        self.label.destroy()
        self.start_bottom_thickness_calc(self.root, self.label)

    def hydra_at_down_calc(self):
        self.label.destroy()
        self.start_hydra_at_down_calc(self.root, self.label)


    def start_ring_search(self, root,  label, ring_list):
        RingSearch(root, label, ring_list)

    def start_force_calc(self, root,  label, ring_list_AMG, ring_list_NGJ):
        ForceHydro(root, label, ring_list_AMG, ring_list_NGJ)

    def start_wall_thickness_calc(self, root,  label):
        WallThickness(root, label)

    def start_threaded_connections_calc(self, root, label):
        ThreadedConnect(root, label)

    def start_ear_calc(self, root, label):
        Ear(root, label)

    def start_bottom_thickness_calc(self, root, label):
        BottomThickness(root, label)

    def start_hydra_at_down_calc(self, root, label):
        HydraAtDown(root, label)



