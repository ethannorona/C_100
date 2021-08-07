class Car(object):
    """
        blueprint for car
    """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("Accelarating...")
        "Accelarator functionality here"

    def changeGear(self, get_type):
        print("Get changed")
        "Gear related functionality here"

audi = Car("A6", "Red", "Audi", 80)
print(audi.stop())