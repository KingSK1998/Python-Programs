class Passenger:
    def __init__(self, pName, pAge, dt):
        self.passengerName = pName
        self.passengerAge  = pAge
        self.distanceTraveled = dt

def calculateTicketFare(passengers, farePerKM):
    ticketFareWithTax = 0
    for passenger in passengers:
        pa = passenger.passengerAge
        dt = passenger.distanceTraveled
        if pa >= 60 or pa < 12:
            ticketFareWithTax += 0 + dt*farePerKM
        elif pa >= 21 and pa <= 59:
            ticketFareWithTax += dt*farePerKM + (12*dt*farePerKM)/100
        elif pa >= 12 and pa <= 20:
            ticketFareWithTax += dt*farePerKM + (10*dt*farePerKM)/100
    return ticketFareWithTax

def countSeniorJuniorPassengers(plist):
    junior = 0
    senior = 0
    for p in plist:
        if p.passengerAge >= 60:
            senior += 1
        if p.passengerAge < 12:
            junior += 1
    return (junior + senior)    

if __name__ == "__main__":
    passengerArray = []
    # number of inputs
    n = int(input())
    # taking n number of object inputs
    for _ in range(n):
        name = input()
        age = int(input())
        travel = int(input())
        passengerArray.append(Passenger(name, age, travel))
    #ticket fare
    ticketFarePerKM = int(input())
    # Display last functions
    print(calculateTicketFare(passengerArray, ticketFarePerKM))
    print(countSeniorJuniorPassengers(passengerArray))