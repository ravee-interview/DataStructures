class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.car_type = {
            1 : big,
            2 : medium,
            3 : small
        }
        

    def addCar(self, car_type): #o(1)
        """
        :type carType: int
        :rtype: bool
        """
        if self.car_type[car_type] == 0:
            return False
        self.car_type[car_type] -=1
        return True
        
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
