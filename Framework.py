import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import tkinter as tk

def center_window(master, width=460, height=160):
    """Center a window that calls this method."""
    # get screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))

class ValueInput:
    """Structure the input window"""
    def __init__(self, master):
        self.master = master
        self.frame = tk.LabelFrame(self.master, text="Submit Values")

        self.lbl_ai_acc = tk.Label(master=self.frame, text="AI accuracy: ")
        self.lbl_ai_acc.config(font=("Consolas",20))

        self.lbl_sys_acc = tk.Label(master=self.frame, text="System accuracy: ")
        self.lbl_sys_acc.config(font=("Consolas",20))

        self.lbl_adherence = tk.Label(master=self.frame, text="Adherence: ")
        self.lbl_adherence.config(font=("Consolas",20))

        self.lbl_percent1 = tk.Label(master=self.frame, text="%")
        self.lbl_percent1.config(font=("Consolas",20))
        self.lbl_percent2 = tk.Label(master=self.frame, text="%")
        self.lbl_percent2.config(font=("Consolas",20))
        self.lbl_percent3 = tk.Label(master=self.frame, text="%")
        self.lbl_percent3.config(font=("Consolas",20))

        self.btn_input_values = tk.Button(master=self.frame, text="Input Values", command=self.input_values)
        self.btn_display_fw = tk.Button(master=self.frame, text="Display Framework", command=self.display_framework)
        self.btn_display_details = tk.Button(master=self.frame, text="Display Details", command=self.display_detailedAdherence)

        self.ent_ai_accuracy = tk.Entry(master=self.frame, width=10)
        self.ent_sys_accuracy = tk.Entry(master=self.frame, width=10)
        self.ent_adherence = tk.Entry(master=self.frame, width=10)

        self.frame.pack()
        self.lbl_ai_acc.grid(sticky="W", column=0, row=0)
        self.lbl_sys_acc.grid(sticky="W", column=0, row=1)
        self.lbl_adherence.grid(sticky="W", column=0, row=2)

        self.lbl_percent1.grid(sticky="W", column=2, row=0)
        self.lbl_percent2.grid(sticky="W", column=2, row=1)
        self.lbl_percent3.grid(sticky="W", column=2, row=2)
        self.btn_input_values.grid(column=0, row=3)
        self.btn_display_fw.grid(column=1, row=3)
        self.btn_display_details.grid(column=2, row=3)
        self.ent_ai_accuracy.grid(column=1, row=0)
        self.ent_sys_accuracy.grid(column=1, row=1)
        self.ent_adherence.grid(column=1, row=2)

        center_window(master)

    def display_framework(self):
        """Open new window with pyplot by calling DisplayFramework"""
        self.app = DisplayFramework(None)

    def display_detailedAdherence(self):
        """Open new window to and call DisplayDetailedAdherence constructor"""
        self.DetailWindow = tk.Toplevel(self.master)
        self.app = DisplayDetailedAdherence(self.DetailWindow)

    def all_values_given(self):
        """Returns 0/1/2 depending on how many input values a user has submitted"""
        global ai_accuracy
        global sys_accuracy
        global adherence
        try:
            ai_accuracy is None
        except NameError:
            return 0 #no ai_accuracy given
        try:
            sys_accuracy is None
            adherence is None
        except NameError:
            return 1 #ai_accuracy given but no other values -> just display framework
        return 2 #display framework and also detailed reliance information

    def input_values(self):
        """Input AI accuracy, and optionally System accuracy and Reliance"""
        global ai_accuracy
        global sys_accuracy
        global adherence

        # can't work with all_values_given Function, because then we couldn't set the values
        try:
            ai_accuracy = int(self.ent_ai_accuracy.get())/100
        except ValueError:
            pass
        try:
            sys_accuracy = int(self.ent_sys_accuracy.get())/100
            adherence = int(self.ent_adherence.get())/100
        except ValueError:
            pass

        self.display_values()
    
    def display_values(self):
        """Display selected values in the GUI"""
        self.lbl_display_acc = tk.Label(master=self.frame)
        self.lbl_display_acc.config(font=("Consolas",10), text="") #override previous text -> not working
        self.lbl_display_acc.grid(column=0, row=4, columnspan = 4)

        if self.all_values_given() == 0:
            selected_accuracy_text = "You have not submitted an AI accuracy value yet."
        else:
            selected_accuracy_text = "Your chosen AI accuracy is: " + str(ai_accuracy*100) + "%."
        self.lbl_display_acc.config(text=selected_accuracy_text)

class DisplayFramework:
    """Structure the Framework window"""
    def __init__(self, master):
        #if ai_accuracy is not submitted, display framework with 0% AI Accuracy
        global ai_accuracy #included because otherwise code has an error in the for loop below
        if ValueInput.all_values_given(self) == 0:
            ai_accuracy = 0

        ### fill list with x and y values
        x = np.linspace(0, 1, 101) #reliance from 0-100%
        y = [] #accuracy upper border
        y_neg = [] #accuracy lower border

        for number in x:
            if (1-ai_accuracy+number)>=1: #accuracy at least as high as reliance
                y.append(1-number+ai_accuracy) #e.g. acc 80%, reliance 80%: 1-0.8+0.8 = 100%
            else: #accuracy lower than reliance
                y.append(1-ai_accuracy+number)
                
        for number in x:
            if (1-ai_accuracy-number)<0: #accuracy + reliance higher than 100%
                y_neg.append(ai_accuracy+number-1) #e.g. acc 80%, reliance 80%: 60%
            else:
                y_neg.append(1-ai_accuracy-number) #e.g. acc 80%, reliance 10%: 10%

        ###dividing line between best and worst case
        avg = []
        a = np.array(y)
        b = np.array(y_neg)
        avg = (a+b)/2

        ###min accuracy is the lower boundry: mathematically you can't gain anything by having a lower reliance
        min_acc = round(100 * max(1-(2*(1-ai_accuracy)),0))

        ###generate a list of the set accuracy (e.g. 80%) to display it in the graph
        accuracy_list = []
        for num in x:
            accuracy_list.append(ai_accuracy)

        ###plot framework
        fig = plt.figure(1, (9,9))
        ax = fig.add_subplot(1,1,1)

        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))

        ax.xaxis.set_minor_locator(mtick.MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(mtick.MultipleLocator(0.1))
        plt.xlim([0, max(x)])
        plt.ylim([0, max(y)])

        plt.plot(x, y, "-g", label="Best Case")
        plt.plot(x, y_neg, "-r", label="Worst Case")
        plt.plot(x, avg, "k", label="Average Case")
        plt.plot(x, accuracy_list, linestyle='dotted', label="AI Accuracy")
        # if sys_accuracy and reliance are not specified, their values are set to 999 and are not visible in the graph
        if ValueInput.all_values_given(self) == 2:
            plt.plot(adherence, sys_accuracy, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
        if ai_accuracy > 0.5: #minimum adherence only exists for an accuracy > 50%
            plt.vlines((min_acc/100), 0, 1, "gray", linestyle='dashed', label="Minimum Adherence: "+str(min_acc)+"%")

        plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.07), fancybox=True, shadow=True, ncol=5)
        
        plt.title("AI Accuracy of "+str(100*ai_accuracy)+"%", fontsize=40)
        plt.xlabel("Adherence a", fontsize=15)
        plt.ylabel("Possible System Accuracy A(a)", fontsize=15)
        plt.show()

class DisplayDetailedAdherence:
    """Structure the DetailedAdherence window"""
    def __init__(self, master):
        self.master = master
        ### initialize a new frame
        self.frame_dA = tk.LabelFrame(self.master, text="Adherence Details")
        self.frame_dA.pack()

        # assign values to x_1, ...
        solution_array = self.solve_LSE()
        x_1 = round(solution_array[0], 2)
        x_2 = round(solution_array[1], 2)
        x_3 = round(solution_array[2], 2)
        x_4 = round(solution_array[3], 2)

        x_1_text = "Correct Adherence: " + str(x_1) + "%"
        x_2_text = "Wrong Adherence: " + str(x_2) + "%"
        x_3_text = "Detrimental Override: " + str(x_3) + "%"
        x_4_text = "Corrective Override: " + str(x_4) + "%"

        # fill in the matrix with values
        self.lbl_x_1 = tk.Label(self.frame_dA, text=x_1_text)
        self.lbl_x_2 = tk.Label(self.frame_dA, text=x_2_text)
        self.lbl_x_3 = tk.Label(self.frame_dA, text=x_3_text)
        self.lbl_x_4 = tk.Label(self.frame_dA, text=x_4_text)
        self.lbl_AI = tk.Label(self.frame_dA, text="AI Recommendation")
        self.lbl_AI_correct = tk.Label(self.frame_dA, text="Correct")
        self.lbl_AI_wrong = tk.Label(self.frame_dA, text="Wrong")
        self.lbl_human = tk.Label(self.frame_dA, text="Human action")
        self.lbl_human_adhere = tk.Label(self.frame_dA, text="Adhere")
        self.lbl_human_override = tk.Label(self.frame_dA, text="Override")
        
        self.lbl_x_1.grid(column=2, row=2, sticky="W")
        self.lbl_x_2.grid(column=3, row=2, sticky="W")
        self.lbl_x_3.grid(column=2, row=3, sticky="W")
        self.lbl_x_4.grid(column=3, row=3, sticky="W")
        self.lbl_AI.grid(column=2, row=0, columnspan=2, sticky="W"+"E")
        self.lbl_AI_correct.grid(column=2, row=1)
        self.lbl_AI_wrong.grid(column=3, row=1)
        self.lbl_human.grid(column=0, row=2, rowspan=2, sticky="W"+"E")
        self.lbl_human_adhere.grid(column=1, row=2)
        self.lbl_human_override.grid(column=1, row=3)

        """
        # create lines for the matrix
        canvas = tk.Canvas(self.frame_dA)
        canvas.create_line(15, 25, 200, 25)
        canvas.pack(fill=tk.BOTH, expand=1)
        """

    def solve_LSE(self):
        """Accesses the golobal variables AI accuracy, System Accuracy and Reliance to calculate Correct Adherence, 
        Wrong Adherence, Detrimental Override, Correct Override"""
        # x_1 = Correct Adherence
        # x_2 = Wrong Adherence
        # x_3 = Detrimental Override
        # x_4 = Correct Override

        # x_1+x_4=Observed System Accuracy
        # x_1+x_2=Observed Adherence to AI Rec.
        # x_1+x_3=AI Accuracy
        # x_1+x_2+ x_3+x_4=Total Amount of AI Supported Decisions

        global ai_accuracy, adherence, sys_accuracy
        left_side = np.array([[1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
        right_side = np.array([sys_accuracy, adherence, ai_accuracy, 1])

        return np.linalg.solve(left_side, right_side)

def main(): 
    root = tk.Tk()
    root.title("Accuracy-Adherence-Framework")
    app = ValueInput(root)
    root.mainloop()

if __name__ == '__main__':
    main()