from tkinter import *
import tkinter.messagebox
import TypingTutor.engine as engine
import time
import logging
import os

__version__ = 2.0

##### creating a log doc to track every word typed ####
# deleting the document everytime we open the program
try:
    open(f"{os.getcwd()}/typing_tracked.txt", 'w').close()
    logging_file_path = f"{os.getcwd()}/typing_tracked.txt"
except FileNotFoundError:
    open(f"{os.getcwd()}/src/TypingTutor/typing_tracked.txt", 'w').close()
    logging_file_path = f"{os.getcwd()}/src/TypingTutor/typing_tracked.txt"


### creating word number counting logger
word_num_logger = logging.getLogger(__name__)
word_num_logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler(logging_file_path)
word_num_logger.addHandler(fileHandler)

formatter = logging.Formatter("%(asctime)s%(name)s%(funcName)s%(message)s")
fileHandler.setFormatter(formatter)

### showing word mistakes logger
mistake_logger = logging.getLogger(__name__)
mistake_logger.setLevel(logging.INFO)

mistake_logger.addHandler(fileHandler)


##### creating memory file #####

startup_bool = 0

# trying the correct file path
try:
    open(f"{os.getcwd()}/typingProgram_memory.txt").close()
    mem_file_path = f"{os.getcwd()}/typingProgram_memory.txt"
except FileNotFoundError:
    open(f"{os.getcwd()}/src/TypingTutor/typingProgram_memory.txt", 'w').close()
    mem_file_path = f"{os.getcwd()}/src/TypingTutor/typingProgram_memory.txt"


with open(mem_file_path, 'r') as f:

    memory = f.read(4)

    if memory[0] == "1":
        startup_bool = 1
    elif memory[0] == "0":
        startup_bool = 0

class GUI:

    def __init__(self, root):

        root.title('typing program')
        root.geometry("1000x600+180+40")
        root.state('zoomed')
        root.iconbitmap(fr"{os.getcwd()}\typingprogramicon.ico")

        #### start up frame ####
        self.startup_frame = Frame(root)

        self.label_frame = Frame(self.startup_frame)
        self.label_frame.pack()

        self.show_again_frame = Frame(self.startup_frame)
        self.show_again_frame.pack(side=LEFT)

        self.next_frame = Frame(self.startup_frame)
        self.next_frame.pack(side=RIGHT)

        self.title = Label(self.label_frame, text="Welcome to the typing program!", font='TimesNewRoman 40 bold',
                           fg='yellow', bg='purple', relief=RAISED, border=4)
        self.title.pack(side=TOP, pady=10)

        self.subtitle1 = Label(self.label_frame, text="Description:", font='Arial 25 underline', fg='green',
                               justify=LEFT)
        self.subtitle1.pack(anchor='w', padx=15)

        content1 = """
 - This program is a typing practicing program, where random text is generated
and you are required to type it. Then statistics about speed and accuracy are
automatically generated along the typing.
        """

        self.content1 = Label(self.label_frame, text=content1, font='Arial 15', justify=LEFT)
        self.content1.pack(anchor='w')

        self.subtitle2 = Label(self.label_frame, text="Speciafications:", font='Arial 25 underline', fg='green',
                               justify=LEFT)
        self.subtitle2.pack(anchor='w', padx=15)

        content2 = """- Instantanious Check, where every time you type a character, it is labeled as Right or wrong.

 - Clear entry field, when you finish typing a word it removed from the entry field.

 - Ongoing Statistics, where after each word the speed and accuracy is updated and presented for the user.

 - Refresh Button, so that you can type a new paragraph.

 - Shortcuts, there's a handful of useful shortcuts

 - Can't get lost, whenever you get lost just click on the escape button and the word and coordinates 
 of the word you should type will appear.

 - Help button, you can always click the help button to know some tips and tricks and the shortcuts.
        """

        self.content2 = Label(self.label_frame, text=content2, font='Arial 15', justify=LEFT)
        self.content2.pack(anchor='w')

        self.nextButton = Button(self.next_frame, text="Skip", font="Arial 10 bold", width=10, bg='yellow', fg='blue',
                                 border=5, command=self.nextButton_func)
        self.nextButton.pack()

        self.startup_bool = IntVar()
        self.startup_bool.set(0)
        self.checkbutton = Checkbutton(self.show_again_frame, text="Don't show this again", variable=self.startup_bool,
                                       command=self.check_checkbutton)
        self.checkbutton.pack()

        #### the main program ####
        self.main_frame = Frame(root)

        ### creating the menubar
        self.menubar = Menu(self.main_frame, tearoff=0)
        root.config(menu=self.menubar)
        ## creating option menu
        self.option_menu = Menu(self.main_frame, tearoff=0)
        self.menubar.add_cascade(label="Paragraph", menu=self.option_menu)
        # normal mode
        self.option_menu.add_command(label='Normal', command=self.normal_mode)
        # random mode
        self.random_menu = Menu(self.main_frame, tearoff=0)
        self.random_menu.add_command(label='Text only', command=self.random_mode1)
        self.random_menu.add_command(label="Text and Numbers", command=self.random_mode2)
        self.random_menu.add_command(label="Text, Numbers and Symbols", command=self.random_mode3)
        self.option_menu.add_cascade(label="random", menu=self.random_menu)
        ## creating the help bar
        # self.help_menu = Menu(self.main_frame, tearoff=0)
        # self.menubar.add_cascade(label="Help")  # heresr

        self.frame1 = Frame(self.main_frame)
        self.frame1.pack()

        self.frame2 = Frame(self.main_frame)
        self.frame2.pack()

        self.frame3 = Frame(self.main_frame)
        self.frame3.pack(pady=30)

        self.frame4 = Frame(self.main_frame)
        self.frame4.pack(side=BOTTOM)

        #creating the paragraph
        with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r') as f:
            memory = f.read(4)
            if memory[1:2] == "n":
                self.paragraph_mode = 'normal'
                self.paragraph_complexity_level = 0
            elif memory[1:3] == "r0":
                self.paragraph_mode = "random"
                self.paragraph_complexity_level = 0
            elif memory[1:3] == "r1":
                self.paragraph_mode = "random"
                self.paragraph_complexity_level = 1
            elif memory[1:3] == "r2":
                self.paragraph_mode = "random"
                self.paragraph_complexity_level = 2

        engine.generate_paragraph(self.paragraph_mode, self.paragraph_complexity_level)

        self.txtToType = Label(self.frame1, text=engine.paragraph, font='Arial 40', relief=RIDGE, border=4, bg='white')
        self.txtToType.pack(pady=30)

        self.statistics_label = Label(self.frame2, text="Errors: -\nAccuracy: -\nSpeed(wpm): -\nSpeed(cpm): -")
        self.statistics_label.pack(side=LEFT, padx=15)

        self.check_label = Label(self.frame2, relief=RIDGE, text="-----", font="Ariel 45", fg='black')
        self.check_label.pack(side=LEFT)

        self.entry_field = Entry(self.frame3, justify=CENTER, font='Arial 40')
        self.entry_field.pack()
        self.entry_field.focus_set()

        self.show_label = Label(self.frame2)
        self.show_label.pack()

        self.help_button = Button(self.frame4, text='Help', fg='blue', command=self.help)
        self.help_button.pack(side=LEFT, padx=10)

        self.refresh_button = Button(self.frame4, text='Refresh', fg='red', command=self.refresh)
        self.refresh_button.pack(side=LEFT, padx=10)

        self.word_num = 0
        self.backspace_num = 0
        self.Char_Entered = False
        self.Char2_Entered = False
        self.First_char_entered = False

        for i in 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+':
            root.bind(i, self.instantanious_check)

        root.bind("<space>", self.SpaceBar)
        root.bind("<BackSpace>", self.backspace)
        root.bind("<Escape>", self.show)
        root.bind("<Alt-r>", self.refresh)

        if startup_bool == True:
            self.startup_frame.pack()
        elif startup_bool == False:
            self.main_frame.pack()

    def normal_mode(self):
        self.paragraph_mode = "normal"
        self.paragraph_complexity_level = 0
        with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
            memory.seek(1)
            memory.write('n')

    def random_mode1(self):
        self.paragraph_mode = 'random'
        self.paragraph_complexity_level = 0
        with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
            memory.seek(1)
            memory.write('r0')

    def random_mode2(self):
        self.paragraph_mode = 'random'
        self.paragraph_complexity_level = 1
        with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
            memory.seek(1)
            memory.write('r1')

    def random_mode3(self):
        self.paragraph_mode = 'random'
        self.paragraph_complexity_level = 2
        with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
            memory.seek(1)
            memory.write('r2')

    def check_checkbutton(self, event=0):
        if self.startup_bool.get() == 1:
            with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
                memory.seek(0)
                memory.write("0")
        elif self.startup_bool.get() == 0:
            with open(f"{os.getcwd()}/typingProgram_memory.txt", 'r+') as memory:
                memory.seek(0)
                memory.write("1")

    def nextButton_func(self, event=0):
        self.startup_frame.destroy()
        self.main_frame.pack()

    def show(self, test):
        x = self.word_num // engine.words_in_line
        y = x * engine.lines
        z = self.word_num - y + 1
        try:
            self.show_label.config(text=f"word: {engine.paragraph_list[self.word_num]}\nrow: {x+1}\ncolumn: {z}")
        except IndexError:
            self.check_label.config(text="You've finished this paragraph!", font="Ariel 45", fg='black')


    def instantanious_check(self, test):
        if self.First_char_entered == False:
            self.First_char_entered = True
            self.start = time.time()
        try:
            if self.entry_field.get() == engine.paragraph_list[self.word_num][:len(self.entry_field.get())]:
                self.check_label.config(text="right", font="Ariel 45", fg='green')
                self.Char_Entered = True
            else:
                self.check_label.config(text='wrong', font='Ariel 45', fg='red')
                self.Char_Entered = True
                word_num_logger.info(f"Word number typed: {self.word_num+1}")
                mistake_logger.info(
                    f"Letter should've written correctly: {engine.paragraph_list[self.word_num][:len(self.entry_field.get())]}")
        except IndexError:
            self.check_label.config(text="You've finished this paragraph!", font="Ariel 45", fg='black')

    def SpaceBar(self, test):
        if self.First_char_entered == False:
            self.First_char_entered = True
            self.start = time.time()
        try:
            if self.entry_field.get() == f"{engine.paragraph_list[self.word_num]} ":
                engine.paragraph_dict[engine.paragraph_list[self.word_num]] = True
                self.typed_word = self.entry_field.get().strip()
            elif self.entry_field.get() != engine.paragraph_list[self.word_num]:
                engine.paragraph_dict[engine.paragraph_list[self.word_num]] = False
                self.typed_word = self.entry_field.get().strip()
        except IndexError:
            self.check_label.config(text="You've finished this paragraph!", font="Ariel 45", fg='black')
        self.do_statistics(test)
        self.word_num += 1

        self.entry_field.delete(0, len(self.entry_field.get()))
        self.Char_Entered = False

        end = time.time()
        time_diff = end - self.start

        ### calculating speed ###
        x = 60 / time_diff
        speed = self.word_num * x
        speed = round(speed)

        self.statistics_label.config(
            text=f"Errors:  {25-self.number_of_correct}\nAccuracy:  {self.percentage}%\nSpeed(wpm):  {speed}\nSpeed(cpm):  {speed*5}")
        word_num_logger.info(f"Word number typed: {self.word_num+1}")

        self.show_label.config(text="")

    def backspace(self, test):
        if self.First_char_entered == False:
            pass
        else:
            if self.entry_field.get() == "" and self.Char_Entered == True:
                self.Char2_Entered = True
                self.Char_Entered = False
                word_num_logger.info(f"Word number typed: {self.word_num+1}")
            elif self.entry_field.get() == "" and self.Char_Entered == False:
                self.word_num -= 1
                self.Char_Entered = False
                self.entry_field.insert(1,self.typed_word)
                word_num_logger.info(f"Word number typed: {self.word_num+1}")
            elif self.entry_field.get() == "" and self.Char2_Entered == True:
                self.word_num -= 1
                self.Char_Entered = False
                word_num_logger.info(f"Word number typed: {self.word_num+1}")

    def do_statistics(self, test):
        self.number_of_correct = 0
        for i in engine.paragraph_dict.values():
            if i == True:
                self.number_of_correct += 1

        self.percentage = (self.number_of_correct / 25) * 100
        self.percentage = round(self.percentage)

    def help(self):
        information = """  Did you know?\n
 - wpm stands for word per minute and cpm stands for character per minute\n
 - Before you refresh you can know exactly when and what did you type, this is stored in typing_tracked.txt document inside your system files, good luck finding this file out ;)

        """
        Shortcuts = """  Shortcuts:\n
 - esc -->  Show the word and coordinate of the word you should type.\n
 - Shift + r -->  Refresh the program so you can start typing a new paragraph all over.
"""
        ShortCuts_box = tkinter.messagebox.showinfo('Tips and Tricks', f"{Shortcuts}\n\n{information}")

    def refresh(self, test=0):
        engine.generate_paragraph(self.paragraph_mode, self.paragraph_complexity_level)
        self.txtToType.config(text=engine.paragraph)
        self.word_num = 0
        self.backspace_num = 0
        self.Char_Entered = False
        self.Char2_Entered = False
        self.First_char_entered = False
        self.entry_field.delete(0, len(self.entry_field.get()))
        open(f"{os.getcwd()}/typing_tracked.txt", 'w').close()


if __name__ == '__main__':
    root = Tk()
    application = GUI(root)
    root.mainloop()
