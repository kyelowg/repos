
#   Kye Lowmon CIS261 project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter employee pay-cycle start date (mm/dd/yyyy): ")
    return fromdate
def GetDatesWorked2():
    todate = input("Enter employee pay-cycle end date (mm/dd/yyyy): ")
    return todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
def list(EmpList):
    for EmpList in EmpListDetail:
        fromdate = float(input(EmpList[0]))
        todate = float(input(EmpList[1]))
        empname = float(input(EmpList[2]))
        hours = float(input(EmpList[3]))
        hourlyrate = float(input(EmpList[4]))
        taxrate = float(input(EmpList[5]))
def list(EmpDetail):
    for i, EmpDetail in enumerate(EmpList, start = [0]):
        print(f'{i}. {EmpList}')
        print()

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        EmpTotals = {"TotEmp" : "TotEmployees"}
        EmpTotals = {"TotHrs" : "TotHours"}
        EmpTotals = {"TotGP" : "TotGrossPay"}
        EmpTotals = {"TTax" : "TotTax"}
        EmpTotals = {"TotNP" : "TotNetPay"}
        
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Income Tax:  {TotTax:,.2f}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")




if __name__ == "__main__":
        TotEmployees = 0
        TotHours = 0.00
        TotGrossPay = 0.00
        TotTax = 0.00
        TotNetPay = 0.00

      
        EmpDetailList = []
        EmpDetail = []
        EmpTotals = {}
        while True:
            empname = GetEmpName()
            if (empname.upper() == "END"):
                break
            
            fromdate = GetDatesWorked()
            todate = GetDatesWorked2()
            hours = GetHoursWorked()
            hourlyrate = GetHourlyRate()
            taxrate = GetTaxRate()



def PrintTotals(EmpTotals):    
    print()

    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {"TotEmp"}')
    print(f'Total Number Of Hours Worked: {"TotHrs"}')
    print(f'Total Amount of Employee Gross Pay: {"TotGP"}')
    print(f'Total Amount of Tax Deduction: {"TTax"}')
    print(f'Total Amount of Employee Net Pay: {"TotNP"}')

        
  
def list(EmpDetail):
    i, EmpDetail in enumerate(EmpList, start = 0)               

EmpDetailList.append(EmpDetail)



printinfo(EmpDetailList)
PrintTotals(EmpTotals)



