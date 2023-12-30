class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, departureCity="", departueCode="", destinationCity="", destinationCode="",
                 price=0, departureDate="", returnDate=""):
        self.departureLocation = (departureCity, departueCode)
        self.destinationLocation = (destinationCity, destinationCode)
        self.price = price
        self.departureDate = departureDate
        self.returnDate = returnDate

    def getDepartureLocation(self):
        return self.departureLocation

    def getDestinationLocation(self):
        return self.destinationLocation

    def getPrice(self):
        return self.price

    def getDepartureDate(self):
        return self.departueDate

    def getReturnDate(self):
        return self.returnDate

    def setDepartureLocation(self, city, code):
        self.departureLocation = (city, code)

    def setDestinationLocation(self, city, code):
        self.destinationLocation = (city, code)

    def setPrice(self, newPrice):
        self.price = newPrice

    def setDepartureDate(self, date):
        self.departueDate = date

    def setReturnDate(self, date):
        self.returnDate = date
