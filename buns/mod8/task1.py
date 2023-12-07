class Transport():
    
    def __init__(self, *args, **kwargs):
        self._coordinates = (args[0], args[1])
        self._speed = args[4]
        self._brand = args[2]
        self._year = args[3]
        self._number = args[5]

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if (not isinstance(coordinates, int)):
            raise TypeError('type error')
        
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if (not isinstance(speed, int)):
            raise TypeError("type error")
        
        if speed < 0:
            raise ValueError("value error")
        
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("type error")
        
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if (not isinstance(year, int)):
            raise TypeError("type error")
        
        elif year < 0:
            raise ValueError("value error")
        
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if (not isinstance(number, int)):
            raise TypeError("type error")
        
        elif number < 0:
            raise ValueError("value error")
        
        self._number = number

    def __str__(self):
        return (f"Transport \n Coordinates = {self.coordinates} \n Speed = {self.speed} \n Brand = {self.brand} \n Year = {self.year} \n Number = {self.number}")

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x, y = self._number
        
        return (pos_x <= x <= pos_x + length) and (pos_y <= y <= pos_y + width)

#
class Passenger():
    
    def __init__(self, *args, **kwargs):
        self.__capacity = args[0]
        self.__num_passengers = args[1]

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if (not isinstance(capacity, int)):
            raise TypeError("type error")
        
        if capacity < 0:
            raise ValueError("value error")
        self.__capacity = capacity

    @property
    def num_passengers(self):
        return self.__num_passengers

    @num_passengers.setter
    def num_passengers(self, num_passengers):
        if (not isinstance(num_passengers, int)):
            raise TypeError("type error")
        
        elif num_passengers < 0:
            raise ValueError("value error")
        
        self.__num_passengers = num_passengers

    def __str__(self):
        return (f"Passenger \n Capacity = {self.capacity} \n Number = {self.num_passengers}")

#
class Cargo():
    
    def __init__(self, *args, **kwargs):
        self.__carrying = args[0]

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, int):
            raise TypeError("type error")
        
        if carrying <= 0:
            raise ValueError("value error")
        
        self.__carrying = carrying

#
class Plane(Transport):
    
    def __init__(self, *args):
        self._height = args[0]
        super().__init__(*args[1::])

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if (not isinstance(height, int)):
            raise TypeError("type error")
        
        if height <= 0:
            raise ValueError("value error")
        
        self._height = height
        
#
class Auto(Transport):

    def __init__(self, *args, **kwargs):
        self.__factory = args[0]
        super().__init__(*args[1::])

    @property
    def factory(self):
        return self.__factory

    @factory.setter
    def factory(self, factory):
        if (not isinstance(factory, str)):
            raise TypeError("type error")
        
        self.__factory = factory
#
class Ship(Transport):
    
    def __init__(self, *args, **kwargs):
        self.__port = args[0]
        super().__init__(*args[1::])

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if (not isinstance(port, str)):
            raise TypeError("type error")
        
        self.__port = port

#

class Car(Auto):
    
    def __init__(self, model, *args):
        self.__model = model
        super().__init__(*args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model

#
class Bus(Auto, Passenger):
    
    def __init__(self, model, capacity, num_passengers, *auto_args):
        self.__model = model
        Passenger.__init__(self, capacity, num_passengers)
        Auto.__init__(self, *auto_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model

#

class CargoAuto(Auto, Cargo):
    
    def __init__(self, model, carrying, *auto_args):
        self.__model = model
        Cargo.__init__(self, carrying)
        Auto.__init__(self, *auto_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model
        
#
class Boat(Ship):
    
    def __init__(self, model, *ship_args):
        self.__model = model
        super().__init__(*ship_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model
#

class PassengerShip(Ship, Passenger):
    
    def __init__(self, model, capacity, num_passengers, *ship_args):
        self.__model = model
        Passenger.__init__(self, capacity, num_passengers)
        Ship.__init__(self, *ship_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model


#
class CargoShip(Ship, Cargo):
    
    def __init__(self, model, carrying, *car_ship_args):
        self.__model = model
        Ship.__init__(self, *car_ship_args)
        Cargo.__init__(self, carrying)
        
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model

#
class Airplane(Plane):
    
    def __init__(self, model, *plane_args):
        self.__model = model
        super().__init__(*plane_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model
#

class PassengerPlane(Plane, Passenger):
    
    def __init__(self, model, capacity, num_passengers, *plane_args):
        self.__model = model
        Passenger.__init__(self, capacity, num_passengers)
        Plane.__init__(self, *plane_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("TypeError")
        
        self.__model = model

#

class CargoPlane(Plane, Cargo):
    
    def __init__(self, model, carrying, *plane_args):
        self.__model = model
        Cargo.__init__(self, carrying)
        Plane.__init__(self, *plane_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("TypeError")
        
        self.__model = model

#
class Seaplane(Plane, Ship):
    
    def __init__(self, model, port, height, *sea_args):
        self.__model = model
        Ship.__port = port
        Plane.__height = height
        Transport.__init__(self, *sea_args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if (not isinstance(model, str)):
            raise TypeError("type error")
        
        self.__model = model
        
auto = Auto("ford", 200, 100, "ford motors", 1953, 99, 134)
print(auto)  
print()
auto.speed = 150  
auto.brand = "toyota"  
auto.year = 2023  
auto.factory = "toyota factory"  
print(auto)  

