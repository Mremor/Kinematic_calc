import math
import threading
from tkinter import *
from tkinter import messagebox as mb


class WallThicknessCalc:
    def __init__(self, root, label, press, diam_clndr, yield_strength, safety_factor, add_to_thick,
                 medium_wall_formula_frame, fat_wall_formula_frame, thin_wall_formula_frame):
        self.root = root
        self.label = label
        self.press = press
        self.diam_clndr = diam_clndr
        self.yield_strength = yield_strength
        self.safety_factor = safety_factor
        self.add_to_thick = add_to_thick
        self.medium_wall_formula_frame = medium_wall_formula_frame
        self.fat_wall_formula_frame = fat_wall_formula_frame
        self.thin_wall_formula_frame = thin_wall_formula_frame
        self.meddium_frame = False
        self.fat_frame = False
        self.thin_frame = False
        self.wall_pre_value = StringVar()
        self.middle_wall_value = StringVar()
        self.fat_wall_value = StringVar()
        self.thin_wall_value = StringVar()
        self.t1 = threading.Timer(0.3, self.pre_output_config_yellow)
        self.t2 = threading.Timer(1, self.pre_output_config)
        self.draw_widgets()
        self.run()


    def draw_widgets(self):
        self.pre_output()

    def pre_output(self):
        self.pre_output_frame = LabelFrame(self.root, text=" Промежуточный результат",
                                           font=("GOST Type BU", 11, "bold", "italic"), bg="#561e18", fg="#f22f08")
        self.pre_output_label = Label(self.pre_output_frame, width=25, height=2, font=("GOST Type BU", 11),
                                      textvariable=self.wall_pre_value, bg="#c05640", fg="#212027")

        self.pre_output_frame.place(in_=self.label, x=510, y=90)
        self.pre_output_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        self.t1.start()

        # self.pre_output_frame.configure(bg="#561e18", fg="#f22f08")

    def pre_output_config(self):
        self.pre_output_frame.configure(bg="#561e18", fg="#f22f08")
        if self.meddium_frame == True:
            self.medium_wall_formula_frame.configure(bg="#e2d810", fg="#322e2f")
            self.output()
            self.output_middle_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        if self.fat_frame == True:
            self.fat_wall_formula_frame.configure(bg="#e2d810", fg="#322e2f")
            self.output()
            self.output_fat_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        if self.thin_frame == True:
            self.thin_wall_formula_frame.configure(bg="#e2d810", fg="#322e2f")
            self.output()
            self.output_thin_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)



    def pre_output_config_yellow(self):
        self.pre_output_frame.configure(bg="#e2d810", fg="#322e2f") #ffc13b
        self.t2.start()

    def output(self):
        self.output_frame = LabelFrame(self.root, text=" Результат расчета",
                                           font=("GOST Type BU", 11, "bold", "italic"), bg="#561e18", fg="#f22f08")
        self.output_middle_label = Label(self.output_frame, width=25, height=2, font=("GOST Type BU", 11),
                                      textvariable=self.middle_wall_value, bg="#c05640", fg="#212027")
        self.output_fat_label = Label(self.output_frame, width=25, height=2, font=("GOST Type BU", 11),
                                         textvariable=self.fat_wall_value, bg="#c05640", fg="#212027")
        self.output_thin_label = Label(self.output_frame, width=25, height=2, font=("GOST Type BU", 11),
                                         textvariable=self.thin_wall_value, bg="#c05640", fg="#212027")


        self.output_frame.place(in_=self.label, x=510, y=220)



    def run(self):
        flag = True
        try:
            self.allow_stress = self.yield_strength / self.safety_factor
            self.wall = ((self.press * self.diam_clndr) / ((4 / math.sqrt(3)) * self.allow_stress - self.press)) * 10
            self.ratio = (self.diam_clndr * 10) / self.wall
            self.wall_pre_value.set(f"Предварительная\nтолщина = {round(self.wall, 3)} мм")

        except ZeroDivisionError:
            flag = False
            mb.showwarning("Ошибка", "ОШИБКА: Деление на ноль, введите другие данные.")
        if flag:
            if self.ratio <= 3.2:
                self.fat_frame = True
                self.fat_wall_calc(self.allow_stress)
            elif self.ratio >= 16:
                self.thin_frame = True
                self.thin_wall_calc(self.allow_stress)
            else:
                self.meddium_frame = True
                self.middle_wall_calc(self.wall)


    def middle_wall_calc(self, wall):
        self.middle_wall = wall / 0.85 + self.add_to_thick
        self.middle_wall_value.set(f"Толщина стенки равна\n{round(self.middle_wall, 3)} мм")


    def fat_wall_calc(self, allow_stress):
        try:
            self.fat_wall = (self.diam_clndr / 2) * ((math.sqrt((allow_stress + 0.4 * self.press) /
                                                                (allow_stress - 1.3 * self.press))) - 1)
        except ZeroDivisionError:
            mb.showerror(f"Упс!", f"Похоже что вы разделили на НОЛЬ! Пожалуйста измените значение предела текучести, "
                                  f"коэффициента запаса прочности или давления")
        except ValueError:
            mb.showerror(f"Упс!", f"Похоже что вы хотите разделить на отрицательное число... Замените материал на более "
                                  f"с выским пределом текучести, или уменьшите значение давления или коэффициента "
                                  f"запаса прочности")
        self.fat_wall = self.fat_wall * 10
        self.fat_wall_value.set(f"Толщина стенки равна\n{round(self.fat_wall, 3)} мм")


    def thin_wall_calc(self, allow_stress):
        self.thin_wall = (self.press * self.safety_factor * self.diam_clndr) / (2 * allow_stress)
        self.thin_wall = self.thin_wall * 10
        self.thin_wall_value.set(f"Толщина стенки равна\n{round(self.thin_wall, 3)} мм")
