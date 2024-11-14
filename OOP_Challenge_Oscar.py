#%% #OOP_Challenge

class Car:
    car_count = 0

    def __init__(self, merke, model, år):
        self.merke = merke
        self.model = model
        self.år = år 
        Car.car_count += 1

    def __str__(self):
        return f"{self.år} {self.merke} {self.model}"
    
    def start_engine(self):
        print("Motoren starter ...")

    def stop_engine(self):
        print("Motoren stopper ...")

    def drive(self):
        print("Bilen kjører ...")


bil_1 = Car("Volvo", "XC90", 2020)
bil_2 = Car("Audi", "E-tron", 2024)

print(bil_1)
print(bil_2)

bil_2.start_engine()
bil_2.stop_engine()
bil_2.drive()

class ElectricCar(Car):
    def __init__(self, merke, model, år, battery_capacity):
        super().__init__(merke, model, år)
        self._battery_capacity = battery_capacity
        self._current_charge = 0

    @property
    def battery_capacity(self):
        return self._battery_capacity

    @battery_capacity.setter

    def battery_capacity(self, value):
        if value > 0:  
            self._battery_capacity = value
        else:
            print("Batterikapasiteten må være større enn 0 kWh.")

    def charge_battery(self, amount):
        if self._current_charge + amount >= self._battery_capacity:
            self._current_charge = self._battery_capacity
            print(f"Batteriet er nå fullt (Kapasitet: {self._battery_capacity} kWh).")
            self.update_software()  
        else:
            self._current_charge += amount
            print(f"Batteriet lades... Nåværende ladning: {self._current_charge} / {self._battery_capacity} kWh")

    def update_software(self):
        print("Oppdaterer systemet ... ")
    
    def drive(self):
        print("Den elektriske bilen kjører på batteriet.")


bil_3 = ElectricCar("Tesla", "Model X", 2023, 100)

print(bil_3)

bil_3.charge_battery(40)

bil_3.charge_battery(100)

bil_3.drive()

print(f"Antall biler opprettet: {Car.car_count}")


# %%
