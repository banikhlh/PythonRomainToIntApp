import tkinter as tk


def romainToInt(s):
    result = 0
    roman = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000,
        'V̅': 5000,
        'X̅': 10000,
        'L̅': 50000,
        'C̅': 100000,
        'D̅': 500000,
        'M̅': 1000000,
        'V̿': 5000000,
        'I̿': 1000000000,
        }
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            result += roman[s[i]] - 2 * roman[s[i-1]]
        else:
            result += roman[s[i]]
    return result


def intToRomain(s):
    result = ''
    val = [
        (1000000000, 'I̿'), (5000000, 'V̿'), (1000000, 'M̅'), (500000, 'D̅'),   
        (100000, 'C̅'), (50000, 'L̅'), (10000, 'X̅'), (5000, 'V̅'),
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    for (integer, symbol) in val:
        while s >= integer:
            result += symbol
            s -= integer
    return result


def update_entries(event):
    try:
        if event.widget == entry_int:
            value = int(entry_int.get())
            entry_romen.delete(0, tk.END)
            entry_romen.insert(0, intToRomain(value))
        elif event.widget == entry_romen:
            value = romainToInt(entry_romen.get())
            entry_int.delete(0, tk.END)
            entry_int.insert(0, value)
    except ValueError:
        pass


window = tk.Tk()
window.title("Roman/Integer")
window.geometry('300x200')

label = tk.Label(window, text="Enter a number or Roman numeral:")
label.grid(column=0, row=0, columnspan=2)


int_label = tk.Label(window, text="Integer:")
int_label.grid(column=0, row=1)
entry_int = tk.Entry(window)
entry_int.grid(column=1, row=1)
entry_int.bind("<KeyRelease>", update_entries)


romen_label = tk.Label(window, text="Roman numeral:")
romen_label.grid(column=0, row=2)
entry_romen = tk.Entry(window)
entry_romen.grid(column=1, row=2)
entry_romen.bind("<KeyRelease>", update_entries)

window.mainloop()