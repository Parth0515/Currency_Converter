import tkinter as tk



root = tk.Tk()

def press():
    a = tk.Entry.get(entry)
    f = drop1.get()
    t = drop2.get()

    if f == "INR" and t == "INR":
        tk.Entry.delete(ent2, 0, tk.END)
        tk.Entry.insert(ent2, tk.END,f"{a}₹")
    elif f == "INR" and t == "USD":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.013423383
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}$")       
    elif f == "INR" and t == "JPY":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*1.530936
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}¥")
    elif f == "INR" and t == "EURO":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.011711135
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}€")


    elif f == "USD" and t == "INR":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*74.485776
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}₹")
    elif f == "USD" and t == "USD":
        tk.Entry.delete(ent2, 0, tk.END)
        tk.Entry.insert(ent2, tk.END, f"{a}$")
    elif f == "USD" and t == "JPY":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*113.99973
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}¥")
    elif f == "USD" and t == "EURO":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.87231732
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}€")


    elif f == "JPY" and t == "INR":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.65341249
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}₹")
    elif f == "JPY" and t == "USD":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.0087722571
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}$")
    elif f == "JPY" and t == "JPY":
        tk.Entry.delete(ent2, 0, tk.END)
        tk.Entry.insert(ent2, tk.END, f"{a}¥")
    elif f == "JPY" and t == "EURO":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*0.0076533218
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}€")


    elif f == "EURO" and t == "INR":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*85.385521
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}₹")
    elif f == "EURO" and t == "USD":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*1.1461968 
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}$")
    elif f == "EURO" and t == "JPY":
        tk.Entry.delete(ent2, 0, tk.END)
        r = int(a)*130.66462
        tk.Entry.insert(ent2, tk.END, f"{round(r,3)}¥")
    else:
        tk.Entry.delete(ent2, 0, tk.END)
        tk.Entry.insert(ent2, tk.END, f"{a}€")



root.title("Currency Converter")
root.iconbitmap("Personal_Project/images/currency_conv.ico")
root.geometry("450x130")
root.minsize(width = 450, height=130)

frm = ["INR", "USD", "JPY", "EURO"]
to = ["INR", "USD", "JPY", "EURO"]


drop1 = tk.StringVar()
drop2 = tk.StringVar()


drop1.set(frm[0])
drop2.set(to[0])

lb1 = tk.Label(root, text="Amount:").grid(row = 0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=12, bd=5)
entry.grid(row=1, column=0, padx=10)

lb2 = tk.Label(root, text="From:").grid(row=0, column=2, padx = 20)
db1 = tk.OptionMenu(root, drop1, *frm)
db1.grid(row = 1, column=2, padx= 20)

lb3 = tk.Label(root, text="To:").grid(row = 0, column= 3, padx= 20)
db2 = tk.OptionMenu(root, drop2, *to)
db2.grid(row = 1, column=3, padx= 20)

result = tk.Label(root, text="Result:").grid(row=0, column=4, padx=20)
ent2 = tk.Entry(root, width=12, bd=5)
ent2.grid(row=1, column=4, padx=20 )

btn = tk.Button(root, text="Convert", padx=20, bd=5, command=press).grid(row=2, column=2, columnspan =2, pady=20)

root.mainloop()


