import math
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook


class ThreadedConnect:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.draw_widgets()
        self.index = 1

    def draw_widgets(self):
        self.draw_label()
        self.draw_mpa_kgcm2_calc()
        self.draw_header()
        self.draw_formula_frame()
        self.draw_data_frame()

    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)

    def draw_mpa_kgcm2_calc(self):
        # МПа в кг/см2 конвертер
        self.mpa_kgcm2 = StringVar()
        self.mpa_calc_frame = Frame(self.root, bg="#3f2a1d")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#8c7462", fg="#24150e")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#8c7462", fg="#24150e")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#24150e",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        #self.mpa_calc_entry.insert(0, "0")
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#8e6248", fg="#f2ebe9", activebackground="#8c7462", relief=GROOVE,
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

    def draw_header(self):
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width=70, font=("GOST Type BU", 13, "bold"),
                                 text="Расчет коэффициента запаса по пластическим деформациям для резьбы.",
                                 bg="#715e4e", fg="#e4ebf2", justify=CENTER)

        self.header_frame.place(in_=self.label, x=340, y=45)
        self.header_calc.pack()

    def draw_formula_frame(self):
        self.formula_frame = LabelFrame(self.root, text=" Основные расчетные формулы  ",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#715e4e", fg="#e4ebf2")
        self.tabs_control = Notebook(self.formula_frame, height=190, width=629, padding=(0, 10, 0, 0))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="Растягивающее напряжение")
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Расчетная нагрузка")
        self.tab_3 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_3, text="Касательное напряжение")
        self.tab_4 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_4, text="Коэффициент запаса")
        self.formula_frame.place(in_=self.label, x=600, y=390)
        self.run_formula_frame()

    def run_formula_frame(self):
        self.tensile_stress_img = PhotoImage(file=r"Data\Tensile_stress_629x183.png")
        self.design_load_img = PhotoImage(file=r"Data\Design_load_629x183.png")
        self.shear_stress_img = PhotoImage(file=r"Data\Shear_stress_629x183.png")
        self.plastic_deform_img = PhotoImage(file=r"Data\Plastic_deform_629x183.png")

        self.tensile_stress_canvas = Canvas(self.tab_1, width=629, height=183, background="white")
        self.design_load_canvas = Canvas(self.tab_2, width=629, height=183, background="white")
        self.shear_stress_canvas = Canvas(self.tab_3, width=629, height=183, background="white")
        self.plastic_deform_canvas = Canvas(self.tab_4, width=629, height=183, background="white")

        self.tensile_stress_image = self.tensile_stress_canvas.create_image(0, 0, anchor='nw',
                                                                            image=self.tensile_stress_img)
        self.design_load_image = self.design_load_canvas.create_image(0, 0, anchor='nw', image=self.design_load_img)
        self.shear_stress_image = self.shear_stress_canvas.create_image(0, 0, anchor='nw', image=self.shear_stress_img)
        self.plastic_deform_image = self.plastic_deform_canvas.create_image(0, 0, anchor='nw',
                                                                            image=self.plastic_deform_img)

        self.tabs_control.pack(fill=BOTH, expand=1)
        self.tensile_stress_canvas.pack()
        self.design_load_canvas.pack()
        self.shear_stress_canvas.pack()
        self.plastic_deform_canvas.pack()


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

    def draw_data_frame(self):
        try:
            self.open_data_calc = open(r"Data\save_data\data_ThreadedConnect_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_ThreadedConnect_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_ThreadedConnect_calc.txt", "r")
        self.open_data_init()
        self.data_frame = LabelFrame(self.root, text=" Ввод данных для расчета  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#52733b", fg="#e4ebf2")
        self.pull_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                 text="Усилие, действующее на резьбовое соединение P, в кг", bg="#84a45a", fg="#715e4e")
        self.pull_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#704307",
                                 validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.groove_diam_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                       text="Диаметр проточки под резьбу d, в мм", bg="#84a45a", fg="#715e4e",
                                       justify=LEFT)
        self.groove_diam_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#704307",
                                       validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.bolt_outer_diam_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                           text="Наружный диаметр болта d0, в мм",
                                           bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.bolt_outer_diam_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                           fg="#704307", validate="key",
                                           validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.tigh_ratio_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                text="Коэффициент затяжки k", bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.tigh_ratio_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#704307",
                                validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.number_of_threads_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                             text="Кол-во резьбовых соединений, учавствующих в работе z",
                                             bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.number_of_threads_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#704307", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.friction_ratio_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                             text="Коэффициент зависящий от коэффициента по трению k1",
                                             bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.friction_ratio_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#704307", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                          text="Предел текучести материала σT, в кг/см2", bg="#84a45a", fg="#715e4e",
                                          justify=LEFT)
        self.yield_strength_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#704307",
                                          validate="key",
                                          validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.connect_calc_btn = Button(self.data_frame, text="Расчет",
                                       font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#818a6f",
                                       fg="#e4ebf2", activebackground="#e0a96d",
                                       relief=GROOVE, bd=3, command=self.threaded_connect_calc)
        self.all_clear_btn = Button(self.data_frame, text="Очистить",
                                       font=("GOST Type BU", 11, "bold"), width=10, height=1, bg="#818a6f",
                                       fg="#e4ebf2", activebackground="#e0a96d",
                                       relief=GROOVE, bd=3, command=self.all_clear)

        if len(self.open_data) == 7:
            self.pull_entry.insert(0, f"{self.open_data[0]}")
            self.groove_diam_entry.insert(0, f"{self.open_data[1]}")
            self.bolt_outer_diam_entry.insert(0, f"{self.open_data[2]}")
            self.tigh_ratio_entry.insert(0, f"{self.open_data[3]}")
            self.number_of_threads_entry.insert(0, f"{self.open_data[4]}")
            self.friction_ratio_entry.insert(0, f"{self.open_data[5]}")
            self.yield_strength_entry.insert(0, f"{self.open_data[6]}")



        self.data_frame.place(in_=self.label, x=50, y=90)
        self.pull_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.pull_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.groove_diam_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.groove_diam_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.bolt_outer_diam_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.bolt_outer_diam_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.tigh_ratio_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.tigh_ratio_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.number_of_threads_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.number_of_threads_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W)
        self.friction_ratio_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        self.friction_ratio_entry.grid(row=6, column=1, padx=10, pady=2, sticky=W)
        self.yield_strength_label.grid(row=7, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry.grid(row=7, column=1, padx=10, pady=2, sticky=W)
        self.connect_calc_btn.grid(row=8, column=1, padx=(0, 10), pady=5, sticky=W + S)
        self.all_clear_btn.grid(row=8, column=0, padx=(0, 15), pady=5, sticky=E + S)

    def all_clear(self):
        self.pull_entry.delete(0, END)
        self.groove_diam_entry.delete(0, END)
        self.bolt_outer_diam_entry.delete(0, END)
        self.number_of_threads_entry.delete(0, END)
        self.yield_strength_entry.delete(0, END)


    def output(self):
        self.design_load_value = StringVar()
        self.tensile_stress_value = StringVar()
        self.reduced_stress_value = StringVar()
        self.plastic_deform_value = StringVar()
        self.output_frame = LabelFrame(self.root, text=" Результаты расчета ",
                                 font=("GOST Type BU", 11, "bold", "italic"), bg="#52733b", fg="#e4ebf2")
        self.design_load_label = Label(self.output_frame, width=40, height=1, font=("GOST Type BU", 11, "bold"),
                                          textvariable=self.design_load_value, bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.tensile_stress_label = Label(self.output_frame, width=40, height=2, font=("GOST Type BU", 11, "bold"),
                                textvariable=self.tensile_stress_value, bg="#84a45a", fg="#715e4e", justify=LEFT)
        self.reduced_stress_label = Label(self.output_frame, width=40, height=2, font=("GOST Type BU", 11, "bold"),
                                          textvariable=self.reduced_stress_value, bg="#84a45a", fg="#715e4e",
                                          justify=LEFT)
        self.plastic_deform_label = Label(self.output_frame, width=40, height=2, font=("GOST Type BU", 11, "bold"),
                                          textvariable=self.plastic_deform_value, bg="#84a45a", fg="#715e4e",
                                          justify=LEFT)
        self.result_frame = Frame(self.output_frame, bg="#84a45a")
        self.plastic_deform_result_label = Label(self.result_frame, width=40, height=2,
                                                 font=("GOST Type BU", 11, "bold"),
                                                 text="Вхождение коэффициента в необходимый\nинтервал "
                                                      "значений от 1.2 до 2.5: ", bg="#84a45a", fg="#715e4e",
                                                 justify=LEFT)
        self.output_frame.place(in_=self.label, x=766, y=90)
        self.result_frame.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.plastic_deform_result_label.grid(row=1, column=0, padx=0, pady=2, sticky=W)

    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

    def threaded_connect_calc(self):
        flag = True
        try:
            self.pull = float(self.pull_entry.get())
            self.groove_diam = float(self.groove_diam_entry.get()) / 10
            self.bolt_outer_diam = float(self.bolt_outer_diam_entry.get()) / 10
            self.tigh_ratio = float(self.tigh_ratio_entry.get())
            self.number_of_threads = float(self.number_of_threads_entry.get())
            self.friction_ratio = float(self.friction_ratio_entry.get())
            self.yield_strength = float(self.yield_strength_entry.get())
        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены,"
                                      f" или введено недопустимое значение")
            self.output_frame.destroy()
        if flag:
            self.output()
            try:
                self.design_load = self.tigh_ratio * self.pull
                self.tensile_stress = (4 * self.design_load) / (math.pi * math.pow(self.groove_diam, 2)
                                                                * self.number_of_threads)
                self.shear_stress = (self.design_load * self.bolt_outer_diam * self.friction_ratio) \
                                    / (0.2 * math.pow(self.groove_diam, 3))
                self.reduced_stress = math.sqrt((math.pow(self.tensile_stress, 2) + 3 * math.pow(self.shear_stress, 2)))
                self.plastic_deform = self.yield_strength / self.reduced_stress

            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.output_frame.destroy()
            if flag:
                self.save_data_calc = open(r"Data\save_data\data_ThreadedConnect_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.pull) + "\n")
                self.save_data_calc.write(str(self.groove_diam * 10) + "\n")
                self.save_data_calc.write(str(self.bolt_outer_diam * 10) + "\n")
                self.save_data_calc.write(str(self.tigh_ratio) + "\n")
                self.save_data_calc.write(str(self.number_of_threads) + "\n")
                self.save_data_calc.write(str(self.friction_ratio) + "\n")
                self.save_data_calc.write(str(self.yield_strength))
                self.save_data_calc.close()

                # Вывод
                self.design_load_value.set(f"Расчетная нагрузка равна {round(self.design_load, 2)} кг")
                self.design_load_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
                self.tensile_stress_value.set(f"Растягивающее напряжение σ в резьбе\nстержня равно "
                                              f"{round(self.tensile_stress, 2)} кг/см2")
                self.tensile_stress_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
                self.reduced_stress_value.set(f"Наибольшее касательное напряжение τ\n"
                                              f"в резьбе равно {round(self.reduced_stress, 2)} кг/см2")
                self.reduced_stress_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
                self.plastic_deform_value.set(f"Коэффициент запаса по пластическим\n"
                                              f"деформациям равен {round(self.plastic_deform, 2)}")
                self.plastic_deform_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)


                if self.plastic_deform < 1.2:
                    self.not_allowed_canvas = Canvas(self.result_frame, width=130, height=20, bg="#84a45a")
                    self.not_allowed_canvas.create_rectangle(3, 3, 130, 20, outline="red", width="3")
                    self.not_allowed_canvas.create_text(65, 12, text="НЕ В ДОПУСКЕ", font=("GOST Type BU", 11),
                                                        fill="red")

                    self.not_allowed_canvas.grid(row=2, column=0, padx=(15, 0), pady=0, sticky=N+W)

                elif self.plastic_deform > 1.2 and self.plastic_deform < 2.5:
                    self.allowed_canvas = Canvas(self.result_frame, width=170, height=20, bg="#84a45a")
                    self.allowed_canvas.create_rectangle(3, 3, 170, 20, outline="#52733b", width="3")
                    self.allowed_canvas.create_text(85, 12, text="Оптимально в допуке",
                                                    font=("GOST Type BU", 11, "bold", "italic"), fill="#52733b")

                    self.allowed_canvas.grid(row=2, column=0, padx=(15, 0), pady=0, sticky=N + W)

                else:
                    self.very_allowed_canvas = Canvas(self.result_frame, width=170, height=20, bg="#84a45a")
                    self.very_allowed_canvas.create_rectangle(3, 3, 170, 20, outline="#52733b", width="3")
                    self.very_allowed_canvas.create_text(85, 12, text="В допуке с запасом",
                                                         font=("GOST Type BU", 11, "bold", "italic"), fill="#52733b")

                    self.very_allowed_canvas.grid(row=2, column=0, padx=(15, 0), pady=0, sticky=N + W)


    # def draw_formula_frame(self):
    #     self.formula_frame = LabelFrame(self.root, text=" Основные расчетные формулы",
    #                                     font=("GOST Type BU", 11, "italic", "bold"), bg="#715e4e", fg="#e4ebf2")
    #     self.formula_canvas = Canvas(self.formula_frame, width=629, height=183, background="white")
    #     self.formula_photo = PhotoImage(file=r"Data\Tensile_stress_629x183.png")
    #     self.formula_image = self.formula_canvas.create_image(0, 0, anchor='nw', image=self.formula_photo)
    #     self.left_scroll_image_btn = Button(self.root, text="", font=("GOST Type BU", 11, "bold"), width=2, height=0,
    #                                         bg="#e4ebf2", fg="#818a6f", activebackground="#e0a96d",
    #                                         relief=GROOVE, bd=3, command=self.scroll_left)
    #     self.right_scroll_image_btn = Button(self.root, text="", font=("GOST Type BU", 11, "bold"), width=2, height=0,
    #                                          bg="#e4ebf2", fg="#818a6f", activebackground="#e0a96d",
    #                                          relief=GROOVE, bd=3, command=self.scroll_right)
    #
    #     self.formula_frame.place(in_=self.label, x=600, y=400)
    #     self.formula_canvas.pack()
    #     self.left_scroll_image_btn.place(in_=self.label, x=1100, y=360)
    #     self.right_scroll_image_btn.place(in_=self.label, x=1140, y=360)
    #
    # def scroll_left(self):
    #     self.index -= 1
    #     if self.index < 1:
    #         self.index = 4
    #     index = self.index
    #     self.scrolling_img(index)
    #
    #
    # def scroll_right(self):
    #     self.index += 1
    #     if self.index > 4:
    #         self.index = 1
    #     index = self.index
    #     self.scrolling_img(index)
    #
    # def scrolling_img(self, index):
    #     self.tensile_stress_img = PhotoImage(file=r"Data\Tensile_stress_629x183.png")
    #     self.design_load_img = PhotoImage(file=r"Data\Design_load_629x183.png")
    #     self.shear_stress_img = PhotoImage(file=r"Data\Shear_stress_629x183.png")
    #     self.plastic_deform_img = PhotoImage(file=r"Data\Plastic_deform_629x183.png")
    #     self.scroll_images = {1: self.tensile_stress_img, 2: self.design_load_img, 3: self.shear_stress_img,
    #                           4: self.plastic_deform_img}
    #     self.formula_photo = self.scroll_images.get(index)
    #     self.formula_image = self.formula_canvas.create_image(0, 0, anchor='nw', image=self.formula_photo)
    #     self.formula_canvas.grid(row=1, column=0)





