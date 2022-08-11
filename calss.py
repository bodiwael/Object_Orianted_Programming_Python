class Car:

    def __init__(self, color, brand, model):
        
        self.color = color
        
        self.brand = brand
        
        self.model = model

    def repaint(self, color):
        
        self.color = color

myCar = Car('Red', 'Dodge', 'Charger')

myCar.repaint('White')

helensCar = Car('Blue', 'Nissan', 'Ultima')

myCar.repaint('Green')