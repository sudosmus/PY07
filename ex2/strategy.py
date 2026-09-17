from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capability import HealCapability, TransformCapability

class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
    
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True
    
    def act(self, creature) -> str:
        return creature.attack()

class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False
    def act(self, creature) -> str:
        if self.is_valid(creature):
            return (f"{creature.transform()}\n{creature.attack()}\n{creature.revert()}")
        else:
            raise InvalidStrategyError(f"Invalid Creature {creature.name} for this aggressive strategy")
  
class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False
    
    def act(self, creature) -> str:
        if self.is_valid(creature):
            return (f"{creature.attack()}\n{creature.heal()}")
        else:
            raise InvalidStrategyError(f"Invalid Creature {creature.name} for this defensive strategy")