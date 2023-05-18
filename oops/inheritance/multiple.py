class Country:
    def __init__(self):
        self.location="Kathmandu"

class Province:
    def __init__(self):
        self.location="Hetauda"

class District(Country, Province):
    def __init__(self):
        super().__init__()
        self.location="Bhaktapur"

dst=District()
print(dst.__dict__)
print(dst.location)