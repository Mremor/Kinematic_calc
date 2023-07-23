import math
from tkinter import *
from tkinter import messagebox as mb


from Scheme_spec_view import SchemeSpecView
from Gen_calc import GeneralCalc


# Именнованные константы для вычислений
ALPHA_ANGLE = math.radians(10)


class Gathering_info:
    def __init__(self, parent, width, height, title=" Калькулятор кинематики", resizeble=(False, False), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)
        self.root.configure(bg="#c66b3d")
        self.escis_kin_calc_img = PhotoImage(file=r"Data\Escis_Kinematic_calc_dop.png")
        self.escis_kin_calc_big_img = PhotoImage(file=r"Data\Escis_Kinematic_calc_1440x1020.png")
        self.draw_widgets()
        self.grab_focus()

    # def run_string(self):
    #     self.run_string_value = StringVar()
    #     self.run_string_frame = Frame(self.root, bg="orange")
    #     self.run_string_label = Label(self.run_string_frame, width=30, height=3,
    #                                          font=("GOST Type BU", 11, "bold"), textvariable=self.run_string_value,
    #                                          bg="#99bfaa", fg="#5c3d46", justify=LEFT)
    #
    #     self.show("a b c", 50, 0.3)
    #
    #     self.run_string_frame.place(in_=self.label, x=20, y=10)
    #     self.run_string_label.pack()
    #
    # def show(self, text, maximum, delay):
    #     text = ' ' * maximum + text
    #     for i in range(len(text)):
    #         self.run_string_value.set(f"{text[i:i + maximum]} \r")
    #         time.sleep(delay)

    # Взятие фокуса дочерним окном
    def grab_focus(self):
        #self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\bg.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=0)

    def draw_header(self):
        self.header_frame = Frame(self.root, bg="#e0a96d")
        self.header_calc = Label(self.header_frame, width=70, height=2, font=("GOST Type BU", 13, "bold"),
                                 text="Калькулятор расчета длин убранного (L2), выпущенного (L4)\n"
                                      "положений нагрузочного цилиндра, а также высоты его заделки (H2)",
                                 bg="#02231c", fg="#c7f6ec", relief=RIDGE, bd=2, justify=CENTER)

        self.header_frame.place(in_=self.label, x=310, y=25)
        self.header_calc.pack()


    # Ввод виджетов
    def draw_widgets(self):
        self.draw_label()
        self.const_alpha()
        self.errors_label()
        self.draw_header()
        self.escis_Kinematic_calc()
        self.draw_Kinematic_calc_data_frame()


    def escis_Kinematic_calc(self):
        self.escis_Kinematic_frame = LabelFrame(self.root, text="  Эскиз кинематики стенда на ресурс ",
                                             font=("GOST Type BU", 11, "bold", "italic"), bg="#107050", fg="#55d9c0") #bg="#415939", fg="#f4f2b1"
        self.escis_kin_calc_label = Label(self.escis_Kinematic_frame, image=self.escis_kin_calc_img)
        self.escis_kin_calc_label.image = self.escis_kin_calc_img

        self.escis_Kinematic_btn = Button(self.escis_Kinematic_frame, width=22, height=1,
                                          text="Увеличенный эскиз", font=("GOST Type BU", 10, "bold"),
                                          bg="#4dd8ad", fg="#02231c", activebackground="#8c7462", relief=GROOVE,
                                          command=self.scheme_spec_view) # bg="#f3efca", fg="#8a5d59"

        self.escis_Kinematic_frame.place(in_=self.label, x=645, y=75)
        self.escis_kin_calc_label.grid(row=1, column=0, padx=5, pady=(9, 0), sticky=W)
        self.escis_Kinematic_btn.grid(row=2, column=0, padx=15, pady=15, sticky=E)

    def scheme_spec_view(self):
        self.start_scheme_spec_view(self.root, 1440, 1020, self.escis_kin_calc_big_img,
                                    title="    Условные обозначения схемы нагружения")

    def start_scheme_spec_view(self, root, width, height, scheme_spec_img, title,
                               resizeble=(False, False), icon=r"Data\kin2_calc.ico"):
        SchemeSpecView(root, width, height, scheme_spec_img, title, resizeble, icon)

    def const_alpha(self):
        self.alpha_angle_const = Label(self.root, width=28, height=1, bg="#1b3a4c", fg="#19c6d4",
                                       text=f"  Угол α - константа: {math.degrees(ALPHA_ANGLE)}˚  ",
                                       font=("GOST Type BU", 11, "bold"), justify=LEFT)

        self.alpha_angle_const.place(in_=self.label, x=1054, y=0)

    def errors_label(self):
        self.errmsg = StringVar()
        self.errors = Label(self.root, width=30, height=4, font=("GOST Type BU", 11, "bold"),
                            textvariable=self.errmsg, wraplength=240, relief=GROOVE, bg="#c7f6ec", fg="#107050",
                            justify=LEFT)

        self.errors.place(in_=self.label, x=1023, y=597)

        # Функция справки
    def start_reference(self):
        mb.showinfo(f"Справка параметров расчета", f"Ход испытуемого г/ц - длина рабочего хода испытуемого "
                                                   f"гидроцилиндра, в мм\n\nL1 - длина испытуемого изделия по точкам "
                                                   f"навески, в мм\n\nУгол β - начальный угол положения рычага-качалки "
                                                   f"относительно плоскости станины стенда, в десятичных градусах. "
                                                   f"Интервал вводимых значений от 30˚ до 60˚\n\n"
                                                   f"R1 - длина рычага-качалки по точкам крепления, в мм. "
                                                   f"Интервал вводимых значений от R1= L1 до R1= 2xL1")

    def start_info(self):
        mb.showinfo(f"Справка параметров сортировки результата",
                                                   f"   За базовый параметр сортировки данных принимается длина R2,"
                                                   f" находящаяся в интервале от 0.5хR1 до 0.75хR1."
                                                   f"   Сортировка допустимых значений проводится сразу по всем"
                                                   f" искомым размерам L2, L4, H2. В сортировке учавствуют ТОЛЬКО"
                                                   f" значения размеров близкие к целочисленным или вещественные "
                                                   f" значения близкие остатком к 0.5 мм."
                                                   f"   В случае если хотябы один из параметров не близок к"
                                                   f" целочисленному или вещественному значению с остатком 0.5 мм"
                                                   f" (с заданной пользователем точностью), то пропускается вся"
                                                   f" выборка размеров и учавствует следующая.")

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

    # Валидация вводных данных
    def validate_amount(self, input):
        try:
            x = input
            if x == ".":
                return True
            x = float(x)
            return True
        except ValueError:
            return False

    def validate_accuracy(self, input):
        try:
            x = input
            if x in [".", "-"]:
                return True
            x = float(x)
            return True
        except ValueError:
            return False


    def draw_Kinematic_calc_data_frame(self):
        try:
            self.open_data_calc = open(r"Data\save_data\data_Get_info_kin_calc.txt", "r")
        except FileNotFoundError:
            with open(r"Data\save_data\data_Get_info_kin_calc.txt", "w") as self.open_data_calc:
                self.open_data_calc = open(r"Data\save_data\data_Get_info_kin_calc.txt", "r")
        self.open_data_init()
        # Прописываю параметры испытуемого цилиндра
        self.Kinematic_data_frame = LabelFrame(self.root, text="  Ввод данных для расчета ",
                                               font=("GOST Type BU", 11, "bold", "italic"), bg="#02231c", fg="#c7f6ec") #bg="#1c2c58", fg="#51a2d9"
        self.isp_clndr_hod_label = Label(self.Kinematic_data_frame, width=62, height=1,
                                         text="Ход испытуемого цилиндра, в мм",
                                         font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT) #bg="#415939", fg="#f4f2b1"
        self.isp_clndr_hod_entry = Entry(self.Kinematic_data_frame, width=8, font=("GOST Type BU", 11),
                                         bg= "white",  fg="#8a140e", validate="key",
                                         validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.l1_label = Label(self.Kinematic_data_frame, width=62, height=1,
                              text="Длина испытуемого цилиндра в убранном положении L1, в мм",
                              font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.l1_entry = Entry(self.Kinematic_data_frame, width=8, font=("GOST Type BU", 11), bg= "white",  fg="#8a140e",
                              validate="key", validatecommand=(self.root.register(self.validate_amount), "%S"))

        # Прописываю данные для расчета
        self.beta_angle_label = Label(self.Kinematic_data_frame, width=62, height=1,
                                      text="Начальный угол положения рычага-качалки β, в градусах",
                                      font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.beta_angle_entry = Entry(self.Kinematic_data_frame, width=8, font=("GOST Type BU", 11),
                                      bg= "white",  fg="#8a140e", validate="key",
                                      validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.r1_label = Label(self.Kinematic_data_frame, width=62, height=1,
                              text="Длина рычага-качалки по точкам крепления R1, в мм",
                              font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.r1_entry = Entry(self.Kinematic_data_frame, width=8, font=("GOST Type BU", 11),
                              bg= "white",  fg="#8a140e", validate="key",
                              validatecommand=(self.root.register(self.validate_amount), "%S"))

        # Кнопки очистки, справки и старта расчетов
        self.submit_btn = Button(self.Kinematic_data_frame, text="Утвердить", font=("GOST Type BU", 10, "bold"), # bg="#f3efca", fg="#8a5d59"
                                 width=12, height=1, bg="#4dd8ad", fg="#02231c", activebackground="#ffc13b",
                                 relief=GROOVE, command=self.form_submit)
        self.all_clear_btn = Button(self.Kinematic_data_frame, width=10, height=1, text="Очистить",
                                    font=("GOST Type BU", 10, "bold"), bg="#4dd8ad", fg="#02231c", relief=GROOVE,
                                    activebackground="#ffc13b", command=self.all_clear_data_Kinematic_calc)
        self.reference_btn = Button(self.Kinematic_data_frame, text="Справка", font=("GOST Type BU", 10, "bold"),
                                    width=10, bg="#4dd8ad", fg="#02231c", activebackground="#ffc13b", relief=GROOVE,
                                    command=self.start_reference)

        if len(self.open_data) == 4:
            self.isp_clndr_hod_entry.insert(0, f"{self.open_data[0]}")
            self.l1_entry.insert(0, f"{self.open_data[1]}")
            self.beta_angle_entry.insert(0, f"{self.open_data[2]}")
            self.r1_entry.insert(0, f"{self.open_data[3]}")

        # Прорисовка виджетов в окне
        self.Kinematic_data_frame.place(in_=self.label, x=15, y=75)
        self.isp_clndr_hod_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.isp_clndr_hod_entry.grid(row=1, column=1, padx=10, pady=(10, 2), sticky=W)
        self.l1_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.l1_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)
        self.beta_angle_label.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        self.beta_angle_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)
        self.r1_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        self.r1_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)
        self.submit_btn.grid(row=5, column=0, padx=15, pady=10, sticky=E + S)
        self.all_clear_btn.grid(row=5, column=1, padx=(0, 10), pady=10, sticky=W + S)
        self.reference_btn.grid(row=5, column=0, padx=15, pady=10, sticky=W + S)

    # Очистка всех полей введеных данных
    def all_clear_data_Kinematic_calc(self):
        self.isp_clndr_hod_entry.delete(0, END)
        self.l1_entry.delete(0, END)
        self.beta_angle_entry.delete(0, END)
        self.r1_entry.delete(0, END)


    # Проверяет данные на вхождение в заданный по умолчанию интервал значений или градусов
    def form_submit(self):
        flag = True
        try:
            self.isp_clndr_hod = float(self.isp_clndr_hod_entry.get())
            self.l1 = float(self.l1_entry.get())
            self.beta_angle = math.radians(float(self.beta_angle_entry.get()))
            self.r1 = float(self.r1_entry.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: Не все поля ввода данных заполнены, или введено некорректное значение")
        if flag:
            if self.r1 < self.l1 or self.r1 > (2 * self.l1):
                flag = False
                self.errmsg.set(f"ОШИБКА: Значение должно находиться в интервале от {self.l1} до {2 * self.l1} мм")
                mb.showwarning(f"Ошибка",
                               f"ОШИБКА: Значение должно находиться в интервале от {self.l1} до {2 * self.l1} мм")

            else:
                self.errmsg.set("")

            if flag:
                if self.beta_angle < math.radians(30) or self.beta_angle > math.radians(60):
                    flag = False
                    self.errmsg.set(f"ОШИБКА: Угол должен находиться в интервале от 30˚ до 60˚ (включительно), "
                                    f"повторите ввод")
                    mb.showwarning(f"Ошибка",
                                   f"ОШИБКА: Угол должен находиться в интервале от 30˚ до 60˚ (включительно), "
                                   f"повторите ввод")

                else:
                    self.errmsg.set("")

                if flag:
                    self.h1_l5_epsilon_calc()

    def h1_l5_epsilon_calc(self):
        flag = True
        try:
            self.l3 = self.dlina_l3(self.l1, self.isp_clndr_hod)
            self.gamma = self.gamma_angle(self.beta_angle)
            self.r3 = self.dlina_r3(self.r1, self.l1, self.gamma)
            self.delta = self.delta_angle(self.r1, self.r3, self.l1)
            self.dzeta = self.dzeta_angle(self.r1, self.r3, self.l3)
            self.beta_1 = self.beta_1_angle(self.dzeta, self.beta_angle, self.delta)
            self.epsilon = self.epsilon_angle(self.beta_angle, self.beta_1)
            self.l5 = self.dlina_l5(self.r3, self.beta_angle, self.delta)
            self.h1 = self.visota_h1(self.r3, self.l5, self.beta_angle, self.delta)
            self.delta_1 = self.delta_1_angle(self.epsilon)
            self.gamma_1 = self.gamma_1_angle(self.delta_1, self.gamma)

        except ZeroDivisionError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
        if flag:
            self.draw_pre_output_frame()
            self.deviation_in()
            self.save_data_calc = open(r"Data\save_data\data_Get_info_kin_calc.txt", "w")

            # Запись
            self.save_data_calc.write(str(self.isp_clndr_hod) + "\n")
            self.save_data_calc.write(str(self.l1) + "\n")
            self.save_data_calc.write(str(math.degrees(self.beta_angle)) + "\n")
            self.save_data_calc.write(str(self.r1))

            self.save_data_calc.close()

            # Вывод
            self.pre_out_epsilon_val.set(f" Угол ε равен:{math.degrees(self.epsilon): .5f}˚ "
                                         f"( {self.degrees_to_dms(math.degrees(self.epsilon))} ).\t\t\t\t\t")
            self.pre_out_l5_val.set(f" Межосевое растояние L5 от оси кронштейна рычага-качалки до оси\n"
                                    f" кронштейна испытуемого цилиндра по горизонтали равно: {round(self.l5, 4)} мм."
                                    f"       ")
            self.pre_out_h1_val.set(f" Межосевое растояние H1 от оси кронштейна рычага-качалки до оси\n"
                                    f" кронштейна испытуемого цилиндра по вертикали равно: {round(self.h1, 4)} мм."
                                    f"         ")


    def draw_pre_output_frame(self):
        self.pre_out_epsilon_val = StringVar()
        self.pre_out_l5_val = StringVar()
        self.pre_out_h1_val = StringVar()
        self.pre_output_frame = LabelFrame(self.root, text="  Предварительные результаты ",
                                           font=("GOST Type BU", 11, "bold", "italic"), bg="#02231c", fg="#c7f6ec")
        self.epsilon_label = Label(self.pre_output_frame, width=73, height=1, font=("GOST Type BU", 11, "bold"),
                                      textvariable=self.pre_out_epsilon_val, bg="#107050", fg="#55d9c0", justify=LEFT)
        self.l5_label = Label(self.pre_output_frame, width=73, height=2, font=("GOST Type BU", 11, "bold"),
                                   textvariable=self.pre_out_l5_val, bg="#107050", fg="#55d9c0", justify=LEFT)
        self.h1_label = Label(self.pre_output_frame, width=73, height=2, font=("GOST Type BU", 11, "bold"),
                                   textvariable=self.pre_out_h1_val, bg="#107050", fg="#55d9c0", justify=LEFT)

        self.pre_output_frame.place(in_=self.label, x=15, y=265)
        self.epsilon_label.grid(row=1, column=0, padx=15, pady=(10, 2), sticky=W)
        self.l5_label.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        self.h1_label.grid(row=3, column=0, padx=15, pady=(2, 10), sticky=W)

    def deviation_in(self):
        self.deviation_frame = LabelFrame(self.root, text="  Ввод допуска сортировки результатов расчета ",
                                           font=("GOST Type BU", 11, "bold", "italic"), bg="#02231c", fg="#c7f6ec")
        self.hdr_dev = Label(self.deviation_frame, width=73, height=3,
                              text=" Введите верхнее и нижнее отклонение в мм от номинала искомых размеров\n"
                                   " L2, L4, H2 или нажмите «Расчет!» для ввода значения по умолчанию\n"
                                   " (+0.1 мм для верхнего предела допуска и -0.1 мм для нижнего)                 ",
                              font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.upper_dev_label = Label(self.deviation_frame, width=43, height=1,
                                         text="Верхнее отклонение, диапазон от 0 до «+0.2»",
                                         font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.upper_dev_entry = Entry(self.deviation_frame, width=8, font=("GOST Type BU", 11),
                                         bg="white", fg="#8a140e", validate="key",
                                         validatecommand=(self.root.register(self.validate_amount), "%S"))
        self.lower_dev_label = Label(self.deviation_frame, width=43, height=1,
                                         text="Нижнее отклонение, диапазон от 0 до «-0.2»",
                                         font=("GOST Type BU", 11, "bold"), bg="#107050", fg="#55d9c0", justify=LEFT)
        self.lower_dev_entry = Entry(self.deviation_frame, width=8, font=("GOST Type BU", 11),
                                         bg="white", fg="#8a140e", validate="key",
                                         validatecommand=(self.root.register(self.validate_accuracy), "%S"))
        self.all_clear_dev_data_btn = Button(self.deviation_frame, width=10, height=1, text="Очистить",
                                    font=("GOST Type BU", 10, "bold"), bg="#4dd8ad", fg="#02231c", relief=GROOVE,
                                    activebackground="#ffc13b", command=self.all_clear_dev_data)
        self.info_dev_data_btn = Button(self.deviation_frame, width=10, height=1, text="Инфо",
                                             font=("GOST Type BU", 10, "bold"), bg="#4dd8ad", fg="#02231c",
                                             relief=GROOVE,
                                             activebackground="#ffc13b", command=self.start_info)
        self.raschet_btn = Button(self.deviation_frame, text="Расчет!", font=("GOST Type BU", 10, "bold"), width=11,
                                  height=3, bg="#4dd8ad", fg="#02231c", activebackground="#ffc13b", relief=GROOVE,
                                  command=self.form_raschet)
        self.upper_dev_entry.insert(0, "+0.1")
        self.lower_dev_entry.insert(0, "-0.1")

        self.deviation_frame.place(in_=self.label, x=15, y=426)
        self.hdr_dev.grid(row=1, column=0, columnspan=4, padx=15, pady=(10, 2), sticky=W)
        self.upper_dev_label.grid(row=2, column=0, padx=(15, 0), pady=2, sticky=W)
        self.upper_dev_entry.grid(row=2, column=1, padx=(4, 0), pady=2, sticky=W)
        self.info_dev_data_btn.grid(row=2, column=2, padx=(4, 0), pady=(2, 4), sticky=W)
        self.lower_dev_label.grid(row=3, column=0, padx=(15, 0), pady=(0, 15), sticky=W)
        self.lower_dev_entry.grid(row=3, column=1, padx=(4, 0), pady=(0, 15), sticky=W)
        self.all_clear_dev_data_btn.grid(row=3, column=2, padx=(4, 0), pady=(0, 15), sticky=W)
        self.raschet_btn.grid(row=2, column=3, rowspan=2, padx=(0, 15), pady=(2, 15), sticky=E + S)


    def all_clear_dev_data(self):
        self.upper_dev_entry.delete(0, END)
        self.lower_dev_entry.delete(0, END)


    def dlina_l3(self, l1, isp_clndr_hod):
        # Вычисляет длину цилиндра по ушам с полным ходом
        return l1 + isp_clndr_hod

    def gamma_angle(self, beta_angle):
        # Высчитывает угол гамма
        return math.radians(180) - ALPHA_ANGLE - beta_angle

    def dlina_r3(self, r1, l1, gamma):
        # Высчитывает длину основания R3
        return math.sqrt(r1 ** 2 + l1 ** 2 - 2 * r1 * l1 * math.cos(gamma))

    def delta_angle(self, r1, r3, l1):
        # Вычисляет угол дельта
        return math.acos((r1 ** 2 + r3 ** 2 - l1 ** 2) / (2 * r1 * r3))

    def dzeta_angle(self, r1, r3, l3):
        # Вычисляет угол дзета
        return math.acos((r1 ** 2 + r3 ** 2 - l3 ** 2) / (2 * r1 * r3))

    def beta_1_angle(self, dzeta, beta_angle, delta):
        # Вычисляет угол эпсилон
        return beta_angle - delta + dzeta

    def epsilon_angle(self, beta_angle, beta_1):
        # Вычисляет угол отклонения качалки
        return beta_1 - beta_angle

    def delta_1_angle(self, epsilon):
        # Вычисляет угол дельта 1
        return (math.radians(180) - epsilon) / 2

    def gamma_1_angle(self, delta_1, gamma):
        # Вычисляет угол гамма 1
        return (math.radians(360) - delta_1 - gamma)

    def degrees_to_dms(self, dec_degrees):
        # Перевод десятичных градусов в градусы, минуты, секунды.
        degrees = math.trunc(dec_degrees)
        minutes = math.trunc((dec_degrees - degrees) * 60)
        seconds = math.ceil((((dec_degrees - degrees) * 60) - minutes) * 60)
        return f"{degrees}˚ {minutes}\' {seconds}\""

    def dlina_l5(self, r3, bata_angle, delta):
        # Вычислает длину L5
        return r3 * math.cos(bata_angle - delta)

    def visota_h1(self, r3, l5, beta_angle, delta):
        # Вычисляет высоту H1
        return math.sqrt(r3 ** 2 + l5 ** 2 - 2 * r3 * l5 * math.cos(beta_angle - delta))




    def form_raschet(self):
        flag = True
        try:
            self.upper_dev = float(self.upper_dev_entry.get())
            self.lower_dev = float(self.lower_dev_entry.get())

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", "ОШИБКА: Не все поля ввода данных заполнены, или введено некорректное значение")
        if flag:
            if self.lower_dev > 0 or self.lower_dev < -0.2:
                flag = False
                self.errmsg.set(f"ОШИБКА: Нижний предел поля допуска должен находиться в интервале значений "
                                f"от «0.0» до «-0.2» (включительно)")
                mb.showwarning("Ошибка", "ОШИБКА: Нижний предел поля допуска должен находиться в интервале значений "
                                                      f"от «0.0» до «-0.2» (включительно)")

            else:
                self.errmsg.set("")
            if flag:
                if self.upper_dev < 0 or self.upper_dev > 0.2:
                    flag = False
                    self.errmsg.set(f"ОШИБКА: Верхний предел поля допуска должен находиться в интервале значений "
                                                       f" от «0.0» до «+0.2» (включительно)")
                    mb.showwarning("Ошибка", "ОШИБКА: Верхний предел поля допуска должен находиться в интервале "
                                             "значений от «0.0» до «+0.2» (включительно)")
                else:
                    self.errmsg.set("")
                if flag:
                    self.start_gen_raschet(self.root, 980, 480, self.l1, self.r1, ALPHA_ANGLE, self.gamma, self.gamma_1,
                                           self.epsilon, self.upper_dev, self.lower_dev)

    def start_gen_raschet(self, root, width, height, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon, upper_dev, lower_dev,
                          title="    Вывод результатов", resizeble=(False, False),
                          icon=r"Data\Ms_graph.ico"):
        GeneralCalc(root,  width, height, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon, upper_dev, lower_dev, title,
                    resizeble, icon)