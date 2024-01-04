def convert_to_gyd(in_currency: str, in_exchange_rate: int, in_amount: float) -> float:
    
    return_val = 0

    try:
        if in_currency.upper() == "USD":
            return_val = in_amount * in_exchange_rate
        else :
            return_val = -1
    except:
        print("Error in exchange rate conversion")
    
    return round(return_val,2)

#Four years and older
def get_total_duty_fyoo(in_cif: int,in_petrol_type: int, in_cc_no: int, in_exchange_rate: int):

    #declare variables 
    cif = convert_to_gyd("USD",in_exchange_rate, in_cif)

    #Gasloine
    if in_petrol_type == 1:
        try:
            #1000cc and below
            if in_cc_no == 1:
                try:
                    duty = 0
                    excise_tax = 800000
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1000cc and below."

            #1001cc to 1500cc
            elif in_cc_no == 2:
                try:
                    duty = 0
                    excise_tax = 800000
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1001cc to 1500cc."

            #1501cc to 1800cc
            elif in_cc_no == 3:
                try:
                    duty = 0
                    excise_tax = round((((cif + (6000 * in_exchange_rate)) * 0.3) + (6000 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1501cc to 1800cc."

            #1801cc to 2000cc
            elif in_cc_no == 4:
                try:
                    duty = 0
                    excise_tax = round((((cif + (6500 * in_exchange_rate)) * 0.3) + (6500 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of #1801cc to 2000cc."

            #2001cc to 3000cc
            elif in_cc_no == 5:
                try:
                    duty = 0
                    excise_tax = round((((cif + (13500 * in_exchange_rate)) * 0.7) + (13500 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 2001cc to 3000cc."


            #3001cc and above
            else:
                try:
                    duty = 0
                    excise_tax = round((((cif + (6000 * in_exchange_rate)) * 1) + (6000 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 3001cc and above."
        except:
            print("Error: Unable to calculate import tax for gasoline vehicles.")

    #Disel/Semi Disel Vehicle
    elif in_petrol_type == 2:
        try:
            #1500cc and below
            if in_cc_no == 1:
                try:
                    duty = 0
                    excise_tax = 800000
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1500cc and below."

            #1501cc to 2000cc
            elif in_cc_no == 2:
                try:
                    duty = 0
                    excise_tax = round((((cif + (15400 * in_exchange_rate)) * 0.3) + (15400 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1501cc to 2000cc."

            #2001cc to 2500cc
            elif in_cc_no == 3:
                try:
                    duty = 0
                    excise_tax = round((((cif + (15400 * in_exchange_rate)) * 0.7) + (15400 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 2001cc to 2500cc."

            #2501cc to 3000cc
            elif in_cc_no == 4:
                try:
                    duty = 0
                    excise_tax = round((((cif + (15500 * in_exchange_rate)) * 0.7) + (15500 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 2501cc to 3000cc."

            #3001cc and above
            else:
                try:
                    duty = 0
                    excise_tax = round((((cif + (17200 * in_exchange_rate)) * 1) + (17200 * in_exchange_rate)),2)
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 3001cc and above."
        except:
            print("Error: Unable to calculate import tax for diesel vehicles.")

    #Electric Vehicle
    else:
        try:
            if in_cc_no == 0:
                duty = 0
                excise_tax = 800000
                vat = 0
                total_duty = round((duty + excise_tax + vat),2)
                total_cost = round((cif + total_duty),2)

                cif = "${:,.2f}".format(cif)
                duty = "${:,.2f}".format(duty)
                excise_tax = "${:,.2f}".format(excise_tax)
                vat = "${:,.2f}".format(vat)
                total_duty = "${:,.2f}".format(total_duty)
                total_cost = "${:,.2f}".format(total_cost)

                result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
        except:
            print("Error: Unable to calculate import tax for electric vehicles.")

    return result_string

#Under Four Years
def get_total_duty_ufy(in_cif: int,in_petrol_type: int, in_cc_no: int, in_exchange_rate: int):

    #declare variables 
    cif = convert_to_gyd("USD",in_exchange_rate, in_cif)

    #Gasloine
    if in_petrol_type == 1:
        try:
            #1000cc and below
            if in_cc_no == 1:
                try:
                    duty = round((0.35 * cif),2)
                    excise_tax = 0
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1000cc and below."

            #1001cc to 1500cc
            elif in_cc_no == 2:
                try:
                    duty = round((0.35 * cif),2)
                    excise_tax = 0
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1001cc to 1500cc."

            #1501cc to 1800cc
            elif in_cc_no == 3:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((0.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1501cc to 1800cc."
                    
            #1801cc to 2000cc
            elif in_cc_no == 4:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((0.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1801cc to 2000cc."

            #2001cc to 3000cc
            elif in_cc_no == 5:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((1.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 2001cc to 3000cc."

            #3001cc and above
            else:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((1.4 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 3001cc and above."
        except:
            print("Error: Unable to calculate import tax for gasoline vehicles.")

    #Disel/Semi Disel Vehicle
    elif in_petrol_type == 2:
        try:
            #1500cc and below
            if in_cc_no == 1:
                try:
                    duty = round((0.35 * cif),2)
                    excise_tax = 0
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1500cc and below."

            #1501cc to 2000cc
            elif in_cc_no == 2:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((0.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 1501cc to 2000cc."

            #2001cc to 2500cc
            elif in_cc_no == 3:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((1.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 2001cc to 2500cc."

            #3001cc and above
            else:
                try:
                    duty = round((0.45 * cif),2)
                    excise_tax = round((1.1 * (cif + duty)),2)
                    vat = round((0.14 * (cif + duty + excise_tax)),2)
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)

                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for vehicle of 3001cc and above."
        except:
            print("Error: Unable to calculate import tax for diesel vehicles.")

    #Electric Vehicle
    else:
        try:
            if in_cc_no == 0:
                try:
                    duty = 0
                    excise_tax = 0
                    vat = 0
                    total_duty = round((duty + excise_tax + vat),2)
                    total_cost = round((cif + total_duty),2)

                    cif = "${:,.2f}".format(cif)
                    duty = "${:,.2f}".format(duty)
                    excise_tax = "${:,.2f}".format(excise_tax)
                    vat = "${:,.2f}".format(vat)
                    total_duty = "${:,.2f}".format(total_duty)
                    total_cost = "${:,.2f}".format(total_cost)
                    
                    result_string = f"-----------------------------------------------------------------\nCost of Car (Including Insurance and Frieght): {cif}\nDuty: {duty}\nExcise: {excise_tax}\nValue Added Tax (VAT): {vat}\nTotal Tax Payable: {total_duty}\n-----------------------------------------------------------------\nTotal Vehicle Cost {total_cost}\n-----------------------------------------------------------------"
                except:
                    result_string = "Error: Unable to calculate import tax for electric vehicles."
        except:
            print("Error: Unable to calculate import tax for electric vehicles.")
            
    return result_string

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
        result_string = get_total_duty_fyoo(int(vehicle_cost), int(petrol_type), int(engine_size), int(exchange_rate))
    else:
        result_string = get_total_duty_ufy(int(vehicle_cost), int(petrol_type), int(engine_size), int(exchange_rate))

    result_text.delete(1.0, END)  # Clear existing content
    result_text.insert(END, result_string)


