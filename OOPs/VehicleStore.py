class Vehicle:
    def __init__(self, number, price, name):
        self.number = number
        self.price = price
        self.name = name

class Store:
    def __init__(self,storeName,vehicleList):
        self.storeName=storeName
        self.vehicleList=vehicleList

    def findminvehbyprice(self):
        minval=min(self.vehicleList,key=lambda a:a.price)
        return minval
        
    def maxvehbynum(self):
        maxval=max(self.vehicleList,key=lambda a:a.number)
        return maxval

if __name__ == "__main__":
    n=int(input())
    l=[]
    for i in range(n):
        number=int(input())
        price=int(input())
        name=input()
        v = Vehicle(number, price, name)
        l.append(v)

    s=Store("ABC",l)
    s1=s.findminvehbyprice()
    print(s1.number)    # 88
    print(s1.price)     # 600000
    print(s1.name)      # Maruti Suzuki Dzire
    
    s2=s.maxvehbynum()
    print(s1.number)    # 95
    print(s1.price)     # 900000
    print(s1.name)      # Tata Altroz