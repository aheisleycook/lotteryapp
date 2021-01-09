import  tkinter as tk
import random

class InfoBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.info = """
        app name = 
        objective:
        this gives the user numbers for letter

        """
        self.lblinfobox = tk.Label(self,text=self.info)
        self.lblinfobox.grid(row=0,column=1)
        self.btnOK = tk.Button(self, width=23,qtext="Ok",command=self.ConfirmOK)
        self.btnOK.grid(row=2,column=3)
    def ConfirmOK(self):
        self.destroy()


class LotteryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.first = tk.IntVar()
        self.second = tk.IntVar()
        self.third = tk.IntVar()
        self.geometry("300x500")
        self.title("looter")
        self.resizable(0,0)
        self.configure(background="lightblue")
        self.lblTitle = tk.Label(self, relief="raised",text="lottery")
        self.lblTitle.grid(row=0,column=3)
        self.lblfirst = tk.Label(self, textvariable=self.first, width=10,background="red", relief="raised",text=self.first)
        self.lblfirst.grid(row=3,column=4)
        self.lblsecond = tk.Label(self, textvariable=self.second, width=10, background="red", relief="raised", text=self.second)
        self.lblsecond.grid(row=3, column=5)
        self.lblthird = tk.Label(self, textvariable=self.third, width=10, background="red", relief="raised", text=self.third)
        self.lblthird.grid(row=3,column=6)
        self.btngen = tk.Button(self,text="get", width=10, relief="raised",command=self.GetShow)
        self.btngen.grid(row=12,column=5)
        self.bind("<q>",self.Quit)
        self.bind("<?>",self.show)


    def show(self,event):
        InfoBox()

    def Quit(self,event):
        self.destroy()


    def GetShow(self):
        self.first.set(random.randint(1,9))
        self.second.set(random.randint(1,9))
        self.third.set(random.randint(1,9))





lotteryapp = LotteryApp()
lotteryapp.mainloop()



