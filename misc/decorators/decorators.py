def outer(msg):
    greet=msg

    def inner():
        print(greet)
    return inner

hello=outer('Hello')
bye=outer('Bye')
hello()
bye()
print("")

def greet(func_run):
    def my_func():
        print("Good Afternoon!!")
        func_run()
        print("This line is also run")
    return my_func

@greet
def helloWorld():
    print("Hello World!")

helloWorld()
print("")

def decoratorFunction(originalFunction):
    def wrapperFunction():
        print(originalFunction)
    return wrapperFunction

@decoratorFunction
def show():
    print("Show function called")

display=decoratorFunction(show)
display()
print("")

def decorateResult(results):
    def distinctionCheck(marks):
        for val in marks:
            if val>=80:
                print("Distinction")
        results(marks)
    return distinctionCheck

@decorateResult
def result(marks):
    for mark in marks:
        if mark>=40:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")

result([50,60,80])
