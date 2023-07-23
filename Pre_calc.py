import math
from tkinter import *
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText

from Gen_calc import GeneralCalc



class PreCalc:
    def __init__(self, root, label, l1, isp_clndr_hod, r1, beta_angle, ALPHA_ANGLE, errmsg):
        self.root = root
        self.label = label
        self.l1 = l1
        self.isp_clndr_hod = isp_clndr_hod
        self.r1 = r1
        self.beta_angle = beta_angle
        self.ALPHA_ANGLE = ALPHA_ANGLE
        self.errmsg = errmsg
        self.hdr_precalc = Label(self.root, width=34, height=1, text="Предварительные результаты",
                    font=("GOST Type BU", 11), wraplength=300, relief= RIDGE, borderwidth=3,
                    bg="#26495c", fg="#e5e5dc")
        self.hdr_dev = Label(self.root, width=121, height=1, text="Ввод допуска для сортировки результатов расчета "
                                                                "по всем искомым параметрам L2, L4, H2.",
                          font=("GOST Type BU", 11), wraplength=800, relief=RIDGE, borderwidth=3,
                          bg="#26495c", fg="#e5e5dc")
        self.st = ScrolledText(self.root, width=26, height=11, bg="#e5e5dc", fg="#26495c", relief=GROOVE, bd= 3,
                               font=("GOST Type BU", 11, "bold"), wrap=WORD, tabs=18, padx=7)
        self.info_block = Label(self.root, width=41, height=0, text="  В сортировке учавствуют ТОЛЬКО "
                                "значения близкие к целочисленным или вещественные значения близкие остатком к 0.5 мм. "
                                                                     "Интерал прохода R2 от 0.5хR1 до 0.75хR1",
                              font=("GOST Type BU", 10, "italic"), wraplength=240, relief=GROOVE, bg="#e5e5dc",
                              fg="#26495c", justify=LEFT)
        self.fon_info = Label(self.root, text="  Информация.\t\t\t\t\t", font=("GOST Type BU", 10, "italic"),
                              width=57, bg="#c66b3d", fg="#26495c", relief=SUNKEN, borderwidth=2, justify=LEFT)
        self.fon_dev_min = Label(self.root, width=41, height=0, bg="#c66b3d", text="Поле допуска от нуля до «-0.2»      ",
                          font=("GOST Type BU", 10, "italic"), fg="#26495c", justify=LEFT, relief=SUNKEN, borderwidth=2)
        self.fon_dev_max = Label(self.root, width=41, height=0, bg="#c66b3d", text="Поле допуска от нуля до «+0.2»      ",
                          font=("GOST Type BU", 10, "italic"), fg="#26495c", justify=LEFT, relief=SUNKEN, borderwidth=2)
        self.deviation_min_label = Label(self.root, width=35, height=0, text="Введите МИНИМАЛЬНОЕ   отклонение в мм от "
                                    "номинала искомых размеров L2, L4, H2 или нажмите «Расчет!» для ввода значения "
                                    "по умолчанию (-0.1)", font=("GOST Type BU", 10, "bold"), wraplength=240,
                                   relief=GROOVE, bg="#e5e5dc", fg="#26495c", justify=LEFT)
        self.deviation_min_entry = Entry(self.root, width=5, font=("GOST Type BU", 10), bg="#e5e5dc", fg="#26495c",
                                    validate="key", validatecommand=(self.label.register(self.validate_amount), "%P"))
        self.deviation_min_entry.insert(0, "-0.1")
        self.deviation_max_label = Label(self.root, width=35, height=0, text="Введите МАКСИМАЛЬНОЕ отклонение в мм от "
                                "номинала искомых размеров L2, L4, H2  или нажмите «Расчет!» для ввода значения по "
                                "умолчанию (+0.1)",
                                   font=("GOST Type BU", 10, "bold"), wraplength=240, relief=GROOVE, bg="#e5e5dc",
                                   fg="#26495c", justify=LEFT)
        self.deviation_max_entry = Entry(self.root, width=5, font=("GOST Type BU", 10), bg="#e5e5dc", fg="#26495c",
                                    validate="key", validatecommand=(self.label.register(self.validate_amount), "%P"))
        self.deviation_max_entry.insert(0, "+0.1")
        self.raschet_btn = Button(self.root, text="Расчет!", font=("GOST Type BU", 10, "bold"), width=11, height=4,
                                  bg="#c4a35a", fg="#26495c", activebackground="#ffc13b", relief=GROOVE, bd=4,
                                  command=self.form_raschet)
        self.run(l1, isp_clndr_hod, r1, beta_angle)

    def dlina_l3(self, l1, isp_clndr_hod):
        # Вычисляет длину цилиндра по ушам с полным ходом
        return l1 + isp_clndr_hod

    def gamma_angle(self, beta_angle):
        # Высчитывает угол гамма
        return math.radians(180) - self.ALPHA_ANGLE - beta_angle

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
        return f"{degrees}˚{minutes}\'{seconds}\""

    def dlina_l5(self, r3, bata_angle, delta):
        # Вычислает длину L5
        return r3 * math.cos(bata_angle - delta)

    def visota_h1(self, r3, l5, beta_angle, delta):
        # Вычисляет высоту H1
        return math.sqrt(r3 ** 2 + l5 ** 2 - 2 * r3 * l5 * math.cos(beta_angle - delta))




    def run(self, l1, isp_clndr_hod, r1, beta_angle):
        # mb.showinfo(f"Введенные значения", f"L1: {l1}, isp_clndr_hod: {isp_clndr_hod}, R1: {r1}, f" beta_angle: {beta_angle}")
        l3 = self.dlina_l3(l1, isp_clndr_hod)
        self.gamma = self.gamma_angle(beta_angle)
        r3 = self.dlina_r3(r1, l1, self.gamma)
        delta = self.delta_angle(r1, r3, l1)
        dzeta = self.dzeta_angle(r1, r3, l3)
        beta_1 = self.beta_1_angle(dzeta, beta_angle, delta)
        self.epsilon = self.epsilon_angle(beta_angle, beta_1)
        l5 = self.dlina_l5(r3, beta_angle, delta)
        h1 = self.visota_h1(r3, l5, beta_angle, delta)
        delta_1 = self.delta_1_angle(self.epsilon)
        self.gamma_1 = self.gamma_1_angle(delta_1, self.gamma)
        self.hdr_precalc.place(in_=self.label, x=642, y=247)
        self.hdr_dev.place(in_=self.label, x=31, y=477)
        self.st.insert("1.1", f"Угол ε равен:{math.degrees(self.epsilon): .5f}˚    "
                              f" ( {self.degrees_to_dms(math.degrees(self.epsilon))} ).\n")
        self.st.insert("2.1", f"\tМежосевое растояние L5 от оси кронштейна "
                              f"рычага-качалки до оси кронштейна испытуемого "
                              f"цилиндра по горизонтали равно: \n/ {round(l5, 4)}   /мм. \n")
        self.st.insert("4.1", f"\tМежосевое растояние H1 от оси кронштейна "
                              f"рычага-качалки до оси кронштейна испытуемого "
                              f"цилиндра по вертикали равно: \n/ {round(h1, 4)}   /мм.")
        self.st.place(in_=self.label, x=640, y=272)
        self.st.tag_config("result", background="#c4a35a", foreground="#26495c", font=("Consolas", 13),
                           justify=CENTER, relief=RAISED, borderwidth=2)
        self.st.tag_add("result", "1.29", "1.40")
        self.st.tag_add("result", "3.1", f"3.{len(str(l5)) - 5}")
        self.st.tag_add("result", "5.1", f"5.{len(str(h1)) - 5}")
        self.info_block.place(in_=self.label, x=534, y=524)
        self.fon_info.place(in_=self.label, x=535, y=503)
        self.fon_dev_min.place(in_=self.label, x=31, y=503)
        self.fon_dev_max.place(in_=self.label, x=283, y=503)
        self.deviation_min_label.place(in_=self.label, x=32, y=524)
        self.deviation_min_entry.place(in_=self.fon_dev_min, x=205, y=-1)
        self.deviation_max_label.place(in_=self.label, x=283, y=524)
        self.deviation_max_entry.place(in_=self.fon_dev_max, x=205, y=-1)
        self.raschet_btn.place(in_=self.label, x=793, y=530)

        #mb.showinfo(f"Предварительный результат", f"Угол ε равен: {math.degrees(epsilon): .5f}˚ "
                                  #f"({self.degrees_to_dms(math.degrees(epsilon))})\n\n"
                                  #f"Межосевое растояние L5 от оси кронштейна\n"
                                  #f"рычага-качалки до оси кронштейна испытуемого\n"
                                  #f"цилиндра равно: {round(l5, 4)} мм\n\n"
                                  #f"Межосевое растояние H1 от оси кронштейна\n"
                                  #f"рычага-качалки до оси кронштейна испытуемого\n"
                                  #f"цилиндра равно: {round(h1, 4)} мм")

    def validate_amount(self, input):
        try:
            x = float(input)
            return True
        except ValueError:
            return False


    def form_raschet(self):
        global deviation_min, deviation_max
        flag = True
        try:
            deviation_min = float(self.deviation_min_entry.get())
            deviation_max = float(self.deviation_max_entry.get())
            if deviation_min > 0 or deviation_min < -0.2:
                flag = False
                self.errmsg.set(f"ОШИБКА: Минимальное отклонение должно находиться в интервале значений "
                                                      f"от «0.0» до «-0.2» (включительно)")
            else:
                self.errmsg.set("")
                if deviation_max < 0 or deviation_max > 0.2:
                    flag = False
                    self.errmsg.set(f"ОШИБКА: Максимальное отклонение должно находиться в интервале значений "
                                                       f" от «0.0» до «0.2» (включительно)")
                else:
                    self.errmsg.set("")

        except ValueError:
            flag = False
            mb.showwarning(f"Ошибка", f"ОШИБКА: "
                                      f"Не все поля ввода данных допуска заполнены корректно!!! ")
        if flag:
            #mb.showinfo(f"Введенные значения", f"deviation_min: {deviation_min}, deviation_max: {deviation_max}")
            #self.out_of_result(910, 609)
            self.start_gen_raschet(self.root, 980, 480, self.l1, self.r1, self.ALPHA_ANGLE, self.gamma, self.gamma_1,
                                   self.epsilon, deviation_min, deviation_max)

            # l1 += (l1_decimal / (10 ** len(str(int(l1_decimal)))))
            # isp_clndr_hod += (isp_clndr_hod_decimal / (10 ** len(str(int(isp_clndr_hod_decimal)))))
            # beta_angle += math.radians(beta_angle_decimal / (10 ** len(str(int(beta_angle_decimal)))))
            # mb.showinfo(f"Введенные значения", f"L1: {l1}, isp_clndr_hod: {isp_clndr_hod}, R1: {r1}, "
            # f"beta_angle: {beta_angle}")
            #self.start_raschet(l1, isp_clndr_hod, r1, beta_angle, self.label, ALPHA_ANGLE)

    def start_gen_raschet(self, root, width, height, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon, deviation_min,
                          deviation_max, title="    Вывод результатов", resizeble=(False, False),
                          icon=r"Data\Ms_graph.ico"):
        GeneralCalc(root,  width, height, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon, deviation_min,
                    deviation_max, title, resizeble, icon)