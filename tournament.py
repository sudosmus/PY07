from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

tour_0 =[
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
]

tour_1 = [
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
]

tour_2 =[
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy())
]
def battle(opponents: list[tuple]) -> None:
    print("*** Tournament ***")
    opponents_list = []
    for factory, strategy in opponents:
        opponents_list.append(f"{factory.create_base().name}+{type(strategy).__name__[:-8]}")
    print(f"[ {', '.join(opponents_list)} ]")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print()
            print("* Battle *")
            print(f"{creature_a.describe()}")
            print(" vs.")
            print(f"{creature_b.describe()}")
            print(" now fight!")
            try:
                print(f"{strategy_a.act(creature_a)}")
                print(f"{strategy_b.act(creature_b)}")
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
        

def main() -> None:
    print("Tournament 0 (basic)")
    battle(tour_0)

    print("Tournament 1 (error)")
    battle(tour_1)

    print("Tournament 2 (multiple)")
    battle(tour_2)

    return

    
if __name__ == "__main__":
    main()


       
        

