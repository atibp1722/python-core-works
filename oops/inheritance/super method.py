class PC(object):
    def __init__(self, ram, sdd):
        self.ram=ram
        self.sdd=sdd
        print("PC constructor called")

class Phone(PC):
    def __init__(self):
        super().__init__("8 gb", "128 gb")
        self.model="Z14 Ultra Pro"
        print("Mobile constructor called")

samsung=Phone()
print(samsung.__dict__)