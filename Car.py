class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedlimit=speedlimit

        

    def start(self):
        print("started")

    def stop(self):
        print("stopped")     

    def accelarate(self):
        print("accelarated") 

    def changegear(self,gear_type):
        print("gear changed")       



audi=Car("a5","red","audi",80)
audi.changegear(2)   