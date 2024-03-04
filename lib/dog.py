#!/usr/bin/env python3
#1. Dog.__init__ with Name and Breed defaulting to "Mutt"
#Define a Dog class in lib/dog.py. In the class, define an __init__ method that accepts an argument for the dog's name. That argument should be stored within a self.name attribute.

#Additionally, Dog.__init__ should accept a second optional argument for the dog's breed stored in an attribute self.breed. When no breed is provided, it should default to "Mutt".


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

    def is_mutt(self):
        return self.breed == "Mutt"

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed
