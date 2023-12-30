from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    ACCOUNT_SID = "" # Enter Info Here and Below
    AUTH_TOKEN = ""
    TWILIO_NUMBER = ""
    PERSONAL_NUMBER = ""

    def __init__(self):
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def sendMessageForOne(self, flight):

        msg = [f"Good News! There's a flight available to {flight['cityTo']} for only ${flight['price']}!"
               f" Check out the details down below."]

        msg.append(f"${flight['price']} flight departing from {flight['cityFrom']}-{flight['cityCodeFrom']}"
                   f" arriving at {flight['cityTo']}-{flight['cityCodeTo']} from {flight['localDepartureDate']}"
                   f" for {flight['nightsInDest']} nights.")

        for text in msg:
            self.client.messages.create(body=text, from_=self.TWILIO_NUMBER, to=self.PERSONAL_NUMBER)

    def sendMessageForMultiple(self, flight, numberOfFlights):

        msg = [f"Good News! There are {numberOfFlights} available flights that are all under budget!"
               f" Check out the details for the highest priority flight down below."]

        msg.append(f"${flight['price']} flight departing from {flight['cityFrom']}-{flight['cityCodeFrom']}"
                   f" arriving at {flight['cityTo']}-{flight['cityCodeTo']} from {flight['localDepartureDate']}"
                   f" for {flight['nightsInDest']} nights.")

        for text in msg:
            self.client.messages.create(body=text, from_=self.TWILIO_NUMBER, to=self.PERSONAL_NUMBER)
