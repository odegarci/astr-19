class Cat:
    def __init__(self, name, arm_length=5.1, leg_length=5.6, num_of_eyes=2, has_tail=True, is_furry=True):
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_of_eyes = num_of_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
        
    def check_tail(self):
        if self.has_tail:
            return f"{self.name} has a tail"
        else:
            return f"{self.name} doesn't have a tail"
    
    def check_furry(self):
        if self.is_furry:
            return f"{self.name} is furry"
        else:
            return f"{self.name} is not furry"

if __name__ == "__main__":
    my_cat = Cat("Monito")
    
    print("My cat, Monito, has an:")
    print(f"- arm length: {my_cat.arm_length}")
    print(f"- leg length: {my_cat.leg_length}")
    print(f"- number of eyes: {my_cat.num_of_eyes}")
    
    print(my_cat.check_tail())
    print(my_cat.check_furry())
    
    #I love my cat Monito so much. He is the stupidest but cutest orange cat ever