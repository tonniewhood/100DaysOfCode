
import requests
import datetime

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    # Data Fields #
    DEPARTURE_AIRPORT = "SLC"
    CODES_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
    SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    header = {
        "apikey" : "CNDafVjoxtBHuB1pQ84PmHjP6_jqQYDv",
        "Content-Type": "application/json",
    }

    # Methods #
    def getIATACodes(self, cities) -> list:

        codes = []

        for city in cities:
            params = {
                "term": city,
                "location_types": "airport",
                "limit": 1,
            }

            response = requests.get(url=self.ENDPOINT, headers=self.header, params=params)

            iataCode = response.json()["locations"][0]["id"]
            newTuple = (city, iataCode)

            codes.append(newTuple)

        return codes

    def determineLowPriceFlights(self, dataIn) -> list:

        dates = self.getTodayAndSixMonthsOut()

        potentialFlights = []

        for row in dataIn:

            params = {
                "fly_from": self.DEPARTURE_AIRPORT,
                "fly_to": row["IATA Code"],
                "date_from": dates[0],
                "date_to": dates[1],
                "price_to": row["Floor Price"],
                "one_for_city": 1,
                "nights_in_dst_from": 1,
                "nights_in_dst_to": 5,
                "curr": "USD",
            }

            response = requests.get(url=self.SEARCH_ENDPOINT, headers=self.header, params=params)

            if len(response.json()["data"]) > 0:
                flight = self.parseRelevantInformation(response.json()["data"][0])
                potentialFlights.append(flight)

        return potentialFlights

    def parseRelevantInformation(self, flight):

        localDeparture = flight["local_departure"].split("T")

        newFlight = {
            "cityFrom": flight["cityFrom"],
            "cityCodeFrom": flight["flyFrom"],
            "cityTo": flight["cityTo"],
            "cityCodeTo": flight["flyTo"],
            "localDepartureDate": localDeparture[0],
            "nightsInDest": flight["nightsInDest"],
            "price": flight["price"]
        }

        return newFlight

    def getTodayAndSixMonthsOut(self) -> tuple:

        today = datetime.datetime.today().date()
        formattedDate = f"{today.day}/{today.month}/{today.year}"

        if today.month + 6 > 12:
            newMonth = today.month - 6
            newYear = today.year + 1
            if newMonth == 2 and today.day > 28:
                newDay = 1
                newMonth = 3
            else:
                newDay = today.day
        else:
            newMonth = today.month + 6
            newYear = today.year
            if newMonth == 2 and today.day > 28:
                newDay = 1
                newMonth = 3
            else:
                newDay = today.day

        sixMonthsAhead = f"{newDay}/{newMonth}/{newYear}"

        return (formattedDate, sixMonthsAhead)
