from classtools import AttrDisplay
class Person(AttrDisplay):
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

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)