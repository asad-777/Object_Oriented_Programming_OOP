class tv:
    def __init__(self, brand, volume):
        self.brand = brand
        self.volume = volume

    # Corrected method signatures
    def volUp(self, volume):
        self.volume += volume
        print(f"The volume of {self.brand} TV is now {self.volume}")

    def volDown(self, volume):
        self.volume -= volume
        print(f"The volume of {self.brand} TV is now {self.volume}")

# Creating an instance of the tv class
tv1 = tv("samsung", 10)
print(f"The volume of tv1 is {tv1.volume}")

# Calling volUp method
tv1.volUp(15)
print(f"The volume of tv1 is {tv1.volume}")
