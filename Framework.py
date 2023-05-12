import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import tkinter as tk
import math

def center_window(master, width=400, height=300):
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
    Structure the input window for AI, System accuracy and reliance.
    It creates a LabelFrame widget with three Labels for AI accuracy, System accuracy, and reliance and also creates three Entry widgets for inputting the values.
    It also creates three buttons for inputting the values, displaying the framework and displaying detailed adherence.
    """
    def __init__(self, master):
        """
        Initializes the LabelFrame, Labels, Entry widgets and Buttons.
        Args:
        master: master frame to which the widgets are added.
        """
        self.master = master
        self.frame_values = tk.LabelFrame(self.master, text="Submit Values")
        self.frame_comparison = tk.LabelFrame(self.master, text="Additional comparison values (optional)")
        self.frame_btns = tk.Frame(self.master)

        self.frame_values.grid(column=0, row=0, pady=10, padx=5)
        self.frame_comparison.grid(column=0, row=1, pady=10, padx=5)
        self.frame_btns.grid(column=0, row=2, pady=10, padx=5)

        self.lbl_ai_acc = tk.Label(master=self.frame_values, text="AI accuracy: ")
        self.lbl_ai_acc.config(font=("Consolas",20))

        self.lbl_sys_acc = tk.Label(master=self.frame_values, text="System accuracy: ")
        self.lbl_sys_acc.config(font=("Consolas",20))

        self.lbl_sys_acc2 = tk.Label(master=self.frame_comparison, text="System accuracy 2: ")
        self.lbl_sys_acc2.config(font=("Consolas",20))

        self.lbl_reliance = tk.Label(master=self.frame_values, text="Reliance: ")
        self.lbl_reliance.config(font=("Consolas",20))

        self.lbl_reliance2 = tk.Label(master=self.frame_comparison, text="Reliance 2: ")
        self.lbl_reliance2.config(font=("Consolas",20))

        self.lbl_human_acc = tk.Label(master=self.frame_values, text="Human accuracy: ")
        self.lbl_human_acc.config(font=("Consolas",20))

        self.lbl_percent1 = tk.Label(master=self.frame_values, text="%")
        self.lbl_percent1.config(font=("Consolas",20))
        self.lbl_percent2 = tk.Label(master=self.frame_values, text="%")
        self.lbl_percent2.config(font=("Consolas",20))
        self.lbl_percent3 = tk.Label(master=self.frame_values, text="%")
        self.lbl_percent3.config(font=("Consolas",20))
        self.lbl_percent4 = tk.Label(master=self.frame_values, text="%")
        self.lbl_percent4.config(font=("Consolas",20))
        self.lbl_percent5 = tk.Label(master=self.frame_comparison, text="%")
        self.lbl_percent5.config(font=("Consolas",20))
        self.lbl_percent6 = tk.Label(master=self.frame_comparison, text="%")
        self.lbl_percent6.config(font=("Consolas",20))

        self.btn_input_values = tk.Button(master=self.frame_btns, text="Input Values", command=self.input_values)
        self.btn_display_fw = tk.Button(master=self.frame_btns, text="Display Framework", command=self.display_framework)
        self.btn_display_details = tk.Button(master=self.frame_btns, text="Display Details", command=self.display_detailedInformation)

        self.ent_ai_accuracy = tk.Entry(master=self.frame_values, width=10)
        self.ent_sys_accuracy = tk.Entry(master=self.frame_values, width=10)
        self.ent_reliance = tk.Entry(master=self.frame_values, width=10)
        self.ent_human_accuracy = tk.Entry(master=self.frame_values, width=10)
        self.ent_sys_accuracy2 = tk.Entry(master=self.frame_comparison, width=10)
        self.ent_reliance2 = tk.Entry(master=self.frame_comparison, width=10)

        #self.frame.pack()
        #pack frame_values
        self.lbl_ai_acc.grid(sticky="W", column=0, row=0)
        self.lbl_sys_acc.grid(sticky="W", column=0, row=1)
        self.lbl_reliance.grid(sticky="W", column=0, row=2)
        self.lbl_human_acc.grid(sticky="W", column=0, row=3)
        self.lbl_percent1.grid(sticky="W", column=2, row=0)
        self.lbl_percent2.grid(sticky="W", column=2, row=1)
        self.lbl_percent3.grid(sticky="W", column=2, row=2)
        self.lbl_percent4.grid(sticky="W", column=2, row=3)

        self.ent_ai_accuracy.grid(column=1, row=0)
        self.ent_sys_accuracy.grid(column=1, row=1)
        self.ent_reliance.grid(column=1, row=2)
        self.ent_human_accuracy.grid(column=1, row=3)

        #pack frame_comparison
        self.lbl_sys_acc2.grid(sticky="W", column=0, row=0)
        self.lbl_reliance2.grid(sticky="W", column=0, row=1)        
        self.lbl_percent5.grid(sticky="W", column=2, row=0)
        self.lbl_percent6.grid(sticky="W", column=2, row=1)

        self.ent_sys_accuracy2.grid(column=1, row=0)
        self.ent_reliance2.grid(column=1, row=1)

        #pack frame_btns
        self.btn_input_values.grid(column=0, row=0)
        self.btn_display_fw.grid(column=1, row=0)
        self.btn_display_details.grid(column=2, row=0)

        center_window(master)

    def display_framework(self):
        """
        Open new window with pyplot by calling DisplayFramework
        """
        self.app = DisplayFramework(None)

    def display_detailedInformation(self):
        """
        Open new window and call DisplayDetailedInformation constructor
        """
        self.DetailWindow = tk.Toplevel(self.master)
        self.app = DisplayDetailedInformation(self.DetailWindow)

    def all_values_given(self):
        """
        Determines the number of input values submitted by the user.

        Returns:
            int: The number of input values submitted:
                - 0: If no AI accuracy value is given.
                - 1: If only the human accuracy value is not given.
                - 2: If only AI accuracy and human accuracy values are given.
                - 3: If only AI accuracy given.
                - 4: If all values (AI accuracy, system accuracy, reliance, human accuracy) are given.
        """
        
        global ai_accuracy
        global sys_accuracy
        global reliance
        global human_accuracy
        try:
            ai_accuracy is None
        except NameError:
            return 0 #no ai_accuracy given
        try:
            human_accuracy is None
        except NameError:
            try:
                sys_accuracy is None
                reliance is None
            except NameError:
                return 3 #only ai accuracy given -> just display framework
            return 1 #only human_accuracy not given -> detailed reliance info available
        try:
            sys_accuracy is None
            reliance is None          
        except NameError:
            return 2 #ai_accuracy and human_accuracy given but no other values -> just display framework
        try:
            human_accuracy is None
            sys_accuracy is None
            reliance is None
        except NameError:
            return 3  #ai_accuracy given but no other values -> just display framework    
        return 4 #all info given: display framework and also detailed reliance information
         
    def comparison_mode_active(self):
        """
        If a second system accuracy and reliance level are given, a second point is displayed to compare.

        Returns:
        int: 0 if no comparison mode is not active, 1 if comparison mode is active
        """
        global sys_accuracy2
        global reliance2
        try:
            sys_accuracy2 is None
            reliance2 is None
        except NameError:
            return 0
        return 1

    def input_values(self):
        """
        This function inputs the AI accuracy, system accuracy, and reliance values from the GUI.
        It converts the values to a decimal form by dividing by 100.
        It also calls the display_values function to update the GUI with the inputted values.
        """
        global ai_accuracy
        global sys_accuracy
        global reliance
        global human_accuracy
        global sys_accuracy2
        global reliance2

        # can't work with all_values_given Function, because then we couldn't set the values
        try:
            ai_accuracy = float(self.ent_ai_accuracy.get())/100
        except ValueError:
            pass
        try:
            sys_accuracy = float(self.ent_sys_accuracy.get())/100
            reliance = float(self.ent_reliance.get())/100
        except ValueError:
            pass
        try:
            human_accuracy = float(self.ent_human_accuracy.get())/100
        except ValueError:
            pass
        try:
            sys_accuracy2 = float(self.ent_sys_accuracy2.get())/100
            reliance2 = float(self.ent_reliance2.get())/100
        except ValueError:
            pass

        #self.display_values() unnecessary
    
    def display_values(self):
        """
        This function displays the selected values in the GUI. It creates a label widget, configures its font and 
        grid layout, and sets the text to display. If no AI accuracy value has been submitted yet, a message 
        indicating this is displayed. Otherwise, the chosen AI accuracy is displayed as a percentage.
        """
        self.lbl_display_acc = tk.Label(master=self.frame)
        self.lbl_display_acc.config(font=("Consolas",10), text="") #override previous text -> not working
        self.lbl_display_acc.grid(column=0, row=7, columnspan = 4)

        if self.all_values_given() == 0:
            selected_accuracy_text = "You have not submitted an AI accuracy value yet."
        else:
            selected_accuracy_text = "Your chosen AI accuracy is: " + str(ai_accuracy*100) + "%."
        self.lbl_display_acc.config(text=selected_accuracy_text)

class DisplayFramework:
    """
    The DisplayFramework class is responsible for generating and displaying the graphical representation of the 
    AI accuracy and reliance relationship.

    Attributes:
    master (Tk): Tkinter master window object
    """
    def __init__(self, master):
        """
        Initializes the class and generates the framework graph using matplotlib.
        It takes in the AI accuracy and reliance values, and displays the best, worst, and average cases 
        for the system accuracy.
        Additionally, it also displays the minimum reliance required for the AI accuracy.
        """
        #if ai_accuracy is not submitted, display framework with 0% AI Accuracy
        global ai_accuracy
        human_accuracy_list = []

        if ValueInput.all_values_given(self) == 0:
            ai_accuracy = 0

        ### fill list with x and y values
        x = np.linspace(0, 1, 10001) #reliance from 0-100% in 0.01% steps
        y = [] #accuracy upper border 
        y_neg = [] #accuracy lower border

        for number in x:
            if number>ai_accuracy: #reliance higher than ai_accuracy
                y.append(1-number+ai_accuracy) #e.g. acc 80%, reliance 80%: 1-0.8+0.8 = 100%
            else: #reliance lower than or equal to ai_accuracy
                y.append(1-ai_accuracy+number)
                
        for number in x:
            if (ai_accuracy+number)>1: #accuracy + reliance higher than 100%
                y_neg.append(ai_accuracy+number-1) #e.g. acc 80%, reliance 80%: 60%
            else:
                y_neg.append(1-ai_accuracy-number) #e.g. acc 80%, reliance 10%: 10%

        ###dividing line between best and worst case
        #avg = []
        #a = np.array(y)
        #b = np.array(y_neg)
        #avg = (a+b)/2

        ###random case
        random = []
        for number in x:
            rdm_value = ai_accuracy*number + (1-ai_accuracy)*(1-number)
            random.append(rdm_value)

        ###min reliance is the lower boundry: mathematically you can't gain appropriate reliance by having a lower reliance
        if ValueInput.all_values_given(self) == 2 or ValueInput.all_values_given(self) == 4: #human acc given
            if human_accuracy > ai_accuracy:
                for reliance_value in x:
                    if reliance_value<=ai_accuracy: #reliance lower than or equal to ai_accuracy, best case line rising
                        best_case_value = round(1-ai_accuracy+reliance_value, 5)
                        if math.isclose(human_accuracy, best_case_value, abs_tol=10**-5):
                            min_rel = round(100*reliance_value, 2)
            else:
                min_rel = round(100 * max(1-(2*(1-ai_accuracy)),0), 2)
        else:
            min_rel = round(100 * max(1-(2*(1-ai_accuracy)),0), 2)

        ###max reliance is the upper boundry: mathematically you can't gain appropriate reliance by having a higher reliance
        if ValueInput.all_values_given(self) == 2 or ValueInput.all_values_given(self) == 4: #human acc given
            if human_accuracy > ai_accuracy:
                for reliance_value in x:
                    if reliance_value>ai_accuracy: #reliance higher than ai_accuracy, best case line is falling
                        best_case_value = round(1-reliance_value+ai_accuracy, 5)
                        if math.isclose(human_accuracy, best_case_value, abs_tol=10**-5):
                            max_rel = round(100*reliance_value,2)

        ###generate a list of AI accuracy values (e.g. 80%) to display it in the graph
        ai_accuracy_list = []
        for num in x:
            ai_accuracy_list.append(ai_accuracy)

        ###generate a list of human accuracy values (e.g. 80%) to display it in the graph
        if ValueInput.all_values_given(self) == 2 or ValueInput.all_values_given(self) == 4:
            for num in x:
                human_accuracy_list.append(human_accuracy)

        ###plot framework
        fig = plt.figure(1, figsize=(9,9))
        ax = fig.add_subplot(1,1,1)

        ## configure axes
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))

        ax.xaxis.set_minor_locator(mtick.MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(mtick.MultipleLocator(0.1))
        plt.axis('scaled')
        plt.xlim([0, max(x)])
        plt.ylim([0, max(y)])
        
        ## draw all the lines and point into the graph
        ax.plot(x, y, "green", label="Best Case")
        ax.plot(x, y_neg, "red", label="Worst Case")
        ax.plot(x, random, "k", label="Random Case")
        ax.plot(x, ai_accuracy_list, "dimgrey", linestyle='dotted', label="AI Accuracy")

        # all_values_given=1: only human acc not given, 2: only ai and human acc given, 3: only ai acc given, 4: all given
        if ValueInput.all_values_given(self) == 1:
            ax.plot(reliance, sys_accuracy, marker="o", markersize=7, markeredgecolor="black", markerfacecolor="black")
        if ValueInput.all_values_given(self) == 2:
            human_acc_legend = round(100*human_accuracy, 2)
            ax.plot(x, human_accuracy_list, "darkgrey", linestyle='dashdot', label="Human Accuracy: "+str(human_acc_legend)+"%")
        if ValueInput.all_values_given(self) == 4:
            human_acc_legend = round(100*human_accuracy, 2)
            ax.plot(reliance, sys_accuracy, marker="o", markersize=7, markeredgecolor="black", markerfacecolor="black")
            ax.plot(x, human_accuracy_list, "darkgrey", linestyle='dashdot', label="Human Accuracy: "+str(human_acc_legend)+"%")
        if ai_accuracy >= 0.5: #minimum reliance only exists for an accuracy >= 50%
            ax.vlines((min_rel/100), 0, 1, "orange", linestyle='dashed', label="Minimum Reliance: "+str(min_rel)+"%")

        try: #if max rel is defined
            ax.vlines((max_rel/100), 0, 1, "red", linestyle='dotted', label="Maximum Reliance: "+str(max_rel)+"%")
        except UnboundLocalError:
            pass

        if ValueInput.comparison_mode_active(self) == 1:
            ax.plot(reliance2, sys_accuracy2, marker="o", markersize=7, markeredgecolor="cornflowerblue", 
                    markerfacecolor="cornflowerblue")

        #Enable Grid layout
        #ax.set_axisbelow(True)
        #ax.yaxis.grid(color='gray', linestyle='solid')
        #ax.xaxis.grid(color='gray', linestyle='solid')

        ## configure labels and legend
        ai_acc_title = round(100*ai_accuracy, 2)
        ax.set_title("AI Accuracy of "+str(ai_acc_title)+"%", fontsize=30)
        ax.set_xlabel("Reliance r", fontsize=15)
        ax.set_ylabel("Possible System Accuracy Aₛᵧₛ(r)", fontsize=15)
        try:
            max_rel is None
            min_rel is None
            ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.07), fancybox=True, shadow=True, ncol=3, fontsize = 10)
        except UnboundLocalError:
            ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.07), fancybox=True, shadow=True, ncol=4, fontsize = 10)
        plt.tight_layout()
        plt.show()

class DisplayDetailedInformation:
    """
    This class is used to structure the DetailedInformation window in a tkinter GUI application. 
    The class displays an adherence matrix and the ADAA (Ability to Discriminate between Right and Wrong AI Advice) value.
    """
    def __init__(self, master):
        """
        Initializes frames with the given master and packs them. Assigns values to variables ca, wa, do, co and 
        creates labels with these values to put them in the adherence matrix and calculate the ADAA.
        """
        self.master = master

        ### initialize frames
        self.frame_interval = tk.LabelFrame(self.master, text="Interval of possible System Accuracy")
        self.frame_interval.grid(column=0, row=0, pady=10, padx=5)
        self.frame_matrix = tk.LabelFrame(self.master, text="Adherence Matrix (values only valid for binary decision cases)")
        self.frame_matrix.grid(column=0, row=1, pady=10, padx=5)
        self.frame_adaa = tk.LabelFrame(self.master, text="ADAA")
        self.frame_adaa.grid(column=0, row=2, pady=10, padx=5)
        self.frame_probability = tk.LabelFrame(self.master, text="Probabilities (values only valid for binary decision cases)")
        self.frame_probability.grid(column=0, row=3, pady=10, padx=5)

        ### display Interval of possible System Accuracy
        sysAccuracyWorstCase = self.return_sysAccuracyWorstCase()
        sysAccuracyBestCase = self.return_sysAccuracyBestCase()
        sysAccuracyWorstCase_text = "The minimum potential System Accuracy is: "
        sysAccuracyBestCase_text = "The maximum potential System Accuracy is: "

        self.lbl_minSysAcc = tk.Label(self.frame_interval, text = (sysAccuracyWorstCase_text+str(sysAccuracyWorstCase))+"%.")
        self.lbl_maxSysAcc = tk.Label(self.frame_interval, text = (sysAccuracyBestCase_text+str(sysAccuracyBestCase))+"%.")
        self.lbl_minSysAcc.grid(column=0, row=0)
        self.lbl_maxSysAcc.grid(column=1, row=0)

        ### display adherence matrix
        # assign values to x_1, ...
        solution_array = self.solve_LSE()
        ca = round(solution_array[0] * 100, 2)
        wa = round(solution_array[1] * 100, 2)
        do = round(solution_array[2] * 100, 2)
        co = round(solution_array[3] * 100, 2)

        ca_text = "Correct Adherence: " + str(ca) + "%"
        wa_text = "Wrong Adherence: " + str(wa) + "%"
        do_text = "Wrong Override: " + str(do) + "%"
        co_text = "Correct Override: " + str(co) + "%"

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

        ### display adaa
        adaa = self.solve_adaa()
        adaa_text = "The ability to discriminate between right and wrong AI advice (ADAA) given your reliance level is: "
        self.lbl_adaa = tk.Label(self.frame_adaa, text = (adaa_text + str(adaa)))
        self.lbl_adaa.grid(column=0, columnspan=4, row=5, sticky="ew")

        ### display the probabilities
        ## display point probability to achieve observed system accuracy given random guessing of user
        point_prob_sys_accuracy, prob_at_above_sys_accuracy = self.calculate_probability()
        point_prob_sys_accuracy_text = ("Point probability to reach observed system accuracy by randomly choosing " +
                                  "when to adhere to AI advice (given the observed reliance): ")
        self.lbl_point_prob_sys_accuracy = tk.Label(self.frame_probability, text = (point_prob_sys_accuracy_text 
                                     + str(point_prob_sys_accuracy) + "%."))
        self.lbl_point_prob_sys_accuracy.grid(column=0, columnspan=4, row=0, sticky="w")

        ## display probability to reach or exceed observed system accuracy given random guessing of user
        prob_at_above_sys_accuracy_text = ("Probability to reach or exceed the system accuracy by randomly choosing " +
                                  "when to adhere to AI advice (given the observed reliance): ")
        self.lbl_at_above_prob_sys_accuracy = tk.Label(self.frame_probability, text = (prob_at_above_sys_accuracy_text 
                                     + str(prob_at_above_sys_accuracy) + "%."))
        self.lbl_at_above_prob_sys_accuracy.grid(column=0, columnspan=4, row=1, sticky="w")

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
        # x_1=Correct Adherence
        # x_2=Wrong Adherence
        # x_3=Detrimental Override
        # x_4=Corrective Override

        # x_1+x_4=Observed System Accuracy
        # x_1+x_2=Observed Adherence to AI Rec.
        # x_1+x_3=AI Accuracy
        # x_1+x_2+ x_3+x_4=Total Amount of AI Supported Decisions

        global ai_accuracy, reliance, sys_accuracy
        left_side = np.array([[1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
        right_side = np.array([sys_accuracy, reliance, ai_accuracy, 1])

        return np.linalg.solve(left_side, right_side)
    
    def solve_adaa(self):
        """
        Solve and return the KPI 'Ability to discriminate between right and wrong AI Advice (ADAA)'

        Returns:
        float: The ADAA value rounded to 2 decimal places.
        """
        global ai_accuracy, reliance, sys_accuracy
        if reliance == 0 or reliance ==  1: #otherwise division by zero
            adaa = 0
        else:
            # best case
            if (1-ai_accuracy+reliance)>=1: #accuracy at least as high as reliance
                sys_acc_best = 1-reliance+ai_accuracy #e.g. acc 80%, reliance 80%: 1-0.8+0.8 = 100%
            else: #accuracy lower than reliance
                sys_acc_best = 1-ai_accuracy+reliance

            # worst case
            if (1-ai_accuracy-reliance)<0: #accuracy + reliance higher than 100%
                sys_acc_worst = ai_accuracy+reliance-1 #e.g. acc 80%, reliance 80%: 60%
            else:
                sys_acc_worst = 1-ai_accuracy-reliance #e.g. acc 80%, reliance 10%: 10%

            # adaa
            adaa = round(((sys_accuracy - sys_acc_worst)/(sys_acc_best - sys_acc_worst)), 2)
        return(adaa)

    def return_sysAccuracyBestCase(self):
        if (1-ai_accuracy+reliance)>=1: #accuracy at least as high as reliance
            sys_acc_best = 1-reliance+ai_accuracy #e.g. acc 80%, reliance 80%: 1-0.8+0.8 = 100%
        else: #accuracy lower than reliance
            sys_acc_best = 1-ai_accuracy+reliance
        return(round(sys_acc_best*100, 2))

    def return_sysAccuracyWorstCase(self):
        if (1-ai_accuracy-reliance)<0: #accuracy + reliance higher than 100%
            sys_acc_worst = ai_accuracy+reliance-1 #e.g. acc 80%, reliance 80%: 60%
        else:
            sys_acc_worst = 1-ai_accuracy-reliance #e.g. acc 80%, reliance 10%: 10%
        return(round(sys_acc_worst*100, 2))
    
    def roundToNearestEven(n):
        """
        Round the input number `n` to the nearest even integer.

        Parameters:
        n (float): The input number to round.

        Returns:
        int: The nearest even integer to `n`.
        """
        rounded = round(n)
        if rounded % 2 == 0:
            return rounded
        elif n >= rounded:
            return rounded + 1
        else:
            return rounded - 1

    def calculate_probability(self):
        """
        Calculates the point probability to achieve observed system accuracy and the probability to reach or exceed 
        that accuracy level, if the user were to randomly guess which advice to follow based on the observed 
        reliance level. This is done by calculating the probability for correct adherence, which directly correlates
        with the system accuracy (as demonstrated by the adherence matrix).
        The term (sys_accuracy_adapt+ai_accuracy_adapt+reliance_adapt-100)/2 describes the number of correct adherence.
        The urn model without replacement and without order can describe the probability of success drawing a ball 
        (i.e. correct adherence) but not correct overrides. Thus, this only works for binary studies in which the 
        system accuracy directly correlates with the correct adherence.

        Limitation: Binomial coefficients requiere natural numbers so the the input values are rounded to the next int.
                    The system accuracy is further rounded to the nearest even integer. This is due to the nature of the 
                    application of the urn model to this problem. If a user (having a certain reliance level) adheres to one
                    more incorrect AI prediction she/ he automatically either overwrites another incorrect one (no change 
                    in system accuracy) or a correct one. For 100 decisions there are only steps of 2% possible regarding 
                    the system accuracy if we look at one person. Having more test subjects enables every possible number. 
                    To be able to calculate the probabilities, the input values are rounded. The probabilities are an 
                    approximation.

        Example: 100 decisions, AI accuracy = 80%, reliance = 20%, system accuracy = 32%, random case = 32% (human can't 
                distinguish between right and wrong AI advice).
                The point probability to achieve 32% system accuracy by randomly guessing which 20% of recommendations
                to follow is 24.57%. The probability to reach or exceed 32% system accuracy is 63.51%. 

        Returns:
        tuple(float, float): A tuple of two float values representing the point probability to achieve observed 
                            system accuracy and the probability to reach or exceed that accuracy level, 
                            respectively. The values are rounded to 2 decimal places. reach
        """
        global ai_accuracy, reliance, sys_accuracy
        ai_accuracy_adapt = int(ai_accuracy * 100 + 0.5)
        reliance_adapt = int(reliance * 100 + 0.5)
        sys_accuracy_adapt = DisplayDetailedInformation.roundToNearestEven(sys_accuracy * 100)
        sysAccuracyWorstCase = self.return_sysAccuracyWorstCase() #already in percent
        #num_correct_adherence = int(self.solve_LSE()[0] * 100 + 0.5)
        #num_correct_adherence = int((sys_accuracy_adapt+ai_accuracy_adapt+reliance_adapt-100)/2)

        #point probability to achieve this exact point
        # (sys_accuracy_adapt+ai_accuracy_adapt+reliance_adapt-100)/2 = number of correct adherence
        x_point_lower = int((sys_accuracy_adapt+ai_accuracy_adapt+reliance_adapt-100)/2)
        y_point_lower = int(reliance_adapt-((sys_accuracy_adapt+ai_accuracy_adapt+reliance_adapt-100)/2))

        x_point = math.comb(ai_accuracy_adapt, x_point_lower)
        y_point = math.comb(100-ai_accuracy_adapt, y_point_lower)
        z_point = math.comb(100, reliance_adapt)
        point_prob_sys_accuracy_rdm = round(x_point*y_point/z_point *100, 2)

        #probability to reach or exceed this point
        prob_to_reach_sys_accuracy_rdm = 0
        sys_accuracy_adapt_array = []
        sys_accuracy_adapt_array = np.arange(int(sysAccuracyWorstCase+0.5),sys_accuracy_adapt+2, 2)

        for sys_acc_adapt in sys_accuracy_adapt_array:
            x_lower = int((sys_acc_adapt+ai_accuracy_adapt+reliance_adapt-100)/2)
            y_lower = int(reliance_adapt-((sys_acc_adapt+ai_accuracy_adapt+reliance_adapt-100)/2))

            x = math.comb(ai_accuracy_adapt, x_lower)
            y = math.comb(100-ai_accuracy_adapt, y_lower)
            z = math.comb(100, reliance_adapt)
            prob_to_reach_sys_accuracy_rdm = prob_to_reach_sys_accuracy_rdm+round(x*y/z *100, 2)

        prob_to_reach_at_above_sys_accuracy_rdm = round(max(0, 100-prob_to_reach_sys_accuracy_rdm)+point_prob_sys_accuracy_rdm, 2)

        return(point_prob_sys_accuracy_rdm, prob_to_reach_at_above_sys_accuracy_rdm)

def main(): 
    root = tk.Tk()
    root.title("Accuracy-Reliance Framework")
    app = ValueInput(root)
    root.mainloop()

if __name__ == '__main__':
    main()