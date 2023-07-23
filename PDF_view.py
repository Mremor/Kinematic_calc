# importing everything from tkinter
from tkinter import *
# importing ttk for styling widgets from tkinter
from tkinter import ttk
# importing filedialog from tkinter
from tkinter import filedialog as fd
# importing os module
import os

# importing the PDFMiner class from the miner file
from miner import PDFMiner

# creating a class called PDFViewer
class PDFViewer:
    def __init__(self, root, width, height, eq, title="    ГОСТ 23825-79 Кольца защитные ",
                 resizeble=(False, False), icon=None):
        self.root = Toplevel(root)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+440+180")
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            self.root.iconbitmap(icon)
        # path for the pdf doc
        self.path = None
        # state of the pdf doc, open or closed
        self.fileisopen = None
        # author of the pdf doc
        self.author = None
        # name for the pdf doc
        self.name = None
        # the current page for the pdf
        self.current_page = 0
        # total number of pages for the pdf doc
        self.numPages = None
        self.eq = eq

        # creating the menu
        self.menu = Menu(self.root)
        # adding it to the main window
        self.root.config(menu=self.menu)
        # creating a sub menu
        self.filemenu = Menu(self.menu)
        # giving the sub menu a label
        self.menu.add_cascade(label="Файл", menu=self.filemenu)
        # adding a two buttons to the sub menus
        self.filemenu.add_command(label="Открыть файл", command=self.open_file)
        self.filemenu.add_command(label="Выйти", command=self.root.destroy)

        # creating the top frame
        self.top_frame = Frame(self.root, width=875, height=630)
        # placing the frame using inside main window using grid()
        self.top_frame.grid(row=0, column=0)
        # the frame will not propagate
        self.top_frame.grid_propagate(False)
        # creating the bottom frame
        self.bottom_frame = Frame(self.root, width=875, height=50)
        # placing the frame using inside main window using grid()
        self.bottom_frame.grid(row=1, column=0)
        # the frame will not propagate
        self.bottom_frame.grid_propagate(False)

        # creating a vertical scrollbar
        self.scrolly = Scrollbar(self.top_frame, orient=VERTICAL)
        # adding the scrollbar
        self.scrolly.grid(row=0, column=1, sticky=N+S)
        # creating a horizontal scrollbar
        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        # adding the scrollbar
        self.scrollx.grid(row=1, column=0, sticky=W+E)

        # creating the canvas for display the PDF pages
        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=855, height=605)
        # inserting both vertical and horizontal scrollbars to the canvas
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        # adding the canvas
        self.output.grid(row=0, column=0)
        # configuring the horizontal scrollbar to the canvas
        self.scrolly.configure(command=self.output.yview)
        # configuring the vertical scrollbar to the canvas
        self.scrollx.configure(command=self.output.xview)

        # loading the button icons
        self.uparrow_icon = PhotoImage(file=r"Data\_uparrow.png")
        self.downarrow_icon = PhotoImage(file=r"Data\downarrow.png")
        # resizing the icons to fit on buttons
        self.uparrow = self.uparrow_icon.subsample(4, 4)
        self.downarrow = self.downarrow_icon.subsample(4, 4)
        # creating an up button with an icon
        self.upbutton = Button(self.bottom_frame, image=self.uparrow, activebackground="#ffc13b",
                                   command=self.previous_page)
        # adding the button
        self.upbutton.grid(row=0, column=1, padx=(380, 5), pady=8)
        # creating a down button with an icon
        self.downbutton = Button(self.bottom_frame, image=self.downarrow, activebackground="#ffc13b",
                                 command=self.next_page)
        # adding the button
        self.downbutton.grid(row=0, column=3, pady=8)
        # label for displaying page numbers
        self.page_label = ttk.Label(self.bottom_frame, text='страницы')
        # adding the label
        self.page_label.grid(row=0, column=4, padx=5)
        if self.eq:
            self.open_file()
    #     root.bind("<MouseWheel>", self.mouse_wheel)
    #
    # def mouse_wheel(self, event):
    #     global count
    #     if event.num == 5 or event.delta == -120:
    #         count -= 1
    #     if event.num == 4 or event.delta == 120:
    #         count += 1

    # function for opening pdf files
    def open_file(self):
        # open the file dialog
        filepath = fd.askopenfilename(title='Выбор PDF файлов', initialdir=r"Data",
                                          filetypes=(('PDF', '*.pdf'),))
        # checking if the file exists
        if filepath:
            # declaring the path
            self.path = filepath
            # extracting the pdf file from the path
            filename = os.path.basename(self.path)
            # passing the path to PDFMiner
            self.miner = PDFMiner(self.path)
            # getting data and numPages
            data, numPages = self.miner.get_metadata()
            # setting the current page to 0
            self.current_page = 0
            # checking if numPages exists
            if numPages:
                # getting the title
                self.name = data.get('title', filename[:-4])
                # getting the author
                self.author = data.get('author', None)
                self.numPages = numPages
                # setting fileopen to True
                self.fileisopen = True
                # calling the display_page() function
                self.display_page()
                # replacing the window title with the PDF document name
                self.root.title(self.name)

    # the function to display the page
    def display_page(self):
        # checking if numPages is less than current_page and if current_page is less than
        # or equal to 0
        if 0 <= self.current_page < self.numPages:
            # getting the page using get_page() function from miner
            self.img_file = self.miner.get_page(self.current_page)
            # inserting the page image inside the Canvas
            self.output.create_image(0, 0, anchor='nw', image=self.img_file)
            # the variable to be stringified
            self.stringified_current_page = self.current_page + 1
            # updating the page label with number of pages
            self.page_label['text'] = str(self.stringified_current_page) + ' из ' + str(self.numPages)
            # creating a region for inserting the page inside the Canvas
            region = self.output.bbox(ALL)
            # making the region to be scrollable
            self.output.configure(scrollregion=region)

    # function for displaying next page
    def next_page(self):
        # checking if file is open
        if self.fileisopen:
            # checking if current_page is less than or equal to numPages-1
            if self.current_page <= self.numPages - 1:
                # updating the page with value 1
                self.current_page += 1
                # displaying the new page
                self.display_page()

    # function for displaying the previous page
    def previous_page(self):
        # checking if fileisopen
        if self.fileisopen:
            # checking if current_page is greater than 0
            if self.current_page > 0:
                # decrementing the current_page by 1
                self.current_page -= 1
                # displaying the previous page
                self.display_page()






