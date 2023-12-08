class Fish:
    def __init__(self, name, age, species, size, prefferedFood, isAggressive, neededSpace):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.prefferedFood = prefferedFood
        self.isAggressive = isAggressive
        self.neededSpace = neededSpace


class Aquarium:
    def __init__(self, totalVolume):
        self.totalVolume = totalVolume
        self.freeSpace = totalVolume
        self.fish_list = []

    def add_fish(self, fish):
        if fish.isAggressive and self.freeSpace >= fish.neededSpace:
            self.fish_list.append(fish)
            self.freeSpace -= fish.neededSpace
            print(f"Рибка {fish.name} додана до акваріуму.")
        elif not fish.isAggressive:
            self.fish_list.append(fish)
            self.freeSpace -= fish.neededSpace
            print(f"Рибка {fish.name} додана до акваріуму.")
        else:
            print(f"Не можна додати рибку {fish.name} через агресивність або нестачу місця.")

    def get_3_largest_fishes(self):
        # сортує список за розміром, key=lambda вказує на сортування за розміром кожної риби
        sorted_fish = sorted(self.fish_list, key=lambda x: x.size, reverse=True)  # reverse=True сортування в зворотньому порядку
        get_3_largest_fishes = sorted_fish[:3]
        for fish in get_3_largest_fishes:  # for використовується для ітерації-процес повторення певної послідовності елементів
            print(f"Ім'я: {fish.name}, Вид: {fish.species}, Розмір: {fish.size}")


if __name__ == "__main__":  # за умови, що програма запускається безпосередньо, а не імпортується як модуль
    aquarium1 = Aquarium(totalVolume=10)
    aquarium2 = Aquarium(totalVolume=15)

    fish1 = Fish("Дорі", 2, "Блакитний хірург", 5, "Водорості", False, 3)
    fish2 = Fish("Норі", 4, "Акула", 12, "Дрібна риба", True, 9)
    fish3 = Fish("Немо", 1, "Клоун", 3, "Планктон", False, 1)
    fish4 = Fish("Локі", 3, "Піранья", 7, "М'ясо", True, 6)

    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish4)
    aquarium2.add_fish(fish3)
    aquarium2.add_fish(fish2)

    aquarium1.get_3_largest_fishes()
    aquarium2.get_3_largest_fishes()
