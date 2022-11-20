import tkinter as t

LARGE_FONT = ("Arial",40,"bold")
DIGIT_FONT =("Arial",24,"bold")
SMALL_FONT =("Arial",16)
LIGHT_GRAY = "#F5F5F5"
WHITE = "#FFFFFF"
LABEL_COLOR = "#25265E"
DEFAULT=("Arial",20)
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

class Calculator:
    def __init__(self):
        self.win = t.Tk()
        self.win.geometry("375x667")
        self.win.title("Woldu's Calculator")
        self.win.resizable(0,0)
        self.total_expression = ""
        self.current_expression = ""

        self.Labelsframe = self.CreateLabelsFrame()
        self.totalLabel, self.totalLabel1 = self.display_Label()

        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operations ={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.buttonsFrame = self.CreateButtonsFrame()

        self.buttonsFrame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttonsFrame.rowconfigure(x, weight=1)
            self.buttonsFrame.columnconfigure(x, weight=1)

        self.createDigitButtons()
        self.createOperator()
        self.createClearButton()
        self.createEqualButton()
        self.bind_keys()
        self.Square()
        self.SquareRoot()
    def createEqualButton(self):
        button = t.Button(self.buttonsFrame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                          font=DEFAULT, borderwidth=0,command=self.evaluateAll)
        button.grid(row=4, column=3, columnspan=2, sticky=t.NSEW)
    def clearButton(self):
        self.current_expression=""
        self.total_expression = ""
        self.updateTotal()
        self.updateCurrent()
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.updateTotal()
        self.updateCurrent()

    def Square(self):
        button = t.Button(self.buttonsFrame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                          font=DEFAULT, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, columnspan=1, sticky=t.NSEW)


    def squareRoot(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.updateTotal()
        self.updateCurrent()
    def SquareRoot(self):
        button = t.Button(self.buttonsFrame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
                      font=DEFAULT, borderwidth=0, command=self.squareRoot)
        button.grid(row=0, column=3, columnspan=1, sticky=t.NSEW)

    def bind_keys(self):
        self.win.bind("<Return>",lambda event:self.evaluateAll())
        for key in self.digits:
            self.win.bind(str(key),lambda event,digit=key:self.addToAll(digit))

        for key in self.operations:
            self.win.bind(key,lambda event,operator=key:self.AddOperator(operator))
    def createClearButton(self):
        button = t.Button(self.buttonsFrame, text="C", bg="red", fg=LABEL_COLOR,
                          font=DEFAULT, borderwidth=0,command=self.clearButton)
        button.grid(row=0, column=1,columnspan=1,sticky=t.NSEW)
    def addToAll(self,value):
        self.current_expression += str(value)
        self.updateTotal()
        self.updateCurrent()
    def evaluateAll(self):
        self.total_expression += self.current_expression
        self.updateTotal()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.updateCurrent()



    def AddOperator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.updateCurrent()
        self.updateTotal()


    def createOperator(self):
        i =0
        for operator,symbol in self.operations.items():
            button = t.Button(self.buttonsFrame,text=symbol,bg=OFF_WHITE,fg=LABEL_COLOR,
                              font=DEFAULT,borderwidth=0,command=lambda x=operator: self.AddOperator(x))
            button.grid(row=i,column=4,sticky=t.NSEW)
            i+=1
    def display_Label(self):
        totalLabel = t.Label(self.Labelsframe,text=self.total_expression,
                             anchor=t.E,fg=LABEL_COLOR,bg=LIGHT_GRAY,padx=24,
                             font=SMALL_FONT)
        totalLabel.pack(expand=True,fill="both")

        totalLabel1 = t.Label(self.Labelsframe, text=self.current_expression,
                             anchor=t.E, fg=LABEL_COLOR, bg=LIGHT_GRAY, padx=24,
                             font=LARGE_FONT)
        totalLabel1.pack(expand=True, fill="both")
        return totalLabel, totalLabel1

    def CreateButtonsFrame(self):
        frame = t.Frame(self.win)
        frame.pack(expand=True, fill="both")
        return frame
    def createDigitButtons(self):
        for digit,grid_value in self.digits.items():
            buttons = t.Button(self.buttonsFrame,text=str(digit),font=DIGIT_FONT,
                               bg=WHITE,fg=LABEL_COLOR,borderwidth=0,command=lambda x= digit: self.addToAll(x))
            buttons.grid(row=grid_value[0],column=grid_value[1],sticky=t.NSEW)
    def CreateLabelsFrame(self):
        frame = t.Frame(self.win,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame
    def updateTotal(self):
        self.totalLabel.config(text=self.total_expression)
    def updateCurrent(self):
        self.totalLabel1.config(text=self.current_expression[:11])

    def run(self):
        self.win.mainloop()

if __name__=="__main__":
    cal = Calculator()
    cal.run()