import math
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
from tkinter.ttk import Notebook
from tkinter import messagebox as mb

from PIL import Image as PiLimage
from PIL import ImageTk

from Scheme_spec_view import SchemeSpecView
from Graph_view import GraphView


class HydraAtDown:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.draw_widgets()
        self.sheme_1 = False
        self.sheme_2 = False
        self.sheme_3 = False
        self.sheme_4 = False
        self.index = 1
        self.scheme_spec_img = PhotoImage(file=r"Data\Scheme_gruz_spec_875x700.png")
        back_img = PiLimage.open(r"Data\Back.png")
        forward_img = PiLimage.open(r"Data\Forward.png")
        back_img = back_img.resize((32, 32), PiLimage.ANTIALIAS)
        forward_img = forward_img.resize((32, 32), PiLimage.ANTIALIAS)
        self.photo_back_image = ImageTk.PhotoImage(back_img)
        self.photo_forward_image = ImageTk.PhotoImage(forward_img)



    def draw_widgets(self):
        self.draw_label()
        self.draw_header(header_text=" Расчет гидроцилиндра на прочность\nи устойчивость ", h=2)
        self.draw_scheme_frame()
        self.draw_scheme_choice()

    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)

    def draw_mpa_kgcm2_calc(self):
        # МПа в кг/см2 конвертер
        self.mpa_kgcm2 = StringVar()
        self.mpa_calc_frame = Frame(self.root, bg="#c2d3da")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#81a3a7", fg="#f1f3f2")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#81a3a7", fg="#f1f3f2")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#272424",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#585a56", fg="#f1f3f2", activebackground="#8c7462", relief=GROOVE,
                                  command=self.convert_mpa_kgcm2)


        self.mpa_calc_frame.place(in_=self.label, x=766, y=0)
        self.mpa_calc_label.grid(row=0, column=0, padx=10, sticky=W)
        self.convert_calc_label.grid(row=0, column=1, padx=10, sticky=W)
        self.mpa_calc_entry.grid(row=0, column=2, padx=10, sticky=W)
        self.convert_btn.grid(row=0, column=3, padx=5, sticky=E)

    def convert_mpa_kgcm2(self):
        flag = True
        try:
            self.mpa_calc = float(self.mpa_calc_entry.get())
        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "Введено некорректное значение")
        if flag:
            self.kgcm2 = self.mpa_calc * 10.19716
            self.mpa_kgcm2.set(f"{round(self.kgcm2, 1)} кг/см2")

    def draw_header(self, header_text, h):
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width=40, height=h, font=("GOST Type BU", 13, "bold"),
                                 text=header_text,
                                 bg="#99bfaa", fg="#e7f5de", justify=CENTER)

        self.header_frame.place(in_=self.label, x=450, y=45)
        self.header_calc.pack()

    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

    def progressbar_view(self):
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", foreground='#e7f5de', background='#e7f5de')
        self.progress_calc = Progressbar(self.root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL,
                                         mode="determinate", length=700)
        self.progress_calc.place(in_=self.label, x=50, y=2)

    def draw_scheme_frame(self):
        self.scheme_frame = LabelFrame(self.root, text="  Общая схема  ",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#e7f5de", fg="#5c868d")
        self.scheme_img = PhotoImage(file=r"Data\Scheme_gruz_800x375.png")
        self.scheme_label = Label(self.scheme_frame, image=self.scheme_img)
        self.scheme_label.image = self.scheme_img

        self.scheme_descrip_label = Label(self.scheme_frame, width=99, height=5, font=("GOST Type BU", 11, "bold"),
                                 text="    Шарнирно закрепленный гидроцилиндр может быть подвержен нагружению"
                                      " по следующим схемам:"
                                      "\n1) эксцентричные продольные сжимающие нагрузки и поперечная сила;"
                                      "\n2) только эксцентричные продольные сжимающие нагрузки;"
                                      "\n3) центральные продольные сжимающие нагрузки и поперечная сила;"
                                      "\n4) только центральные продольные сжимающие нагрузки.",
                                          bg="#99bfaa", fg="#e7f5de", justify=LEFT)

        self.scheme_spec_view_btn = Button(self.scheme_frame, text="Просмотр условных обозначений",
                                         font=("GOST Type BU", 11, "bold"), width=30, bg="#c8d6ca", fg="#5c868d",
                                         activebackground="#e0a96d", relief=GROOVE, command=self.scheme_spec_view)

        self.scheme_frame.place(in_=self.label, x=50, y=100)
        self.scheme_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.scheme_descrip_label.grid(row=2, column=0, padx=(19, 15), pady=2, sticky=W)
        self.scheme_spec_view_btn.grid(row=3, column=0, padx=15, pady=(0, 10), sticky=N+E)

    def scheme_spec_view(self):
        self.start_scheme_spec_view(self.root, 875, 700, self.scheme_spec_img,
                                    title="    Условные обозначения схемы нагружения")

    def start_scheme_spec_view(self, root, width, height, scheme_spec_img, title,
                               resizeble=(False, False), icon=r"Data\hydro.ico"):
        SchemeSpecView(root, width, height, scheme_spec_img, title, resizeble, icon)

    def draw_scheme_choice(self):
        self.choice_frame = Frame(self.root, bg="#e0a96d")
        self.scheme_choice_label = Label(self.choice_frame, width=45, font=("GOST Type BU", 11, "bold"),
                                         text=" Выберите схему нагружения гидроцилиндра.", bg="#99bfaa", fg="#e7f5de",
                                         justify=CENTER)

        self.scheme_1_btn = Button(self.root, text=" 1) Эксцентричные\nпродольные\nсжимающие\nнагрузки и\nпоперечная сила",
                                   font=("GOST Type BU", 11, "bold"), width=20, height=7, bg="#c8d6ca", fg="#5c868d",
                                   activebackground="#e0a96d", relief=RAISED, bd=3, command=self.start_scheme_1)
        self.scheme_2_btn = Button(self.root, text=" 2) Только\nэксцентричные\nпродольные\nсжимающие нагрузки",
                                   font=("GOST Type BU", 11, "bold"), width=20, height=7, bg="#c8d6ca", fg="#5c868d",
                                   activebackground="#e0a96d", relief=RAISED, bd=3, command=self.start_scheme_2)
        self.scheme_3_btn = Button(self.root, text=" 3) Центральные\nпродольные\nсжимающие\nнагрузки и\nпоперечная сила",
                                   font=("GOST Type BU", 11, "bold"), width=20, height=7, bg="#c8d6ca", fg="#5c868d",
                                   activebackground="#e0a96d", relief=RAISED, bd=3, command=self.start_scheme_3)
        self.scheme_4_btn = Button(self.root, text=" 4) Только\nцентральные\nпродольные\nсжимающие нагрузки",
                                   font=("GOST Type BU", 11, "bold"), width=20, height=7, bg="#c8d6ca", fg="#5c868d",
                                   activebackground="#e0a96d", relief=RAISED, bd=3, command=self.start_scheme_4)


        self.choice_frame.place(in_=self.label, x=900, y=100)
        self.scheme_choice_label.pack()

        self.scheme_1_btn.place(in_=self.label, x=910, y=150)
        self.scheme_2_btn.place(in_=self.label, x=1090, y=150)
        self.scheme_3_btn.place(in_=self.label, x=910, y=300)
        self.scheme_4_btn.place(in_=self.label, x=1090, y=300)

    def start_scheme_1(self):
        self.sheme_1 = True
        self.sheme_2 = False
        self.sheme_3 = False
        self.sheme_4 = False
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text="  Расчет гидроцилиндра на устойчивость", h=1)
        self.draw_formula_stab_frame()
        self.draw_moment_inert_frame()

    def start_scheme_2(self):
        self.sheme_2 = True
        self.sheme_1 = False
        self.sheme_3 = False
        self.sheme_4 = False
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text="  Расчет гидроцилиндра на устойчивость", h=1)
        self.draw_formula_stab_frame()
        self.draw_moment_inert_frame()

    def start_scheme_3(self):
        self.sheme_3 = True
        self.sheme_1 = False
        self.sheme_2 = False
        self.sheme_4 = False
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text="  Расчет гидроцилиндра на устойчивость", h=1)
        self.draw_formula_stab_frame()
        self.draw_moment_inert_frame()

    def start_scheme_4(self):
        self.sheme_4 = True
        self.sheme_1 = False
        self.sheme_2 = False
        self.sheme_3 = False
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text="  Расчет гидроцилиндра на устойчивость", h=1)
        self.draw_formula_stab_frame()
        self.draw_moment_inert_frame()


    def draw_formula_stab_frame(self):
        self.formula_stab_frame = LabelFrame(self.root, text="  Расчетная формула ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.crit_force_img = PhotoImage(file=r"Data\Crit_force_600x190.png")
        self.crit_force_label = Label(self.formula_stab_frame, image=self.crit_force_img)
        self.crit_force_label.image = self.crit_force_img

        self.back_scheme_choice_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                             text=" Назад к выбору\n  схем нагружения",
                                             font=("GOST Type BU", 10, "bold"), width=180, height=40,
                                             bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)

        self.formula_stab_frame.place(in_=self.label, x=660, y=100)
        self.crit_force_label.pack()
        self.back_scheme_choice_btn.place(in_=self.label, x=40, y=40)


    def back_scheme_choice(self):
        self.label.destroy()
        self.draw_widgets()

    def open_data_init(self):
        self.line = self.open_data_calc.readline()
        self.open_data = []
        while self.line != "":
            self.line = float(self.line)
            if self.line % 1 == 0.0:
                self.open_data.append(int(self.line))
            else:
                self.open_data.append(self.line)
            self.line = self.open_data_calc.readline()
        self.open_data_calc.close()


    def draw_moment_inert_frame(self):
        self.moment_inert_shtock_value = StringVar()
        self.moment_inert_sleeve_value = StringVar()
        self.moment_inert_dev_value = StringVar()
        self.progressbar_view()
        self.progress_calc.configure(value=17)
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_moment_inert_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_moment_inert_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_moment_inert_calc.txt", "r")
        self.open_data_init()
        self.moment_inert_frame = LabelFrame(self.root, text=" Ввод данных для расчета момента инерции  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.our_diam_shtock_label = Label(self.moment_inert_frame, width=60, height=1,
                                           font=("GOST Type BU", 11, "bold"),
                                           text="Наружный диаметр штока (для неполого штока) dнш, в мм", bg="#99bfaa",
                                           fg="#5c3d46")
        self.our_diam_shtock_entry = Entry(self.moment_inert_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                           fg="#5c3d46", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.our_diam_sleeve_label = Label(self.moment_inert_frame, width=60, height=1,
                                           font=("GOST Type BU", 11, "bold"),
                                           text="Наружный диаметр гильзы dнг, в мм", bg="#99bfaa", fg="#5c3d46")
        self.our_diam_sleeve_entry = Entry(self.moment_inert_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                           fg="#5c3d46", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.inner_diam_sleeve_label = Label(self.moment_inert_frame, width=60, height=1,
                                             font=("GOST Type BU", 11, "bold"),
                                             text="Внутренний диаметр гильзы dвг, в мм", bg="#99bfaa", fg="#5c3d46")
        self.inner_diam_sleeve_entry = Entry(self.moment_inert_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                           fg="#5c3d46", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.length_shtock_to_point_A_label = Label(self.moment_inert_frame, width=60, height=1,
                                                    font=("GOST Type BU", 11, "bold"),
                                                    text="Расстояние l1 от уха штока до точки А (см общую схему), в мм",
                                                    bg="#99bfaa", fg="#5c3d46")
        self.length_shtock_to_point_A_entry = Entry(self.moment_inert_frame, width=8, font=("GOST Type BU", 11),
                                                    bg="white", fg="#5c3d46", validate="key",
                                                    validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.length_clndr_to_point_A_label = Label(self.moment_inert_frame, width=60, height=1,
                                                    font=("GOST Type BU", 11, "bold"),
                                                text="Расстояние l2 от уха цилиндра до точки А (см общ. схему), в мм",
                                                    bg="#99bfaa", fg="#5c3d46")
        self.length_clndr_to_point_A_entry = Entry(self.moment_inert_frame, width=8, font=("GOST Type BU", 11),
                                                    bg="white", fg="#5c3d46", validate="key",
                                                    validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.moment_inert_output_frame = Frame(self.moment_inert_frame, bg="#c8d6ca")
        self.header_moment_inert_shtock_label = Label(self.moment_inert_output_frame, width=28, height=2,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      text="Момент инерции\nсечения штока", bg="#99bfaa", fg="#5c3d46",
                                                      justify=CENTER)
        self.header_moment_inert_sleeve_label = Label(self.moment_inert_output_frame, width=28, height=2,
                                              font=("GOST Type BU", 11,  "bold"), text="Момент инерции\nсечения гильзы",
                                              bg="#99bfaa", fg="#5c3d46", justify=CENTER)
        self.moment_inert_shtock_output_label = Label(self.moment_inert_output_frame, width=28, height=2,
                                              font=("GOST Type BU", 11,  "bold"),
                                              textvariable=self.moment_inert_shtock_value, bg="#99bfaa", fg="#5c3d46",
                                              justify=LEFT)
        self.moment_inert_sleeve_output_label = Label(self.moment_inert_output_frame, width=28, height=2,
                                              font=("GOST Type BU", 11,  "bold"),
                                              textvariable=self.moment_inert_sleeve_value, bg="#99bfaa", fg="#5c3d46",
                                              justify=LEFT)
        self.moment_inert_dev_output_label = Label(self.moment_inert_output_frame, width=58, height=2,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      textvariable=self.moment_inert_dev_value, bg="#99bfaa",
                                                      fg="#5c3d46",
                                                      justify=LEFT)
        self.moment_inert_calc_btn = Button(self.moment_inert_frame, text=" Расчет\nмоментов\nинерции",
                                    font=("GOST Type BU", 10, "bold"), width=10, height=3, bg="#c8d6ca", fg="#5c868d",
                                    activebackground="#e0a96d", relief=GROOVE, command=self.moment_inert_calc)
        self.all_clear_moment_inert_btn = Button(self.moment_inert_frame, text="Очистить",
                                                 font=("GOST Type BU", 10, "bold"), width=10, height=1, bg="#c8d6ca",
                                                 fg="#5c868d", activebackground="#e0a96d", relief=GROOVE,
                                                 command=self.all_clear_moment_inert)

        if len(self.open_data) == 5:
            self.our_diam_shtock_entry.insert(0, f"{self.open_data[0]}")
            self.our_diam_sleeve_entry.insert(0, f"{self.open_data[1]}")
            self.inner_diam_sleeve_entry.insert(0, f"{self.open_data[2]}")
            self.length_shtock_to_point_A_entry.insert(0, f"{self.open_data[3]}")
            self.length_clndr_to_point_A_entry.insert(0, f"{self.open_data[4]}")


        self.moment_inert_frame.place(in_=self.label, x=40, y=100)
        self.our_diam_shtock_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.our_diam_shtock_entry.grid(row=1, column=1, padx=10, pady=(10, 2), sticky=W)
        self.our_diam_sleeve_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.our_diam_sleeve_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.inner_diam_sleeve_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.inner_diam_sleeve_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.length_shtock_to_point_A_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.length_shtock_to_point_A_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.length_clndr_to_point_A_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.length_clndr_to_point_A_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W)
        self.moment_inert_output_frame.grid(row=6, column=0, padx=15, pady=(2, 5), sticky=W)
        self.header_moment_inert_shtock_label.grid(row=1, column=0, padx=(8, 0), pady=2, sticky=W)
        self.header_moment_inert_sleeve_label.grid(row=1, column=1, padx=(10, 8), pady=2, sticky=W)
        self.moment_inert_shtock_output_label.grid(row=2, column=0, padx=(8, 0), pady=2, sticky=W)
        self.moment_inert_sleeve_output_label.grid(row=2, column=1, padx=(10, 8), pady=2, sticky=W)
        self.moment_inert_dev_output_label.grid(row=3, column=0, columnspan=2, padx=8, pady=2, sticky=W)
        self.moment_inert_calc_btn.grid(row=6, column=1, padx=(0, 10), pady=5, sticky=W + S)
        self.all_clear_moment_inert_btn.grid(row=6, column=1, padx=(0, 10), pady=15, sticky=W + N)

    def all_clear_moment_inert(self):
        self.our_diam_shtock_entry.delete(0, END)
        self.our_diam_sleeve_entry.delete(0, END)
        self.inner_diam_sleeve_entry.delete(0, END)
        self.length_shtock_to_point_A_entry.delete(0, END)
        self.length_clndr_to_point_A_entry.delete(0, END)
        self.moment_inert_shtock_value.set(f"")
        self.moment_inert_sleeve_value.set(f"")
        self.moment_inert_dev_value.set(f"")
        self.stab_frame.destroy()
        self.shtock_calc_btn.destroy()



    def draw_stab_frame(self):
        self.crit_force_value = StringVar()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_stab_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_stab_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_stab_calc.txt", "r")
        self.open_data_init()
        self.progress_calc.configure(value=34)
        self.stab_frame = LabelFrame(self.root, text=" Ввод данных для расчета на устойчивость  ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.scheme_graph_view_btn = Button(self.stab_frame, text=" Графики для определения критической силы ",
                                            font=("GOST Type BU", 11, "bold"), width=50, bg="#c8d6ca", fg="#5c868d",
                                            activebackground="#e0a96d", relief=GROOVE, command=self.scheme_graph_view)
        self.crit_force_dev_label = Label(self.stab_frame, width=60, height=1, font=("GOST Type BU", 11, "bold"),
                                      text="Отношение √(Pкр/J1) найденое из графика", bg="#99bfaa", fg="#5c3d46")
        self.crit_force_dev_entry = Entry(self.stab_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#5c3d46",
                                      validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.pull_label = Label(self.stab_frame, width=60, height=1, font=("GOST Type BU", 11, "bold"),
                            text="Усилие развиваемое гидроцилиндром (без потерь) P, в кг", bg="#99bfaa", fg="#5c3d46")
        self.pull_entry = Entry(self.stab_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#5c3d46",
                                validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.stability_output_label = Label(self.stab_frame, width=60, height=2,
                                                   font=("GOST Type BU", 11, "bold"),
                                                   textvariable=self.crit_force_value, bg="#99bfaa", fg="#5c3d46",
                                                   justify=LEFT)
        self.stab_calc_btn = Button(self.stab_frame, text="Расчет",
                                    font=("GOST Type BU", 10, "bold"), width=10, height=1, bg="#c8d6ca",
                                    fg="#5c868d", activebackground="#e0a96d", relief=GROOVE, command=self.stab_calc)
        self.all_clear_stab_btn = Button(self.stab_frame, text="Очистить",
                                         font=("GOST Type BU", 10, "bold"), width=10, height=1, bg="#c8d6ca",
                                         fg="#5c868d", activebackground="#e0a96d", relief=GROOVE,
                                         command=self.all_clear_stab)
        self.shtock_calc_btn = Button(self.root, text="Далее расчет\nштока на прочность  ", compound=RIGHT,
                                      font=("GOST Type BU", 10, "bold"), image=self.photo_forward_image, width=200,
                                      height=40, bg="#c8d6ca", fg="#5c868d", justify=LEFT, activebackground="#e0a96d",
                                      relief=GROOVE, command=self.shtock_calc)

        if len(self.open_data) == 2:
            self.crit_force_dev_entry.insert(0, f"{self.open_data[0]}")
            self.pull_entry.insert(0, f"{self.open_data[1]}")

        self.stab_frame.place(in_=self.label, x=40, y=418)
        self.scheme_graph_view_btn.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.crit_force_dev_label.grid(row=2, column=0, padx=15, pady=(10, 2), sticky=W)
        self.crit_force_dev_entry.grid(row=2, column=1, padx=10, pady=(10, 2), sticky=W)
        self.pull_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.pull_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.stability_output_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.all_clear_stab_btn.grid(row=4, column=1, padx=(0, 10), pady=(13, 5), sticky=W + S)
        self.stab_calc_btn.grid(row=5, column=1, padx=(0, 10), pady=5, sticky=W + S)

    def all_clear_stab(self):
        self.crit_force_dev_entry.delete(0, END)
        self.pull_entry.delete(0, END)
        self.crit_force_value.set(f"")
        self.shtock_calc_btn.destroy()




    def scheme_graph_view(self):
        self.start_graph_view(self.root, 760, 1080, self.moment_inert_dev,
                                    title="  Графики для определения критической силы ")

    def start_graph_view(self, root, width, height, moment_inert_dev, title,
                               resizeble=(False, False), icon=r"Data\graphic.ico"):
        GraphView(root, width, height, moment_inert_dev, title, resizeble, icon)

    def moment_inert_calc(self):
        flag = True
        try:
            self.our_diam_shtock = float(self.our_diam_shtock_entry.get()) / 10
            self.our_diam_sleeve = float(self.our_diam_sleeve_entry.get()) / 10
            self.inner_diam_sleeve = float(self.inner_diam_sleeve_entry.get()) / 10
            self.length_shtock_to_point_A = float(self.length_shtock_to_point_A_entry.get()) / 10
            self.length_clndr_to_point_A = float(self.length_clndr_to_point_A_entry.get()) / 10

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.stab_frame.destroy()
            self.moment_inert_shtock_value.set(f"")
            self.moment_inert_sleeve_value.set(f"")
            self.moment_inert_dev_value.set(f"")

        if flag:
            self.draw_stab_frame()
            try:
                self.c_ratio = self.inner_diam_sleeve / self.our_diam_sleeve
                self.point_A_ratio = self.length_clndr_to_point_A / self.length_shtock_to_point_A
                self.moment_inert_shtock = (math.pi * math.pow(self.our_diam_shtock, 4)) / 64
                self.moment_inert_sleeve = ((math.pi * math.pow(self.our_diam_sleeve, 4)) / 64) \
                                             * (1 - math.pow(self.c_ratio, 4))
                self.moment_inert_dev = math.sqrt(self.moment_inert_sleeve / self.moment_inert_shtock)

            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.stab_frame.destroy()
                self.moment_inert_shtock_value.set(f"")
                self.moment_inert_sleeve_value.set(f"")
                self.moment_inert_dev_value.set(f"")

            if flag:
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_moment_inert_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.our_diam_shtock * 10) + "\n")
                self.save_data_calc.write(str(self.our_diam_sleeve * 10) + "\n")
                self.save_data_calc.write(str(self.inner_diam_sleeve * 10) + "\n")
                self.save_data_calc.write(str(self.length_shtock_to_point_A * 10) + "\n")
                self.save_data_calc.write(str(self.length_clndr_to_point_A * 10))
                self.save_data_calc.close()

                # Вывод
                self.moment_inert_shtock_value.set(f"J1 = {round(self.moment_inert_shtock, 4)} см4")
                self.moment_inert_sleeve_value.set(f"J2 = {round(self.moment_inert_sleeve, 4)} см4")
                self.moment_inert_dev_value.set(f"l2/l1 = {round(self.point_A_ratio, 2)}      "
                                                f"√(J2/J1) = {round(self.moment_inert_dev, 2)}")


    def stab_calc(self):
        flag = True
        try:
            self.crit_force_dev = float(self.crit_force_dev_entry.get())
            self.pull = float(self.pull_entry.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.crit_force_value.set(f"")
            self.shtock_calc_btn.place_forget()
        if flag:
            self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_stab_calc.txt", "w")

            # Запись
            self.save_data_calc.write(str(self.crit_force_dev) + "\n")
            self.save_data_calc.write(str(self.pull))
            self.save_data_calc.close()

            # Расчет
            self.crit_force = math.pow(self.crit_force_dev, 2) * self.moment_inert_shtock

            if self.crit_force > self.pull:
                self.crit_force_value.set(f"Pкр = {round(self.crit_force, 2)} > {round(self.pull, 2)} "
                                          f"условие устойчивости выдержано")
            else:
                self.crit_force_value.set(f"Pкр = {round(self.crit_force, 2)}  {round(self.pull, 2)} "
                                          f"условие устойчивости не выдержано")
            self.progress_calc.configure(value=51)
            self.shtock_calc_btn.place(in_=self.label, x=660, y=492)

    def shtock_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text=" Расчет штока на прочность.\nОпределение начального прогиба.", h=2)
        self.applicability_method_calc()
        self.progressbar_view()
        self.progress_calc.configure(value=58)
        self.back_moment_inert_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                             text=" Назад",
                                             font=("GOST Type BU", 11, "bold"), width=100, height=40,
                                             bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d",
                                             relief=GROOVE, command=self.back_moment_inert)
        self.back_scheme_choice_btn = Button(self.root, text="К выбору\nсхем нагружения", width=18, height=2,
                                             font=("GOST Type BU", 11, "bold"), bg="#c8d6ca", fg="#5c868d",
                                             activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)
        self.back_moment_inert_btn.place(in_=self.label, x=40, y=45)
        self.back_scheme_choice_btn.place(in_=self.label, x=170, y=44)

    def back_moment_inert(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text="  Расчет гидроцилиндра на устойчивость", h=1)
        self.draw_formula_stab_frame()
        self.draw_moment_inert_frame()

    def applicability_method(self):
        self.app_method_value = StringVar()
        self.app_method_frame = LabelFrame(self.root, text=" Проверка применимости методики расчета, условие:  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.app_method_formula_img = PhotoImage(file=r"Data\app_method_250x100.png")
        self.app_method_formula_label = Label(self.app_method_frame, image=self.app_method_formula_img)
        self.app_method_formula_label.image = self.app_method_formula_img

        self.app_method_output_label = Label(self.app_method_frame, width=30, height=3,
                                            font=("GOST Type BU", 11, "bold"), textvariable=self.app_method_value,
                                            bg="#99bfaa", fg="#5c3d46", justify=LEFT)

        self.buckling_calc_btn = Button(self.app_method_frame, text=" Расчет штока\nна продольный изгиб ",
                                            font=("GOST Type BU", 11, "bold"), width=30, bg="#c8d6ca", fg="#5c868d",
                                            activebackground="#e0a96d", relief=GROOVE, command=self.buckling_calc)

        self.app_method_frame.place(in_=self.label, x=40, y=100)
        self.app_method_formula_label.grid(row=1, column=0, rowspan=2, padx=15, pady=2, sticky=W)
        self.app_method_output_label.grid(row=1, column=1, padx=(0, 15), pady=2, sticky=W)

    def applicability_method_calc(self):
        self.applicability_method()
        self.app_method = 505 * math.pow(self.our_diam_shtock, 2) * math.sqrt((1 / self.pull))
        if self.app_method >= self.length_shtock_to_point_A:
            self.app_method_value.set(f"X = {round(self.app_method, 1)} см  l1 = {self.length_shtock_to_point_A} см\n"
                                      f"данная методика расчета\nприменима.")
            self.draw_formula_init_deflection_frame()
            self.draw_table_gap_frame()
            if self.sheme_1:
                self.draw_data_init_deflection_sch1()
            elif self.sheme_2:
                self.draw_data_init_deflection_sch2()
            elif self.sheme_3:
                self.draw_data_init_deflection_sch3()
            else:
                self.draw_data_init_deflection_sch4()

        else:
            self.app_method_value.set(f"X = {round(self.app_method, 1)} см < l1 = {self.length_shtock_to_point_A} см\n"
                                      f"данная методика расчета\nне применима, рекомендуется:")
            self.buckling_calc_btn.grid(row=2, column=1, padx=(0, 15), pady=2, sticky=W)

    def buckling_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text=" Расчет штока на продольный изгиб", h=1)
        self.draw_mpa_kgcm2_calc()
        self.progressbar_view()
        self.progress_calc.configure(value=73)
        self.back_moment_inert_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                            text=" Назад",
                                            font=("GOST Type BU", 11, "bold"), width=100, height=40,
                                            bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d",
                                            relief=GROOVE, command=self.back_moment_inert)
        self.back_scheme_choice_btn = Button(self.root, text="К выбору\nсхем нагружения", width=18, height=2,
                                             font=("GOST Type BU", 11, "bold"), bg="#c8d6ca", fg="#5c868d",
                                             activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)
        self.back_moment_inert_btn.place(in_=self.label, x=40, y=45)
        self.back_scheme_choice_btn.place(in_=self.label, x=170, y=44)
        self.draw_applic_Euler_formula()

    def draw_applic_Euler_formula(self):
        self.applic_Euler_value = StringVar()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_buckling_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_buckling_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_buckling_calc.txt", "r")
        self.open_data_init()
        self.Euler_formula_frame = LabelFrame(self.root,
                                             text=" Ввод данных для проверки применимости  ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.applic_Euler_formula_img = PhotoImage(file=r"Data\applic_Euler_540x146.png")
        self.applic_Euler_formula_label = Label(self.Euler_formula_frame, image=self.applic_Euler_formula_img)
        self.applic_Euler_formula_label.image = self.applic_Euler_formula_img

        self.reduced_length_factor_label = Label(self.Euler_formula_frame, width=67, height=1,
                                            font=("GOST Type BU", 11, "bold"),
                                            text="Коэффициент приведеной длины μ",
                                            bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.reduced_length_factor_entry = Entry(self.Euler_formula_frame, width=8, font=("GOST Type BU", 11),
                                            bg="white", fg="#5c3d46", validate="key",
                                            validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.weight_shtock_label = Label(self.Euler_formula_frame, width=67, height=1,
                                                 font=("GOST Type BU", 11, "bold"),
                                                 text="Масса штока m, в кг",
                                                 bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.weight_shtock_entry = Entry(self.Euler_formula_frame, width=8, font=("GOST Type BU", 11),
                                                 bg="white", fg="#5c3d46", validate="key",
                                                 validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.limit_of_proport_label = Label(self.Euler_formula_frame, width=67, height=1,
                                            font=("GOST Type BU", 11, "bold"),
                                            text="Предел пропорциональности материала штока σпр, в кг/см2",
                                            bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.limit_of_proport_entry = Entry(self.Euler_formula_frame, width=8, font=("GOST Type BU", 11),
                                          bg="white", fg="#5c3d46", validate="key",
                                          validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.elastic_modulus_label = Label(self.Euler_formula_frame, width=67, height=1,
                                           text="Модуль упругости материала штока E, в кг/см2",
                                           font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.elastic_modulus_entry = Entry(self.Euler_formula_frame, width=8,
                                           font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.applic_Euler_output_label = Label(self.Euler_formula_frame, width=67, height=2,
                                                  textvariable=self.applic_Euler_value,
                                                  font=("GOST Type BU", 11, "bold"),
                                                  bg="#99bfaa", fg="#5c3d46")
        self.app_check_btn = Button(self.Euler_formula_frame, text="Проверить применимость и расчитать",
                                    font=("GOST Type BU", 10, "bold"), width=37, height=1, bg="#c8d6ca", fg="#5c868d",
                                    activebackground="#e0a96d", relief=GROOVE, command=self.flexibility_calc)
        self.all_clear_Euler_formula_frame_btn = Button(self.Euler_formula_frame, text="Очистить",
                                    font=("GOST Type BU", 10, "bold"), width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                    activebackground="#e0a96d", relief=GROOVE, command=self.all_clear_Euler_formula_frame)

        if len(self.open_data) == 4:
            self.reduced_length_factor_entry.insert(0, f"{self.open_data[0]}")
            self.weight_shtock_entry.insert(0, f"{self.open_data[1]}")
            self.limit_of_proport_entry.insert(0, f"{self.open_data[2]}")
            self.elastic_modulus_entry.insert(0, f"{self.open_data[3]}")

        self.Euler_formula_frame.place(in_=self.label, x=40, y=100)
        self.applic_Euler_formula_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.reduced_length_factor_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.reduced_length_factor_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.weight_shtock_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.weight_shtock_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.limit_of_proport_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.limit_of_proport_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.elastic_modulus_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.elastic_modulus_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W)
        self.applic_Euler_output_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.app_check_btn.grid(row=8, column=0, padx=15, pady=10, sticky=E + S)
        self.all_clear_Euler_formula_frame_btn.grid(row=8, column=1, padx=(0, 10), pady=10, sticky=W + S)

    def all_clear_Euler_formula_frame(self):
        self.reduced_length_factor_entry.delete(0, END)
        self.weight_shtock_entry.delete(0, END)
        self.limit_of_proport_entry.delete(0, END)
        self.elastic_modulus_entry.delete(0, END)
        self.applic_Euler_value.set(f"")
        if hasattr(self, "flexibility_output_frame"):
            self.flexibility_output_frame.destroy()
        if hasattr(self, "crit_stress_frame"):
            self.crit_stress_frame.destroy()

    def output_flexibility(self, Euler):
        self.crit_stress_value = StringVar()
        self.flexibility_output_frame = LabelFrame(self.root, text=" Результат расчета штока на изгиб ",
                                                      font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de",
                                                      fg="#5c868d")
        self.crit_stress_output_label = Label(self.flexibility_output_frame, width=64, height=2,
                                              textvariable=self.crit_stress_value,
                                              font=("GOST Type BU", 11, "bold"),
                                              bg="#99bfaa", fg="#5c3d46")
        self.Yasinsky_formula_btn = Button(self.flexibility_output_frame, text="Формула Ясинского",
                                           font=("GOST Type BU", 10, "bold"), width=20, height=1, bg="#c8d6ca",
                                           fg="#5c868d",
                                           activebackground="#e0a96d", relief=GROOVE,
                                           command=self.draw_Yasinsky_formula_calc)
        self.parabolic_law_btn = Button(self.flexibility_output_frame, text="Расчет по параболическому закону",
                                           font=("GOST Type BU", 10, "bold"), width=40, height=1, bg="#c8d6ca",
                                           fg="#5c868d",
                                           activebackground="#e0a96d", relief=GROOVE,
                                           command=self.draw_parabolic_law_calc)

        self.flexibility_output_frame.place(in_=self.label, x=715, y=310)
        if Euler:
            self.crit_stress_output_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        else:
            if 40 <= self.flexibility_shtock < 100:
                self.Yasinsky_formula_btn.grid(row=1, column=1, padx=10, pady=10, sticky=N+E+S+W)
            else:
                self.parabolic_law_btn.grid(row=1, column=1, padx=10, pady=10, sticky=N+E+S+W)


    def flexibility_calc(self):
        flag = True
        try:
            self.reduced_length_factor = float(self.reduced_length_factor_entry.get())
            self.weight_shtock = float(self.weight_shtock_entry.get())
            self.limit_of_proport = float(self.limit_of_proport_entry.get())
            self.elastic_modulus = float(self.elastic_modulus_entry.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
        if flag:
            try:
                self.square_shtock = (math.pi * math.pow(self.our_diam_shtock, 2)) / 4
                self.length_hydro = self.length_shtock_to_point_A + self.length_clndr_to_point_A
                self.moment_inert_shtock_min = 0.5 * self.weight_shtock * math.pow((self.our_diam_shtock / 2), 2)
                self.radius_gyr_of_section = math.sqrt((self.moment_inert_shtock_min / self.square_shtock))
                self.flexibility_shtock = (self.reduced_length_factor * self.length_hydro) / self.radius_gyr_of_section
                self.applicability = math.pi * math.sqrt((self.elastic_modulus / self.limit_of_proport))
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")

            if flag:
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_buckling_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.reduced_length_factor) + "\n")
                self.save_data_calc.write(str(self.weight_shtock) + "\n")
                self.save_data_calc.write(str(self.limit_of_proport) + "\n")
                self.save_data_calc.write(str(self.elastic_modulus))
                self.save_data_calc.close()
                if self.flexibility_shtock > self.applicability:
                    self.crit_stress = (math.pow(math.pi, 2) * self.elastic_modulus) \
                                       / math.pow(self.flexibility_shtock, 2)
                    self.crit_force_Euler = self.crit_stress * self.square_shtock

                    # Вывод
                    self.applic_Euler_value.set(f"λ = {round(self.flexibility_shtock, 2)} "
                                            f"> π√(E/σпр) = {round(self.applicability, 2)} формула расчета применима")
                    self.output_flexibility(Euler=True)
                    if self.Yasinsky_formula_btn:
                        self.Yasinsky_formula_btn.destroy()
                    self.crit_stress_value.set(f"Критическое напряжение σкр = {round(self.crit_stress, 2)} кг/см2\n"
                                           f"Критическая сила Pкр = {round(self.crit_force_Euler, 2)} кг")
                    self.progress_calc.configure(value=100)
                    self.draw_crit_stress_formula()

                else:
                    if hasattr(self, "flexibility_output_frame"):
                        self.flexibility_output_frame.destroy()
                    if hasattr(self, "crit_stress_frame"):
                        self.crit_stress_frame.destroy()
                    self.output_flexibility(Euler=False)
                    if 40 <= self.flexibility_shtock < 100:
                        self.applic_Euler_value.set(f"λ = {round(self.flexibility_shtock, 2)} "
                                                    f" π√(E/σпр) = {round(self.applicability, 2)} формула Эйлера "
                                                    f"для расчета\nне применима, "
                                                    f"воспользуйтесь рачетом по формуле Ясинского.")
                        self.progress_calc.configure(value=80)
                    else:
                        self.applic_Euler_value.set(f"λ = {round(self.flexibility_shtock, 2)} "
                                                    f" π√(E/σпр) = {round(self.applicability, 2)} формула Эйлера "
                                                    f"для расчета\nне применима, "
                                                    f"воспользуйтесь рачетом по параболическому закону.")
                        self.progress_calc.configure(value=80)


    def draw_crit_stress_formula(self):
        self.crit_stress_frame = LabelFrame(self.root, text=" Формулы для расчета ",
                                            font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.crit_stress_img = PhotoImage(file=r"Data\crit_stress_540x180.png")
        self.crit_stress_formula_label = Label(self.crit_stress_frame, image=self.crit_stress_img)
        self.crit_stress_formula_label.image = self.crit_stress_img


        self.crit_stress_frame.place(in_=self.label, x=715, y=100)
        self.crit_stress_formula_label.pack(side=LEFT)

    def draw_parabolic_law_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text=" Расчет штока по параболическому закону", h=1)
        self.draw_mpa_kgcm2_calc()
        self.draw_parabolic_law_formula()
        self.draw_parabolic_law_graph()
        self.draw_parabolic_law_data_frame()
        self.progressbar_view()
        self.progress_calc.configure(value=86)
        self.back_moment_inert_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                            text=" Назад",
                                            font=("GOST Type BU", 11, "bold"), width=100, height=40,
                                            bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d",
                                            relief=GROOVE, command=self.buckling_calc)
        self.back_scheme_choice_btn = Button(self.root, text="К выбору\nсхем нагружения", width=18, height=2,
                                             font=("GOST Type BU", 11, "bold"), bg="#c8d6ca", fg="#5c868d",
                                             activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)
        self.back_moment_inert_btn.place(in_=self.label, x=50, y=45)
        self.back_scheme_choice_btn.place(in_=self.label, x=180, y=44)

    def draw_parabolic_law_formula(self):
        self.parabolic_law_frame = LabelFrame(self.root, text="Расчет штока по параболическому закону",
                                         font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.parabolic_law_img = PhotoImage(file=r"Data\parabolic_law_formula_510x195.png")
        self.parabolic_law_label = Label(self.parabolic_law_frame, image=self.parabolic_law_img)
        self.parabolic_law_label.image = self.parabolic_law_img

        self.parabolic_law_frame.place(in_=self.label, x=660, y=100)
        self.parabolic_law_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)

    def draw_parabolic_law_graph(self):
        self.parabolic_law_frame = LabelFrame(self.root, text="График гибкости от напряжения",
                                              font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.parabolic_law_img = PhotoImage(file=r"Data\parabolic_law_graph_510x408.png")
        self.parabolic_law_label = Label(self.parabolic_law_frame, image=self.parabolic_law_img)
        self.parabolic_law_label.image = self.parabolic_law_img

        self.parabolic_law_msg_label = Label(self.parabolic_law_frame, width=63, height=5,
                                           text="a — коэффициент, определяемый из условия сопряжения с кривой\n"
                                                "Эйлера. Для хрупких материалов в формулы для определения\n"
                                                "критического напряжения вместо предела текучести σT\nподставляют "
                                                "предел прочности на сжатие σВ.\n"
                                                "Материалы взяты с сайта http://sopromatu.net/",
                                           font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)

        self.parabolic_law_frame.place(in_=self.label, x=50, y=100)
        self.parabolic_law_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        self.parabolic_law_msg_label.grid(row=2, column=0, padx=(16, 15), pady=(5, 10), sticky=W)

    def draw_parabolic_law_data_frame(self):
        self.parabolic_law_value = StringVar()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_parabolic_law_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_parabolic_law_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_parabolic_law_calc.txt", "r")
        self.open_data_init()
        self.parabolic_law_data_frame = LabelFrame(self.root, text=" Ввод предела текучести и расчет  ",
                                              font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.yield_strength_label = Label(self.parabolic_law_data_frame, width=50, height=1,
                                          font=("GOST Type BU", 11, "bold"),
                                          text="Предел текучести материала σT, в кг/см2", bg="#99bfaa", fg="#5c3d46",
                                          justify=LEFT)
        self.yield_strength_entry = Entry(self.parabolic_law_data_frame, width=8, font=("GOST Type BU", 11),
                                          bg="white", fg="#5c3d46", validate="key",
                                          validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.parabolic_law_output_label = Label(self.parabolic_law_data_frame, width=50, height=2,
                                           textvariable=self.parabolic_law_value, font=("GOST Type BU", 11, "bold"),
                                           bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.parabolic_law_calc_btn = Button(self.parabolic_law_data_frame, text="Расчет",
                                    font=("GOST Type BU", 10, "bold"), width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                    activebackground="#e0a96d", relief=GROOVE, command=self.parabolic_law_calc)
        self.all_clear_parabolic_law_frame_btn = Button(self.parabolic_law_data_frame, text="Очистить",
                                                        font=("GOST Type BU", 10, "bold"), width=10, height=1,
                                                        bg="#c8d6ca", fg="#5c868d",
                                                        activebackground="#e0a96d", relief=GROOVE,
                                                        command=self.all_clear_parabolic_law_frame)
        if len(self.open_data) == 1:
            self.yield_strength_entry.insert(0, f"{self.open_data[0]}")

        self.parabolic_law_data_frame.place(in_=self.label, x=660, y=350)
        self.yield_strength_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.yield_strength_entry.grid(row=1, column=1, padx=10, pady=(10, 2), sticky=W)
        self.parabolic_law_output_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.parabolic_law_calc_btn.grid(row=3, column=0, padx=15, pady=(2, 10), sticky=E + S)
        self.all_clear_parabolic_law_frame_btn.grid(row=3, column=1, padx=(10, 15), pady=(2, 10), sticky=W + S)

    def all_clear_parabolic_law_frame(self):
        self.yield_strength_entry.delete(0, END)
        self.parabolic_law_value.set(f"")
        self.progress_calc.configure(value=86)


    def parabolic_law_calc(self):
        flag = True
        try:
            self.yield_strength = float(self.yield_strength_entry.get())
        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены, или ввод некорректных значений")
            self.parabolic_law_value.set(f"")
        if flag:
            try:
                self.a_ratio_parabolic_law = (self.yield_strength - self.limit_of_proport) / \
                                             (math.pow(self.applicability, 2))
                self.crit_stress_parabolic_law = self.yield_strength - self.a_ratio_parabolic_law *\
                                   (math.pow(self.flexibility_shtock, 2))
                self.crit_force_parabolic_law = self.crit_stress_parabolic_law * self.square_shtock
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.parabolic_law_value.set(f"")
            if flag:
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_parabolic_law_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.yield_strength) + "\n")
                self.save_data_calc.close()

                # Вывод
                self.parabolic_law_value.set(f"Критическое напряжение σкр = {round(self.crit_stress_parabolic_law, 2)} "
                                             f"кг/см2\nКритическая сила Pкр = "
                                             f"{round(self.crit_force_parabolic_law, 2)} кг")
                self.progress_calc.configure(value=100)


    def draw_Yasinsky_formula_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text=" Расчет штока по формуле Ясинского", h=1)
        self.draw_mpa_kgcm2_calc()
        self.draw_Yasinsky_formula()
        self.draw_Yasinsky_data_frame()
        self.progressbar_view()
        self.progress_calc.configure(value=86)
        self.back_moment_inert_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                            text=" Назад",
                                            font=("GOST Type BU", 11, "bold"), width=100, height=40,
                                            bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d",
                                            relief=GROOVE, command=self.buckling_calc)
        self.back_scheme_choice_btn = Button(self.root, text="К выбору\nсхем нагружения", width=18, height=2,
                                             font=("GOST Type BU", 11, "bold"), bg="#c8d6ca", fg="#5c868d",
                                             activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)
        self.back_moment_inert_btn.place(in_=self.label, x=40, y=45)
        self.back_scheme_choice_btn.place(in_=self.label, x=170, y=44)

    def draw_Yasinsky_formula(self):
        self.Yasinsky_frame = LabelFrame(self.root, text=" Эмпирическая формула Ясинского для средней гибкости стержня "
                                                         "(40  λ < 100) ",
                                            font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.Yasinsky_formula_img = PhotoImage(file=r"Data\Yasinsky_formula_550x125.png")
        self.Yasinsky_formula_label = Label(self.Yasinsky_frame, image=self.Yasinsky_formula_img)
        self.Yasinsky_formula_label.image = self.Yasinsky_formula_img

        self.Yasinsky_table_img = PhotoImage(file=r"Data\Yasinsky_table_550x383.png")
        self.Yasinsky_table_label = Label(self.Yasinsky_frame, image=self.Yasinsky_table_img)
        self.Yasinsky_table_label.image = self.Yasinsky_table_img

        self.Yasinsky_frame.place(in_=self.label, x=50, y=100)
        self.Yasinsky_formula_label.grid(row=1, column=0, padx=15, pady=(5, 0), sticky=W)
        self.Yasinsky_table_label.grid(row=2, column=0, padx=15, pady=(0, 10), sticky=W)

    def draw_Yasinsky_data_frame(self):
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_Yasinsky_formula_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_Yasinsky_formula_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_Yasinsky_formula_calc.txt", "r")
        self.open_data_init()
        self.Yasinsky_data_frame = LabelFrame(self.root, text=" Ввод данных для расчета  ",
                                              font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.a_ratio_label = Label(self.Yasinsky_data_frame, width=44, height=1,
                                               text="Введите коэффициент a, в кг/см2",
                                               font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                               justify=LEFT)
        self.a_ratio_entry = Entry(self.Yasinsky_data_frame, width=8, font=("GOST Type BU", 11),
                                   bg="white", fg="#5c3d46", validate="key",
                                   validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.b_ratio_label = Label(self.Yasinsky_data_frame, width=44, height=1,
                                   text="Введите коэффициент b, в кг/см2",
                                   font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                   justify=LEFT)
        self.b_ratio_entry = Entry(self.Yasinsky_data_frame, width=8, font=("GOST Type BU", 11),
                                   bg="white", fg="#5c3d46", validate="key",
                                   validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.parabolic_law_label = Label(self.Yasinsky_data_frame, width=50, height=5, text="Для стержней средней и "
                                         "малой гибкости\nкритическое напряжение можно определить\n(если для материала "
                                         "отсутствуют справочные\nданные для формулы Ясинского)  по\n"
                                         "параболическому закону", font=("GOST Type BU", 11, "italic"),
                                         bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.parabolic_law_btn = Button(self.Yasinsky_data_frame, width=17, height=3, text="Расчет по\n"
                                                                                           "параболическому\nзакону",
                                        font=("GOST Type BU", 10, "bold"), bg="#c8d6ca", fg="#5c868d",
                                        activebackground="#e0a96d", relief=GROOVE, command=self.draw_parabolic_law_calc)
        self.Yasinsky_calc_btn = Button(self.Yasinsky_data_frame, width=10, height=1, text="Расчет",
                                        font=("GOST Type BU", 10, "bold"), bg="#c8d6ca", fg="#5c868d",
                                        activebackground="#e0a96d", relief=GROOVE, command=self.Yasinsky_calc)
        self.all_clear_Yasinsky_data_btn = Button(self.Yasinsky_data_frame, width=10, height=1, text="Очистить",
                                        font=("GOST Type BU", 10, "bold"), bg="#c8d6ca", fg="#5c868d",
                                        activebackground="#e0a96d", relief=GROOVE, command=self.all_clear_Yasinsky_data)

        if len(self.open_data) == 2:
            self.a_ratio_entry.insert(0, f"{self.open_data[0]}")
            self.b_ratio_entry.insert(0, f"{self.open_data[1]}")

        self.Yasinsky_data_frame.place(in_=self.label, x=670, y=100)
        self.a_ratio_label.grid(row=1, column=0, padx=15, pady=(5, 0), sticky=W)
        self.a_ratio_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.b_ratio_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.b_ratio_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.parabolic_law_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.parabolic_law_btn.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.Yasinsky_calc_btn.grid(row=4, column=0, padx=15, pady=10, sticky=E + S)
        self.all_clear_Yasinsky_data_btn.grid(row=4, column=1, padx=(0, 10), pady=10, sticky=W + S)

    def Yasinsky_calc(self):
        flag = True
        try:
            self.a_ratio = float(self.a_ratio_entry.get())
            self.b_ratio = float(self.b_ratio_entry.get())
        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля данных заполнены, или введено некорректное значение")
            self.Yasinsky_output_frame.destroy()
        if flag:
            self.output_Yasinsky_calc()
            self.crit_stress = self.a_ratio - self.b_ratio * self.flexibility_shtock
            self.crit_force_Yasinsky = self.crit_stress * self.square_shtock

            self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_Yasinsky_formula_calc.txt", "w")

            # Запись
            self.save_data_calc.write(str(self.a_ratio) + "\n")
            self.save_data_calc.write(str(self.b_ratio))
            self.save_data_calc.close()

            # Вывод
            self.Yasinsky_formula_value.set(f"Критическое напряжение σкр = {round(self.crit_stress, 2)} кг/см2\n"
                                        f"Критическая сила Pкр = {round(self.crit_force_Yasinsky, 2)} кг")

    def all_clear_Yasinsky_data(self):
        self.a_ratio_entry.delete(0, END)
        self.b_ratio_entry.delete(0, END)
        self.Yasinsky_output_frame.destroy()
        self.progress_calc.configure(value=86)

    def output_Yasinsky_calc(self):
        self.Yasinsky_formula_value = StringVar()
        self.progress_calc.configure(value=100)
        self.Yasinsky_output_frame = LabelFrame(self.root, text="Результат расчета по формуле Ясинского",
                                                font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d",)
        self.Yasinsky_output_label = Label(self.Yasinsky_output_frame, width=62, height=2,
                                   textvariable=self.Yasinsky_formula_value, font=("GOST Type BU", 11, "bold"),
                                           bg="#99bfaa", fg="#5c3d46", justify=LEFT)

        self.Yasinsky_output_frame.place(in_=self.label, x=670, y=340)
        self.Yasinsky_output_label.grid(row=1, column=0, padx=15, pady=10, sticky=W)



    def draw_formula_init_deflection_frame(self):
        self.formula_init_deflection_frame = LabelFrame(self.root, text="  Расчетная формула начального прогиба ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        if self.sheme_1:
            self.init_deflection_img = PhotoImage(file=r"Data\initial_deflection_sch1_600x105.png")
        elif self.sheme_2:
            self.init_deflection_img = PhotoImage(file=r"Data\initial_deflection_sch2_600x105.png")
        elif self.sheme_3:
            self.init_deflection_img = PhotoImage(file=r"Data\initial_deflection_sch3_600x105.png")
        else:
            self.init_deflection_img = PhotoImage(file=r"Data\initial_deflection_sch4_600x105.png")
        self.init_deflection_label = Label(self.formula_init_deflection_frame, image=self.init_deflection_img)
        self.init_deflection_label.image = self.init_deflection_img

        self.formula_init_deflection_frame.place(in_=self.label, x=600, y=100)
        self.init_deflection_label.pack()

    def draw_table_gap_frame(self):
        self.table_gap_frame = LabelFrame(self.root, text="  Таблица зазоров ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")

        self.table_gap_img = PhotoImage(file=r"Data\gap_table_540x385.png")
        self.table_gap_label = Label(self.table_gap_frame, image=self.table_gap_img)
        self.table_gap_label.image = self.table_gap_img

        self.table_gap_frame.place(in_=self.label, x=40, y=240)
        self.table_gap_label.pack()

    def draw_data_init_deflection(self):
        self.data_init_deflection_frame = LabelFrame(self.root,
                                                          text=" Ввод данных для расчета начального прогиба  ",
                                                          font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de",
                                                          fg="#5c868d")
        self.gap_guide_to_shtock_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                               text="Зазор на диаметр в направляющей штока Δ1 (см. табл.), в см",
                                               font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                               justify=LEFT)
        self.gap_guide_to_shtock_entry = Entry(self.data_init_deflection_frame, width=8,
                                               font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                               validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.gap_clndr_to_pistol_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                               text="Зазор на диаметр между поршнем и цилиндром Δ2 (см. табл.), в см",
                                               font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                               justify=LEFT)
        self.gap_clndr_to_pistol_entry = Entry(self.data_init_deflection_frame, width=8,
                                               font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                               validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.length_guide_to_pistol_label = Label(self.data_init_deflection_frame, width=65, height=2,
                                                  text="Расстояние от начала передней направляющей штока\n"
                                                       "до конца поршня a, в мм (см. общую схему)",
                                                  font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                                  justify=LEFT)
        self.length_guide_to_pistol_entry = Entry(self.data_init_deflection_frame, width=8,
                                                  font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                                  validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.weight_hydra_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                        text="Вес гидроцилиндра G, в кг", font=("GOST Type BU", 11, "bold"),
                                        bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.weight_hydra_entry = Entry(self.data_init_deflection_frame, width=8,
                                        font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                        validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.alpha_angle_label = Label(self.data_init_deflection_frame, width=65, height=2,
                                       text="Угол α между осью гидроцилиндра\nи горизонтальной плоскостью в градусах",
                                       font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.alpha_angle_entry = Entry(self.data_init_deflection_frame, width=8,
                                       font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                       validatecommand=(self.root.register(self.validate_amount), "%S"))

        self.init_deflection_output_label = Label(self.data_init_deflection_frame, width=65, height=2,
                                                  textvariable=self.init_deflection_value,
                                                  font=("GOST Type BU", 11, "bold"),
                                                  bg="#99bfaa", fg="#5c3d46")
        self.full_deflection_btn = Button(self.data_init_deflection_frame,
                                          text="Далее\nк расчету\nполного\nпрогиба",
                                          font=("GOST Type BU", 10, "bold"),
                                          width=12, height=4, bg="#c8d6ca", fg="#5c868d",
                                          activebackground="#e0a96d", relief=GROOVE,
                                          command=self.full_deflection_condition)

        self.data_init_deflection_frame.place(in_=self.label, x=600, y=240)
        self.gap_guide_to_shtock_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.gap_guide_to_shtock_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.gap_clndr_to_pistol_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.gap_clndr_to_pistol_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.length_guide_to_pistol_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.length_guide_to_pistol_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W + N)
        self.weight_hydra_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.weight_hydra_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.alpha_angle_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.alpha_angle_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W + N)

    def all_clear_init_deflection(self):
        self.gap_guide_to_shtock_entry.delete(0, END)
        self.gap_clndr_to_pistol_entry.delete(0, END)
        self.length_guide_to_pistol_entry.delete(0, END)
        self.weight_hydra_entry.delete(0, END)
        self.alpha_angle_entry.delete(0, END)
        self.init_deflection_value.set(f"")
        if self.full_deflection_btn:
            self.full_deflection_btn.destroy()

    def all_clear_init_deflection_sch1(self):
        self.long_force_eccentricity_shtock_entry.delete(0, END)
        self.long_force_eccentricity_clndr_entry.delete(0, END)
        self.shear_force_entry.delete(0, END)
        self.length_shear_force_entry.delete(0, END)
        self.all_clear_init_deflection()

    def all_clear_init_deflection_sch2(self):
        self.long_force_eccentricity_shtock_entry.delete(0, END)
        self.long_force_eccentricity_clndr_entry.delete(0, END)
        self.all_clear_init_deflection()

    def all_clear_init_deflection_sch3(self):
        self.shear_force_entry.delete(0, END)
        self.length_shear_force_entry.delete(0, END)
        self.all_clear_init_deflection()

    def all_clear_init_deflection_sch4(self):
        self.all_clear_init_deflection()


    def draw_data_init_deflection_sch1(self):
        self.init_deflection_value = StringVar()
        self.draw_data_init_deflection()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc1_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_init_deflection_sc1_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc1_calc.txt", "r")
        self.open_data_init()
        self.long_force_eccentricity_shtock_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                           text="Эксцентриситет продольной силы относительно оси штока e1, в мм",
                                           font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.long_force_eccentricity_shtock_entry = Entry(self.data_init_deflection_frame, width=8,
                                                   font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                                   validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.long_force_eccentricity_clndr_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                            text="Эксцентриситет продольной силы относительно оси цилиндра e2, в мм",
                                            font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.long_force_eccentricity_clndr_entry = Entry(self.data_init_deflection_frame, width=8,
                                                   font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                                   validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.shear_force_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                               text="Поперечная сила Q, в кг", font=("GOST Type BU", 11, "bold"),
                                       bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.shear_force_entry = Entry(self.data_init_deflection_frame, width=8,
                                               font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                               validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.length_shear_force_label = Label(self.data_init_deflection_frame, width=65, height=2,
                                    text="Расстояние от точки приложения поперечной силы\n"
                                         "до шарнира цилиндра l3, в мм",
                                    font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.length_shear_force_entry = Entry(self.data_init_deflection_frame, width=8,
                                       font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                       validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.init_deflection_sch1_calc_btn = Button(self.data_init_deflection_frame,
                                               text="Расчитать начальный прогиб", font=("GOST Type BU", 10, "bold"),
                                               width=30, height=1, bg="#c8d6ca", fg="#5c868d",
                                               activebackground="#e0a96d", relief=GROOVE,
                                               command=self.init_deflection_sch1_calc)
        self.all_clear_init_deflection_sch1_btn = Button(self.data_init_deflection_frame,
                                                    text="Очистить",
                                                    font=("GOST Type BU", 10, "bold"),
                                                    width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                                    activebackground="#e0a96d", relief=GROOVE,
                                                    command=self.all_clear_init_deflection_sch1)


        if len(self.open_data) == 9:
            self.gap_guide_to_shtock_entry.insert(0, f"{self.open_data[0]}")
            self.gap_clndr_to_pistol_entry.insert(0, f"{self.open_data[1]}")
            self.length_guide_to_pistol_entry.insert(0, f"{self.open_data[2]}")
            self.weight_hydra_entry.insert(0, f"{self.open_data[3]}")
            self.alpha_angle_entry.insert(0, f"{self.open_data[4]}")
            self.long_force_eccentricity_shtock_entry.insert(0, f"{self.open_data[5]}")
            self.long_force_eccentricity_clndr_entry.insert(0, f"{self.open_data[6]}")
            self.shear_force_entry.insert(0, f"{self.open_data[7]}")
            self.length_shear_force_entry.insert(0, f"{self.open_data[8]}")

        self.long_force_eccentricity_shtock_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.long_force_eccentricity_shtock_entry.grid(row=6, column=1, padx=(10, 20), pady=2, sticky=W)
        self.long_force_eccentricity_clndr_label.grid(row=7, column=0, padx=15, pady=2, sticky=W)
        self.long_force_eccentricity_clndr_entry.grid(row=7, column=1, padx=(10, 20), pady=2, sticky=W)
        self.shear_force_label.grid(row=8, column=0, padx=15, pady=2, sticky=W)
        self.shear_force_entry.grid(row=8, column=1, padx=(10, 20), pady=2, sticky=W)
        self.length_shear_force_label.grid(row=9, column=0, padx=15, pady=2, sticky=W)
        self.length_shear_force_entry.grid(row=9, column=1, padx=(10, 20), pady=2, sticky=W + N)
        self.init_deflection_output_label.grid(row=10, column=0, padx=15, pady=2, sticky=W + N)
        self.init_deflection_sch1_calc_btn.grid(row=11, column=0, padx=(0, 15), pady=(5, 6), sticky=E + N)
        self.all_clear_init_deflection_sch1_btn.grid(row=11, column=0, padx=(0, 250), pady=(5, 6), sticky=E + N)


    def draw_data_init_deflection_sch2(self):
        self.init_deflection_value = StringVar()
        self.draw_data_init_deflection()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc2_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_init_deflection_sc2_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc2_calc.txt", "r")
        self.open_data_init()
        self.long_force_eccentricity_shtock_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                                text="Эксцентриситет продольной силы относительно оси штока e1, в мм",
                                                font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                                justify=LEFT)
        self.long_force_eccentricity_shtock_entry = Entry(self.data_init_deflection_frame, width=8,
                                                          font=("GOST Type BU", 11), bg="white", fg="#5c3d46",
                                                          validate="key",
                                                          validatecommand=(
                                                          self.root.register(self.validate_amount), "%S"))
        self.long_force_eccentricity_clndr_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                                         text="Эксцентриситет продольной силы относительно оси цилиндра e2, в мм",
                                                         font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                                         justify=LEFT)
        self.long_force_eccentricity_clndr_entry = Entry(self.data_init_deflection_frame, width=8,
                                                         font=("GOST Type BU", 11), bg="white", fg="#5c3d46",
                                                         validate="key",
                                                         validatecommand=(
                                                         self.root.register(self.validate_amount), "%S"))
        self.init_deflection_sch2_calc_btn = Button(self.data_init_deflection_frame,
                                                    text="Расчитать начальный прогиб",
                                                    font=("GOST Type BU", 10, "bold"),
                                                    width=30, height=1, bg="#c8d6ca", fg="#5c868d",
                                                    activebackground="#e0a96d", relief=GROOVE,
                                                    command=self.init_deflection_sch2_calc)
        self.all_clear_init_deflection_sch2_btn = Button(self.data_init_deflection_frame,
                                                         text="Очистить",
                                                         font=("GOST Type BU", 10, "bold"),
                                                         width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                                         activebackground="#e0a96d", relief=GROOVE,
                                                         command=self.all_clear_init_deflection_sch2)

        if len(self.open_data) == 7:
            self.gap_guide_to_shtock_entry.insert(0, f"{self.open_data[0]}")
            self.gap_clndr_to_pistol_entry.insert(0, f"{self.open_data[1]}")
            self.length_guide_to_pistol_entry.insert(0, f"{self.open_data[2]}")
            self.weight_hydra_entry.insert(0, f"{self.open_data[3]}")
            self.alpha_angle_entry.insert(0, f"{self.open_data[4]}")
            self.long_force_eccentricity_shtock_entry.insert(0, f"{self.open_data[5]}")
            self.long_force_eccentricity_clndr_entry.insert(0, f"{self.open_data[6]}")

        self.long_force_eccentricity_shtock_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.long_force_eccentricity_shtock_entry.grid(row=6, column=1, padx=10, pady=2, sticky=W)
        self.long_force_eccentricity_clndr_label.grid(row=7, column=0, padx=15, pady=2, sticky=W)
        self.long_force_eccentricity_clndr_entry.grid(row=7, column=1, padx=10, pady=2, sticky=W)
        self.init_deflection_output_label.grid(row=8, column=0, padx=15, pady=2, sticky=W + N)
        self.init_deflection_sch2_calc_btn.grid(row=9, column=0, padx=(0, 15), pady=(5, 6), sticky=E + N)
        self.all_clear_init_deflection_sch2_btn.grid(row=9, column=0, padx=(0, 250), pady=(5, 6), sticky=E + N)



    def draw_data_init_deflection_sch3(self):
        self.init_deflection_value = StringVar()
        self.draw_data_init_deflection()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc3_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_init_deflection_sc3_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc3_calc.txt", "r")
        self.open_data_init()
        self.shear_force_label = Label(self.data_init_deflection_frame, width=65, height=1,
                                       text="Поперечная сила Q, в кг", font=("GOST Type BU", 11, "bold"),
                                       bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.shear_force_entry = Entry(self.data_init_deflection_frame, width=8,
                                       font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                       validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.length_shear_force_label = Label(self.data_init_deflection_frame, width=65, height=2,
                                              text="Расстояние от точки приложения поперечной силы\n"
                                                   "до шарнира цилиндра l3, в мм",
                                              font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46",
                                              justify=LEFT)
        self.length_shear_force_entry = Entry(self.data_init_deflection_frame, width=8,
                                              font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                              validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.init_deflection_sch3_calc_btn = Button(self.data_init_deflection_frame,
                                                    text="Расчитать начальный прогиб",
                                                    font=("GOST Type BU", 10, "bold"),
                                                    width=30, height=1, bg="#c8d6ca", fg="#5c868d",
                                                    activebackground="#e0a96d", relief=GROOVE,
                                                    command=self.init_deflection_sch3_calc)
        self.all_clear_init_deflection_sch3_btn = Button(self.data_init_deflection_frame,
                                                         text="Очистить",
                                                         font=("GOST Type BU", 10, "bold"),
                                                         width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                                         activebackground="#e0a96d", relief=GROOVE,
                                                         command=self.all_clear_init_deflection_sch3)

        if len(self.open_data) == 7:
            self.gap_guide_to_shtock_entry.insert(0, f"{self.open_data[0]}")
            self.gap_clndr_to_pistol_entry.insert(0, f"{self.open_data[1]}")
            self.length_guide_to_pistol_entry.insert(0, f"{self.open_data[2]}")
            self.weight_hydra_entry.insert(0, f"{self.open_data[3]}")
            self.alpha_angle_entry.insert(0, f"{self.open_data[4]}")
            self.shear_force_entry.insert(0, f"{self.open_data[5]}")
            self.length_shear_force_entry.insert(0, f"{self.open_data[6]}")

        self.shear_force_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.shear_force_entry.grid(row=6, column=1, padx=10, pady=2, sticky=W)
        self.length_shear_force_label.grid(row=7, column=0, padx=15, pady=2, sticky=W)
        self.length_shear_force_entry.grid(row=7, column=1, padx=10, pady=2, sticky=W + N)
        self.init_deflection_output_label.grid(row=8, column=0, padx=15, pady=2, sticky=W + N)
        self.init_deflection_sch3_calc_btn.grid(row=9, column=0, padx=(0, 15), pady=(5, 6), sticky=E + N)
        self.all_clear_init_deflection_sch3_btn.grid(row=9, column=0, padx=(0, 250), pady=(5, 6), sticky=E + N)


    def draw_data_init_deflection_sch4(self):
        self.init_deflection_value = StringVar()
        self.draw_data_init_deflection()
        try:
            self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc4_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_HydraAtDown_init_deflection_sc4_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc4_calc.txt", "r")
        self.open_data_init()
        self.init_deflection_sch4_calc_btn = Button(self.data_init_deflection_frame,
                                                    text="Расчитать начальный прогиб",
                                                    font=("GOST Type BU", 10, "bold"),
                                                    width=30, height=1, bg="#c8d6ca", fg="#5c868d",
                                                    activebackground="#e0a96d", relief=GROOVE,
                                                    command=self.init_deflection_sch4_calc)
        self.all_clear_init_deflection_sch4_btn = Button(self.data_init_deflection_frame,
                                                         text="Очистить",
                                                         font=("GOST Type BU", 10, "bold"),
                                                         width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                                         activebackground="#e0a96d", relief=GROOVE,
                                                         command=self.all_clear_init_deflection_sch4)

        if len(self.open_data) == 5:
            self.gap_guide_to_shtock_entry.insert(0, f"{self.open_data[0]}")
            self.gap_clndr_to_pistol_entry.insert(0, f"{self.open_data[1]}")
            self.length_guide_to_pistol_entry.insert(0, f"{self.open_data[2]}")
            self.weight_hydra_entry.insert(0, f"{self.open_data[3]}")
            self.alpha_angle_entry.insert(0, f"{self.open_data[4]}")

        self.init_deflection_output_label.grid(row=6, column=0, padx=15, pady=2, sticky=W + N)
        self.init_deflection_sch4_calc_btn.grid(row=7, column=0, padx=(0, 15), pady=(5, 6), sticky=E + N)
        self.all_clear_init_deflection_sch4_btn.grid(row=7, column=0, padx=(0, 250), pady=(5, 6), sticky=E + N)

    def init_deflection_sch1_calc(self):
        flag = True
        try:
            self.gap_guide_to_shtock = float(self.gap_guide_to_shtock_entry.get())
            self.gap_clndr_to_pistol = float(self.gap_clndr_to_pistol_entry.get())
            self.length_guide_to_pistol = float(self.length_guide_to_pistol_entry.get()) / 10
            self.weight_hydra = float(self.weight_hydra_entry.get())
            self.alpha_angle = math.radians(float(self.alpha_angle_entry.get()))
            self.long_force_eccentricity_shtock = float(self.long_force_eccentricity_shtock_entry.get()) / 10
            self.long_force_eccentricity_clndr = float(self.long_force_eccentricity_clndr_entry.get()) / 10
            self.shear_force = float(self.shear_force_entry.get())
            self.length_shear_force = float(self.length_shear_force_entry.get()) / 10

        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.init_deflection_value.set(f"")
            self.full_deflection_btn.grid_forget()
        if flag:
            try:
                self.length_hydro = self.length_shtock_to_point_A + self.length_clndr_to_point_A
                self.gap_hydro = self.gap_guide_to_shtock + self.gap_clndr_to_pistol
                self.init_deflection = self.long_force_eccentricity_shtock - \
                                    ((self.long_force_eccentricity_shtock - self.long_force_eccentricity_clndr) /
                                     self.length_hydro) * self.length_shtock_to_point_A +\
                                    ((self.gap_hydro * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                     (2 * self.length_guide_to_pistol * self.length_hydro)) +\
                                    ((self.shear_force * self.length_shear_force * self.length_shtock_to_point_A) /
                                     (self.pull * self.length_hydro)) +\
                                    ((self.weight_hydra * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                     (2 * self.pull * self.length_hydro)) * math.cos(self.alpha_angle)

            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.init_deflection_value.set(f"")
                self.full_deflection_btn.grid_forget()
            if flag:
                self.progress_calc.configure(value=75)
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc1_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.gap_guide_to_shtock) + "\n")
                self.save_data_calc.write(str(self.gap_clndr_to_pistol) + "\n")
                self.save_data_calc.write(str(self.length_guide_to_pistol * 10) + "\n")
                self.save_data_calc.write(str(self.weight_hydra) + "\n")
                self.save_data_calc.write(str(math.degrees(self.alpha_angle)) + "\n")
                self.save_data_calc.write(str(self.long_force_eccentricity_shtock * 10) + "\n")
                self.save_data_calc.write(str(self.long_force_eccentricity_clndr * 10) + "\n")
                self.save_data_calc.write(str(self.shear_force) + "\n")
                self.save_data_calc.write(str(self.length_shear_force * 10))
                self.save_data_calc.close()

                # Вывод
                self.init_deflection_value.set(f"Начальный прогиб δнач = {round(self.init_deflection, 2)} см")
                # self.full_deflection_btn.place(in_=self.label, x=1150, y=10)
                self.full_deflection_btn.grid(row=10, column=1, rowspan=2, columnspan=2, padx=(0, 10), pady=(5, 6),
                                              sticky=W + S)

    def init_deflection_sch2_calc(self):
        flag = True
        try:
            self.gap_guide_to_shtock = float(self.gap_guide_to_shtock_entry.get())
            self.gap_clndr_to_pistol = float(self.gap_clndr_to_pistol_entry.get())
            self.length_guide_to_pistol = float(self.length_guide_to_pistol_entry.get()) / 10
            self.weight_hydra = float(self.weight_hydra_entry.get())
            self.alpha_angle = math.radians(float(self.alpha_angle_entry.get()))
            self.long_force_eccentricity_shtock = float(self.long_force_eccentricity_shtock_entry.get()) / 10
            self.long_force_eccentricity_clndr = float(self.long_force_eccentricity_clndr_entry.get()) / 10

        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.init_deflection_value.set(f"")
            self.full_deflection_btn.grid_forget()

        if flag:
            try:
                self.length_hydro = self.length_shtock_to_point_A + self.length_clndr_to_point_A
                self.gap_hydro = self.gap_guide_to_shtock + self.gap_clndr_to_pistol
                self.init_deflection = self.long_force_eccentricity_shtock - \
                                   ((self.long_force_eccentricity_shtock - self.long_force_eccentricity_clndr) /
                                    self.length_hydro) * self.length_shtock_to_point_A + \
                                   ((self.gap_hydro * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.length_guide_to_pistol * self.length_hydro)) + \
                                   ((self.weight_hydra * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.pull * self.length_hydro)) * math.cos(self.alpha_angle)
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.init_deflection_value.set(f"")
                self.full_deflection_btn.grid_forget()
            if flag:
                self.progress_calc.configure(value=75)
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc2_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.gap_guide_to_shtock) + "\n")
                self.save_data_calc.write(str(self.gap_clndr_to_pistol) + "\n")
                self.save_data_calc.write(str(self.length_guide_to_pistol * 10) + "\n")
                self.save_data_calc.write(str(self.weight_hydra) + "\n")
                self.save_data_calc.write(str(math.degrees(self.alpha_angle)) + "\n")
                self.save_data_calc.write(str(self.long_force_eccentricity_shtock * 10) + "\n")
                self.save_data_calc.write(str(self.long_force_eccentricity_clndr * 10))
                self.save_data_calc.close()

                # Вывод
                self.init_deflection_value.set(f"Начальный прогиб δнач = {round(self.init_deflection, 2)} см")
                self.full_deflection_btn.grid(row=8, column=1, rowspan=2, columnspan=2, padx=(0, 10), pady=(5, 6),
                                           sticky=W + S)

    def init_deflection_sch3_calc(self):
        flag = True
        try:
            self.gap_guide_to_shtock = float(self.gap_guide_to_shtock_entry.get())
            self.gap_clndr_to_pistol = float(self.gap_clndr_to_pistol_entry.get())
            self.length_guide_to_pistol = float(self.length_guide_to_pistol_entry.get()) / 10
            self.weight_hydra = float(self.weight_hydra_entry.get())
            self.alpha_angle = math.radians(float(self.alpha_angle_entry.get()))
            self.shear_force = float(self.shear_force_entry.get())
            self.length_shear_force = float(self.length_shear_force_entry.get()) / 10

        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.init_deflection_value.set(f"")
            self.full_deflection_btn.grid_forget()
        if flag:
            try:
                self.length_hydro = self.length_shtock_to_point_A + self.length_clndr_to_point_A
                self.gap_hydro = self.gap_guide_to_shtock + self.gap_clndr_to_pistol
                self.init_deflection = ((self.gap_hydro * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.length_guide_to_pistol * self.length_hydro)) + \
                                   ((self.shear_force * self.length_shear_force * self.length_shtock_to_point_A) /
                                    (self.pull * self.length_hydro)) + \
                                   ((self.weight_hydra * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.pull * self.length_hydro)) * math.cos(self.alpha_angle)
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.init_deflection_value.set(f"")
                self.full_deflection_btn.grid_forget()
            if flag:
                self.progress_calc.configure(value=75)
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc3_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.gap_guide_to_shtock) + "\n")
                self.save_data_calc.write(str(self.gap_clndr_to_pistol) + "\n")
                self.save_data_calc.write(str(self.length_guide_to_pistol * 10) + "\n")
                self.save_data_calc.write(str(self.weight_hydra) + "\n")
                self.save_data_calc.write(str(math.degrees(self.alpha_angle)) + "\n")
                self.save_data_calc.write(str(self.shear_force) + "\n")
                self.save_data_calc.write(str(self.length_shear_force * 10))
                self.save_data_calc.close()

                # Вывод
                self.init_deflection_value.set(f"Начальный прогиб δнач = {round(self.init_deflection, 2)} см")
                self.full_deflection_btn.grid(row=8, column=1, rowspan=2, columnspan=2, padx=(0, 10), pady=(5, 6),
                                              sticky=W + S)


    def init_deflection_sch4_calc(self):
        flag = True
        try:
            self.gap_guide_to_shtock = float(self.gap_guide_to_shtock_entry.get())
            self.gap_clndr_to_pistol = float(self.gap_clndr_to_pistol_entry.get())
            self.length_guide_to_pistol = float(self.length_guide_to_pistol_entry.get()) / 10
            self.weight_hydra = float(self.weight_hydra_entry.get())
            self.alpha_angle = math.radians(float(self.alpha_angle_entry.get()))

        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.init_deflection_value.set(f"")
            self.full_deflection_btn.grid_forget()
        if flag:
            try:
                self.length_hydro = self.length_shtock_to_point_A + self.length_clndr_to_point_A
                self.gap_hydro = self.gap_guide_to_shtock + self.gap_clndr_to_pistol
                self.init_deflection = ((self.gap_hydro * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.length_guide_to_pistol * self.length_hydro)) + \
                                   ((self.weight_hydra * self.length_shtock_to_point_A * self.length_clndr_to_point_A) /
                                    (2 * self.pull * self.length_hydro)) * math.cos(self.alpha_angle)
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.init_deflection_value.set(f"")
                self.full_deflection_btn.grid_forget()
            if flag:
                self.progress_calc.configure(value=75)
                self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_init_deflection_sc4_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.gap_guide_to_shtock) + "\n")
                self.save_data_calc.write(str(self.gap_clndr_to_pistol) + "\n")
                self.save_data_calc.write(str(self.length_guide_to_pistol * 10) + "\n")
                self.save_data_calc.write(str(self.weight_hydra) + "\n")
                self.save_data_calc.write(str(math.degrees(self.alpha_angle)))
                self.save_data_calc.close()

                # Вывод
                self.init_deflection_value.set(f"Начальный прогиб δнач = {round(self.init_deflection, 2)} см")
                self.full_deflection_btn.grid(row=6, column=1, rowspan=2, columnspan=2, padx=(0, 10), pady=(5, 6),
                                              sticky=W + S)


    def full_deflection_condition(self):
        self.label.destroy()
        self.draw_label()
        self.draw_header(header_text=" Расчет штока на прочность.\nОпределение полного прогиба. ", h=2)
        self.draw_mpa_kgcm2_calc()
        self.draw_table_moment_resist_frame()
        self.progressbar_view()
        self.progress_calc.configure(value=83)
        self.back_init_deflection_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                            text=" Назад",
                                            font=("GOST Type BU", 11, "bold"), width=100, height=40,
                                            bg="#c8d6ca", fg="#5c868d", activebackground="#e0a96d",
                                            relief=GROOVE, command=self.back_init_deflection)
        self.back_scheme_choice_btn = Button(self.root, text="К выбору\nсхем нагружения", width=18, height=2,
                                             font=("GOST Type BU", 11, "bold"), bg="#c8d6ca", fg="#5c868d",
                                             activebackground="#e0a96d", relief=GROOVE,
                                             command=self.back_scheme_choice)
        self.back_init_deflection_btn.place(in_=self.label, x=40, y=45)
        self.back_scheme_choice_btn.place(in_=self.label, x=170, y=44)

        if (self.length_hydro / self.our_diam_shtock) <= 5:
            self.full_deflection = self.init_deflection
            self.event = 1
            self.draw_full_deflection_formula()
            self.draw_data_full_deflection()
        elif (self.length_hydro / self.our_diam_shtock) > 5 and self.length_shtock_to_point_A == self.length_clndr_to_point_A \
                or (self.length_hydro / self.our_diam_shtock) > 5 and self.moment_inert_sleeve >= 5 * self.moment_inert_shtock:
            self.event = 2
            self.draw_full_deflection_formula()
            self.draw_data_full_deflection()
            self.elastic_modulus_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
            self.elastic_modulus_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        else:
            self.event = 3
            self.draw_full_deflection_formula()
            self.draw_data_full_deflection()
            self.elastic_modulus_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
            self.elastic_modulus_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)



    def back_init_deflection(self):
        self.shtock_calc()

    def draw_full_deflection_formula(self):
        self.full_deflection_formula_frame = LabelFrame(self.root, text=" Расчетная формула полного прогиба  ",
                                                        font=("GOST Type BU", 11, "bold", "italic"),
                                                        bg="#e7f5de", fg="#5c868d")
        self.tabs_control = Notebook(self.full_deflection_formula_frame, height=225, width=600, padding=(0, 5, 0, 0))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="l/d1  5")
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="l/d1 > 5; J2  5J1")
        self.tab_3 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_3, text="l/d1 > 5; J2 < 5J1")

        if self.event == 1:
            self.tabs_control.select(self.tab_1)
        if self.event == 2:
            self.tabs_control.select(self.tab_2)
        if self.event == 3:
            self.tabs_control.select(self.tab_3)
        self.full_deflection_formula_frame.place(in_=self.label, x=40, y=375)
        self.run_deflection()

    def run_deflection(self):
        self.full_deflection_1_img = PhotoImage(file=r"Data\full_deflection_1_600x225.png")
        self.full_deflection_2_img = PhotoImage(file=r"Data\full_deflection_2_600x225.png")
        self.full_deflection_3_img = PhotoImage(file=r"Data\full_deflection_3_600x225.png")

        self.full_defl1_canvas = Canvas(self.tab_1, width=600, height=225, background="white")
        self.full_defl2_canvas = Canvas(self.tab_2, width=600, height=225, background="white")
        self.full_defl3_canvas = Canvas(self.tab_3, width=600, height=225, background="white")

        self.full_defl1_image = self.full_defl1_canvas.create_image(0, 0, anchor='nw',
                                                                              image=self.full_deflection_1_img)
        self.full_defl2_image = self.full_defl2_canvas.create_image(0, 0, anchor='nw',
                                                                              image=self.full_deflection_2_img)
        self.full_defl3_image = self.full_defl3_canvas.create_image(0, 0, anchor='nw',
                                                                              image=self.full_deflection_3_img)

        self.tabs_control.pack(fill=BOTH, expand=1)
        self.full_defl1_canvas.pack()
        self.full_defl2_canvas.pack()
        self.full_defl3_canvas.pack()



    def draw_data_full_deflection(self):
        if self.event == 1:
            try:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_calc.txt", "r")
            except FileNotFoundError:
                with open(r"Data\save_data\data_HydraAtDown_full_deflection_calc.txt", "w") as self.open_data_calc:
                    self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_calc.txt", "r")
        elif self.event == 2:
            try:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_event2_calc.txt", "r")
            except FileNotFoundError:
                with open(r"Data\save_data\data_HydraAtDown_full_deflection_event2_calc.txt", "w") as self.open_data_calc:
                    self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_event2_calc.txt", "r")
        elif self.event == 3:
            try:
                self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_event3_calc.txt", "r")
            except FileNotFoundError:
                with open(r"Data\save_data\data_HydraAtDown_full_deflection_event3_calc.txt", "w") as self.open_data_calc:
                    self.open_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_event3_calc.txt", "r")
        self.open_data_init()
        self.data_full_deflection_frame = LabelFrame(self.root,
                                             text=" Ввод данных для расчета полного прогиба и запаса прочности  ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.moment_of_resist_label = Label(self.data_full_deflection_frame, width=60, height=1,
                                            text="Момент сопротивления круглого сечения W (см. табл.), в см3",
                                            font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.moment_of_resist_entry = Entry(self.data_full_deflection_frame, width=8,
                                            font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                            validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label = Label(self.data_full_deflection_frame, width=60, height=1, font=("GOST Type BU", 11, "bold"),
                                          text="Предел текучести материала штока σT, в кг/см2",
                                          bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.yield_strength_entry = Entry(self.data_full_deflection_frame, width=8, font=("GOST Type BU", 11),
                                          bg="white", fg="#5c3d46", validate="key",
                                          validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.elastic_modulus_label = Label(self.data_full_deflection_frame, width=60, height=1,
                                           text="Модуль упругости материала штока E, в кг/см2",
                                           font=("GOST Type BU", 11, "bold"), bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.elastic_modulus_entry = Entry(self.data_full_deflection_frame, width=8,
                                           font=("GOST Type BU", 11), bg="white", fg="#5c3d46", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.highest_stress_calc_btn = Button(self.data_full_deflection_frame,
                                                    text="Расчитать полный прогиб и запас прочности",
                                                    font=("GOST Type BU", 10, "bold"),
                                                    width=46, height=1, bg="#c8d6ca", fg="#5c868d",
                                                    activebackground="#e0a96d", relief=GROOVE,
                                              command=self.highest_stress_calc)
        self.all_clear_full_deflection_btn = Button(self.data_full_deflection_frame,
                                              text="Очистить", font=("GOST Type BU", 10, "bold"),
                                              width=10, height=1, bg="#c8d6ca", fg="#5c868d",
                                              activebackground="#e0a96d", relief=GROOVE,
                                              command=self.all_clear_full_deflection)


        if self.event == 1:
            if len(self.open_data) == 2:
                self.moment_of_resist_entry.insert(0, f"{self.open_data[0]}")
                self.yield_strength_entry.insert(0, f"{self.open_data[1]}")
        elif self.event == 2:
            if len(self.open_data) == 3:
                self.moment_of_resist_entry.insert(0, f"{self.open_data[0]}")
                self.yield_strength_entry.insert(0, f"{self.open_data[1]}")
                self.elastic_modulus_entry.insert(0, f"{self.open_data[2]}")
        elif self.event == 3:
            if len(self.open_data) == 3:
                self.moment_of_resist_entry.insert(0, f"{self.open_data[0]}")
                self.yield_strength_entry.insert(0, f"{self.open_data[1]}")
                self.elastic_modulus_entry.insert(0, f"{self.open_data[2]}")

        self.data_full_deflection_frame.place(in_=self.label, x=40, y=100)
        self.moment_of_resist_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.moment_of_resist_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.yield_strength_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.highest_stress_calc_btn.grid(row=4, column=0, padx=15, pady=10, sticky=E + S)
        self.all_clear_full_deflection_btn.grid(row=4, column=1, padx=(0, 10), pady=10, sticky=W + S)

    def all_clear_full_deflection(self):
        if self.event == 2 or self.event == 3:
            self.elastic_modulus_entry.delete(0, END)
        self.moment_of_resist_entry.delete(0, END)
        self.yield_strength_entry.delete(0, END)
        self.full_deflection_sch1_value.set(f"")
        self.highest_stress_value.set(f"")
        self.allow_safity_value.set(f"")
        self.highest_stress_output_frame.destroy()




    def draw_table_moment_resist_frame(self):
        self.table_moment_resist_frame = LabelFrame(self.root, text="  Таблица моментов сопротивления "
                                                                    "круглого сечения ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")

        self.table_moment_resist_img = PhotoImage(file=r"Data\Moment_of_resist_600x420.png")
        self.table_moment_resist_label = Label(self.table_moment_resist_frame, image=self.table_moment_resist_img)
        self.table_moment_resist_label.image = self.table_moment_resist_img

        self.table_moment_resist_frame.place(in_=self.label, x=655, y=100)
        self.table_moment_resist_label.pack()

    def highest_stress_output(self):
        self.full_deflection_sch1_value = StringVar()
        self.highest_stress_value = StringVar()
        self.allow_safity_value = StringVar()
        self.progress_calc.configure(value=100)
        self.highest_stress_output_frame = LabelFrame(self.root, text=" Результаты расчета штока на прочность",
                                       font=("GOST Type BU", 11, "bold", "italic"), bg="#e7f5de", fg="#5c868d")
        self.full_deflection_sch1_label = Label(self.highest_stress_output_frame, width=71, height=1,
                                                font=("GOST Type BU", 11, "bold"),
                                                textvariable=self.full_deflection_sch1_value,
                                                bg="#99bfaa", fg="#5c3d46", justify=LEFT)
        self.highest_stress_label = Label(self.highest_stress_output_frame, width=71, height=1,
                                                font=("GOST Type BU", 11, "bold"),
                                                textvariable=self.highest_stress_value, bg="#99bfaa",
                                                fg="#5c3d46",
                                                justify=LEFT)
        self.allow_safity_label = Label(self.highest_stress_output_frame, width=71, height=1,
                                          font=("GOST Type BU", 11, "bold"),
                                          textvariable=self.allow_safity_value, bg="#99bfaa",
                                          fg="#5c3d46",
                                          justify=LEFT)

        self.highest_stress_output_frame.place(in_=self.label, x=40, y=265)
        self.full_deflection_sch1_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.highest_stress_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.allow_safity_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)

    def highest_stress_calc(self):
        flag = True
        try:
            self.moment_of_resist = float(self.moment_of_resist_entry.get())
            self.yield_strength = float(self.yield_strength_entry.get())
            self.square_shtock = (math.pi * math.pow(self.our_diam_shtock, 2)) / 4

        except ValueError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.full_deflection_sch1_value.set(f"")
            self.highest_stress_value.set(f"")
            self.allow_safity_value.set(f"")
            self.highest_stress_output_frame.destroy()

        if flag:
            self.highest_stress_output()
            if self.event == 1:
                try:
                    self.highest_stress = (self.pull / self.square_shtock) + ((self.pull * self.full_deflection)
                                                                              / self.moment_of_resist)
                    self.allow_safity = self.yield_strength / self.highest_stress

                except ZeroDivisionError:
                    flag = False
                    mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                    self.full_deflection_sch1_value.set(f"")
                    self.highest_stress_value.set(f"")
                    self.allow_safity_value.set(f"")
                    self.highest_stress_output_frame.destroy()
                if flag:
                    self.save_data_calc = open(r"Data\save_data\data_HydraAtDown_full_deflection_calc.txt", "w")

                    # Запись
                    self.save_data_calc.write(str(self.moment_of_resist) + "\n")
                    self.save_data_calc.write(str(self.yield_strength))
                    self.save_data_calc.close()

                    # Вывод
                    self.full_deflection_sch1_value.set(f" Полный прогиб для условия l/d1  5 равен начальному "
                                                        f"и составляет {round(self.full_deflection, 3)} см")
                    self.highest_stress_value.set(f"Наибольшее напряжение при сжатии и изгибе составляет "
                                                  f"{round(self.highest_stress, 1)} кг/см2")
                    self.allow_safity_value.set(f"Коэффициент запаса прочности "
                                                f"составляет {round(self.allow_safity, 1)}")

            elif self.event == 2:
                try:
                    self.elastic_modulus = float(self.elastic_modulus_entry.get())
                except ValueError:
                    flag = False
                    mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены"
                                             " или введено некорректное значение.")
                    self.full_deflection_sch1_value.set(f"")
                    self.highest_stress_value.set(f"")
                    self.allow_safity_value.set(f"")
                    self.highest_stress_output_frame.destroy()
                if flag:
                    try:
                        self.k1 = math.sqrt(self.pull / (self.elastic_modulus * self.moment_inert_shtock))
                        self.t1 = math.tan(self.k1 * self.length_shtock_to_point_A)
                        self.full_deflection = self.init_deflection / ((self.k1 / self.t1) * (self.length_hydro / 4)
                                                                         + 0.5)
                        self.highest_stress = (self.pull / self.square_shtock) + \
                                              ((self.pull * self.full_deflection) / self.moment_of_resist)
                        self.allow_safity = self.yield_strength / self.highest_stress
                    except ZeroDivisionError:
                        flag = False
                        mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                        self.full_deflection_sch1_value.set(f"")
                        self.highest_stress_value.set(f"")
                        self.allow_safity_value.set(f"")
                        self.highest_stress_output_frame.destroy()
                    if flag:
                        self.save_data_calc = \
                            open(r"Data\save_data\data_HydraAtDown_full_deflection_event2_calc.txt", "w")

                        # Запись
                        self.save_data_calc.write(str(self.moment_of_resist) + "\n")
                        self.save_data_calc.write(str(self.yield_strength) + "\n")
                        self.save_data_calc.write(str(self.elastic_modulus))
                        self.save_data_calc.close()

                        # Вывод
                        self.full_deflection_sch1_value.set(f" Полный прогиб для условия l/d1 > 5; J2  5J1 равен "
                                                    f"{round(self.full_deflection, 3)} см")
                        self.highest_stress_value.set(f"Наибольшее напряжение при сжатии и изгибе составляет "
                                              f"{round(self.highest_stress, 1)} кг/см2")
                        self.allow_safity_value.set(f"Коэффициент запаса прочности "
                                                    f"составляет {round(self.allow_safity, 1)}")

            elif self.event == 3:
                try:
                    self.elastic_modulus = float(self.elastic_modulus_entry.get())
                except ValueError:
                    flag = False
                    mb.showwarning("Ошибка", "ОШИБКА: Не все поля ввода данных заполнены"
                                             " или введено некорректное значение.")
                    self.full_deflection_sch1_value.set(f"")
                    self.highest_stress_value.set(f"")
                    self.allow_safity_value.set(f"")
                    self.highest_stress_output_frame.destroy()
                if flag:
                    try:
                        self.k1 = math.sqrt(self.pull / (self.elastic_modulus * self.moment_inert_shtock))
                        self.t1 = math.tan(self.k1 * self.length_shtock_to_point_A)
                        self.k2 = math.sqrt(self.pull / (self.elastic_modulus * self.moment_inert_sleeve))
                        self.t2 = math.tan(self.k2 * self.length_clndr_to_point_A)
                        self.full_deflection = self.init_deflection / (((self.k1 / self.t1) + (self.k2 / self.t2))
                                                        * self.length_shtock_to_point_A * self.length_clndr_to_point_A)
                        self.highest_stress = (self.pull / self.square_shtock) + \
                                             ((self.pull * self.full_deflection) / self.moment_of_resist)
                        self.allow_safity = self.yield_strength / self.highest_stress
                    except ZeroDivisionError:
                        flag = False
                        mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                        self.full_deflection_sch1_value.set(f"")
                        self.highest_stress_value.set(f"")
                        self.allow_safity_value.set(f"")
                        self.highest_stress_output_frame.destroy()
                    if flag:
                        self.save_data_calc = \
                            open(r"Data\save_data\data_HydraAtDown_full_deflection_event3_calc.txt", "w")

                        # Запись
                        self.save_data_calc.write(str(self.moment_of_resist) + "\n")
                        self.save_data_calc.write(str(self.yield_strength) + "\n")
                        self.save_data_calc.write(str(self.elastic_modulus))
                        self.save_data_calc.close()

                        # Вывод
                        self.full_deflection_sch1_value.set(f" Полный прогиб для условия l/d1 > 5; J2 < 5J1 равен "
                                                    f"{round(self.full_deflection, 3)} см")
                        self.highest_stress_value.set(f"Наибольшее напряжение при сжатии и изгибе составляет "
                                              f"{round(self.highest_stress, 1)} кг/см2")
                        self.allow_safity_value.set(f"Коэффициент запаса прочности "
                                                    f"составляет {round(self.allow_safity, 1)}")
















