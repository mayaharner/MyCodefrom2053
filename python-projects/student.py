class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        # declare instance variables
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return f"{self.lname}:{self.id}"
    
    # CLASS METHODS!
    def greeting(self):
        print(f"{self.fname} {self.lname} says Hello!")
    def take_exam(self):
        if self.energy_level > 0:
            self.energy_level = self.energy_level - 1 # subtract 1 from student's energy level
        return self.energy_level 
    def get_energy_level(self):
        return self.energy_level # return current energy level