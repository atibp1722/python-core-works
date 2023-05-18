class Finance:

    name="New Finance"
    interest=10.25

    @staticmethod
    def simpleInterest(p, t):
        total=(p*t*Finance.interest)/100
        print(f"The interest is {total}")

p=float(input("Enter principal: "))
t=int(input("Enter years: "))
Finance.simpleInterest(p, t)