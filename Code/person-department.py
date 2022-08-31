# File person-department.py
# Aggregate embedded objects into a composite
class Person:
    def __init__(this,name,job=None,pay=0):
        this.name=name
        this.job=job
        this.pay=pay
    def lastName(this):
        return this.name.split()[-1]
    def giveRaise(this,percent):
        this.pay=int(this.pay*(1+percent))
    def __repr__(this):
        return "[Person:%s, %s]"%(this.name,this.pay)
class Manager(Person):
    def __init__(this,name,pay):
        Person.__init__(this,name,'mgr',pay)
    def giveRaise(this,percent,bonus=0.1):
        Person.giveRaise(this,percent+bonus)
class Department:
    def __init__(this,*args):
        this.members=list(args)
    def addMember(this,person):
        this.members.append(person)
    def giveRaises(this,percent):
        for person in this.members:
            person.giveRaise(percent)
    def showAll(this):
        for person in this.members:
            print(person)
if __name__=="__main__":
    bob=Person("Bob Smith")
    sue=Person("Sue Jones",job='dev',pay=100000)
    tom=Manager("Tom Jones",50000)
    development=Department(bob,sue)
    development.addMember(tom)
    development.giveRaises(0.1)
    development.showAll()