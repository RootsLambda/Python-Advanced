# File factory.py
def factory(aClass, *pargs, **kargs): # Varargs tuple, dict
    return aClass(*pargs, **kargs) # Call aClass
class Spam:
    def doit(self, message):
        print(message)
class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job