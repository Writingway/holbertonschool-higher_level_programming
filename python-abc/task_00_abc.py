#!/usr/bin/python3
"""
This module defines an abstract class 'Animal' with an abstract method 'sound'.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to return
        the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Represents a dog, inherits from Animal
    """
    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a cat, inherits from Animal
    """
    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
