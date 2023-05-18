class Decorator:
    def __init__(self, func):
        self.func=func

    def __call__(self, x, y):
        # Add fucntion
        sum=self.func(x,y)
        # Square of summed nums
        return sum**2

@Decorator
def add(x,y):
    return x+y

# add=Decorator(add)
# print(add(5,5))

print(add(5,5))
print("")

class Decorator(object):
    def __init__(self, function):
        self.function=function

    def __call__(self, *args):
        try:
            if any([isinstance(val, str) for val in args]):
                raise TypeError("String not allowed")
            else:
                return self.function(*args)
        except Exception as err:
            return err

@Decorator
def add(*args):
    sum1=0
    for val in args:
        sum1=sum1+val
    return sum1

print(add(5,5))
print(add(1,'2',3))