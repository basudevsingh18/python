import datetime
import functions

print("Welcome to Vehicle Duty Calculator")
print("")
print("Press 1 for menu")

cif = 0
duty = 0
excise_tax = 0
vat = 0
total_duty = 0
total_cost = 0

today = datetime.date.today()
year = today.year
four_years_old_and_over  = int(year) - 4


go_to_menu = int(input())

if go_to_menu == 1:

    #Getting exchange rate
    print("Please enter the exchange rate you are using (GYD to USD)")
    exchange_rate = int(input())

    #Getting vehicle age
    print("Press ""1"" if your vehicle age is Four Years and Over (i.e. Anytime before) " + str(four_years_old_and_over))
    print("Press ""2"" if your vehicle age is Four Years Old (i.e. Anytime from) " + str(four_years_old_and_over))
    vehicle_age = int(input())

    #Vehicle age of Four years and Over    
    if vehicle_age == 1:

        #Getting petro type
        print("Is the vehicle using Gasoline or Disel or Electric?")
        print("Press ""1"" for Gasoline ")
        print("Press ""2"" for Disel or Semi-Disel")
        print("Press ""3"" for Electric")
        petro_type = int(input())

        #Gasoline Vehicle
        if petro_type == 1:
            print("How many Cubic Centimeters (CC) is the vehicle?")
            print("Press 1 for 1000cc and below")
            print("Press 2 for 1001cc to 1500cc")
            print("Press 3 for 1501cc to 1800cc")
            print("Press 4 for 1801cc to 2000cc")
            print("Press 5 for 2001cc to 3000cc")
            print("Press 6 for 3001cc and above")
            gasoline_engine_cc = int(input())

            print("What is the cost of the vehicle (Including insurance and freight) in USD?")
            cif = int(input())
            print(functions.get_total_duty_fyoo(cif, petro_type, gasoline_engine_cc, exchange_rate))

        #Disel/Semi-Disel Vehicle
        elif petro_type == 2:
            print("How many Cubic Centimeters (CC) is the vehicle?")
            print("Press 1 for 1500cc and below")
            print("Press 2 for 1501cc to 2000cc")
            print("Press 3 for 2001cc to 2500cc")
            print("Press 4 for 2501cc to 3000cc")
            print("Press 5 for 3001cc and above")
            disel_engine_cc = int(input())

            print("What is the cost of the vehicle (Including insurance and freight) in USD?")
            cif = int(input())
            print(functions.get_total_duty_fyoo(cif, petro_type, disel_engine_cc, exchange_rate))
        
        #Electric Vehicle
        else:
            print("What is the cost of the vehicle (Including insurance and freight) in USD?")
            cif = int(input())
            print(functions.get_total_duty_fyoo(cif, petro_type, 0, exchange_rate))

    #Vehicle age of Under Four Years     
    else:

        #Getting petro type
        print("Is the vehicle using Gasoline or Disel or Electric?")
        print("Press ""1"" for Gasoline ")
        print("Press ""2"" for Disel or Semi-Disel")
        print("Press ""3"" for Electric")
        petro_type = int(input())

        #Gasoline Vehicle
        if petro_type == 1:
            print("How many Cubic Centimeters (CC) is the vehicle?")
            print("Press 1 for 1000cc and below")
            print("Press 2 for 1001cc to 1500cc")
            print("Press 3 for 1501cc to 1800cc")
            print("Press 4 for 1801cc to 2000cc")
            print("Press 5 for 2001cc to 3000cc")
            print("Press 6 for 3001cc and above")
            gasoline_engine_cc = int(input())

            print("What is the cost of the vehicle (Including insurance and freight) in USD?")
            cif = int(input())
            print(functions.get_total_duty_ufy(cif, petro_type, gasoline_engine_cc, exchange_rate))

        #Disel/Semi-Disel Vehicle
        elif petro_type == 2:
            print("How many Cubic Centimeters (CC) is the vehicle?")
            print("Press 1 for 1500cc and below")
            print("Press 2 for 1501cc to 1800cc")
            print("Press 3 for 2000cc to 2500cc")
            print("Press 4 for above 2500cc")
            disel_engine_cc = int(input())

            print("What is the cost of the vehicle (Including insurance and freight) in USD?")
            cif = int(input())
            print(functions.get_total_duty_ufy(cif, petro_type, disel_engine_cc, exchange_rate))

        #Eelectric Vehicle
        else:
            print("What is the cost of the vehicle (Including insurance and freight) in USD?")

            cif = int(input())
            print(functions.get_total_duty_ufy(cif, petro_type, 0, exchange_rate))

#Rounding of Values
# cif = round(cif,2)
# duty = round(duty,2)
# excise_tax = round(excise_tax,2)
# vat = round(vat,2)
# total_duty = round(total_duty,2)
# total_cost = round(total_cost,2)
    
#Summary of Costs
# print("")
# print("-----------------------------------------------------------------")
# print("Cost of Car (Including Insurance and Frieght): $" + str(cif))
# print("Duty: $" + str(duty))
# print("Excise: $" + str(excise_tax))
# print("Value Added Tax (VAT): $" + str(vat))
# print("Total Tax Payable: $" + str(total_duty))
# print("Total Vehicle Cost $" + str(total_cost))
# print("-----------------------------------------------------------------")
