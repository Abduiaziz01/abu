import random

class GameEntity:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return f"{self.name} health: {self.health} damage: {self.damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.defence = None

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return "BOSS " + super().__str__() + f" super_power: {self.defence}"
    
class Heroes(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.super_ability = super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_power(self, boss, heroes):
        coef = random.randint(1, 5)
        boss.health -= self.damage * coef
        print(f"CRITICAL_DAMAGE {self.damage * coef}")

class Berserk(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "PART_DAMAGE")
    
    def apply_super_power(self, boss, heroes):
        part_damage_point = boss.health - boss.damage
        print(f"PART_DAMAGE POINT {part_damage_point}")

class Magic(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 15)
        print(f"BOOST POINT {boost_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.damage += boost_point

class Defender(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SHIELD")

    def apply_super_power(self, boss, heroes):
        shield_point = 20
        print(f"SHIELD POINT {shield_point}")
        for hero in heroes:
            if hero.health > 0:
                hero.health += shield_point

class Health_burner(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BURNING")

    def apply_super_power(self, boss, heroes):
        burning_point = random.randint(5,20)
        boss.health -= burning_point
        print(f"BURNING POINT {burning_point}")
        

class Medic(Heroes):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HEAL")

    def apply_super_power(self, boss, heroes):
        heal_point = random.randint(5, 11)
        print(f"HEAL POINT {heal_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.health += heal_point


round_counter = 0


def print_statistic(boss, heroes):
    print(f'_____________ ROUND {round_counter} _____________')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_power(boss, heroes)

    print_statistic(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!")

    return all_heroes_dead


def start_game():
    boss = Boss("SIMON", 750, 45)

    warrior = Warrior("Abu", 100, 10)
    medic = Medic("Rayona", 100, 0)
    magic = Magic("Mona", 70, 2)
    defender = Defender("Artur", 50, 0)
    health_burner = Health_burner("Artac", 90, 5)
    berserk = Berserk("Каэль", 100, 5)

    heroes = [warrior, medic, magic, defender, health_burner, berserk]

    print_statistic(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)

start_game()