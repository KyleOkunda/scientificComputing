# Part 1: Design Your Own Class (Superhero)
# This example uses inheritance and encapsulation.

class Character:

    def __init__(self, name):
        self.name = name
    
    def move(self):
        
        print(f"{self.name} is moving.")

class Superhero(Character):

    # Class-level attribute, shared by all Superhero objects
    _heroes_created = 0

    def __init__(self, name, secret_identity, power, catchphrase):
        # 3. Use a constructor to initialize unique values.
        super().__init__(name) # Call the constructor of the parent class
        
        # 2. Add attributes to bring the class to life.
        # Encapsulation: using a "private" attribute with a leading underscore.
        self._secret_identity = secret_identity
        self.power = power
        self.catchphrase = catchphrase
        
        Superhero._heroes_created += 1

    # 2. Add methods to bring the class to life.
    def speak(self):
        
        print(f"[{self.name}]: '{self.catchphrase}'")

    def use_power(self):
        
        print(f"{self.name} uses their power of {self.power}!")

    def get_secret_identity(self):
        
        return self._secret_identity

    # Override the move() method from the parent class (Polymorphism)
    def move(self):
        
        print(f"{self.name} is flying through the sky!")

# 4. Add an inheritance layer to explore polymorphism.
class Sidekick(Character):

    def __init__(self, name, partner_name):
        super().__init__(name)
        self.partner_name = partner_name

    # Override the move() method from the parent class (Polymorphism)
    def move(self):
        
        print(f"{self.name} is running quickly to help {self.partner_name}!")


# Part 2: Polymorphism Challenge
# Use the classes to demonstrate the polymorphic `move()` method.

def demonstrate_movement(characters):
   
    print("\n--- Demonstrating Movement (Polymorphism) ---")
    for character in characters:
        character.move()

if __name__ == "__main__":
    # Create objects (instances) of our classes
    superman = Superhero(
        name="Superman", 
        secret_identity="Clark Kent",
        power="Flight and Super Strength",
        catchphrase="Up, up, and away!"
    )
    
    batman_sidekick = Sidekick(
        name="Robin",
        partner_name="Batman"
    )
    
    
    print("--- Superhero in Action ---")
    superman.speak()
    superman.use_power()
    print(f"The secret identity of {superman.name} is {superman.get_secret_identity()}.")
    print(f"Total heroes created: {Superhero._heroes_created}\n")

    # Put the objects in a list to demonstrate polymorphism
    all_characters = [superman, batman_sidekick]
    
    # Call the function that demonstrates polymorphism
    demonstrate_movement(all_characters)
