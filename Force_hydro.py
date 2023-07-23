import math
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook




class ForceHydro:
    def __init__(self, root, label, ring_list_AMG, ring_list_NGJ):
        self.root = root
        self.label = label
        self.ring_list = []
        self.ring_list_AMG = ring_list_AMG
        self.ring_list_NGJ = ring_list_NGJ
        self.draw_widgets()
        self.index = 2


    def draw_widgets(self):
        self.draw_label()
        self.draw_mpa_kgcm2_calc()
        self.draw_formula_frame()
        self.draw_tiporazmer_frame()
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width=50, font=("GOST Type BU", 13, "bold"),
                                 text="Расчет усилия, создаваемое гидроцилиндром", bg="#ddc3a5", fg="#201e20",
                                 justify=CENTER)


        self.header_frame.place(in_=self.label, x=390, y=45)
        self.header_calc.pack()
        self.draw_initial_frame()


    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\Escis_hydro_1280x680.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=-5)

    def draw_tiporazmer_frame(self):
        self.tiporazmer_frame = LabelFrame(self.root, text="Типоразмеры", font=("GOST Type BU", 11, "italic"),
                                           bg="#ddc3a5", fg="#201e20")
        self.tiporazmer_img = PhotoImage(file=r"Data\Diameters_640x230.png")
        self.tiporazmer_label = Label(self.tiporazmer_frame, image=self.tiporazmer_img)
        self.tiporazmer_label.image = self.tiporazmer_img
        self.tiporazmer_frame.place(in_=self.label, x=610, y=95)
        self.tiporazmer_label.pack(side=LEFT)


    def draw_formula_frame(self):
        self.formula_frame = LabelFrame(self.root, text="Формулы для расчета", font=("GOST Type BU", 11, "italic"),
                                        bg="#ddc3a5", fg="#201e20")
        self.tabs_control = Notebook(self.formula_frame, height=230, width=640, padding=(0, 10, 0, 0))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="Усилие")
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Трение")
        self.tab_3 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_3, text="Сопротивление")
        self.formula_frame.place(in_=self.label, x=610, y=362)
        self.run_formula_frame()


    def run_formula_frame(self):
        self.usilie_img = PhotoImage(file=r"Data\Usilie_hydro_640x230.png")
        self.friction_img = PhotoImage(file=r"Data\Friction_formul_640x230.png")
        self.drain_img = PhotoImage(file=r"Data\p_sliv_640x230.png")

        self.usilie_canvas = Canvas(self.tab_1, width=600, height=225, background="white")
        self.friction_canvas = Canvas(self.tab_2, width=600, height=225, background="white")
        self.drain_canvas = Canvas(self.tab_3, width=600, height=225, background="white")

        self.usilie_image = self.usilie_canvas.create_image(0, 0, anchor='nw',
                                                                    image=self.usilie_img)
        self.friction_image = self.friction_canvas.create_image(0, 0, anchor='nw',
                                                                    image=self.friction_img)
        self.drain_image = self.drain_canvas.create_image(0, 0, anchor='nw',
                                                                    image=self.drain_img)

        self.tabs_control.pack(fill=BOTH, expand=1)
        self.usilie_canvas.pack()
        self.friction_canvas.pack()
        self.drain_canvas.pack()

    def draw_mpa_kgcm2_calc(self):
        # МПа в кг/см2 конвертер
        self.mpa_kgcm2 = StringVar()
        self.mpa_calc_frame = Frame(self.root, bg="#e5e5dc")
        self.mpa_calc_label = Label(self.mpa_calc_frame, width=15, text="МПа в кг/см2",
                                    font=("GOST Type BU", 11, "bold"), bg="#e5e5dc", fg="#201e20")
        self.convert_calc_label = Label(self.mpa_calc_frame, width=15, textvariable=self.mpa_kgcm2,
                                    font=("GOST Type BU", 11, "bold"), bg="#ddc3a5", fg="#201e20")
        self.mpa_calc_entry = Entry(self.mpa_calc_frame, width=6, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                    validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        #self.mpa_calc_entry.insert(0, "0")
        self.convert_btn = Button(self.mpa_calc_frame, text="Конвертировать", font=("GOST Type BU", 11, "bold"),
                                  width=17, bg="#e5e5dc", fg="#201e20", activebackground="#e0a96d", relief=GROOVE,
                                  command=self.convert_mpa_kgcm2)


        self.mpa_calc_frame.place(in_=self.label, x=766, y=0)
        self.mpa_calc_label.grid(row=0, column=0, padx=10, sticky=W)
        self.convert_calc_label.grid(row=0, column=1, padx=10, sticky=W)
        self.mpa_calc_entry.grid(row=0, column=2, padx=10, sticky=W)
        self.convert_btn.grid(row=0, column=3, padx=5, sticky=E)

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


    def draw_initial_frame(self):
        self.pull_shtock_value = StringVar()
        self.pull_piston_value = StringVar()
        try:
            self.open_data_calc = open(r"Data\save_data\dataA_force_hydro_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\dataA_force_hydro_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\dataA_force_hydro_calc.txt", "r")
        self.open_data_init()
        self.initial_frame = LabelFrame(self.root, text=" Предварительный расчет "
                                                       "(без потерь на трение и сопротивление) ",
                                        font=("GOST Type BU", 11, "italic"), bg="#ddc3a5", fg="#201e20")
        self.press_label = Label(self.initial_frame, width=45, height=1, font=("GOST Type BU", 11),
                                 text="Рабочее давление жидкости, в кг/см2", bg="#e0a96d", fg="#201e20")
        self.press_entry = Entry(self.initial_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                 validate="key", validatecommand=(self.label.register(self.validate_amount), "%S"))
        self.diam_piston_label = Label(self.initial_frame, width=45, height=1, font=("GOST Type BU", 11),
                                       text="Диаметр поршня, в мм", bg="#e0a96d", fg="#201e20", justify=LEFT)
        self.diam_piston_entry = Entry(self.initial_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                       validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.diam_shtock_label = Label(self.initial_frame, width=45, height=1, font=("GOST Type BU", 11),
                                       text="Диаметр штока, в мм", bg="#e0a96d", fg="#201e20",
                                       justify=LEFT)
        self.diam_shtock_entry = Entry(self.initial_frame, width=8, font=("GOST Type BU", 11), bg="white", fg="#26495c",
                                       validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.pull_calc_btn = Button(self.initial_frame, text="Предварительный\nрезультат",
                                    font=("GOST Type BU", 10, "bold"), width=17, height=2, bg="#e5e5dc", fg="#201e20",
                                    activebackground="#e0a96d", relief=GROOVE, bd=3, command=self.pull_calc)
        self.pull_output_frame = Frame(self.initial_frame, bg="#ddc3a5")
        self.header_pull_shtock_label = Label(self.pull_output_frame, width=21, height=2, font=("GOST Type BU", 11),
                                              text="Усилие штоковой\nполости, в кг", bg="#e0a96d", fg="#201e20",
                                              justify=CENTER)
        self.header_pull_piston_label = Label(self.pull_output_frame, width=21, height=2, font=("GOST Type BU", 11),
                                              text="Усилие поршневой\n полости, в кг", bg="#e0a96d", fg="#201e20",
                                              justify=CENTER)
        self.pull_shtock_output_label = Label(self.pull_output_frame, width=21, height=2, font=("GOST Type BU", 11),
                                              textvariable=self.pull_shtock_value, bg="#e0a96d",
                                              fg="#201e20", justify=LEFT)
        self.pull_piston_output_label = Label(self.pull_output_frame, width=21, height=2, font=("GOST Type BU", 11),
                                              textvariable=self.pull_piston_value, bg="#e0a96d",
                                              fg="#201e20", justify=LEFT)
        self.all_clear_btn = Button(self.initial_frame, text="Очистить все", font=("GOST Type BU", 10, "bold"),
                                    width=17, height=2, bg="#e5e5dc", fg="#201e20",
                                    activebackground="#e0a96d", relief=GROOVE, bd=3, command=self.all_clear)

        if len(self.open_data) == 3:
            self.press_entry.insert(0, f"{self.open_data[0]}")
            self.diam_piston_entry.insert(0, f"{self.open_data[1]}")
            self.diam_shtock_entry.insert(0, f"{self.open_data[2]}")

        self.initial_frame.place(in_=self.label, x=50, y=97)
        self.press_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.press_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        self.diam_piston_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.diam_piston_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.diam_shtock_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.diam_shtock_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.all_clear_btn.grid(row=4, column=1, padx=(0, 10), pady=(2, 5), sticky=W + N)
        self.pull_calc_btn.grid(row=4, column=1, padx=(0, 10), pady=8, sticky=W + S)
        self.pull_output_frame.grid(row=4, column=0, padx=(15, 0), pady=2, sticky=W)
        self.header_pull_shtock_label.grid(row=1, column=0, padx=0, pady=0, sticky=W)
        self.header_pull_piston_label.grid(row=1, column=1, padx=14, pady=0, sticky=W)
        self.pull_shtock_output_label.grid(row=2, column=0, padx=0, pady=(5, 7), sticky=W)
        self.pull_piston_output_label.grid(row=2, column=1, padx=14, pady=(5, 7), sticky=W)

    def all_clear(self):
        self.press_entry.delete(0, END)
        self.diam_piston_entry.delete(0, END)
        self.diam_shtock_entry.delete(0, END)
        self.pull_shtock_value.set(f"")
        self.pull_piston_value.set(f"")
        self.res_calc_frame.destroy()
        self.draw_clac_frame()
        self.press_sliv_entry.delete(0, END)

    def draw_clac_frame(self):
        self.oil_choise = IntVar(value=1)
        self.res_shtock_friction_value = StringVar()
        self.res_piston_friction_value = StringVar()
        self.full_pull_shtock_value = StringVar()
        self.full_pull_piston_value = StringVar()
        try:
            self.open_sliv_data = open(r"Data\save_data\dataB_force_hydro_calc.txt", "r")
            self.line = float(self.open_sliv_data.readline())
        except FileNotFoundError:
            with open(r"Data\save_data\dataB_force_hydro_calc.txt", "w") as self.open_sliv_data:
                self.open_sliv_data = open(r"Data\save_data\dataB_force_hydro_calc.txt", "r")

        self.sliv_data  = []
        if self.line != "":
            if self.line % 1 == 0.0:
                self.sliv_data.append(int(self.line))
            else:
                self.sliv_data.append(self.line)
        self.open_sliv_data.close()

        self.res_calc_frame = LabelFrame(self.root, text=" Полный расчет", font=("GOST Type BU", 11, "italic"),
                                        bg="#ddc3a5", fg="#201e20")
        self.press_sliv_label = Label(self.res_calc_frame, width=50, height=1, font=("GOST Type BU", 11),
                                      text=" Давление в линии слива Pсл, кг/см2", bg="#e0a96d", fg="#201e20",
                                      justify=LEFT)
        self.press_sliv_entry = Entry(self.res_calc_frame, width=8, font=("GOST Type BU", 11), bg="white",
                                      fg="#26495c", validate="key",
                                      validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.oil_choise_NGJ = Radiobutton(self.res_calc_frame, text="Масло синтетическое (НГЖ-5у и др)",
                                          font=("GOST Type BU", 11), width=47, bg="#e0a96d", fg="#201e20",
                                          variable=self.oil_choise, value=0, activebackground="#e0a96d", justify=LEFT)
        self.oil_choise_AMG = Radiobutton(self.res_calc_frame, text="Масло минеральное (АМГ-10 и др)   ",
                                          font=("GOST Type BU", 11), width=47, bg="#e0a96d", fg="#201e20",
                                          variable=self.oil_choise, value=1, activebackground="#e0a96d", justify=LEFT)
        self.header_ring_search_label = Label(self.res_calc_frame, width=50, height=1,
                                              font=("GOST Type BU", 11),
                                              text="Доступные прессформы на кольца в цеху №10:", bg="#e0a96d",
                                              fg="#201e20", justify=CENTER)
        self.friction_frame = Frame(self.res_calc_frame, bg="#ddc3a5")
        self.shtock_pressform_label = Label(self.friction_frame, width=24, height=1, text="По диаметру штока",
                                            font=("GOST Type BU", 11), bg="#e0a96d", fg="#201e20", justify=CENTER)
        self.piston_pressform_label = Label(self.friction_frame, width=24, height=1, text="По диаметру поршня",
                                            font=("GOST Type BU", 11), bg="#e0a96d", fg="#201e20", justify=CENTER)
        self.Combo_shtock_ring_search = Combobox(self.friction_frame, width=21, font=("GOST Type BU", 11),
                                                 state="readonly")
        self.Combo_piston_ring_search = Combobox(self.friction_frame, width=21, font=("GOST Type BU", 11),
                                                 state="readonly")
        self.res_shtock_friction_label = Label(self.friction_frame, width=24, height=2,
                                               font=("GOST Type BU", 11), textvariable=self.res_shtock_friction_value,
                                               bg="#e0a96d", fg="#201e20", justify=LEFT)
        self.res_piston_friction_label = Label(self.friction_frame, width=24, height=2,
                                               font=("GOST Type BU", 11), textvariable=self.res_piston_friction_value,
                                               bg="#e0a96d", fg="#201e20", justify=LEFT)

        self.result_frame = Frame(self.res_calc_frame, bg="#ddc3a5")

        self.full_pull_shtock_label = Label(self.result_frame, width=50, height=2,
                                               font=("GOST Type BU", 11), textvariable=self.full_pull_shtock_value,
                                               bg="#e0a96d", fg="#201e20", justify=LEFT)
        self.full_pull_piston_label = Label(self.result_frame, width=50, height=2,
                                               font=("GOST Type BU", 11), textvariable=self.full_pull_piston_value,
                                               bg="#e0a96d", fg="#201e20", justify=LEFT)
        self.full_pull_calc_btn = Button(self.res_calc_frame, text="Расчет",
                                         font=("GOST Type BU", 11, "bold"), width=10, bg="#e5e5dc", fg="#201e20",
                                         activebackground="#e0a96d", relief=GROOVE, bd=3, command=self.resistance_sliv)

        if self.sliv_data:
            self.press_sliv_entry.insert(0, f"{self.sliv_data[0]}")

        self.res_calc_frame.place(in_=self.label, x=50, y=307)
        self.press_sliv_label.grid(row=1, column=0, padx=15, pady=2, sticky=W)
        self.press_sliv_entry.grid(row=1, column=1, padx=(0, 10), pady=2, sticky=W)
        self.oil_choise_AMG.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.oil_choise_NGJ.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.header_ring_search_label.grid(row=4, column=0, padx=(15, 5), pady=2, sticky=W)
        self.friction_frame.grid(row=5, column=0, padx=0, pady=2, sticky=W)
        self.shtock_pressform_label.grid(row=1, column=0, padx=(15, 8), pady=2, sticky=W)
        self.piston_pressform_label.grid(row=1, column=1, padx=(0, 5), pady=2, sticky=W)
        self.Combo_shtock_ring_search.grid(row=2, column=0, padx=(15, 2), pady=2, sticky=W)
        self.Combo_shtock_ring_search.bind("<<ComboboxSelected>>", self.resistance_gasket_shtock_calc)
        self.Combo_piston_ring_search.grid(row=2, column=1, padx=0, pady=2, sticky=W)
        self.Combo_piston_ring_search.bind("<<ComboboxSelected>>", self.resistance_gasket_piston_calc)
        self.res_shtock_friction_label.grid(row=3, column=0, padx=(15, 8), pady=2, sticky=W)
        self.res_piston_friction_label.grid(row=3, column=1, padx=(0, 5), pady=2, sticky=W)

        self.result_frame.grid(row=6, column=0, padx=0, pady=(0, 2), sticky=W)
        self.full_pull_shtock_label.grid(row=1, column=0, padx=15, pady=(0, 2), sticky=W)
        self.full_pull_piston_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.full_pull_calc_btn.grid(row=6, column=1, padx=(0, 12), pady=5, sticky=E + S)

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

    def convert_to_float_and_int(self, value):
        value = float(value)
        if value % 1 != 0.5:
            value = int(value)
        return value

    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

    def pull_calc(self):
        flag = True
        try:
            self.press = float(self.press_entry.get())
            self.diam_piston = float(self.diam_piston_entry.get()) / 10
            self.diam_shtock = float(self.diam_shtock_entry.get()) / 10
            if self.diam_shtock >= self.diam_piston:
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Диаметр штока не может быть больше либо равен диаметру поршня.")

            if self.diam_shtock < 0.3 or self.diam_shtock > 29:
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Диапазон значений диаметра штока от 3 до 290 мм")

            if self.diam_piston < 0.5 or self.diam_piston > 30.5:
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Диапазон значений диаметра штока от 5 до 305 мм")

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены"
                                      f" или введено некорректное значение.")
            self.res_calc_frame.destroy()

        if flag:
            self.draw_clac_frame()
            self.square_piston = (math.pi * math.pow(self.diam_piston, 2)) / 4
            self.square_shtock = (math.pi * (math.pow(self.diam_piston, 2) - math.pow(self.diam_shtock, 2))) / 4
            self.pull_shtock = self.press * self.square_shtock
            self.pull_piston = self.press * self.square_piston
            self.pull_shtock_value.set(f"{round(self.pull_shtock, 4)}")
            self.pull_piston_value.set(f"{round(self.pull_piston, 4)}")
            self.get_pressform(self.diam_shtock * 10, self.diam_piston * 10)

            self.save_data_calc = open(r"Data\save_data\dataA_force_hydro_calc.txt", "w")

            # Запись файлов
            self.save_data_calc.write(str(self.press) + "\n")
            self.save_data_calc.write(str(self.diam_piston * 10) + "\n")
            self.save_data_calc.write(str(self.diam_shtock * 10) + "\n")
            self.save_data_calc.close()

    def get_pressform(self, diam_shtock, diam_piston):
        if self.oil_choise.get() == 1:
            self.ring_list = self.ring_list_AMG
        else:
            self.ring_list = self.ring_list_NGJ
        diam_shtock = self.convert_to_float_and_int(diam_shtock)
        diam_piston = self.convert_to_float_and_int(diam_piston)
        pressform_shtock = []
        pressform_piston = []
        for item in self.ring_list:
            if diam_shtock == item[:][0]:
                pressform_shtock.append(item)
            if diam_piston == item[:][1]:
                pressform_piston.append(item)

        self.Combo_shtock_ring_search.set('')
        self.Combo_shtock_ring_search['values'] = pressform_shtock
        self.Combo_piston_ring_search.set('')
        self.Combo_piston_ring_search['values'] = pressform_piston

    def resistance_sliv(self):
        flag = True
        try:
            self.press_sliv = float(self.press_sliv_entry.get())
            if self.press_sliv == 0:
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Неуказано давление линии слива.")
            if self.Combo_shtock_ring_search == "":
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Типоразмер уплотнительного кольца для штока не выбран.")
            if self.Combo_piston_ring_search == "":
                flag = False
                mb.showwarning(f"Ошибка", f"ОШИБКА: Типоразмер уплотнительного кольца для поршня не выбран.")

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены или введено некорректое значение.")
        if flag:
            self.res_sliv_shtock = self.press_sliv * self.square_shtock
            self.res_sliv_piston = self.press_sliv * self.square_piston
            self.full_pull_calc()
            self.save_sliv_data = open(r"Data\save_data\dataB_force_hydro_calc.txt", "w")

            # Запись
            self.save_sliv_data.write(str(self.press_sliv))
            self.save_sliv_data.close()

    def resistance_gasket_shtock_calc(self, event):
        # index = self.shtock_ring_search_LB.curselection()
        # pressform = self.shtock_ring_search_LB.get(index[0])
        pressform = tuple(self.Combo_shtock_ring_search.get().split())
        size = float(pressform[:][2])
        self.res_friction_shtock = 0.1 * math.pi * self.diam_shtock * (size / 10) * self.press
        self.res_shtock_friction_value.set(f"Rш = {round(self.res_friction_shtock, 4)} кг")

    def resistance_gasket_piston_calc(self, event):
        pressform = tuple(self.Combo_piston_ring_search.get().split())
        size = float(pressform[:][2])
        self.res_friction_piston = 0.1 * math.pi * self.diam_piston * (size / 10) * self.press
        self.res_piston_friction_value.set(f"Rп = {round(self.res_friction_piston, 4)} кг")

    def full_pull_calc(self):
        self.full_pull_shtock = self.pull_shtock - self.res_friction_shtock - self.res_friction_piston - self.res_sliv_shtock
        self.full_pull_piston = self.pull_piston - self.res_friction_shtock - self.res_friction_piston - self.res_sliv_piston
        self.full_pull_shtock_value.set(
            f"P шток. = pF - Rш - Rп - Rсл.порш. = {round(self.full_pull_shtock, 4)} кг")
        self.full_pull_piston_value.set(
            f"P порш. = pF - Rш - Rп - Rсл.шток. = {round(self.full_pull_piston, 4)} кг")

            # self.performance = float(self.performance_entry.get())
            # self.viscosity = float(self.viscosity_entry.get())
            # self.pipe_sliv = float(self.pipe_sliv_entry.get())
            # self.ray_digit = 21200 * (self.performance/(self.pipe_sliv * self.viscosity))
            # if self.ray_digit <= 2200:
            #     self.laminar_canvas.grid(row=1, column=0, padx=15, pady=10, sticky=W)
            # else:
            #     self.turbo_canvas.grid(row=1, column=0, padx=15, pady=10, sticky=W)



        ##### Мусор

        # self.performance_label = Label(self.res_calc_frame, width=50, height=1, font=("GOST Type BU", 10),
        #                                text=" Величина потока Q, л/мин", bg="#e0a96d", fg="#201e20",
        #                                justify=LEFT)
        # self.performance_entry = Entry(self.res_calc_frame, width=8, font=("GOST Type BU", 10), bg="white",
        #                                fg="#26495c")
        # self.viscosity_label = Label(self.res_calc_frame, width=50, height=1, font=("GOST Type BU", 10),
        #                                text=" Вязкость масла ν, мм2/с", bg="#e0a96d", fg="#201e20",
        #                                justify=LEFT)
        # self.viscosity_entry = Entry(self.res_calc_frame, width=8, font=("GOST Type BU", 10), bg="white",
        #                                fg="#26495c")
        # self.length_sliv_label = Label(self.res_calc_frame, width=50, height=1, font=("GOST Type BU", 10),
        #                              text=" Длина сливной магистрали L, в м", bg="#e0a96d", fg="#201e20",
        #                              justify=LEFT)
        # self.length_sliv_entry = Entry(self.res_calc_frame, width=8, font=("GOST Type BU", 10), bg="white",
        #                              fg="#26495c")
        # self.pipe_sliv_label = Label(self.res_calc_frame, width=50, height=1, font=("GOST Type BU", 10),
        #                                text=" Диаметр сливной магистрали Dсл, в мм", bg="#e0a96d", fg="#201e20",
        #                                justify=LEFT)
        # self.pipe_sliv_entry = Entry(self.res_calc_frame, width=8, font=("GOST Type BU", 10), bg="white",
        #                                fg="#26495c")



        # self.shtock_ring = StringVar()
        # self.piston_ring = StringVar()
        # self.shtock_ring_search_label = Label(self.pull_calc_advance_frame, width=18, height=6,
        #                                       font=("GOST Type BU", 10), textvariable=self.shtock_ring,
        #                                       bg="#e0a96d", fg="#201e20", justify=LEFT)
        # self.piston_ring_search_label = Label(self.pull_calc_advance_frame, width=18, height=6,
        #                                       font=("GOST Type BU", 10), textvariable=self.piston_ring,
        #                                       bg="#e0a96d", fg="#201e20", justify=LEFT)



        # self.laminar_canvas = Canvas(self.result_frame, width=130, height=20, bg="#ddc3a5")
        # self.laminar_canvas.create_rectangle(3, 3, 130, 20, outline="green", width="3")
        # self.laminar_canvas.create_text(65, 11, text="Ламинарный поток", font=("GOST Type BU", 10, "italic"),
        #                                 fill="green")
        # self.turbo_canvas = Canvas(self.result_frame, width=130, height=20, bg="#ddc3a5")
        # self.turbo_canvas.create_rectangle(3, 3, 130, 20, outline="red", width="3")
        # self.turbo_canvas.create_text(65, 11, text="Турбулентный поток", font=("GOST Type BU", 10),
        #                                 fill="red")
        # self.shtock_ring_search_LB = Listbox(self.pull_calc_advance_frame, width=10, height=3, highlightcolor="#d72631")
        # self.piston_ring_search_LB = Listbox(self.pull_calc_advance_frame, width=10, height=3, highlightcolor="#d72631")


        # self.performance_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        # self.performance_entry.grid(row=3, column=1, padx=(0, 10), pady=2, sticky=W)
        # self.viscosity_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        # self.viscosity_entry.grid(row=4, column=1, padx=(0, 10), pady=2, sticky=W)
        # self.length_sliv_label.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        # self.length_sliv_entry.grid(row=5, column=1, padx=(0, 10), pady=2, sticky=W)
        # self.pipe_sliv_label.grid(row=6, column=0, padx=15, pady=2, sticky=W)
        # self.pipe_sliv_entry.grid(row=6, column=1, padx=(0, 10), pady=2, sticky=W)




        #self.laminar_canvas.grid(row=1, column=0, padx=15, pady=10, sticky=W)
        #self.turbo_canvas.grid(row=1, column=0, padx=15, pady=10, sticky=W)




        # a = []
        # for item in size_ring:
        #     if item[:][1] == b and item[:][2] == c:
        #         a.append(item[:][0])

        # def frange(self, start, stop, step):
        #     i = start
        #     while i < stop:
        #         yield i
        #         i += step



    # def check_auto_load(self):
    #     if not self.auto_save.get() and self.auto_load.get():
    #         if mb.askyesno("Ошибка", "Автозагрузка без автосохранения. Хотите установить автосохранение ?"):
    #             self.auto_save.set(True)

    # def auto_save_changed(self):
    #     mb.showinfo("AutoSave", f"Value: {self.auto_save.get()}")
