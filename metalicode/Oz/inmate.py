import time
from datetime import datetime

from dateutil.relativedelta import relativedelta

from person import Person


class Inmate(Person):
    # cntor
    def __init__(self, fname, lname, idNum, prisonerNumber, crime, time):
        self.prisonerNumber = prisonerNumber
        self.crime = crime
        self.jailTimeInYears = time
        self.firstDayInJail = datetime.now()
        self.isGoodInmate = False
        self.punishmentInMonths = 0
        self.hasDrugs = False
        super().__init__(fname,lname,idNum)

    # calc time left until freedom
    def calcTimeToFreedom(self):
        return self.getReleaseDate - datetime.now()

    # calc the time spent in jail
    def calcTimeSpentInJail(self):
        nowTime = datetime.now()
        return nowTime - self.firstDayInJail

    # calc the release date
    @property
    def getReleaseDate(self):
        delta = relativedelta(years=self.jailTimeInYears, months= self.punishmentInMonths)
        return self.firstDayInJail + delta

    # add punishment time
    def addTime(self, timeInMonths):
        self.punishmentInMonths += timeInMonths

    # buy drugs
    def buyDrugs(self):
        self.hasDrugs = True

    def useDrugs(self):
        if self.hasDrugs:
            print(f"{self.fname}: mmmmm...i love drugs...")
            self.hasDrugs = False
        else:
            print(f"{self.fname}: has no drugs...")

    def __repr__(self):
        return super().__repr__() + f"ID: {self.idNum}\n prisoner Number:{self.prisonerNumber}\n Crime: {self.crime}"

##### TEST ##########
def testInmate():
    inmate = Inmate("Simon","Adebisi",123,111,'killer',10)
    time.sleep(4)
    print(inmate.calcTimeSpentInJail())
    print(inmate.getReleaseDate)
    inmate.addTime(5)
    print(inmate.getReleaseDate)
    print(inmate.calcTimeToFreedom())

