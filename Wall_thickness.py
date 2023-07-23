from tkinter import *
from tkinter import messagebox as mb

from Wall_thickness_calc import WallThicknessCalc


class WallThickness:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.draw_widgets()


    def draw_widgets(self):
        self.draw_label()
        self.draw_header()
        self.draw_mpa_kgcm2_calc()
        self.draw_formula_frame()
        self.draw_medium_wall_formula_frame()
        self.draw_fat_wall_formula_frame()
        self.draw_thin_wall_formula_frame()
        self.draw_mech_properties_stali()
        self.draw_data_frame()


    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)

    def draw_header(self):
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width=35, font=("GOST Type BU", 13, "bold"),
                                    text="Расчет толщины стенки гильзы.",
                                    bg="#594346", fg="#f22f08", justify=CENTER)

        self.header_frame.place(in_=self.label, x=470, y=45)
        self.header_calc.pack()

    def draw_formula_frame(self):
        self.formula_frame = LabelFrame(self.root, text=" Формула распределения",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#561e18", fg="#f22f08")
        self.formula_canvas = Canvas(self.formula_frame, width=390, height=90, background="white")
        self.formula_photo = PhotoImage(file=r"Data\formula_raspred_390x90.png")
        self.form_image = self.formula_canvas.create_image(0, 0, anchor='nw', image=self.formula_photo)

        self.formula_frame.place(in_=self.label, x=740, y=90)
        self.formula_canvas.pack()

    def draw_medium_wall_formula_frame(self):
        self.medium_wall_formula_frame = LabelFrame(self.root, text=" Формула расчета толщины стенки по нормам ЦКТИ",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#561e18", fg="#f22f08")
        self.medium_wall_formula_canvas = Canvas(self.medium_wall_formula_frame, width=390, height=90,
                                                 background="white")
        self.medium_wall_formula_photo = PhotoImage(file=r"Data\srednyaya_formula_390x90.png")
        self.medium_wall_formula_image = self.medium_wall_formula_canvas.create_image(0, 0,
                                                                    anchor='nw', image=self.medium_wall_formula_photo)
        self.interval_medium_wall_canvas = Canvas(self.medium_wall_formula_frame, width=130, height=90,
                                                  background="white")
        self.interval_medium_wall_photo = PhotoImage(file=r"Data\bolshe_3.2_123x54.png")
        self.interval_medium_wall_image = self.interval_medium_wall_canvas.create_image(5, 18, anchor='nw',
                                                                image=self.interval_medium_wall_photo)

        self.medium_wall_formula_frame.place(in_=self.label, x=740, y=220)
        self.medium_wall_formula_canvas.grid(row=0, column=0, sticky=W + N)
        self.interval_medium_wall_canvas.grid(row=0, column=1, sticky=W + N)

    def draw_fat_wall_formula_frame(self):
        self.fat_wall_formula_frame = LabelFrame(self.root, text=" Формула для толстостенных гильз",
                                        font=("GOST Type BU", 11, "italic", "bold"), bg="#561e18", fg="#f22f08")
        self.fat_wall_canvas = Canvas(self.fat_wall_formula_frame, width=390, height=90, background="white")
        self.fat_wall_photo = PhotoImage(file=r"Data\Wall_thickness_tolsto_390x90.png")
        self.fat_wall_image = self.fat_wall_canvas.create_image(0, 0, anchor='nw', image=self.fat_wall_photo)

        self.interval_fat_wall_canvas = Canvas(self.fat_wall_formula_frame, width=130, height=90, background="white")
        self.interval_fat_wall_photo = PhotoImage(file=r"Data\menshe_3.2_123x54.png")
        self.interval_fat_wall_image = self.interval_fat_wall_canvas.create_image(5, 18, anchor='nw',
                                                                                  image=self.interval_fat_wall_photo)

        self.fat_wall_formula_frame.place(in_=self.label, x=740, y=350)
        self.fat_wall_canvas.grid(row=0, column=0, sticky=W+N)
        self.interval_fat_wall_canvas.grid(row=0, column=1, sticky=W+N)

    def draw_thin_wall_formula_frame(self):
        self.thin_wall_formula_frame = LabelFrame(self.root, text=" Формула для тонкостенных гильз",
                                                 font=("GOST Type BU", 11, "italic", "bold"), bg="#561e18",
                                                 fg="#f22f08")
        self.thin_wall_canvas = Canvas(self.thin_wall_formula_frame, width=390, height=90, background="white")
        self.thin_wall_photo = PhotoImage(file=r"Data\Wall_thickness_tonko_390x90.png")
        self.thin_wall_image = self.thin_wall_canvas.create_image(0, 0, anchor='nw', image=self.thin_wall_photo)
        self.interval_thin_wall_canvas = Canvas(self.thin_wall_formula_frame, width=130, height=90, background="white")
        self.interval_thin_wall_photo = PhotoImage(file=r"Data\bolshe_16_123x54.png")
        self.interval_thin_wall_image = self.interval_thin_wall_canvas.create_image(5, 18, anchor='nw',
                                                                                    image=self.interval_thin_wall_photo)

        self.thin_wall_formula_frame.place(in_=self.label, x=740, y=480)
        self.thin_wall_canvas.grid(row=0, column=0, sticky=W+N)
        self.interval_thin_wall_canvas.grid(row=0, column=1, sticky=W+N)

    def draw_mech_properties_stali(self):
        self.mech_prop_stali_frame = LabelFrame(self.root, text=" Допустимые матералы и их мех. свойства",
                                             font=("GOST Type BU", 11, "italic", "bold"), bg="#561e18", fg="#f22f08")
        self.header_stali_canvas = Canvas(self.mech_prop_stali_frame, width=623, height=108, background="white")
        self.header_stali_photo = PhotoImage(file=r"Data\Header_stali_623x108.png")
        self.header_stali_image = self.header_stali_canvas.create_image(0, 0, anchor='nw',
                                                                        image=self.header_stali_photo)
        self.mech_prop_stali_canvas = Canvas(self.mech_prop_stali_frame, width=623, height=137, background="white")
        self.mech_prop_stali_photo = PhotoImage(file=r"Data\Stali_623x137.png")
        self.mech_prop_stali_image = self.mech_prop_stali_canvas.create_image(0, 0, anchor='nw',
                                                                        image=self.mech_prop_stali_photo)

        self.mech_prop_stali_frame.place(in_=self.label, x=50, y=322)
        self.header_stali_canvas.grid(row=0, column=0, sticky=W + N)
        self.mech_prop_stali_canvas.grid(row=1, column=0, sticky=W + N)

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
            self.open_data_calc = open(r"Data\save_data\data_WallThickness_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_WallThickness_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_WallThickness_calc.txt", "r")
        self.open_data_init()
        self.data_frame = LabelFrame(self.root, text=" Ввод данных для расчета",
                                     font=("GOST Type BU", 11, "bold", "italic"), bg="#561e18", fg="#f22f08")
        self.press_label = Label(self.data_frame, width=45, height=1, font=("GOST Type BU", 11),
                                 text="Рабочее давление жидкости p, в кг/см2", bg="#c05640", fg="#212027")
        self.press_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                 validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.diam_clndr_label = Label(self.data_frame, width=45, height=1, font=("GOST Type BU", 11),
                                       text="Внутренний диаметр цилиндра D, в мм", bg="#8d2f23", fg="#212027", justify=LEFT)
        self.diam_clndr_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                       validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.yield_strength_label = Label(self.data_frame, width=45, height=1, font=("GOST Type BU", 11),
                                          text="Предел текучести материала σT, в кг/см2", bg="#c05640", fg="#212027",
                                          justify=LEFT)
        self.yield_strength_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                      validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.safety_factor_label = Label(self.data_frame, width=45, height=1, font=("GOST Type BU", 11),
                                        text="Коэффициент запаса прочности n", bg="#8d2f23", fg="#212027",
                                        justify=LEFT)
        self.safety_factor_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.add_to_thick_label = Label(self.data_frame, width=45, height=1, font=("GOST Type BU", 11),
                                        text="Прибавка к толщине стенки на коррозию C, в мм", bg="#c05640",
                                        fg="#212027", justify=LEFT)
        self.add_to_thick_entry = Entry(self.data_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.wall_calc_btn = Button(self.data_frame, text="Расчет", font=("GOST Type BU", 11, "bold"),
                                    width=10, bg="#594346", fg="#f22f08", activebackground="#e0a96d", relief=GROOVE,
                                    command=self.take_data)
        self.all_clear_btn = Button(self.data_frame, text="Очистить", font=("GOST Type BU", 11, "bold"),
                                    width=10, bg="#594346", fg="#f22f08", activebackground="#e0a96d", relief=GROOVE,
                                    command=self.all_clear)

        if len(self.open_data) == 5:
            self.press_entry.insert(0, f"{self.open_data[0]}")
            self.diam_clndr_entry.insert(0, f"{self.open_data[1]}")
            self.yield_strength_entry.insert(0, f"{self.open_data[2]}")
            self.safety_factor_entry.insert(0, f"{self.open_data[3]}")
            self.add_to_thick_entry.insert(0, f"{self.open_data[4]}")


        self.data_frame.place(in_=self.label, x=50, y=90)
        self.press_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.press_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        self.diam_clndr_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.diam_clndr_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.yield_strength_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.yield_strength_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.safety_factor_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.safety_factor_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.add_to_thick_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        self.add_to_thick_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W)
        self.wall_calc_btn.grid(row=6, column=1, padx=(0, 10), pady=5, sticky=W + S)
        self.all_clear_btn.grid(row=6, column=0, padx=(0, 15), pady=5, sticky=E + S)

    def all_clear(self):
        self.press_entry.delete(0, END)
        self.diam_clndr_entry.delete(0, END)
        self.yield_strength_entry.delete(0, END)
        self.safety_factor_entry.delete(0, END)


    def draw_mpa_kgcm2_calc(self):
        # МПа в кг/см2 конвертер
        self.mpa_kgcm2 = StringVar()
        self.mpa_calc_frame = Frame(self.root, bg="#d9138a")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#e2d810", fg="#322e2f")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#e2d810", fg="#322e2f")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#322e2f",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#12a4d9", fg="#322e2f", activebackground="#12a4d9", relief=GROOVE,
                                  command=self.convert_mpa_kgcm2)


        self.mpa_calc_frame.place(in_=self.label, x=766, y=0)
        self.mpa_calc_label.grid(row=0, column=0, padx=10, sticky=W)
        self.convert_calc_label.grid(row=0, column=1, padx=10, sticky=W)
        self.mpa_calc_entry.grid(row=0, column=2, padx=10, sticky=W)
        self.convert_btn.grid(row=0, column=3, padx=5, sticky=E)

    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

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

    def take_data(self):
        self.medium_wall_formula_frame.configure(bg="#561e18", fg="#f22f08")
        self.fat_wall_formula_frame.configure(bg="#561e18", fg="#f22f08")
        self.thin_wall_formula_frame.configure(bg="#561e18", fg="#f22f08")
        flag = True
        try:
            self.press = float(self.press_entry.get())
            self.diam_clndr = float(self.diam_clndr_entry.get()) / 10
            self.yield_strength = float(self.yield_strength_entry.get())
            self.safety_factor = float(self.safety_factor_entry.get())
            self.add_to_thick = float(self.add_to_thick_entry.get())
        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректное значение.")
            # self.pre_output_frame.destroy()
        if flag:
            self.save_data_calc = open(r"Data\save_data\data_WallThickness_calc.txt", "w")

            # Запись
            self.save_data_calc.write(str(self.press) + "\n")
            self.save_data_calc.write(str(self.diam_clndr * 10) + "\n")
            self.save_data_calc.write(str(self.yield_strength) + "\n")
            self.save_data_calc.write(str(self.safety_factor) + "\n")
            self.save_data_calc.write(str(self.add_to_thick) + "\n")
            self.save_data_calc.close()
            self.wall_calc(self.root, self.label, self.press, self.diam_clndr, self.yield_strength, self.safety_factor,
                           self.add_to_thick, self.medium_wall_formula_frame, self.fat_wall_formula_frame,
                           self.thin_wall_formula_frame)

    def wall_calc(self, root, label, press, diam_clndr, yield_strength, safety_factor, add_to_thick,
                  medium_wall_formula_frame, fat_wall_formula_frame, thin_wall_formula_frame):
        WallThicknessCalc(root, label, press, diam_clndr, yield_strength, safety_factor, add_to_thick,
                          medium_wall_formula_frame, fat_wall_formula_frame, thin_wall_formula_frame)








