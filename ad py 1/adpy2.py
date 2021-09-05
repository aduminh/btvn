from typing import Mapping


class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self):
        return str(self.numerator) + "/"+str(self.denominator) 

    def __add__(self,fra2):
        top=self.numerator* fra2.denominator +self.denominator*fra2.numerator
        bot=self.numerator*fra2.denominator
        return Fraction(top,bot)
    def __sub__(self,fra2):
        top=self.numerator*fra2.denominator-self.denominator*fra2.numerator
        bot=self.numerator*fra2.denominator
        return function(top,bot)
fraction_1=Fraction(1,2)
fraction_2=Fraction(2,3)

print(fraction_1+fraction_2)

class Animal:
    def __init__(self,name):
        self.name=name
        def eat(self):
            print("eating")
animal_1=Animal("John")
class Cat(Animal):
    def __init__(self, name, age):
        # code1
        super().__init__(name)
        self.age=age
        # code2
        self.name=name
        self.age=age
        # code3
        def scratch(self):
            print("scratching")
        def eat(self):
            print("meow")
class TabbyCat(Cat):
    pass
cat_1=Cat("Peter",5)

class BankAccount():
    def __init__(self, account_id):
        self.account_id=account_id
    def deposit(self,number):
        self.account_id+=number
    def withdraw(self,number):
        self.account_id-=number
    def get_amount(self):
        return self.account_id
    def clear(self):
        self.account_id=0
class SavingAccount(BankAccount):
    def __init__(self, account_id):
        super().__init__(account_id)
    


