# Can you change the self-parameter inside a class to something else (say "something"). Try changing self to "slf" or "something" and see the effects.

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(myname, fromm, to):
        print(f"Ticket is booked in train no: {myname.trainNo} from {fromm} to {to}")

train = Train(126946)
train.book("Rampur", "Delhi")

# It's properly working with "slf" or "something"