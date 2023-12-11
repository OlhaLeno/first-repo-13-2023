class Fish:
    def __init__(self, name, age, species, size, preffered_food, is_aggressive, needed_space):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preffered_food = preffered_food
        self.is_aggressive = is_aggressive
        self.needed_space = needed_space


class Aquarium:
    def __init__(self, total_volume):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.fish_list = []

    def add_fish(self, fish):
        if fish.is_aggressive and self.free_space >= fish.needed_space:
            self.fish_list.append(fish)
            self.free_space -= fish.needed_space
            print(f"Рибка {fish.name} додана до акваріуму.")
        elif not fish.is_aggressive:
            self.fish_list.append(fish)
            self.free_space -= fish.needed_space
            print(f"Рибка {fish.name} додана до акваріуму.")
        else:
            print(f"Не можна додати рибку {fish.name} через агресивність або нестачу місця.")

    def get_3_largest_fishes(self):
        sorted_fish = sorted(self.fish_list, key=lambda x: x.size, reverse=True)
        get_3_largest_fishes = sorted_fish[:3]
        for fish in get_3_largest_fishes:
            print(f"Ім'я: {fish.name}, Вид: {fish.species}, Розмір: {fish.size}")


if __name__ == "__main__":
    aquarium1 = Aquarium(total_volume=35)
    aquarium2 = Aquarium(total_volume=20)

    fish1 = Fish("Дорі", 2, "Блакитний хірург", 5, "Водорості", False, 3)
    fish2 = Fish("Норі", 4, "Акула", 12, "Дрібна риба", True, 10)
    fish3 = Fish("Немо", 1, "Клоун", 3, "Планктон", False, 1)
    fish4 = Fish("Локі", 3, "Піранья", 7, "М'ясо", True, 6)
    fish5 = Fish("Сенді", 2, "Золота рибка", 2, "Корм", False, 4)
    fish6 = Fish("Корді", 5, "Блакитний тан", 7, "Водорості", False, 5)
    fish7 = Fish("Ідол", 3, "Мавританський ідол", 10, "Дрібна риба", True, 9)
    
    aquarium1.add_fish(fish2)
    aquarium1.add_fish(fish4)
    aquarium1.add_fish(fish7)
    aquarium2.add_fish(fish1)
    aquarium2.add_fish(fish3)
    aquarium2.add_fish(fish5)
    aquarium2.add_fish(fish6)

    aquarium1.get_3_largest_fishes()
    aquarium2.get_3_largest_fishes()
