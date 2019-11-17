import datetime
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.geometry("1200x720")
window.title(" Calculate your age ")
name = tk.Label(text="Name")
name.grid(column=0, row=1)
year = tk.Label(text="Year")
year.grid(column=0, row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Day")
date.grid(column=0, row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate



    def age(self):
        days_in_year = 365.2425
        age = int((datetime.date.today() -self.birthdate).days / days_in_year)
        return age


def getInput():
    name = nameEntry.get()
    agecalc =Person(name, datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))

    if  name== '' or yearEntry== '' or monthEntry == '' or dateEntry == '':
        tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
    else:
         answer = " Heyy {agecalc}!!!. You are""{age} years old!!! ".format(agecalc=name, age=agecalc.age())
         tk.messagebox.showinfo("Age box",answer)

button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)
window.mainloop()

