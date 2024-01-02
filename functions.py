def convert_to_gyd(in_currency: str, in_exchange_rate: int, in_amount: float) -> float:
    
    return_val = 0

    if in_currency.upper() == "USD":
        return_val = in_amount * in_exchange_rate
    else :
        return_val = -1
    
    return round(return_val,2)

#Four years and older
def get_total_duty_fyoo(in_cif: int,in_petrol_type: int, in_cc_no: int, in_exchange_rate: int):

    #declare variables 
    cif = convert_to_gyd("USD",in_exchange_rate, in_cif)

    #Gasloine
    if in_petrol_type == 1:
        #1000cc and below
        if in_cc_no == 1:

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

        #1001cc to 1500cc
        elif in_cc_no == 2:

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

        #1501cc to 1800cc
        elif in_cc_no == 3:

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

        #1801cc to 2000cc
        elif in_cc_no == 4:

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

        #2001cc to 3000cc
        elif in_cc_no == 5:

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

        #3001cc and above
        else:

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

    #Disel/Semi Disel Vehicle
    elif in_petrol_type == 2:
        #1500cc and below
        if in_cc_no == 1:

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

        #1501cc to 2000cc
        elif in_cc_no == 2:

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

        #2001cc to 2500cc
        elif in_cc_no == 3:

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

        #2501cc to 3000cc
        elif in_cc_no == 4:

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

        #3001cc and above
        else:

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

    #Electric Vehicle
    else:
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


    return result_string

#Under Four Years
def get_total_duty_ufy(in_cif: int,in_petrol_type: int, in_cc_no: int, in_exchange_rate: int):

    #declare variables 
    cif = convert_to_gyd("USD",in_exchange_rate, in_cif)

    #Gasloine
    if in_petrol_type == 1:
        #1000cc and below
        if in_cc_no == 1:

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

        #1001cc to 1500cc
        elif in_cc_no == 2:

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

        #1501cc to 1800cc
        elif in_cc_no == 3:

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

        #1801cc to 2000cc
        elif in_cc_no == 4:

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

        #2001cc to 3000cc
        elif in_cc_no == 5:

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

        #3001cc and above
        else:

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

    #Disel/Semi Disel Vehicle
    elif in_petrol_type == 2:
        #1500cc and below
        if in_cc_no == 1:

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

        #1501cc to 2000cc
        elif in_cc_no == 2:

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

        #2001cc to 2500cc
        elif in_cc_no == 3:

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

        #3001cc and above
        else:

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

    #Electric Vehicle
    else:
        if in_cc_no == 0:
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
    
    return result_string




