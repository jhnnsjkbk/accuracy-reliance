import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import tkinter as tk
import math

def center_window(master, width=460, height=160):
    """
    This function centers a window (that calls this method) on the screen.

    Args:
    master (tk.Tk): The master tkinter object of the window to center.
    width (int): The width of the window. Default is 460.
    height (int): The height of the window. Default is 160.

    Returns:
    None
    """
    # get screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))

class ValueInput:
    """
    Structure the input window for AI, System accuracy and Adherence.
    It creates a LabelFrame widget with three Labels for AI accuracy, System accuracy, and Adherence and also creates three Entry widgets for inputting the values.
    It also creates three buttons for inputting the values, displaying the framework and displaying detailed adherence.
    """
    def __init__(self, master):
        """
        Initializes the LabelFrame, Labels, Entry widgets and Buttons.
        Args:
        master: master frame to which the widgets are added.
        """
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
        """
        Open new window with pyplot by calling DisplayFramework
        """
        self.app = DisplayFramework(None)

    def display_detailedAdherence(self):
        """
        Open new window and call DisplayDetailedAdherence constructor
        """
        self.DetailWindow = tk.Toplevel(self.master)
        self.app = DisplayDetailedAdherence(self.DetailWindow)

    def all_values_given(self):
        """
        Determines the number of input values submitted by the user.

        Returns:
        int: 0 if no AI accuracy value is given, 1 if AI accuracy value is given but no other values are given, 2 if all values are given.
        """
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
        """
        This function inputs the AI accuracy, system accuracy, and adherence values from the GUI.
        It converts the values to a decimal form by dividing by 100.
        It also calls the display_values function to update the GUI with the inputted values.
        """
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
        """
        This function displays the selected values in the GUI. It creates a label widget, configures its font and 
        grid layout, and sets the text to display. If no AI accuracy value has been submitted yet, a message 
        indicating this is displayed. Otherwise, the chosen AI accuracy is displayed as a percentage.
        """
        self.lbl_display_acc = tk.Label(master=self.frame)
        self.lbl_display_acc.config(font=("Consolas",10), text="") #override previous text -> not working
        self.lbl_display_acc.grid(column=0, row=4, columnspan = 4)

        if self.all_values_given() == 0:
            selected_accuracy_text = "You have not submitted an AI accuracy value yet."
        else:
            selected_accuracy_text = "Your chosen AI accuracy is: " + str(ai_accuracy*100) + "%."
        self.lbl_display_acc.config(text=selected_accuracy_text)

class DisplayFramework:
    """
    The DisplayFramework class is responsible for generating and displaying the graphical representation of the 
    AI accuracy and adherence relationship.

    Attributes:
    master (Tk): Tkinter master window object
    """
    def __init__(self, master):
        """
        Initializes the class and generates the framework graph using matplotlib.
        It takes in the AI accuracy and adherence values, and displays the best, worst, and average cases 
        for the system accuracy.
        Additionally, it also displays the minimum adherence required for the AI accuracy.
        """
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
    """
    This class is used to structure the DetailedAdherence window in a tkinter GUI application. 
    The class displays an adherence matrix and the ADAA (Ability to Discriminate between Right and Wrong AI Advice) value.
    """
    def __init__(self, master):
        """
        Initializes a new frame with the given master and packs it. Assigns values to variables ca, wa, do, co and 
        creates labels with these values to put them in the adherence matrix and calculate the ADAA.
        """
        self.master = master
        ### initialize a new frame
        self.frame_matrix = tk.LabelFrame(self.master, text="Adherence Matrix")
        self.frame_matrix.pack()
        self.frame_adaa = tk.LabelFrame(self.master, text="ADAA")
        self.frame_adaa.pack()

        # assign values to x_1, ...
        solution_array = self.solve_LSE()
        ca = round(solution_array[0], 2)
        wa = round(solution_array[1], 2)
        do = round(solution_array[2], 2)
        co = round(solution_array[3], 2)

        ca_text = "Correct Adherence: " + str(ca) + "%"
        wa_text = "Wrong Adherence: " + str(wa) + "%"
        do_text = "Detrimental Override: " + str(do) + "%"
        co_text = "Corrective Override: " + str(co) + "%"

        # fill in the matrix with values
        self.lbl_ca = tk.Label(self.frame_matrix, text=ca_text)
        self.lbl_wa = tk.Label(self.frame_matrix, text=wa_text)
        self.lbl_do = tk.Label(self.frame_matrix, text=do_text)
        self.lbl_co = tk.Label(self.frame_matrix, text=co_text)
        self.lbl_AI = tk.Label(self.frame_matrix, text="AI Recommendation")
        self.lbl_AI_correct = tk.Label(self.frame_matrix, text="Correct")
        self.lbl_AI_wrong = tk.Label(self.frame_matrix, text="Wrong")
        self.lbl_human = tk.Label(self.frame_matrix, text="Human action")
        self.lbl_human_adhere = tk.Label(self.frame_matrix, text="Adhere")
        self.lbl_human_override = tk.Label(self.frame_matrix, text="Override")
        
        self.lbl_ca.grid(column=2, row=2, sticky="W")
        self.lbl_wa.grid(column=3, row=2, sticky="W")
        self.lbl_do.grid(column=2, row=3, sticky="W")
        self.lbl_co.grid(column=3, row=3, sticky="W")
        self.lbl_AI.grid(column=2, row=0, columnspan=2, sticky="W"+"E")
        self.lbl_AI_correct.grid(column=2, row=1)
        self.lbl_AI_wrong.grid(column=3, row=1)
        self.lbl_human.grid(column=0, row=2, rowspan=2, sticky="W"+"E")
        self.lbl_human_adhere.grid(column=1, row=2)
        self.lbl_human_override.grid(column=1, row=3)

        # display adaa
        adaa = self.solve_adaa()
        self.lbl_adaa = tk.Label(self.frame_adaa, text = ("The ability to discriminate between right and wrong AI advice (ADAA) is: " + str(adaa)))
        self.lbl_adaa.grid(column=0, columnspan=4, row=5, sticky="ew")

        """
        # create lines for the matrix
        canvas = tk.Canvas(self.frame_dA)
        canvas.create_line(15, 25, 200, 25)
        canvas.pack(fill=tk.BOTH, expand=1)
        """

    def solve_LSE(self):
        """
        Calculates the values of Correct Adherence, Wrong Adherence, Detrimental Override, and Correct Override based on 
        Observed System Accuracy, Observed Adherence to AI Recommendations, and AI Accuracy.

        The function uses a matrix equation to solve for the values of the four variables, which are stored as global variables.

        Returns:
        numpy.ndarray: The values of Correct Adherence, Wrong Adherence, Detrimental Override, and Correct Override.

        """
        # x_1 = Correct Adherence
        # x_2 = Wrong Adherence
        # x_3 = Detrimental Override
        # x_4 = Corrective Override

        # x_1+x_4=Observed System Accuracy
        # x_1+x_2=Observed Adherence to AI Rec.
        # x_1+x_3=AI Accuracy
        # x_1+x_2+ x_3+x_4=Total Amount of AI Supported Decisions

        global ai_accuracy, adherence, sys_accuracy
        left_side = np.array([[1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
        right_side = np.array([sys_accuracy, adherence, ai_accuracy, 1])

        return np.linalg.solve(left_side, right_side)
    
    def solve_adaa(self):
        """
        Solve and return the KPI 'Ability to discriminate between right and wrong AI Advice (ADAA)'

        Returns:
        float: The ADAA value rounded to 2 decimal places.
        """
        global ai_accuracy, adherence, sys_accuracy
        if adherence == 0 or adherence ==  1: #otherwise division by zero
            adaa = 0
        else:
            # best case
            if (1-ai_accuracy+adherence)>=1: #accuracy at least as high as reliance
                sys_acc_best = 1-adherence+ai_accuracy #e.g. acc 80%, reliance 80%: 1-0.8+0.8 = 100%
            else: #accuracy lower than reliance
                sys_acc_best = 1-ai_accuracy+adherence

            # worst case
            if (1-ai_accuracy-adherence)<0: #accuracy + reliance higher than 100%
                sys_acc_worst = ai_accuracy+adherence-1 #e.g. acc 80%, reliance 80%: 60%
            else:
                sys_acc_worst = 1-ai_accuracy-adherence #e.g. acc 80%, reliance 10%: 10%

            # adaa
            adaa = round(((sys_accuracy - sys_acc_worst)/(sys_acc_best - sys_acc_worst)) * math.pow(sys_acc_best, 3), 2)
        return(adaa)

def main(): 
    root = tk.Tk()
    root.title("Accuracy-Adherence Framework")
    app = ValueInput(root)
    root.mainloop()

if __name__ == '__main__':
    main()