from ex0 import CreatureFactory
from abc import ABC, abstractmethod
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0.creatures import Creature

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()
    
    def create_evolved(self) -> Creature:
        return Morphagon()
    
