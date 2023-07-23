from tkinter import *

from PIL import Image as PilImage
from PIL import ImageTk

from Extra_menu import AdvanceMenu
from Get_info import Gathering_info

MSG1 = "     ВНИМАНИЕ!!! Калькулятор предназначен для\n" \
       " кинематических расчетов цилиндровых стендов для\n" \
       " испытаний на ресурс с нагрузками на дожатие на\n" \
       " испытуемом цилиндре до 10 000 кгс. Все проведенные\n" \
       " вычисления носят рекомендательный характер\n" \
       " и не несут ответственности за их исполнение."

MSG2 = "     Раздел проектирования гидроцилиндров включает\n" \
       " в себя подразделы подбора уплотнительных колец,\n" \
       " расчет усилия гидроцилиндров, расчет толщины\n" \
       " стенки гильзы, расчет резьбовых соединений, расчет\n" \
       " проушины и др. Все выполняемые расчеты приведены\n" \
       " для ознакомления и не учавствуют в разработках."

MSG3 = "     Используемая литература:\n" \
       " Марутов В.А., Павловский С.А. - Гидроцилиндры.\n" \
       " Конструкция и расчет - 1966 г.\n" \
       "     Интелектуальная собственность принадлежит \n" \
       " АО Авиаагрегат, Бюро нестандартного оборудования,\n" \
       " 2023 год."





class Window:
    def __init__(self, width, height, title="MyWindow", resizeble=(False, False),
                 icon=r"Data\kin2_calc.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+320+185")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.configure(bg="#c66b3d")
        if icon:
            self.root.iconbitmap(icon)
        # Импорт картинки для кнопки запуска калькулятора
        img = PilImage.open(f"Data\calc2.png")
        img_calc = img.resize((64, 64), PilImage.ANTIALIAS)
        self.photo_image_calc = ImageTk.PhotoImage(img_calc)
        # Импорт картинки для кнопки запуска расчета гидроцилиндра и подбора колец
        img_hydro = PilImage.open(f"Data\hydro.ico")
        img_hydro = img_hydro.resize((64, 64), PilImage.ANTIALIAS)
        self.photo_image_hydro = ImageTk.PhotoImage(img_hydro)


    def draw_label(self):
        self.background_img = PhotoImage(file=r"Data\diver_800x450.png")
        self.label = Label(self.root, image=self.background_img)
        self.label.image = self.background_img
        self.label.place(x=-2, y=0)

    def run(self):
        self.draw_label()
        self.draw_widgets()
        self.root.mainloop()

    def start_kinematic_calc(self):
        self.root.withdraw()
        MainWindow.create_kinematic(1300, 680)
        self.root.deiconify()

    def start_create_hydro(self):
        self.root.withdraw()
        MainWindow.create_hydro(1280, 680)
        self.root.deiconify()

    def draw_widgets(self):
        self.left_frame = LabelFrame(self.root, text=" Предупреждение ", font=("GOST Type BU", 10, "bold"),
                                     bg="#05716c", fg="#1fbfb8")
        self.right_frame = LabelFrame(self.root, text=" Возможности ", font=("GOST Type BU", 10, "bold"),
                                     bg="#05716c", fg="#1fbfb8")
        self.disclamer = Label(self.left_frame, width=52, height=7, text=MSG1, font=("GOST Type BU", 10, "bold"),
                               bg="#031163", fg="#1978a5", relief=GROOVE, bd=3, justify=LEFT)
        self.disclamer2 = Label(self.left_frame, width=52, height=7, text=MSG2, font=("GOST Type BU", 10, "bold"),
                                bg="#031163", fg="#1978a5", relief=GROOVE, bd=3, justify=LEFT)
        self.disclamer3 = Label(self.left_frame, width=52, height=7, text=MSG3, font=("GOST Type BU", 10, "bold"),
                                bg="#031163", fg="#1978a5", relief=GROOVE, bd=3, justify=LEFT)
        self.kin_calc_label = Label(self.right_frame, width=19, height=2, text="Калькулятор кинематики",
                              font=("GOST Type BU", 10, "bold"), wraplength=100, bg="#031163", fg="#1fbfb8")
        self.kin_calc_btn = Button(self.right_frame, image=self.photo_image_calc, bg="#1e3d59",
                                   activebackground="#ffc13b", command=self.start_kinematic_calc)
        self.hydro_label = Label(self.right_frame, width=19, height=2, text="Проектирование\nгидроцилиндров",
                                 font=("GOST Type BU", 10, "bold"), bg="#031163", fg="#1fbfb8")
        self.hydro_btn = Button(self.right_frame, image=self.photo_image_hydro, bg="#1fbfb8",
                                      activebackground="#ffc13b", command=self.start_create_hydro)
        self.build_version = Label(self.root, width=18, height=2, text="Версия 2.03 .420",
                                   font=("GOST Type BU", 10, "italic"), wraplength=100, bg="#e75874", fg="#322514")

        self.left_frame.place(in_=self.label, x=10, y=30)
        self.right_frame.place(in_=self.label, x=420, y=30)
        self.disclamer.grid(row=1, column=0, padx=15, pady=(10, 5), sticky=W)
        self.disclamer2.grid(row=2, column=0, padx=15, pady=(0, 5), sticky=W)
        self.disclamer3.grid(row=3, column=0, padx=15, pady=(0, 10), sticky=W)
        self.kin_calc_label.grid(row=1, column=0, padx=10, pady=(10, 6))
        self.kin_calc_btn.grid(row=2, column=0, padx=45, pady=(0, 6), sticky=W)
        self.hydro_label.grid(row=3, column=0, padx=10, pady=(0, 6))
        self.hydro_btn.grid(row=4, column=0, padx=45, pady=(0, 6), sticky=W)
        self.build_version.place(in_=self.label, x=445, y=330)

    def create_kinematic(self, width, height, title="    Калькулятор кинематики ресурсных стендов",
                         resizeble=(True, True), icon=r"Data\kin2_calc.ico"):
        Gathering_info(self.root, width, height, title, resizeble, icon)

    def create_hydro(self, width, height, title="    Проектирование гидроцилиндров",
                         resizeble=(False, False), icon=r"Data\hydro.ico"):
        AdvanceMenu(self.root, width, height, title, resizeble, icon)


if __name__ == "__main__":
    MainWindow = Window(800, 450, "    Главное меню")
    MainWindow.run()