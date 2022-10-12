'''
small musicians application with Object Oriented Programming.

* Band (base class): instances, to_list(), play_solos() ,__str__(), __repr__(),get_instrument()

* Musician class (parent class)
musicians types: 
- Guitarist (child from Musician):  name, instrument ,__str__(), __repr__(),get_instrument(),play_solo()
- Drummer  (child from Musician): name, instrument __str__(), __repr__(),get_instrument(),play_solo() 
- Bassist  (child from Musician): name, instrument,__str__(), __repr__(),get_instrument(),play_solo()
'''

from abc import ABC,abstractmethod
# parent class or base class(superclass)
class Musician(ABC):
    '''this is musicians account app
    1 instance attribute  --- name :str
    3 methodes --- (__init__  ,
    get_instrument,play_solo   as abstractmethod 
    )
    '''
    def __init__(self,name):
        self.name = name

    #Getter
    @abstractmethod
    def get_instrument(self):
        pass 

    @abstractmethod
    def play_solo(self):
        pass 

    
      
# child class (subclass)
class Guitarist(Musician):
    '''child class from parent class(Musician)
     instance attribute ---- name=> str  
       methods:
        1. __init__ 
        2. __str__
        3. __repr__
        4. get_instrument
        5. play_solo
   
    '''
    instrument = "guitar"  # the instrument for all the guitarist is guitar

    def __init__(self,name):
        super().__init__(name)
    def __repr__(self) -> str:
        return f"Guitarist instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    def get_instrument(self):
        return f"{self.instrument}"
    def play_solo(self):
        return f"face melting {self.instrument} solo" 

    

class Drummer(Musician):
    '''child class from parent class(Musician)
     instance attribute ---- name=> str  
       methods:
        1. __init__ 
        2. __str__
        3. __repr__
        4. get_instrument
        5. play_solo
    '''
    instrument = "drums"  # the instrument for all the Drummer is drums

    def __init__(self,name):
        super().__init__(name)

    def __repr__(self) -> str:
        return f"Drummer instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    def get_instrument(self):
        return f"{self.instrument}"
    def play_solo(self):
        return "rattle boom crash" 


class Bassist(Musician):
    '''child class from parent class(Musician)
     instance attribute ---- name=> str  
       methods:
        1. __init__ 
        2. __str__
        3. __repr__
        4. get_instrument
        5. play_solo
    '''
    instrument = "bass"  # the instrument for all the Bassist is bass

    def __init__(self,name):
        super().__init__(name)
    def __repr__(self) -> str:
        return f"Bassist instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    def get_instrument(self):
        return f"{self.instrument}"
    def play_solo(self):
        return "bom bom buh bom"  

#new class name Band
class Band:
    '''
    * Band (base class): instances, to_list(), play_solos() ,__str__(), __repr__(),get_instrument()

    '''
    instances=[]
    def __init__(self,name,members =[]):
        self.name = name
        self.members=members
        Band.instances.append(self)
    def get_instrument(self):
        return "h"
    def play_solos(self):
        x=[]
        for member in self.members:
            x.append(member.play_solo())
        return(x)
    @classmethod
    def to_list(cls):
        return Band.instances

    def __repr__(self) -> str:
        return self.name
    def __str__(self):
        return self.name
    





if __name__=="__main__":
    music=Drummer("walaa")
    print(music)
    print(repr(music))