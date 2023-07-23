import math
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image as PilImage
from PIL import ImageTk
from tkinter.ttk import Notebook



class Ear:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.draw_widgets()
        self.index = 1
        back_img = PilImage.open(r"Data\back_ear.png")
        back_img = back_img.resize((32, 32), PilImage.ANTIALIAS)
        self.photo_back_image = ImageTk.PhotoImage(back_img)


    def draw_widgets(self):
        self.draw_label()
        self.draw_header(header_text= " Расчет проушины ", w_number= 20, h_number= 1, x_coord=540)
        self.draw_scheme_choice()

    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)

    def draw_mpa_kgcm2_calc(self):
        # МПа в кг/см2 конвертер
        self.mpa_kgcm2 = StringVar()
        self.mpa_calc_frame = Frame(self.root, bg="#2a3457")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#16235a", fg="#a4a4bf")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#a4a4bf", fg="#2a3457")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#583e2e",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#888c46", fg="#f2eaed", activebackground="#bf988f", relief=GROOVE,
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

    def draw_header(self, header_text, w_number, h_number, x_coord):
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width= w_number, height= h_number, text= header_text,
                                 font=("GOST Type BU", 13, "bold"), bg="#9199be", fg="#212624", justify=CENTER)

        self.header_frame.place(in_=self.label, x=x_coord, y=45)
        self.header_calc.pack()

    def draw_scheme_choice(self):
        self.choice_frame = Frame(self.root, bg="#e0a96d")
        self.scheme_choice_label = Label(self.choice_frame, width=72, font=("GOST Type BU", 11, "bold"),
                                 text=" Выберите схему нагружения проушины.\n"
                                      "Нагружение по схеме б и в отражает наличие зазора в проушине,\n"
                                      "на этих схемах давление не распределено равномерно по диаметру,\n"
                                      "а приложено в виде сосредоточенной силы в двух и в одной точке.",
                                 bg="#9199be", fg="#212624", justify=CENTER)

        self.choice_scheme_frame = Frame(self.root, bg="#6c6b74")
        scheme_A = PilImage.open(f"Data\Cxema_A_570x570.png")
        scheme_B = PilImage.open(f"Data\Cxema_B_570x570.png")
        scheme_C = PilImage.open(f"Data\Cxema_C_570x570.png")
        scheme_A = scheme_A.resize((200, 200), PilImage.ANTIALIAS)
        scheme_B = scheme_B.resize((200, 200), PilImage.ANTIALIAS)
        scheme_C = scheme_C.resize((200, 200), PilImage.ANTIALIAS)
        self.photo_scheme_A = ImageTk.PhotoImage(scheme_A)
        self.photo_scheme_B = ImageTk.PhotoImage(scheme_B)
        self.photo_scheme_C = ImageTk.PhotoImage(scheme_C)
        self.scheme_A_btn = Button(self.choice_scheme_frame, image=self.photo_scheme_A, bg="#2e303e",
                                activebackground="#ffc13b", command=self.start_scheme_A_calc)
        self.scheme_B_btn = Button(self.choice_scheme_frame, image=self.photo_scheme_B, bg="#2e303e",
                                activebackground="#ffc13b", command=self.start_scheme_B_calc)
        self.scheme_C_btn = Button(self.choice_scheme_frame, image=self.photo_scheme_C, bg="#2e303e",
                                activebackground="#ffc13b", command=self.start_scheme_C_calc)

        self.choice_frame.place(in_=self.label, x=345, y=132)
        self.scheme_choice_label.pack()

        self.choice_scheme_frame.place(in_=self.label, x=300, y=210)
        self.scheme_A_btn.grid(row=1, column=0, padx=(15, 5), pady=10, sticky=W)
        self.scheme_B_btn.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        self.scheme_C_btn.grid(row=1, column=2, padx=(5, 15), pady=10, sticky=W)



    def start_scheme_A_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_mpa_kgcm2_calc()
        self.draw_header(header_text= "Расчет проушины по формуле Ляме.\nСхема нагружения \"а\"", w_number= 40,
                         h_number=2, x_coord=480)
        self.draw_formula_scheme_A_frame()
        self.draw_data_frame_scheme_A()


    def start_scheme_B_calc(self):
        self.label.destroy()
        self.draw_label()
        self.draw_mpa_kgcm2_calc()
        self.draw_header(header_text= "Расчет проушины.\nСхема нагружения \"б\"", w_number= 30, h_number= 2,
                         x_coord=500)
        self.draw_formula_scheme_B_frame()
        self.draw_scheme_B_frame()
        self.draw_data_frame_scheme_B()

    def draw_scheme_B_frame(self):
        self.scheme_B_frame = LabelFrame(self.root, text=" Схема расчета ",
                                                 font=("GOST Type BU", 11, "italic", "bold"), bg="#9199be",
                                                 fg="#212624")
        self.scheme_B_img = PhotoImage(file=r"Data\Cxema_D_306x292.png")
        self.scheme_B_label = Label(self.scheme_B_frame, image=self.scheme_B_img)
        self.scheme_B_label.image = self.scheme_B_img

        self.scheme_B_frame.place(in_=self.label, x=1002, y=50)
        self.scheme_B_label.grid(row=1, column=1, padx=10, pady=4, sticky=W)

    def start_scheme_C_calc(self):
        mb.showinfo(f"Уведомление", f"Не наш случай.\nМожно расчитать по схеме б")



    def draw_formula_scheme_A_frame(self):
        self.formula_scheme_A_frame = LabelFrame(self.root, text=" Основная расчетная формула (формула Ляме) ",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#9199be", fg="#212624")
        self.formula_scheme_A_img = PhotoImage(file=r"Data\ear_stress_620x250.png")
        self.formula_scheme_A_label = Label(self.formula_scheme_A_frame, image=self.formula_scheme_A_img)
        self.formula_scheme_A_label.image = self.formula_scheme_A_img

        self.formula_scheme_A_frame.place(in_=self.label, x=610, y=350)
        self.formula_scheme_A_label.pack(side=LEFT)


    def draw_formula_scheme_B_frame(self):
        self.formula_scheme_B_frame = LabelFrame(self.root, text=" Основные расчетные формулы ",
                                                 font=("GOST Type BU", 11, "italic", "bold"), bg="#9199be",
                                                 fg="#212624")
        self.tabs_control = Notebook(self.formula_scheme_B_frame, height=292, width=512, padding=(5, 10, 5, 0))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="Изгибающий момент")
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Напряжение в поперечных сечениях")
        self.formula_scheme_B_frame.place(in_=self.label, x=720, y=292)
        self.run_formula_frame()

    def run_formula_frame(self):
        self.izgib_moment_img = PhotoImage(file=r"Data\Izgib_moment_512x292.png")
        self.surface_stress_img = PhotoImage(file=r"Data\surface_stress_512x292.png")

        self.izgib_moment_canvas = Canvas(self.tab_1, width=512, height=292, background="white")
        self.surface_stress_canvas = Canvas(self.tab_2, width=512, height=292, background="white")

        self.usilie_image = self.izgib_moment_canvas.create_image(0, 0, anchor='nw',
                                                                image=self.izgib_moment_img)
        self.friction_image = self.surface_stress_canvas.create_image(0, 0, anchor='nw',
                                                                    image=self.surface_stress_img)

        self.tabs_control.pack(fill=BOTH, expand=1)
        self.izgib_moment_canvas.pack()
        self.surface_stress_canvas.pack()


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


    def draw_data_frame_scheme_A(self):
        try:
            self.open_data_calc = open(r"Data\save_data\dataA_ear_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\dataA_ear_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\dataA_ear_calc.txt", "r")
        self.open_data_init()
        self.data_frame_A = LabelFrame(self.root, text=" Ввод данных и расчет  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#54678f", fg="#9199be")
        self.pull_label_A = Label(self.data_frame_A, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                 text="Усилие, действующее на проушину P, в кг", bg="#9199be", fg="#212624")
        self.pull_entry_A = Entry(self.data_frame_A, width=8, font=("GOST Type BU", 11), bg="white", fg="#2e303e",
                                 validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.lug_width_label_A = Label(self.data_frame_A, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                     text="Ширина проушины b, в мм", bg="#9199be", fg="#212624")
        self.lug_width_entry_A = Entry(self.data_frame_A, width=8, font=("GOST Type BU", 11), bg="white", fg="#2e303e",
                                     validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.lug_inside_radius_label_A = Label(self.data_frame_A, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                     text="Внутренний радиус проушины R1, в мм", bg="#9199be", fg="#212624")
        self.lug_inside_radius_entry_A = Entry(self.data_frame_A, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#2e303e", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.lug_outer_radius_label_A = Label(self.data_frame_A, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                             text="Наружний радиус проушины R2, в мм", bg="#9199be", fg="#212624")
        self.lug_outer_radius_entry_A = Entry(self.data_frame_A, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#2e303e", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label_A = Label(self.data_frame_A, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                          text="Предел текучести материала σT, в кг/см2", bg="#9199be", fg="#212624",
                                          justify=LEFT)
        self.yield_strength_entry_A = Entry(self.data_frame_A, width=8, font=("GOST Type BU", 11), bg="white", fg="#212624",
                                          validate="key",
                                          validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.ear_calc_btn_A = Button(self.data_frame_A, text="Расчет",
                                       font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#9199be",
                                       fg="#212624", activebackground="#e0a96d",
                                       relief=GROOVE, bd=3, command=self.ear_calc_scheme_A)
        self.all_clear_btn = Button(self.data_frame_A, text="Очистить",
                                     font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#9199be",
                                     fg="#212624", activebackground="#e0a96d",
                                     relief=GROOVE, bd=3, command=self.all_clear_A)
        self.back_choice_scheme_A_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                               text=" Вернуться к выбору\nсхем нагружения",
                                               font=("GOST Type BU", 11, "bold"), width=200, height=40, bg="#888c46",
                                               fg="#f2eaed", activebackground="#e0a96d",
                                               relief=GROOVE, bd=3, command=self.back_choice_scheme)
        if len(self.open_data) == 5:
            self.pull_entry_A.insert(0, f"{self.open_data[0]}")
            self.lug_width_entry_A.insert(0, f"{self.open_data[1]}")
            self.lug_inside_radius_entry_A.insert(0, f"{self.open_data[2]}")
            self.lug_outer_radius_entry_A.insert(0, f"{self.open_data[3]}")
            self.yield_strength_entry_A.insert(0, f"{self.open_data[4]}")

        self.data_frame_A.place(in_=self.label, x=50, y=100)
        self.pull_label_A.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.pull_entry_A.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.lug_width_label_A.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.lug_width_entry_A.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.lug_inside_radius_label_A.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.lug_inside_radius_entry_A.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.lug_outer_radius_label_A.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.lug_outer_radius_entry_A.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.yield_strength_label_A.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry_A.grid(row=5, column=1, padx=10, pady=2, sticky=W)
        self.ear_calc_btn_A.grid(row=6, column=1, padx=(0, 10), pady=5, sticky=W + S)
        self.all_clear_btn.grid(row=6, column=0, padx=(0, 15), pady=5, sticky=E + S)
        self.back_choice_scheme_A_btn.place(in_=self.label, x=50, y=40)

    def all_clear_A(self):
        self.pull_entry_A.delete(0, END)
        self.lug_width_entry_A.delete(0, END)
        self.lug_inside_radius_entry_A.delete(0, END)
        self.lug_outer_radius_entry_A.delete(0, END)
        self.yield_strength_entry_A.delete(0, END)

    def draw_data_frame_scheme_B(self):
        try:
            self.open_data_calc = open(r"Data\save_data\dataB_ear_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\dataB_ear_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\dataB_ear_calc.txt", "r")
        self.open_data_init()
        self.data_frame_B = LabelFrame(self.root, text=" Ввод данных и расчет  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#54678f", fg="#9199be")
        self.pull_label_B = Label(self.data_frame_B, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                text="Усилие, действующее на проушину P, в кг", bg="#9199be", fg="#212624")
        self.pull_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white", fg="#2e303e",
                                validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))

        self.lug_inside_radius_label_B = Label(self.data_frame_B, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                             text="Внутренний радиус проушины R1, в мм", bg="#9199be", fg="#212624")
        self.lug_inside_radius_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#2e303e", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))

        self.lug_outer_radius_label_B = Label(self.data_frame_B, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                            text="Наружний радиус проушины R2, в мм", bg="#9199be", fg="#212624")
        self.lug_outer_radius_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white",
                                            fg="#2e303e", validate="key",
                                            validatecommand=(self.root.register(self.validate_amount), "%S"))


        self.lug_width_label_B = Label(self.data_frame_B, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                       text="Ширина проушины b, в мм", bg="#9199be", fg="#212624")
        self.lug_width_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white", fg="#2e303e",
                                       validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))

        self.alpha_angle_label_B = Label(self.data_frame_B, width=50, height=1, font=("GOST Type BU", 11, "bold"),
                                         text="Угол альфа в градусах", bg="#9199be", fg="#212624")
        self.alpha_angle_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white",
                                         fg="#2e303e", validate="key",
                                         validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label_B = Label(self.data_frame_B, width=50, height=1,
                                            font=("GOST Type BU", 11, "bold"),
                                            text="Предел текучести материала σT, в кг/см2", bg="#9199be", fg="#212624",
                                            justify=LEFT)
        self.yield_strength_entry_B = Entry(self.data_frame_B, width=8, font=("GOST Type BU", 11), bg="white",
                                            fg="#212624",
                                            validate="key",
                                            validatecommand=(self.root.register(self.validate_amount), "%S"))

        self.ear_calc_btn_B = Button(self.data_frame_B, text="Расчет",
                                     font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#9199be",
                                     fg="#212624", activebackground="#e0a96d",
                                     relief=GROOVE, bd=3, command=self.ear_calc_scheme_B)
        self.all_clear_btn = Button(self.data_frame_B, text="Очистить",
                                         font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#9199be",
                                         fg="#212624", activebackground="#e0a96d",
                                         relief=GROOVE, bd=3, command=self.all_clear_B)
        self.back_choice_scheme_B_btn = Button(self.root, image=self.photo_back_image, compound=LEFT,
                                               text=" Вернуться к выбору\nсхем нагружения",
                                               font=("GOST Type BU", 11, "bold"), width=200, height=40, bg="#888c46",
                                               fg="#f2eaed", activebackground="#e0a96d",
                                               relief=GROOVE, bd=3, command=self.back_choice_scheme)

        if len(self.open_data) == 6:
            self.pull_entry_B.insert(0, f"{self.open_data[0]}")
            self.lug_inside_radius_entry_B.insert(0, f"{self.open_data[1]}")
            self.lug_outer_radius_entry_B.insert(0, f"{self.open_data[2]}")
            self.lug_width_entry_B.insert(0, f"{self.open_data[3]}")
            self.alpha_angle_entry_B.insert(0, f"{self.open_data[4]}")
            self.yield_strength_entry_B.insert(0, f"{self.open_data[5]}")


        self.data_frame_B.place(in_=self.label, x=50, y=100)
        self.back_choice_scheme_B_btn.place(in_=self.label, x=50, y=40)
        self.pull_label_B.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.pull_entry_B.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.lug_inside_radius_label_B.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.lug_inside_radius_entry_B.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.lug_outer_radius_label_B.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.lug_outer_radius_entry_B.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.lug_width_label_B.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.lug_width_entry_B.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.alpha_angle_label_B.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.alpha_angle_entry_B.grid(row=5, column=1, padx=(10, 15), pady=2, sticky=W)
        self.yield_strength_label_B.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry_B.grid(row=6, column=1, padx=10, pady=2, sticky=W)
        self.ear_calc_btn_B.grid(row=7, column=1, padx=(0, 10), pady=5, sticky=W+S)
        self.all_clear_btn.grid(row=7, column=0, padx=(0, 15), pady=5, sticky=E+S)


    def all_clear_B(self):
        self.pull_entry_B.delete(0, END)
        self.lug_inside_radius_entry_B.delete(0, END)
        self.lug_outer_radius_entry_B.delete(0, END)
        self.lug_width_entry_B.delete(0, END)
        self.alpha_angle_entry_B.delete(0, END)
        self.yield_strength_entry_B.delete(0, END)


    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

    def output_A(self):
        self.stress_A_value = StringVar()
        self.safity_factor_A_value = StringVar()
        self.output_A_frame = LabelFrame(self.root, text=" Результаты расчета ",
                                 font=("GOST Type BU", 11, "bold", "italic"), bg="#54678f", fg="#9199be")
        self.stress_label = Label(self.output_A_frame, width=58, height=2, font=("GOST Type BU", 11, "bold"),
                                  textvariable=self.stress_A_value, bg="#9199be", fg="#212624", justify=LEFT)
        self.safity_factor_label = Label(self.output_A_frame, width=58, height=2, font=("GOST Type BU", 11, "bold"),
                                  textvariable=self.safity_factor_A_value, bg="#9199be", fg="#212624", justify=LEFT)

        self.output_A_frame.place(in_=self.label, x=610, y=100)
        self.stress_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.safity_factor_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)


    def output_B(self):
        self.B_B_bending_moment_value_B = StringVar()
        self.A_A_bending_moment_value_B = StringVar()
        self.B_B_force_normal_value_B = StringVar()
        self.A_A_force_normal_value_B = StringVar()
        self.B_B_outer_surface_stress_B_value = StringVar()
        self.A_A_outer_surface_stress_B_value = StringVar()
        self.B_B_inner_surface_stress_B_value = StringVar()
        self.A_A_inner_surface_stress_B_value = StringVar()
        self.safity_factor_B_value = StringVar()

        self.output_B_frame = LabelFrame(self.root, text=" Результат вычислений ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#54678f", fg="#9199be")
        self.A_A_frame = Frame(self.output_B_frame, bg="#54678f")
        self.B_B_frame = Frame(self.output_B_frame, bg="#54678f")
        self.A_A_force_normal_B_label = Label(self.A_A_frame, width=38, height=2,
                                              font=("GOST Type BU", 11, "bold"),
                                              textvariable=self.A_A_force_normal_value_B, bg="#9199be", fg="#212624",
                                              justify=LEFT)
        self.A_A_bending_moment_B_label = Label(self.A_A_frame, width=38, height=2,
                                                font=("GOST Type BU", 11, "bold"),
                                                textvariable=self.A_A_bending_moment_value_B, bg="#9199be",
                                                fg="#212624",
                                                justify=LEFT)
        self.A_A_inner_surface_stress_B_label = Label(self.A_A_frame, width=38, height=3,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      textvariable=self.A_A_inner_surface_stress_B_value, bg="#9199be",
                                                      fg="#212624",
                                                      justify=LEFT)
        self.A_A_outer_surface_stress_B_label = Label(self.A_A_frame, width=38, height=3,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      textvariable=self.A_A_outer_surface_stress_B_value, bg="#9199be",
                                                      fg="#212624",
                                                      justify=LEFT)

        self.B_B_force_normal_B_label = Label(self.B_B_frame, width=38, height=2,
                                              font=("GOST Type BU", 11, "bold"),
                                              textvariable=self.B_B_force_normal_value_B, bg="#9199be", fg="#212624",
                                              justify=LEFT)
        self.B_B_bending_moment_B_label = Label(self.B_B_frame, width=38, height=2,
                                                font=("GOST Type BU", 11, "bold"),
                                                textvariable=self.B_B_bending_moment_value_B, bg="#9199be",
                                                fg="#212624",
                                                justify=LEFT)
        self.B_B_inner_surface_stress_B_label = Label(self.B_B_frame, width=38, height=3,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      textvariable=self.B_B_inner_surface_stress_B_value, bg="#9199be",
                                                      fg="#212624",
                                                      justify=LEFT)
        self.B_B_outer_surface_stress_B_label = Label(self.B_B_frame, width=38, height=3,
                                                font=("GOST Type BU", 11, "bold"),
                                                textvariable=self.B_B_outer_surface_stress_B_value, bg="#9199be",
                                                fg="#212624",
                                                justify=LEFT)

        self.safity_factor_B_label = Label(self.output_B_frame, width=77, height=1,
                                                      font=("GOST Type BU", 11, "bold"),
                                                      textvariable=self.safity_factor_B_value, bg="#9199be",
                                                      fg="#212624",
                                                      justify=LEFT)


        self.output_B_frame.place(in_=self.label, x=50, y=350)
        self.A_A_frame.grid(row=1, column=0, padx=0, pady=(10, 0), sticky=W)
        self.A_A_force_normal_B_label.grid(row=1, column=0, padx=(10, 0), pady=2, sticky=W)
        self.A_A_bending_moment_B_label.grid(row=2, column=0, padx=(10, 0), pady=2, sticky=W)
        self.A_A_inner_surface_stress_B_label.grid(row=3, column=0, padx=(10, 0), pady=2, sticky=W)
        self.A_A_outer_surface_stress_B_label.grid(row=4, column=0, padx=(10, 0), pady=2, sticky=W)

        self.B_B_frame.grid(row=1, column=1, padx=0, pady=(10, 0), sticky=E)
        self.B_B_force_normal_B_label.grid(row=1, column=0, padx=(5, 10), pady=2, sticky=W)
        self.B_B_bending_moment_B_label.grid(row=2, column=0, padx=(5, 10), pady=2, sticky=W)
        self.B_B_inner_surface_stress_B_label.grid(row=3, column=0, padx=(5, 10), pady=2, sticky=W)
        self.B_B_outer_surface_stress_B_label.grid(row=4, column=0, padx=(5, 10), pady=2, sticky=W)

        self.safity_factor_B_label.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky=W)


    def ear_calc_scheme_A(self):
        flag = True
        try:
            self.pull_A = float(self.pull_entry_A.get())
            self.lug_width_A = float(self.lug_width_entry_A.get()) / 10
            self.lug_inside_radius_A = float(self.lug_inside_radius_entry_A.get()) / 10
            self.lug_outer_radius_A = float(self.lug_outer_radius_entry_A.get()) / 10
            self.yield_strength_A = float(self.yield_strength_entry_A.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены "
                                      f"или введено некорректное значение.")
            self.output_A_frame.destroy()

        if flag:
            self.output_A()
            try:
                self.hole_diam = 2 * self.lug_inside_radius_A
                self.stress_A = ((math.pow(self.lug_inside_radius_A, 2) + math.pow(self.lug_outer_radius_A, 2))
                                / (math.pow(self.lug_outer_radius_A, 2) - math.pow(self.lug_inside_radius_A, 2))) \
                                * (self.pull_A / (self.hole_diam * self.lug_width_A))
                self.stress_A_value.set(f"Наибольшее напряжение в проушине равно {round(self.stress_A, 4)} кг/см2")
                self.safity_factor_A = self.yield_strength_A / self.stress_A
                self.safity_factor_A_value.set(f"Коэффициент запаса по прочности {round(self.safity_factor_A, 1)}")
            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.output_A_frame.destroy()

            if flag:
                self.save_data_calc = open(r"Data\save_data\dataA_ear_calc.txt", "w")

                # Запись файлов
                self.save_data_calc.write(str(self.pull_A) + "\n")
                self.save_data_calc.write(str(self.lug_width_A * 10) + "\n")
                self.save_data_calc.write(str(self.lug_inside_radius_A * 10) + "\n")
                self.save_data_calc.write(str(self.lug_outer_radius_A * 10) + "\n")
                self.save_data_calc.write(str(self.yield_strength_A))
                self.save_data_calc.close()


    def ear_calc_scheme_B(self):
        flag = True
        try:
            self.pull_B = float(self.pull_entry_B.get())
            self.lug_inside_radius_B = float(self.lug_inside_radius_entry_B.get()) / 10
            self.lug_outer_radius_B = float(self.lug_outer_radius_entry_B.get()) / 10
            self.lug_width_B = float(self.lug_width_entry_B.get()) / 10
            self.alpha_angle_B = math.radians(float(self.alpha_angle_entry_B.get()))
            self.yield_strength_B = float(self.yield_strength_entry_B.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены "
                                      f"или введено некорректное значение.")
            self.output_B_frame.destroy()

        if flag:
            self.output_B()
            try:
                self.axis_radius_B = (self.lug_outer_radius_B - self.lug_inside_radius_B) / 2 + self.lug_inside_radius_B
                self.B_B_bending_moment_B = ((self.axis_radius_B * self.pull_B) / math.pi) * ((math.pi / 2) -
                          math.sin(self.alpha_angle_B) - math.cos(self.alpha_angle_B) *
                          ((math.pi / 2) - self.alpha_angle_B))
                self.A_A_bending_moment_B = - ((self.axis_radius_B * self.pull_B) / 2) \
                                            * (1 - math.cos(self.alpha_angle_B)) + self.B_B_bending_moment_B
                self.B_B_force_normal_B = self.pull_B / 2
                self.A_A_force_normal_B = 0
                self.lug_wall_thickness_B = self.lug_outer_radius_B - self.lug_inside_radius_B
                self.B_B_outer_surface_stress_B = (1 / (self.lug_width_B * self.lug_wall_thickness_B)) \
                                                  * ((2 * self.B_B_bending_moment_B)
                                                     * ((6 * self.axis_radius_B + self.lug_wall_thickness_B)
                                                        / (self.lug_wall_thickness_B
                                                           * (2 * self.axis_radius_B + self.lug_wall_thickness_B)))
                                                     + self.B_B_force_normal_B)

                self.A_A_outer_surface_stress_B = (1 / (self.lug_width_B * self.lug_wall_thickness_B)) \
                                                  * ((2 * self.A_A_bending_moment_B)
                                                     * ((6 * self.axis_radius_B + self.lug_wall_thickness_B)
                                                        / (self.lug_wall_thickness_B
                                                           * (2 * self.axis_radius_B + self.lug_wall_thickness_B)))
                                                     + self.A_A_force_normal_B)

                self.B_B_inner_surface_stress_B = (1 / (self.lug_width_B * self.lug_wall_thickness_B)) \
                                                  * (((-2) * self.B_B_bending_moment_B)
                                                     * ((6 * self.axis_radius_B - self.lug_wall_thickness_B)
                                                        / (self.lug_wall_thickness_B
                                                           * (2 * self.axis_radius_B - self.lug_wall_thickness_B)))
                                                     + self.B_B_force_normal_B)

                self.A_A_inner_surface_stress_B = (1 / (self.lug_width_B * self.lug_wall_thickness_B)) \
                                                  * (((-2) * self.A_A_bending_moment_B)
                                                     * ((6 * self.axis_radius_B - self.lug_wall_thickness_B)
                                                        / (self.lug_wall_thickness_B
                                                           * (2 * self.axis_radius_B - self.lug_wall_thickness_B)))
                                                     + self.A_A_force_normal_B)

                self.surface_stress_B = [abs(self.B_B_outer_surface_stress_B), abs(self.A_A_outer_surface_stress_B),
                                         abs(self.B_B_inner_surface_stress_B), abs(self.A_A_inner_surface_stress_B)]

                self.safity_factor_B = self.yield_strength_B / max(self.surface_stress_B)


            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.output_B_frame.destroy()

            if flag:
                self.save_data_calc = open(r"Data\save_data\dataB_ear_calc.txt", "w")

                # Запись файлов
                self.save_data_calc.write(str(self.pull_B) + "\n")
                self.save_data_calc.write(str(self.lug_inside_radius_B * 10) + "\n")
                self.save_data_calc.write(str(self.lug_outer_radius_B * 10) + "\n")
                self.save_data_calc.write(str(self.lug_width_B * 10) + "\n")
                self.save_data_calc.write(str(math.degrees(self.alpha_angle_B)) + "\n")
                self.save_data_calc.write(str(self.yield_strength_B))
                self.save_data_calc.close()
                self.B_B_bending_moment_value_B.set(f"Изгибающий момент в сечении В-В\nравен "
                                                    f"{round((self.B_B_bending_moment_B * 0.0980664999999998), 2)} Н*м "
                                                    f"({round(self.B_B_bending_moment_B, 2)} кг*см)")
                self.A_A_bending_moment_value_B.set(f"Изгибающий момент в сечении А-А\nравен "
                                                    f"{round((self.A_A_bending_moment_B * 0.0980664999999998), 2)} Н*м "
                                                    f"({round(self.A_A_bending_moment_B, 2)} кг*см)")
                self.B_B_force_normal_value_B.set(f"Сила нормальная к сечению В-В    \nравна "
                                                  f"{round(self.B_B_force_normal_B, 4)} кг")
                self.A_A_force_normal_value_B.set(f"Сила нормальная к сечению А-А    \nравна "
                                                  f"{self.A_A_force_normal_B} кг")
                self.B_B_outer_surface_stress_B_value.set(
                    f"Наибольшее напряжение наружней\nповерхности проушины в сечении\n"
                    f"В-В составляет {round(self.B_B_outer_surface_stress_B, 4)} кг/см2")
                self.A_A_outer_surface_stress_B_value.set(
                    f"Наибольшее напряжение наружней\nповерхности проушины в сечении\n"
                    f"А-А составляет {round(self.A_A_outer_surface_stress_B, 4)} кг/см2")
                self.B_B_inner_surface_stress_B_value.set(
                    f"Наибольшее напряжение внутренней\nповерхности проушины в сечении\n"
                    f"В-В составляет {round(self.B_B_inner_surface_stress_B, 4)} кг/см2")
                self.A_A_inner_surface_stress_B_value.set(
                    f"Наибольшее напряжение внутренней\nповерхности проушины в сечении\n"
                    f"А-А составляет {round(self.A_A_inner_surface_stress_B, 4)} кг/см2")
                self.safity_factor_B_value.set(f"Коэффициент запаса прочности для введенных параметров "
                                               f"составляет: {round(self.safity_factor_B, 1)}")



    def back_choice_scheme(self):
        self.label.destroy()
        self.draw_widgets()























