#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def updateIATACodes(dataManager, flightSearcher):
    cities = dataManager.getCities()
    codes = flightSearcher.getIATACodes(cities)
    dataManager.enterIATACodes(codes)


dataManager = DataManager()
flightSearcher = FlightSearch()

# updateIATACodes(dataManager, flightSearcher)

data = dataManager.getData()
# flightSearcher.determineLowPriceFlights(data)
flights = flightSearcher.determineLowPriceFlights(data)

if len(flights) > 0:
    notifier = NotificationManager()

    if len(flights) == 1:
        notifier = notifier.sendMessageForOne(flights[0])
    else:
        notifier = notifier.sendMessageForMultiple(flights[0], len(flights))