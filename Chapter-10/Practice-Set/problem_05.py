# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indain Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fromm, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fromm} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fromm, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fromm} to {to} is {randint(1111, 9999)}")

train = Train(126946)
train.book("Rampur", "Delhi")
train.getFare("Rampur", "Delhi")
train.getStatus()