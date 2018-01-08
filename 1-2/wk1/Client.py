from Hardwares import *

stater = [input("Company | Ex.'Microsoft': "), input("Series | Ex.'MS2017': "), float(input("Price | 'Ex.29.99': "))]
while True:
    start_type = input("Please Choose: Monitor, Printer, Mouse: ")
    if start_type == "Monitor":
        Monitor = Monitor(stater)
        Monitor.updateDetail(input("Resolution | Ex.'1920x1080': "), int(input("Refresh Rate | Ex.60: ")), int(input("Response Time | Ex.4: ")))
        Monitor.checkDetail(Monitor.company, Monitor.price)
        print("\nCompany: {0} \nSeries: {1} \nPrice: {2} $".format(Monitor.company, Monitor.series, Monitor.price))
        print("-" * 29)
        print("Resolution: {0} \nRefresh Rate: {1} \nResponse Time: {2}".format(Monitor.resolution, Monitor.refreshRate, Monitor.respontime))
        print("-" * 10, "Success", "-" * 10)
        break
    elif start_type == "Printer":
        Printer = Printer(stater)
        Printer.updateDetail(int(input("Page Per Minute | Ex.30: ")), input("Color | Ex.'black/white': "), input("Paper Size | Ex.595,842: "))
        Printer.printRate(Printer.pagePerMin, Printer.paperSize)
        print("\nCompany: {0} \nSeries: {1} \nPrice: {2} $".format(Printer.company, Printer.series, Printer.price))
        print("-" * 29)
        print("Page Per Minute: {0} \nColor: {1} \nPaper Size: {2}".format(Printer.pagePerMin, Printer.color, Printer.paperSize))
        print("-" * 10, "Success", "-" * 10)
        break
    elif start_type == "Mouse":
        Mouse = Mouse(stater)
        Mouse.updateDetail(int(input("DPI | Ex.300: ")), bool(input("Side Button | Ex.'True or 1': ")))
        Mouse.performance(Mouse.company, Mouse.price)
        print("\nCompany: {0} \nSeries: {1} \nPrice: {2} $".format(Mouse.company, Mouse.series, Mouse.price))
        print("-" * 29)
        print("DPI: {0} \nSide Button: {1}".format(Mouse.dpi, Mouse.sideButton))
        print("-" * 10, "Success", "-" * 10)
        break