
from tkinter import *
from tkinter import ttk 
import functions

def calculate_totals():
    vehicle_cost = input_vehicle_cost.get()
    petrol_type = dict_fuel_type[input_fuel_type.get()]
    engine_size = input_engine_size.get()
    exchange_rate = input_exchange_rate.get()
    vehicle_age = dict_vehicle_age[input_vehicle_age.get()]

    if int(vehicle_age) == 1:
        if int(petrol_type) == 1:
            if engine_size == '1000cc and below':
                engine_size = 1
            elif engine_size == '1001cc to 1500cc':
                engine_size = 2
            elif engine_size == '1501cc to 1800cc':
                engine_size = 3
            elif engine_size == '1801cc to 2000cc':
                engine_size = 4
            elif engine_size == '2001cc to 3000cc':
                engine_size = 5
            else:
                engine_size = 6
        elif int(petrol_type) == 2:
            if engine_size == '1500cc and below':
                engine_size = 1
            elif engine_size == '1501cc to 2000cc':
                engine_size = 2
            elif engine_size == '2001cc to 2500cc':
                engine_size = 3
            elif engine_size == '2501cc to 3000cc':
                engine_size = 4
            else:
                engine_size = 5
        else:
            engine_size = 0
    else:
        if int(petrol_type) == 1:
            if engine_size == '1000cc and below':
                engine_size = 1
            elif engine_size == '1001cc to 1500cc':
                engine_size = 2
            elif engine_size == '1501cc to 1800cc':
                engine_size = 3
            elif engine_size == '1801cc to 2000cc':
                engine_size = 4
            elif engine_size == '2001cc to 3000cc':
                engine_size = 5
            else:
                engine_size = 6
        elif int(petrol_type) == 2:
            if engine_size == '1500cc and below':
                engine_size = 1
            elif engine_size == '1501cc to 1800cc':
                engine_size = 2
            elif engine_size == '2000cc to 2500cc':
                engine_size = 3
            else:
                engine_size = 4
        else:
            engine_size = 0

    if int(vehicle_age) == 1:
        result_string = functions.get_total_duty_fyoo(int(vehicle_cost), int(petrol_type), int(engine_size), int(exchange_rate))
    else:
        result_string = functions.get_total_duty_ufy(int(vehicle_cost), int(petrol_type), int(engine_size), int(exchange_rate))

    result_text.delete(1.0, END)  # Clear existing content
    result_text.insert(END, result_string)

def update_options(event):
    selected_category = list_fuel_type.get()
    vehicle_age = dict_vehicle_age[input_vehicle_age.get()]
    
    # Clear current options in the second ComboBox
    input_engine_size['values'] = []

    # Update options in the second ComboBox based on the selected category

    if int(vehicle_age) == 1:
        if selected_category == 'Gasoline':
            input_engine_size['values'] = ('1000cc and below', '1001cc to 1500cc', '1501cc to 1800cc','1801cc to 2000cc','2001cc to 3000cc','3001cc and above')
        elif selected_category == 'Diesel':
            input_engine_size['values'] = ('1500cc and below', '1501cc to 2000cc', '2001cc to 2500cc', '2501cc to 3000cc', '3001cc and above')
        elif selected_category == 'Electric':
            input_engine_size['values'] = ('None')
    else:
        if selected_category == 'Gasoline':
            input_engine_size['values'] = ('1000cc and below', '1001cc to 1500cc', '1501cc to 1800cc','1801cc to 2000cc','2001cc to 3000cc','3001cc and above')
        elif selected_category == 'Diesel':
            input_engine_size['values'] = ('1500cc and below', '1501cc to 1800cc', '2000cc to 2500cc', '2500cc and above')
        elif selected_category == 'Electric':
            input_engine_size['values'] = ('None')

root = Tk()

root.title("Vehicle Import Calculator")
root.geometry('500x500')

label_vehicle_cost = Label(root, text="What is the cost of the vehicle (Including insurance and freight) in USD?")
label_vehicle_cost.grid(row=0, column=0, sticky='w')

input_vehicle_cost = Entry(root)
input_vehicle_cost.grid(row=1, column=0, sticky='w')

label_exchange_rate = Label(root, text="Please enter the exchange rate you are using (GYD to USD)")
label_exchange_rate.grid(row=2, column=0, sticky='w')

input_exchange_rate = Entry(root)
input_exchange_rate.grid(row=3, column=0, sticky='w')

label_vehicle_age = Label(root, text="What is the Vehicle Age?")
label_vehicle_age.grid(row=4, column=0, sticky='w')

list_vehicle_age = StringVar()
input_vehicle_age = ttk.Combobox(root, textvariable=list_vehicle_age, values=('Four Years and Older', 'Four Years Old'))
input_vehicle_age.grid(row=5, column=0, sticky='w')
dict_vehicle_age = {'Four Years and Older' : 1, "Four Years Old" :  2}

label_fuel_type = Label(root, text="Fuel Type")
label_fuel_type.grid(row=6, column=0, sticky='w')

list_fuel_type = StringVar()
input_fuel_type = ttk.Combobox(root, textvariable=list_fuel_type)
input_fuel_type['values'] = ('Gasoline', 'Diesel', 'Electric')
input_fuel_type.grid(row=7, column=0, sticky='w')
dict_fuel_type = {'Gasoline': 1, 'Diesel': 2, 'Electric': 3}


list_engine_size = StringVar()
label_engine_size = Label(root, text="How many Cubic Centimeters (CC) is the vehicle?")
label_engine_size.grid(row=8, column=0, sticky='w')
input_engine_size = ttk.Combobox(root, textvariable=list_engine_size)
input_engine_size.grid(row=9, column=0, sticky='w')

input_fuel_type.bind("<<ComboboxSelected>>", update_options)


button_calculate = Button(root, text="Calculate Costs", command=calculate_totals)
button_calculate.grid(row=10, column=0, sticky='w')

result_text = Text(root, wrap=WORD, height=15, width=80)
result_text.grid(row=11, column=0, sticky='w')


root.mainloop()