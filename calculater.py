import tkinter as tk
from tkinter import ttk

# ---------------- BASIC CALCULATOR ---------------- #

def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------------- SIP CALCULATOR ---------------- #

def calculate_sip():
    try:
        P = float(entry_invest.get())
        r = float(entry_rate.get()) / 100 / 12
        n = float(entry_years.get()) * 12

        future_value = P * (((1 + r)**n - 1) / r) * (1 + r)

        sip_result.config(text="Future Value: ₹ " + str(round(future_value,2)))
    except:
        sip_result.config(text="Invalid Input")

# ---------------- EMI CALCULATOR ---------------- #

def calculate_emi():
    try:
        loan = float(entry_loan.get())
        rate = float(entry_interest.get()) / 100 / 12
        months = float(entry_time.get()) * 12

        emi = loan * rate * (1 + rate)**months / ((1 + rate)**months - 1)

        emi_result.config(text="Monthly EMI: ₹ " + str(round(emi,2)))
    except:
        emi_result.config(text="Invalid Input")

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Modern Multi Calculator")
root.geometry("350x450")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ================= BASIC CALCULATOR TAB ================= #

frame1 = tk.Frame(notebook)
notebook.add(frame1, text="Calculator")

entry = tk.Entry(frame1, width=20, font=("Arial",20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('+',4,2)
]

for (text,row,col) in buttons:
    tk.Button(frame1,text=text,width=5,height=2,
              command=lambda t=text: click(t)).grid(row=row,column=col,padx=5,pady=5)

tk.Button(frame1,text="=",width=5,height=2,command=equal).grid(row=4,column=3)
tk.Button(frame1,text="C",width=22,height=2,command=clear).grid(row=5,column=0,columnspan=4,pady=5)

# ================= SIP CALCULATOR TAB ================= #

frame2 = tk.Frame(notebook)
notebook.add(frame2, text="SIP Calculator")

tk.Label(frame2,text="Monthly Investment (₹)").pack(pady=5)
entry_invest = tk.Entry(frame2)
entry_invest.pack()

tk.Label(frame2,text="Expected Annual Return (%)").pack(pady=5)
entry_rate = tk.Entry(frame2)
entry_rate.pack()

tk.Label(frame2,text="Investment Period (Years)").pack(pady=5)
entry_years = tk.Entry(frame2)
entry_years.pack()

tk.Button(frame2,text="Calculate SIP",command=calculate_sip).pack(pady=10)

sip_result = tk.Label(frame2,text="",font=("Arial",12))
sip_result.pack()

# ================= EMI CALCULATOR TAB ================= #

frame3 = tk.Frame(notebook)
notebook.add(frame3, text="EMI Calculator")

tk.Label(frame3,text="Loan Amount (₹)").pack(pady=5)
entry_loan = tk.Entry(frame3)
entry_loan.pack()

tk.Label(frame3,text="Interest Rate (%)").pack(pady=5)
entry_interest = tk.Entry(frame3)
entry_interest.pack()

tk.Label(frame3,text="Loan Time (Years)").pack(pady=5)
entry_time = tk.Entry(frame3)
entry_time.pack()

tk.Button(frame3,text="Calculate EMI",command=calculate_emi).pack(pady=10)

emi_result = tk.Label(frame3,text="",font=("Arial",12))
emi_result.pack()

root.mainloop()