class car:

    #make = None
    #model = None
    #year = None
    #color = None

    def __init__(self,make,model,year,color):
        self.make = make
        self.year = year
        self.model = model
        self.color = color

    def drive(self):
        print('this' + self.make  +  ' is driving')

    def stop(self):
        print('This car is stopping')