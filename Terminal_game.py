import random
import time

# Clase base para personajes/Base class for Characters
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.blocking = False

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        damage = random.randint(10, 20)
        if target.blocking:
            damage //= 2
        target.hp -= damage
        print(f"{self.name} attacks {target.name} causing {damage} damage.")

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        print(f"{self.name} heals {heal_amount} health points.")

    def block(self):
        self.blocking = True
        print(f"{self.name} prepares to block the next attack.")

# Enemigos normales/Normal Enemies
class Goblin(Character):
    def __init__(self):
        super().__init__("Goblin 🧟", 100)

class Orc(Character):
    def __init__(self):
        super().__init__("Orc 🧌", 120)

    def attack(self, target):
        damage = random.randint(15, 25)
        if target.blocking:
            damage //= 2
        target.hp -= damage
        print(f"{self.name} brutally hits {target.name} causing {damage} damage.")

class Skeleton(Character):
    def __init__(self):
        super().__init__("Skeleton 🩻", 80)

    def heal(self):
        print(f"{self.name} can't heal...")

# Jefes finales/Final boss
class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon 🐉", 200)

    def attack(self, target):
        damage = random.randint(25, 40)
        if target.blocking:
            damage //= 2
        target.hp -= damage
        print(f"{self.name} throws a flare at{target.name} causing {damage} damage.")

class DarkKnight(Character):
    def __init__(self):
        super().__init__("Dark Knight 🤺", 180)

    def heal(self):
        heal_amount = random.randint(30, 50)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        print(f"{self.name} absorbs  dark energy and heals {heal_amount} points of health.")

# Acción del enemigo/Enemies actions
def npc_action(npc, player):
    action = random.choice(["attack", "block", "heal"])
    if action == "attack":
        npc.attack(player)
    elif action == "block":
        npc.block()
    elif action == "heal":
        npc.heal()

# Mostrar estado/Show status
def print_status(player, npc):
    print(f"\n{player.name}: {player.hp} HP | {npc.name}: {npc.hp} HP\n")

# Juego principal/Main Game
def main():
    player = Character("Hero", 100)

    # Lista de enemigos normales y jefes/List of enemies and boss
    normal_enemies = [Goblin, Orc, Skeleton]
    boss_enemies = [Dragon, DarkKnight]

    # Probabilidad de jefe: 30%/Probability being a boss : 30%
    if random.random() < 0.3:
        npc = random.choice(boss_enemies)()
        print(f"A boss appears!Get ready to face the {npc.name}!\n")
    else:
        npc = random.choice(normal_enemies)()
        print(f"¡A {npc.name} appears!\n")

    while player.is_alive() and npc.is_alive():
        print_status(player, npc)
        player.blocking = False

        print("Choose one action:")
        print("1. Attack")
        print("2. Block")
        print("3. Heal")

        choice = input("> ")

        if choice == "1":
            player.attack(npc)
        elif choice == "2":
            player.block()
        elif choice == "3":
            player.heal()
        else:
            print("Invalid option. You lose your turn.")

        time.sleep(1)

        if npc.is_alive():
            npc.blocking = False
            npc_action(npc, player)
            time.sleep(1)

    print_status(player, npc)

    if player.is_alive():
        print("¡You Win⚔️!")
    else:
        print("You've been defeated...💀")

if __name__ == "__main__":
    main()
