class Person:
    PersonName = None
    PersonHeight = None
    PersonWeight = None
    PersonBMI = None
    PersonBMIStatus = None

    def __init__(self, name, height, weight):
        self.PersonName = name
        self.PersonHeight = height
        self.PersonWeight = weight
        self.PersonBMI = 0
        self.PersonBMIStatus = ""

    def calculateBMI(self):
        self.PersonBMI = self.PersonWeight/(self.PersonHeight*self.PersonHeight)
        self.PersonBMI = round(self.PersonBMI)
    
class Society:
    bmi_status = {}     #? BMIStatus{BMI_status: (lower_BMI_limit, upper_BMI_limit)}
    person_list = []    #? Persons

    def __init__(self, status, person):
        self.bmi_status = status
        self.person_list = person
    
    def calculateBmiAndStatusByName(self, personName):  # getting name of a person
        foundYOU = False
        for person in self.person_list:
            if person.PersonName == personName:
                foundYOU = True                         # Till here person is found
                person.calculateBMI()                   # and calculated his bmi and he is happy
                # find his status godammit
                for key, val in self.bmi_status.items():
                    if person.PersonBMI >= val[0] and person.PersonBMI <= val[1]:
                        person.PersonBMIStatus = key
        return foundYOU

    def removeInvalidPersons(self, personBMI):
        invalids = []
        for person in self.person_list:
            person.calculateBMI()
            if person.PersonBMI < personBMI:
                invalids.append(person)
        return invalids

n = int(input())
persons = []
for _ in range(n):
    name = input()
    height = int(input())
    weight = int(input())
    persons.append(Person(name, height, weight))

m = int(input())
bmistatus = {}
for _ in range(m):
    status = input()
    lowerLimit = int(input())
    upperLimit = int(input())
    if lowerLimit > upperLimit:
        bmistatus[status] = (upperLimit, lowerLimit)
    else:
        bmistatus[status] = (lowerLimit, upperLimit)
society = Society(bmistatus, persons)

name = input()
if society.calculateBmiAndStatusByName(name):
    for person in society.person_list:
        if person.PersonBMI != 0 and person.PersonName == name:
            print(person.PersonBMI, person.PersonBMIStatus)
else:
    print("No Person Exists")

bmiValue = int(input())
for invalid in society.removeInvalidPersons(bmiValue):
    print(invalid.PersonName, invalid.PersonBMI)