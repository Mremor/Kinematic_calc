import math
from tkinter import *
from tkinter import messagebox as mb


class BottomThickness:
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
        self.mpa_calc_frame = Frame(self.root, bg="#d9ac2a")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#d8d583", fg="#720017")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#d8d583", fg="#720017")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#763f02",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#720017", fg="#d8d583", activebackground="#8c7462", relief=GROOVE,
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
        self.header_calc = Label(self.header_frame, width=40, font=("GOST Type BU", 13, "bold"),
                                 text=" Расчет толщины днища гидроцилиндра ",
                                 bg="#423a01", fg="#f4d993", justify=CENTER)

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

    def draw_formula_frame(self):
        self.formula_frame = LabelFrame(self.root, text=" Расчетная формула",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#704404", fg="#f2ece1")
        self.formula_img = PhotoImage(file=r"Data\bottom_thickness_575x292.png")
        self.formula_label = Label(self.formula_frame, image=self.formula_img)
        self.formula_label.image = self.formula_img

        self.fig_img = PhotoImage(file=r"Data\hydra_bottom_250x292.png")
        self.fig_label = Label(self.formula_frame, image=self.fig_img)
        self.fig_label.image = self.fig_img

        self.formula_frame.place(in_=self.label, x=50, y=310)
        self.formula_label.grid(row=1, column=0, padx=(15, 0), pady=(2, 4), sticky=W)
        self.fig_label.grid(row=1, column=1, padx=(0, 15), pady=(2, 4), sticky=W)

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
            self.open_data_calc = open(r"Data\save_data\data_BottomThickness_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_BottomThickness_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_BottomThickness_calc.txt", "r")
        self.open_data_init()
        self.data_frame = LabelFrame(self.root, text=" Ввод данных для расчета  ",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#776B04", fg="#f2ece1")
        self.press_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                text="Рабочее давление жидкости p, в кг/см2", bg="#f4d993", fg="#423a01")
        self.press_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#423a01",
                                validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.bottom_inner_diam_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                text="Внутренний диаметр днища d, в мм", bg="#f4d993", fg="#423a01")
        self.bottom_inner_diam_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#423a01", validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label = Label(self.data_frame, width=54, height=1,
                                            font=("GOST Type BU", 11, "bold"),
                                            text="Предел текучести материала σT, в кг/см2", bg="#f4d993", fg="#423a01",
                                            justify=LEFT)
        self.yield_strength_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                            fg="#423a01",
                                            validate="key",
                                            validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.safity_factor_label = Label(self.data_frame, width=54, height=1, font=("GOST Type BU", 11, "bold"),
                                             text="Коэффициент запаса прочности n", bg="#f4d993", fg="#423a01")
        self.safity_factor_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                             fg="#423a01",
                                             validate="key",
                                             validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.thickness_calc_btn = Button(self.data_frame, text="Расчет", font=("GOST Type BU", 11, "bold"),
                                    width=10, bg="#423a01", fg="#f4d993", activebackground="#e0a96d", relief=GROOVE,
                                    command=self.thickness_calc)
        self.all_clear_btn = Button(self.data_frame, text="Очистить", font=("GOST Type BU", 11, "bold"),
                                         width=10, bg="#423a01", fg="#f4d993", activebackground="#e0a96d",
                                         relief=GROOVE,
                                         command=self.all_clear)

        if len(self.open_data) == 4:
            self.press_entry.insert(0, f"{self.open_data[0]}")
            self.bottom_inner_diam_entry.insert(0, f"{self.open_data[1]}")
            self.yield_strength_entry.insert(0, f"{self.open_data[2]}")
            self.safity_factor_entry.insert(0, f"{self.open_data[3]}")


        self.data_frame.place(in_=self.label, x=50, y=100)
        self.press_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.press_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.bottom_inner_diam_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.bottom_inner_diam_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.yield_strength_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.safity_factor_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.safity_factor_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.thickness_calc_btn.grid(row=5, column=1, padx=(0, 10), pady=5, sticky=W + S)
        self.all_clear_btn.grid(row=5, column=0, padx=(0, 15), pady=5, sticky=E + S)

    def all_clear(self):
        self.press_entry.delete(0, END)
        self.bottom_inner_diam_entry.delete(0, END)
        self.yield_strength_entry.delete(0, END)
        self.safity_factor_entry.delete(0, END)

    def thickness_calc(self):
        flag = True
        try:
            self.press = float(self.press_entry.get())
            self.bottom_inner_diam = float(self.bottom_inner_diam_entry.get()) / 10
            self.yield_strength = float(self.yield_strength_entry.get())
            self.safity_factor = float(self.safity_factor_entry.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            self.output_frame.destroy()
        if flag:
            self.output()
            try:
                self.allow_stress = self.yield_strength / self.safity_factor
                self.bottom_thickness = 0.433 * self.bottom_inner_diam * math.sqrt((self.press / self.allow_stress))

            except ZeroDivisionError:
                flag = False
                mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
                self.output_frame.destroy()
            if flag:
                self.save_data_calc = open(r"Data\save_data\data_BottomThickness_calc.txt", "w")

                # Запись
                self.save_data_calc.write(str(self.press) + "\n")
                self.save_data_calc.write(str(self.bottom_inner_diam * 10) + "\n")
                self.save_data_calc.write(str(self.yield_strength) + "\n")
                self.save_data_calc.write(str(self.safity_factor))
                self.save_data_calc.close()

                self.bottom_thickness_value.set(f"Толщина днища равна:\n{round((self.bottom_thickness * 10), 3)} мм")



    def output(self):
        self.bottom_thickness_value = StringVar()
        self.output_frame = LabelFrame(self.root, text=" Результат расчета ",
                                         font=("GOST Type BU", 11, "bold", "italic"), bg="#776B04", fg="#f2ece1")
        self.bottom_thickness_label = Label(self.output_frame, width=31, height=2, font=("GOST Type BU", 11, "bold"),
                                  textvariable=self.bottom_thickness_value, bg="#f4d993", fg="#423a01", justify=CENTER)

        self.output_frame.place(in_=self.label, x=630, y=100)
        self.bottom_thickness_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)






