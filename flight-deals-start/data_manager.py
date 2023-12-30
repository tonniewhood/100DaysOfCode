
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    # Data Fields #
    ENDPOINT = "https://api.sheety.co/cfda42ddc48a36a5363894b4f599c821/flightTracker/sheet1"
    header = {
        "Authorization": "Bearer thisIsASecret",
        "Content-Type": "application/json",
    }

    # Methods #

    def getCities(self) -> list:

        response = requests.get(url=self.ENDPOINT, params="", headers=self.header)

        cities = []
        for entry in response.json()["sheet1"]:
            cities.append(entry["location"])

        print(response.text)

        # with open("Untitled spreadsheet - Sheet1.csv") as data:
        #
        #     document = data.readlines()
        #     document.pop(0)
        #
        #     cities = []
        #     for line in document:
        #         lineAsList = line.split(",")
        #         cities.append(lineAsList[0])

        return cities

    def enterIATACodes(self, codes):

        objectId = 2
        for city, code in codes:

            putEndpoint = f"{self.ENDPOINT}/{objectId}"
            objectId += 1

            body = {
                "sheet1": {
                    "iataCode": code
                }
            }

            response = requests.put(url=putEndpoint, headers=self.header, json=body)

            print(response.text)

    def getData(self) -> list:

        with open("Flight Tracker - Sheet1.csv") as data:

            document = data.readlines()
            document.pop(0)

            data = []
            for line in document:
                newData = line.split(",")
                newEntry = {
                    "City": newData[0],
                    "IATA Code": newData[1],
                    "Floor Price": int(newData[2])
                }
                data.append(newEntry)

        return data

