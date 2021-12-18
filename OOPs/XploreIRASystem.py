class Service:
    serviceId = 0
    regNo = ""
    model = ""
    mileage = 0
    isInsured = ""
    paymentRecvd = 0.0

    def __init__(self, serviceId, regNo, model, mileage, isInsured, paymentRecvd):
        self.serviceId = serviceId
        self.regNo = regNo
        self.model = model
        self.mileage = mileage
        self.isInsured = isInsured
        self.paymentRecvd = paymentRecvd
    
class ServiceCenter:
    milagedict = {}
    serviceList = list(Service)

    def __init__(self, mileageDict, serviceList):
        self.milagedict = mileageDict
        self.serviceList = serviceList   

    def getTotalPaymentOfInsuredCars(self, manufactureName, stateCode):
        for e in self.serviceList:
            if e.manufactureName == manufactureName and e.stateCode == stateCode:
                return manufactureName.upper() + str(stateCode) + e.paymentRecvd
        return None

    def getServicedCarWithProperMileage(self):
        
        pass


# Main
if __name__ == "__main__":
    noOfService = int(input())
    service = []

    for i in range(noOfService):
        serviceId = int(input())
        regNo = input()
        model = input()
        mileage = int(input())
        isInsured = input()
        paymentRecvd = float(input())
        obj = Service(serviceId, regNo, model, mileage, isInsured, paymentRecvd)
        service.append(obj)

    noOfMileageDict = int(input())
    serviceCenter = {}

    for i in range(noOfMileageDict):
        model = input()
        expectedMielage = int(input())
        serviceCenter[model] = expectedMielage

    manufactureName = input()
    stateCode = int(input())

    obj = ServiceCenter(serviceCenter, service)
    obj.getTotalPaymentOfInsuredCars(manufactureName, stateCode)
    obj.getServicedCarWithProperMileage()
        
