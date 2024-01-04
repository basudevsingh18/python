from tkinter import *
import functions
import customtkinter

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

def toggle_theme():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")

def create_gui():

    customtkinter.set_appearance_mode("System")

    root = customtkinter.CTk()

    try:
        root.title("Vehicle Import Calculator")
        root.geometry('500x500')

        label_vehicle_cost = customtkinter.CTkLabel(master=root, text="What is the cost of the vehicle (Including insurance and freight) in USD?")
        label_vehicle_cost.pack(pady=10, padx=10)

        input_vehicle_cost = customtkinter.CTkEntry(master=root)
        input_vehicle_cost.pack(pady=1, padx=10)

        label_exchange_rate = customtkinter.CTkLabel(master=root, text="Please enter the exchange rate you are using (GYD to USD)")
        label_exchange_rate.pack(pady=10, padx=10)

        input_exchange_rate = customtkinter.CTkEntry(master=root)
        input_exchange_rate.pack(pady=1, padx=10)

        label_vehicle_age = customtkinter.CTkLabel(master=root, text="What is the Vehicle Age?")
        label_vehicle_age.pack(pady=10, padx=10)

        list_vehicle_age = StringVar()
        # input_vehicle_age = customtkinter.CTkComboBox(master=root, textvariable=list_vehicle_age, values=('Four Years and Older', 'Four Years Old'))
        input_vehicle_age = customtkinter.CTkComboBox(master=root, values=('Four Years and Older', 'Four Years Old'))
        input_vehicle_age.pack(pady=1, padx=10)
        dict_vehicle_age = {'Four Years and Older' : 1, "Four Years Old" :  2}

        label_fuel_type = customtkinter.CTkLabel(master=root, text="Fuel Type")
        label_fuel_type.pack(pady=10, padx=10)

        list_fuel_type = StringVar()
        # input_fuel_type = customtkinter.CTkComboBox(master=root, textvariable=list_fuel_type)
        input_fuel_type = customtkinter.CTkComboBox(master=root, values=('Gasoline', 'Diesel', 'Electric'))
        # input_fuel_type['values'] = ('Gasoline', 'Diesel', 'Electric')
        input_fuel_type.pack(pady=1, padx=10)
        dict_fuel_type = {'Gasoline': 1, 'Diesel': 2, 'Electric': 3}


        # list_engine_size = StringVar()
        # label_engine_size = customtkinter.CTkLabel(master=root, text="How many Cubic Centimeters (CC) is the vehicle?")
        # label_engine_size.pack(pady=10, padx=10)
        # # input_engine_size = ttk.Combobox(root, textvariable=list_engine_size)
        # input_engine_size = ttk.Combobox(root)
        # input_engine_size.pack(pady=1, padx=10)

        # # input_fuel_type.bind("<<ComboboxSelected>>", update_options)


        button_calculate = customtkinter.CTkButton(master=root, text="Calculate Costs", command=functions.calculate_totals)
        button_calculate.pack(pady= 10, padx=10)

        button_toggle_theme = customtkinter.CTkButton(master=root, text="Switch Theme", command=toggle_theme)
        button_toggle_theme.pack(pady= 1, padx=10)

        # result_text = Text(root, wrap=WORD, height=15, width=80)
        # result_text.grid(row=11, column=0, sticky='w')


        root.mainloop()
        
    except:
        print("Error: Unable to create GUI.")
