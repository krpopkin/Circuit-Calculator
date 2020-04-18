# helpful links:
# https://dev.to/abdurrahmaanj/building-an-oop-calculator-and-what-it-means-to-write-a-widget-library-4560
# https://effbot.org/tkinterbook/grid.htm
# https://stackoverflow.com/questions/47378715/tkinter-how-to-get-the-value-of-an-entry-widget

import tkinter as tk

root = tk.Tk()
root.geometry("600x300")

formula_name = ' '

# FUNCTIONS


def clear_():
    p1.delete(0, 'end')
    p2.delete(0, 'end')
    p3.delete(0, 'end')
    p4.delete(0, 'end')
    p5.delete(0, 'end')

    p1.grid_remove()
    p2.grid_remove()
    p3.grid_remove()
    p4.grid_remove()
    p5.grid_remove()


def labels_(text_, row_, col_, fontcolor_, bgcolor_, font_size_, width_):
    labels = tk.Label(root, text=text_, width=width_, height=1, bg=bgcolor_, anchor='w',
                      fg=fontcolor_, font=('Calibri', font_size_, 'italic'))
    labels.grid(row=row_, column=col_, sticky='W', pady=0)


def calc_profit():
    clear_()

    labels_('cost', 5, 0, 'black', 'gray94', 10, 10)
    labels_('margin', 5, 2, 'black', 'gray94', 10, 10)
    labels_(' ', 5, 4, 'black', 'gray94', 10, 10)
    labels_(' ', 5, 6, 'black', 'gray94', 10, 10)
    labels_(' ', 5, 8, 'black', 'gray94', 10, 10)

    p1.grid()
    p2.grid()

    global formula_name
    formula_name = 'calc_profit'


def calc_circuit_sum():
    clear_()

    labels_('circuit1', 5, 0, 'black', 'gray94', 10, 10)
    labels_('circuit2', 5, 2, 'black', 'gray94', 10, 10)
    labels_('circuit3', 5, 4, 'black', 'gray94', 10, 10)
    labels_('circuit4', 5, 6, 'black', 'gray94', 10, 10)
    labels_('circuit5', 5, 8, 'black', 'gray94', 10, 10)

    p1.grid()
    p2.grid()
    p3.grid()
    p4.grid()
    p5.grid()

    global formula_name
    formula_name = 'calc_circuit_sum'


def equals():
    result = 0
    #formula = ' '
    if formula_name == 'calc_profit':
        #formula = 'profit * margin'
        result = float(p1.get()) * float(p2.get())
    elif formula_name == 'calc_circuit_sum':
        #formula = 'circuit1 + circuit2 + circuit3 + circuit4 + circuit5'
        result = float(p1.get()) + float(p2.get()) + \
            float(p3.get()) + float(p4.get()) + \
            float(p5.get())

    labels_(result, 8, 4, 'green', 'white', 12, 10)
    #labels_(formula, 9, 0, 'black', 'gray94', 10, 10)


def button_(text_, row_, col_, command_, font_size_):
    b = tk.Button(
        root, text=text_, width=10,
        height=1, font=('Calibri', font_size_, 'normal'),
        command=command_)
    b.grid(row=row_, column=col_, sticky='W',
           padx=10, pady=0)


# RUN
labels_('Formulas:', 1, 0, 'blue', 'gray94', 12, 10)
button_('Profit', 2, 0, calc_profit, 10)
button_('Circuit Sum', 2, 2, calc_circuit_sum, 10)

labels_(' ', 3, 0, 'blue', 'gray94', 12, 10)
labels_('Parameters:', 4, 0, 'blue', 'gray94', 12, 10)

p1 = tk.Entry(root)
p1.config(width=10, )
p1.grid(row=6, column=0, sticky='W',
        padx=0, pady=0, columnspan=5)
p1.grid_remove()

p2 = tk.Entry(root)
p2.config(width=10)
p2.grid(row=6, column=2, sticky='W',
        padx=0, pady=0, columnspan=5)
p2.grid_remove()

p3 = tk.Entry(root)
p3.config(width=10)
p3.grid(row=6, column=4, sticky='W',
        padx=0, pady=0, columnspan=5)
p3.grid_remove()

p4 = tk.Entry(root)
p4.config(width=10)
p4.grid(row=6, column=6, sticky='W',
        padx=0, pady=0, columnspan=5)
p4.grid_remove()

p5 = tk.Entry(root)
p5.config(width=10)
p5.grid(row=6, column=8, sticky='W',
        padx=0, pady=0, columnspan=5)
p5.grid_remove()

labels_(' ', 7, 0, 'black', 'gray94', 12, 10)
labels_('Answer:', 8, 0, 'blue', 'gray94', 12, 10)
button_('=', 8, 2, equals, 10)


root.title('Circuit Calculator')
root.mainloop()
