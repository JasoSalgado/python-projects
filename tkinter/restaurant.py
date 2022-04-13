"""
Restaurant manager
"""

# Modules
from glob import glob
from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime
from unicodedata import numeric

# Food, beverage and dessert prices list
operator = ''
food_prices = [10.17, 18.36, 3.84, 28.59, 19.23, 3.69, 42.85]
beverage_prices = [4, 6, 5, 5, 4, 5, 1]
dessert_prices = [1.19, 8.58, 6.64, 18.6, 22.42, 20.42, 13.10]

# Methods
def click_button(number):
    global operator
    operator = operator + number
    calculator_visor.delete(0, END)
    calculator_visor.insert(END, operator)


def delete():
    global operator
    operator = ''
    calculator_visor.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_visor.delete(0, END)
    calculator_visor.insert(0, result)
    operator = ''


def revise_checkbox():
    # Food
    counter = 0

    for c in food_square:
        if food_variables[counter].get() == 1:
            food_square[counter].config(state=NORMAL)

            if food_square[counter].get() == '0':
                food_square[counter].delete(0, END)
            food_square[counter].focus()
        
        else:
            food_square[counter].config(state=DISABLED)
            food_text[counter].set('0')
        counter += 1
    
    # Beverage
    counter = 0

    for c in beverage_square:
        if beverage_variables[counter].get() == 1:
            beverage_square[counter].config(state=NORMAL)

            if beverage_square[counter].get() == '0':
                beverage_square[counter].delete(0, END)
            beverage_square[counter].focus()
        
        else:
            beverage_square[counter].config(state=DISABLED)
            beverage_text[counter].set('0')
        counter += 1
    
    # Dessert
    counter = 0

    for c in dessert_square:
        if dessert_variables[counter].get() == 1:
            dessert_square[counter].config(state=NORMAL)

            if dessert_square[counter].get() == '0':
                dessert_square[counter].delete(0, END)
            dessert_square[counter].focus()
        
        else:
            dessert_square[counter].config(state=DISABLED)
            dessert_text[counter].set('0')
        counter += 1


def total():
    subtotal_food = 0
    price = 0

    # Food
    for amount in food_text:
        subtotal_food = subtotal_food + (float(amount.get()) * food_prices[price])
        price += 1
    
    # Beverage
    for amount in beverage_text:
        subtotal_beverage = subtotal_beverage + (float(amount.get()) * beverage_prices[price])
        price += 1
    
    # Dessert
    for amount in dessert_text:
        subtotal_dessert = subtotal_dessert + (float(amount.get()) * dessert_prices[price])
        price += 1
    
    # Subtotal, taxes and total
    subtotal = subtotal_food + subtotal_beverage + subtotal_dessert
    taxes = subtotal * 0.16
    total = subtotal + taxes

    var_food_price.set(f'${round(subtotal_food, 2)}')
    var_beverage_price.set(f'${round(subtotal_beverage, 2)}')
    var_dessert_price.set(f'${round(subtotal_dessert, 2)}')
    var_taxes.set(f'${round(taxes, 2)}')
    var_total.set(f'${round(total, 2)}')


def receipt():
    receipt_text.delete(1.0, END)
    receipt_number = f'No. - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    receipt_text.insert(END, f'Data:\t{receipt_number}\t\t{receipt_date}\n')
    receipt_text.insert(END, f'*' * 47 + '\n')
    receipt_text.insert(END, 'Items\t\tAmount\tPrice of Items\n')
    receipt_text.insert(END, f'-' * 54 + '\n')

    #Food
    counter = 0
    for food in food_text:
        if food.get() != '0':
            receipt_text.insert(END, f'{food_list[counter]}\t\t{food.get()}\t'
                                    f'${int(food.get()) * food_prices[counter]}\n')
        counter += 1

    # Beverage
    counter = 0
    for beverage in beverage_text:
        if beverage.get() != '0':
            receipt_text.insert(END, f'{beverage_list[counter]}\t\t{beverage.get()}\t'
                                    f'${int(beverage.get()) * beverage_prices[counter]}\n')
        counter += 1
    
    # Dessert
    counter = 0
    for dessert in dessert_text:
        if dessert.get() != '0':
            receipt_text.insert(END, f'{dessert_list[counter]}\t\t{dessert.get()}\t'
                                    f'${int(dessert.get()) * dessert_prices[counter]}\n')
        counter += 1

    receipt_text.insert(END, f'-' * 54 + '\n')
    receipt_text.insert(END, f' Food price: \t\t\t{var_food_price.get()}\n')
    receipt_text.insert(END, f' Beverage price: \t\t\t{var_beverage_price.get()}\n')
    receipt_text.insert(END, f' Dessert price: \t\t\t{var_dessert_price.get()}\n')
    receipt_text.insert(END, f'-' * 54 + '\n')
    receipt_text.insert(END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    receipt_text.insert(END, f' Taxes: \t\t\t{var_taxes.get()}\n')
    receipt_text.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    receipt_text.insert(END, f'*' * 47 + '\n')
    receipt_text.insert(END, 'Thanks for coming!')

def save():
    # Delete before adding a new order
    receipt_text.delete(0.1, END)

    # Reset data
    for text in food_text:
        text.set('0')
    for text in beverage_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')
    
    # Deactivate checkbox 
    for square in food_square:
        square.config(state=DISABLED)
    for square in beverage_square:
        square.config(state=DISABLED)
    for square in dessert_square:
        square.config(state=DISABLED)
    
    # Reset
    for v in food_variables:
        v.set(0)
    for v in beverage_variables:
        v.set(0)
    for v in dessert_variables:
        v.set(0)
    
    var_food_price.set('')
    var_beverage_price.set('')
    var_dessert_price.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')

# Init tkinter
application = Tk()

# Window size
application.geometry('1020x360+0+0')

# Avoid maximize window
application.resizable(0, 0)

# Window title
application.title('Python Restaurant - Billing System')

# Window color
application.config(bg='burlywood')

# Top panel
top_panel = Frame(application, bd=1, relief=FLAT) 
top_panel.pack(side=TOP)

# Title label
title_label = Label(top_panel, text='Billing System',
                    fg='azure4', font=('Dosis', 58),
                    bg='burlywood', width=27)
title_label.grid(row=0, column=0)

left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Price panel
price_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=50)
price_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
food_panel.pack(side=LEFT)

# Beverage panel
beverage_panel = LabelFrame(left_panel, text='Beverage', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
beverage_panel.pack(side=LEFT)

# Dessert panel
panel_postres = LabelFrame(left_panel, text='Dessert', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
receipt_panel.pack()

# Buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
buttons_panel.pack()

# List of products
food_list = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
beverage_list = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
dessert_list = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# Generate food items
food_variables = []
food_square = []
food_text = []
counter = 0
for food in food_list:
    # crear checkbutton
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                         text=food.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=food_variables[counter],
                         command=revise_checkbox)

    food.grid(row=counter,
                column=0,
                sticky=W)

    # Create entry squares
    food_square.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_square[counter] = Entry(food_panel,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=food_text[counter])
    food_square[counter].grid(row=counter,
                                  column=1)
    counter += 1

# Generate beverage items
beverage_variables = []
beverage_square = []
beverage_text = []
counter = 0
for beverage in beverage_list:
    # crear checkbutton
    beverage_variables.append('')
    beverage_variables[counter] = IntVar()
    beverage = Checkbutton(beverage_panel,
                         text=beverage.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=beverage_variables[counter],
                         command=revise_checkbox)
    beverage.grid(row=counter,
                column=0,
                sticky=W)

    # Create entry squares
    beverage_square.append('')
    beverage_text.append('')
    beverage_text[counter] = StringVar()
    beverage_text[counter].set('0')
    beverage_square[counter] = Entry(beverage_panel,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=beverage_text[counter])
    beverage_square[counter].grid(row=counter,
                                  column=1)

    counter += 1

# Generate dessert items
dessert_variables = []
dessert_square = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    # crear checkbutton
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_square,
                          text=dessert.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[counter],
                         command=revise_checkbox)
    dessert.grid(row=counter,
                 column=0,
                 sticky=W)

    # Create entry squares
    dessert_square.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_square[counter] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=dessert_text[counter])
    dessert_square[counter].grid(row=counter,
                                   column=1)
    counter += 1


# variables
var_food_price = StringVar()
var_beverage_price = StringVar()
var_dessert_price = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()

# Cost label and entry fields
label_food_price = Label(price_panel,
                              text='Food price',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
label_food_price.grid(row=0, column=0)

text_food_price = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_food_price)
text_food_price.grid(row=0, column=1, padx=41)

label_beverage_price = Label(price_panel,
                              text='Beverage price',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
label_beverage_price.grid(row=1, column=0)

text_beverage_price = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_beverage_price)
text_beverage_price.grid(row=1, column=1, padx=41)

label_dessert_price = Label(price_panel,
                              text='Dessert price',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
label_dessert_price.grid(row=2, column=0)

text_dessert_price = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_dessert_price)
text_dessert_price.grid(row=2, column=1, padx=41)

label_subtotal = Label(price_panel,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
label_subtotal.grid(row=0, column=2)

text_subtotal = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx=41)

taxes_label = Label(price_panel,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
taxes_label.grid(row=1, column=2)

taxes_text = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_taxes)
taxes_text.grid(row=1, column=3, padx=41)

total_label = Label(price_panel,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
total_label.grid(row=2, column=2)

total_text = Entry(price_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
total_text.grid(row=2, column=3, padx=41)

# Buttons
buttons = ['total', 'recibo', 'guardar', 'resetear']
created_buttons = []

columns = 0
for button in buttons:
    button = Button(buttons_panel,
                   text=button.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    created_buttons.append(button)

    button.grid(row=0,
               column=columns)
    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=receipt)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

# Rceipt area
receipt_text = Text(receipt_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
receipt_text.grid(row=0,
                  column=0)

# Calculator
calculator_visor = Entry(calculator_panel,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
calculator_visor.grid(row=0,
                       column=0,
                       columnspan=4)

calculator_buttons = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
saved_buttons = []

row = 1
column = 0
for  button in calculator_buttons:
    button = Button(calculator_panel,
                text= button.title(),
                font=('Dosis', 16, 'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=8)

    saved_buttons.append(button)

    button.grid(row=row,
            column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda : click_button('7'))
saved_buttons[1].config(command=lambda : click_button('8'))
saved_buttons[2].config(command=lambda : click_button('9'))
saved_buttons[3].config(command=lambda : click_button('+'))
saved_buttons[4].config(command=lambda : click_button('4'))
saved_buttons[5].config(command=lambda : click_button('5'))
saved_buttons[6].config(command=lambda : click_button('6'))
saved_buttons[7].config(command=lambda : click_button('-'))
saved_buttons[8].config(command=lambda : click_button('1'))
saved_buttons[9].config(command=lambda : click_button('2'))
saved_buttons[10].config(command=lambda : click_button('3'))
saved_buttons[11].config(command=lambda : click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda : click_button('0'))
saved_buttons[15].config(command=lambda : click_button('/'))



# evitar que la pantalla se cierre
application.mainloop()

