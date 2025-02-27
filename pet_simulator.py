from abc import ABC, abstractmethod
import random
import time

class Pet:
    @abstractmethod
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value > 100:
            print(f"{self.name} starved to deth")
            quit()
        elif value < 0:
            print(f"{self.name} got diabetes and died due to blood clots")
            quit()
        self.__hunger = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value > 100:
            print(
                f"Delusional {self.name} unknowingly attacked neighbor, so it was put down.")
            quit()
        elif value < 0:
            print(f"{self.name} commited suicide.")
            quit()
        self.__happiness = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value > 100:
            print(f"{self.name} had a heart attack and died")
            quit()
        elif value < 0:
            print(f"{self.name}'s organs shut down")
            quit()
        self.__energy = value

    def feed(self):
        self.hunger -= 20
        self.energy += 10

    def play(self):
        self.happiness += 15
        self.energy -= 10

    def sleep(self):
        self.energy += 20
        self.hunger += 10

    def show_status(self):
        return f"Hunger:{self.hunger}, Happiness:{self.happiness}, Energy:{self.energy}"

    def random_event(self):
        event = random.randint(1, 3)
        if event == 1:
            choice = random.randint(1, 4)
            if choice == 1:
                print("Pet finds a snack, Hunger -10")
                self.hunger -= 10
            elif choice == 2:
                print("Pet plays alone,happiness +10")
                self.happiness += 10
            elif choice == 3:
                print("Pet has a bad dream,energy -10")
                self.energy -=10
            elif choice == 4:
                print("Pet finds a toy,happiness +15 ")
                self.happiness +=15 

    def special_ability(self):
        pass


class Dog(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(name, hunger, happiness, energy)

    def play(self):
        self.happiness += 20
        self.energy -= 10

    def special_ability(self):
        """Loyal Companion"""
        if self.happiness >= 80:
            print(
                f"{self.name} Uses Loyal Companion.\nIt's very effective. Gain 10 hunger.")
            self.hunger += 10
        else:
            print(
                f"{self.name} Uses Independent Napper.\nIt missed, Happiness Stat Not High Enough")


class Cat(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(name, hunger, happiness, energy)

    def sleep(self):
        self.energy += 30
        self.hunger += 5

    def special_ability(self):
        """Independent Napper"""
        if self.energy <= 20:
            print(
                f"{self.name} Uses Independent Napper.\nIt's very effective. Gain 15 energy.")
            self.energy += 15
        else:
            print(
                f"{self.name} Uses Independent Napper.\nIt missed, Energy Stat Not Low Enough")


class Dragon(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(name, hunger, happiness, energy)

    def play(self):
        self.happiness += 25
        self.energy -= 5
        self.hunger += 10

    def feed(self):
        self.hunger -= 30
        self.energy += 15
        self.happiness += 10

    def special_ability(self):
        """Fiery Roar"""
        if self.happiness >= 70:
            print(
                f"{self.name} Uses Fiery Roar.\nIt's very effective. Lose 5 Hunger, Gain 5 energy.")
            self.hunger -= 5
            self.energy += 5
        else:
            print(
                f"{self.name} Uses Fiery Roar.\nIt missed, Happiness Stat Not High Enough")






if __name__ == "__main__":
    
    name = str(input("What is the name of your pet?: "))
    
    c = Cat(name)
    dr = Dragon(name)
    select = int(input("What pet do you want? \n 1.Dog 🐶 \n 2.Cat 🐱 \n 3.Dragon 🐉 \n:"))
    if select == 1:
        d = Dog(name)
        while True:
            d.show_status()
            choice = int(input("Do you want to: \n 1.Feed\n 2.Play\n 3.Sleep\n 4.Use Special Ability\n 5.Exit "))
            if choice == 1:
                d.feed()
                print(d.show_status())
                d.random_event()
                print(d.show_status())
                time.sleep(1)
            elif choice == 2:
                d.play()
                print(d.show_status())
                d.random_event()
                print(d.show_status())
                time.sleep(1)
            elif choice == 3:
                d.sleep()
                print(d.show_status())
                d.random_event()
                print(d.show_status())
                time.sleep(1)
            elif choice == 4:
                d.special_ability()
                print(d.show_status())
                d.random_event()
                print(d.show_status())
                time.sleep(1)
            elif choice == 5:
                d.random_event()
                print(d.show_status())
                time.sleep(1)
                quit()
    