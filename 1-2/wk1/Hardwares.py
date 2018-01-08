class Hardwares:
    def __init__(self, company, series, price):
        self.company = "Microsoft"
        self.series = "MS2017"
        self.price = 29.99 #ดอลล่า

class Monitor(Hardwares):
    def __init__(self,stater):
        super().__init__(stater[0], stater[1], stater[2])

    def updateDetail(self, resolution, refreshRate, responseTime):
        self.resolution = resolution
        self.refreshRate = refreshRate
        self.respontime = responseTime
    def checkDetail(self, company, series):
        if company == "Microsoft" and series == "MS2017":
            self.detail = "Microsoft Monitor 2017 Thailand only."
        else:
            self.detail = "Notfound."

class Printer(Hardwares):
    def __init__(self, stater):
        super().__init__(stater[0], stater[1], stater[2])

    def updateDetail(self, pagePerMin, color, paperSize):
        self.pagePerMin = pagePerMin
        self.color = color
        self.paperSize = paperSize
    def printRate(self, pagePerMin, paperSize):
        paperSize.split(',')
        self.printRate = round((pagePerMin * 60) / (int(paperSize[0] + paperSize[1]) / 2)) #ตัวอย่างไม่ได้อ้างอิงจากใหน

class Mouse(Hardwares):
    def __init__(self, stater):
        super().__init__(stater[0], stater[1], stater[2])
    def updateDetail(self, dpi, sideButton):
        self.dpi = dpi
        self.sideButton = sideButton
    def performance(self, company, series):
        if company == "Microsoft" and series == "MS2017":
            self.performance = 10
        else:
            self.performance = 0
