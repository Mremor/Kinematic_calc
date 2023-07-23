import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


class GeneralCalc:
    def __init__(self, root,  width, height, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon, upper_dev,
                 lower_dev, title=" Результаты", resizeble=(False, False), icon=None):
        self.root = Toplevel(root)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+50")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)
        self.root.configure(bg="#c66b3d")
        self.l1 = l1
        self.r1 = r1
        self.ALPHA_ANGLE = ALPHA_ANGLE
        self.gamma = gamma
        self.gamma_1 = gamma_1
        self.epsilon = epsilon
        self.upper_dev = upper_dev
        self.lower_dev = lower_dev


        res_list = self.run(l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon)
        self.draw_table(res_list)



    def dlina_l6(self, r2, epsilon):
        # Вычисляет длину основания L6
        return r2 * math.sqrt(2 - 2 * math.cos(epsilon))

    def dlina_delta_r1_r2(self, r1, r2):
        # Вычисляет разницу R1 и R2
        return r1 - r2

    def visota_h3(self, delta_r1_r2, gamma):
        # Вычисляет высоту H3
        return delta_r1_r2 * math.sin(math.radians(180) - gamma)

    def dlina_l7(self, delta_r1_r2, h3, gamma):
        # Вычисляет длину L7
        return math.sqrt(delta_r1_r2 ** 2 + h3 ** 2 - 2 * delta_r1_r2 * h3 * math.cos(gamma - math.radians(90)))

    def visota_h2(self, h3, ALPHA_ANGLE):
        # Вычисляет высоту расположения нагрузочного цилиндра H2
        return h3 / math.cos(ALPHA_ANGLE)

    def dlina_l8(self, h2, h3, ALPHA_ANGLE):
        # Вычисляет длину L8
        return math.sqrt(h2 ** 2 + h3 ** 2 - 2 * h2 * h3 * math.cos(ALPHA_ANGLE))

    def dlina_l2(self, l1, l7, l8):
        # Вычисляет длину основания L2 (длина убранного положения нагрузочного цилиндра с навеской)
        return l1 + l7 + l8

    def dlina_l4(self, l6, l2, gamma_1):
        # Вычисляет длину основания L4 (длина выпущенного положения нагрузочного цилиндра с навеской)
        return math.sqrt(l6 ** 2 + l2 ** 2 - 2 * l6 * l2 * math.cos(gamma_1))

    def general_raschet(self, l1, r1, r2, ALPHA_ANGLE, gamma, gamma_1, epsilon):
        # Проводит основной расчет по нахождению длин L2, L4, высоты H2.
        l6 = self.dlina_l6(r2, epsilon)
        delta_r1_r2 = self.dlina_delta_r1_r2(r1, r2)
        h3 = self.visota_h3(delta_r1_r2, gamma)
        l7 = self.dlina_l7(delta_r1_r2, h3, gamma)
        h2 = self.visota_h2(h3, ALPHA_ANGLE)
        l8 = self.dlina_l8(h2, h3, ALPHA_ANGLE)
        l2 = self.dlina_l2(l1, l7, l8)
        l4 = self.dlina_l4(l6, l2, gamma_1)
        res_arg = [r2, l2, l4, h2]
        return res_arg

    def run(self, l1, r1, ALPHA_ANGLE, gamma, gamma_1, epsilon):

        r2 = r1 / 2
        result = []
        while r2 < (r1 * 3) / 4:
            gen_rsch = self.general_raschet(l1, r1, r2, ALPHA_ANGLE, gamma, gamma_1, epsilon)
            temp = []
            for res in gen_rsch:
                nominal = math.trunc(res)
                deviation = res - nominal
                if 1 + self.lower_dev <= deviation < 1 or 0 <= deviation <= self.upper_dev:
                    temp.append(round(res, 4))
                elif 0.5 + self.lower_dev <= deviation < 0.5 or 0.5 <= deviation <= self.upper_dev + 0.5:
                    temp.append(round(res, 4))
            if len(temp) == 4:
                k = r1 / temp[0]
                temp.insert(0, round(k, 4))
                result.append(tuple(temp))
            r2 += 0.5
        if result != []:
            return result
            #mb.showinfo(f"Результаты",
                        #f"result")
        else:
            mb.showinfo(f"Результаты",
                        f"Подходящих под введенный допуск данных не оказалось.\n"
                        f"Измените поле допуска или введите другие параметры рычага-качалки.")
            #for i in result:
                #for char in i:

    def draw_table(self, res_list):
        heads = ["R1/R2", "R2", "L2", "L4", "H2"]
        table = ttk.Treeview(self.root, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor=CENTER)
            table.column(header, anchor=CENTER)
        for row in res_list:
            table.insert('', END, values=row)

        scroll_pane = ttk.Scrollbar(self.root, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=RIGHT, fill=Y)

        table.pack(expand=YES, fill=BOTH)