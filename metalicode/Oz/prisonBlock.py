from inmate import Inmate
from warden import Warden


class PrisonBlock:
    # ctor
    def __init__(self, name, numOfCells, wardon):
        self.wardon = wardon
        self.name = name
        self.numOfCells = numOfCells
        self.numOfInmatesInCell = 3
        self.numOfInmatesInBlock = 0
        self.cells = []
        for i in range(0, numOfCells):
            self.cells.append([])

    # add inmate to cell
    def addInmate(self,inmate):
        for i in range(0, self.numOfCells):
            wasAdd = False
            if len(self.cells[i]) < self.numOfInmatesInCell:
                self.cells[i].append(inmate)
                wasAdd = True
                self.numOfInmatesInBlock+=1
                print(f"prisonerNumber:{inmate.prisonerNumber}\tname:{inmate.fname} {inmate.lname} was added to cell {i}")
                break

            if not wasAdd:
                print(f"no room for inmate {inmate.prisonerNumber}")

    # make class iterable
    def __iter__(self):
        self.inmateCounter = 0
        return self

    def __next__(self):
        if int(self.inmateCounter/3) < self.numOfCells and self.inmateCounter < self.numOfInmatesInBlock:
            self.inmateCounter +=1
            return self.cells[((self.inmateCounter-1)/3)][(self.inmateCounter-1)%3]
        else:
            raise StopIteration

    def __repr__(self):
        return f"Block name: {self.name}\n Block Warden: {self.wardon}\n Inmates: {self.cells}"



def testPrisonBlock():
    w = Warden("Tim", "McManus", 12321, 10)
    block_a = PrisonBlock("ameraldCity")
    print(block_a.cells)
    print("\n")

