
import customtkinter
from tkinter import *
from tkinter import ttk 
import functions

# list_fuel_type = None
# list_engine_size = None
# input_vehicle_age = None
# dict_vehicle_age = None
# dict_fuel_type = None
# input_engine_size = None
# input_vehicle_cost = None
# input_fuel_type = None
# input_exchange_rate = None
# result_text = None

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

def toggle_theme():
    current_theme = customtkinter.get_appearance_mode()

    if current_theme == "Light":
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("Light")

def update_options(*args):
    selected_category = list_fuel_type.get()
    vehicle_age = dict_vehicle_age[input_vehicle_age.get()]

    if int(vehicle_age) == 1:
        if selected_category == 'Gasoline':
            input_engine_size.configure (values=['1000cc and below', '1001cc to 1500cc', '1501cc to 1800cc','1801cc to 2000cc','2001cc to 3000cc','3001cc and above'])
        elif selected_category == 'Diesel':
            input_engine_size.configure (values=['1500cc and below', '1501cc to 2000cc', '2001cc to 2500cc', '2501cc to 3000cc', '3001cc and above'])
        elif selected_category == 'Electric':
            input_engine_size.configure (values=['None'])
    else:
        if selected_category == 'Gasoline':
            input_engine_size.configure (values=['1000cc and below', '1001cc to 1500cc', '1501cc to 1800cc','1801cc to 2000cc','2001cc to 3000cc','3001cc and above'])
        elif selected_category == 'Diesel':
            input_engine_size.configure (values=['1500cc and below', '1501cc to 1800cc', '2000cc to 2500cc', '2500cc and above'])
        elif selected_category == 'Electric':
            input_engine_size.configure (values=['None'])

def create_gui():
    global list_fuel_type, input_vehicle_age, dict_vehicle_age, dict_fuel_type, input_engine_size, input_vehicle_cost, input_fuel_type, input_exchange_rate, result_text

    root = customtkinter.CTk()

    root.title("Vehicle Import Calculator")
    root.geometry('900x700')

    #Vehicle Cost Label
    label_vehicle_cost = customtkinter.CTkLabel(root, text="What is the cost of the vehicle (Including insurance and freight) in USD?")
    label_vehicle_cost.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    #Vehicle Cost Input 
    input_vehicle_cost = customtkinter.CTkEntry(root, placeholder_text="Enter CIF here...")
    input_vehicle_cost.grid(row=0, column=1, columnspan=5, padx=20, pady=20, sticky="ew")

    #Exchange Rate Label
    label_exchange_rate = customtkinter.CTkLabel(root, text="Please enter the exchange rate you are using (GYD to USD)")
    label_exchange_rate.grid(row=1, column=0, padx=20, pady=20, sticky='w')

    #Exchange Rate Input
    input_exchange_rate = customtkinter.CTkEntry(root, placeholder_text="Enter exchange rate here...")
    input_exchange_rate.grid(row=1, column=1, columnspan=5, padx=20, pady=20, sticky="ew")

    #Vehicle Age Label
    label_vehicle_age = customtkinter.CTkLabel(root, text="What is the Vehicle Age?")
    label_vehicle_age.grid(row=2, column=0, padx=20, pady=20, sticky='w')

    #Vehicle Age Input
    list_vehicle_age = customtkinter.StringVar(value='--Select an option--')
    # input_vehicle_age = customtkinter.CTkOptionMenu(root, textvariable=list_vehicle_age, values=('Four Years and Older', 'Four Years Old'))
    input_vehicle_age = customtkinter.CTkOptionMenu(root, values=['Four Years and Older', 'Four Years Old'], variable=list_vehicle_age)
    input_vehicle_age.grid(row=2, column=1, columnspan=5, padx=20, pady=20, sticky="ew")
    dict_vehicle_age = {'Four Years and Older' : 1, "Four Years Old" :  2}

    #Vehicle Fuel Type Label
    label_fuel_type = customtkinter.CTkLabel(root, text="What type of fuel/energy does the vehicle use?")
    label_fuel_type.grid(row=3, column=0, padx=20, pady=20, sticky='w')

    #Vehicle Fuel Type Input
    list_fuel_type = customtkinter.StringVar(root)
    list_fuel_type.set("Select fuel type") #Nice to have
    input_fuel_type = customtkinter.CTkOptionMenu(master=root, values=['Gasoline', 'Diesel', 'Electric'], variable=list_fuel_type, command=update_options)
    input_fuel_type.grid(row=3, column=1, columnspan=5, padx=20, pady=20, sticky='ew')
    dict_fuel_type = {'Gasoline': 1, 'Diesel': 2, 'Electric': 3}

    #Vehicle Engine Size Label
    label_engine_size = customtkinter.CTkLabel(root, text="How many Cubic Centimeters (CC) is the vehicle?")
    label_engine_size.grid(row=4, column=0, padx=20, pady=20, sticky='w')

    #Vehicle Engine Size Input
    list_engine_size = customtkinter.StringVar(root)
    input_engine_size = customtkinter.CTkOptionMenu(master=root, values=[], variable=list_engine_size)
    input_engine_size.grid(row=4, column=1, columnspan=5, padx=20, pady=20, sticky='ew')

    button_calculate = customtkinter.CTkButton(root, text="Calculate Costs", command=calculate_totals)
    button_calculate.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky='ew')

    button_theme = customtkinter.CTkButton(root, text="Change Theme", command=toggle_theme)
    button_theme.grid(row=5, column=3, columnspan=2, padx=20, pady=20, sticky='ew')

    label_result_text = customtkinter.CTkLabel(root, text="Breakdown to Results")
    label_result_text.grid(row=6, column=0, columnspan=5, padx=20, pady=0, sticky='w')
    result_text = Text(root, wrap=WORD, height=15, width=80)
    result_text.grid(row=7, column=0, columnspan=5, padx =20, pady=0, sticky='ew')


    root.mainloop()

if __name__ == "__main__":
    create_gui()