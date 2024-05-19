class Animal:
    def __init__(self, name, voice, food):
        self.name = name
        self.voice = voice
        self.food = food

    def make_sound(self):
        return f"{self.name} - {self.voice}"

    def eat(self):
        print(f"{self.name} потребляет в пищу - {self.food}")

    def __str__(self):
        return f"Животное: {self.name}, Звук: {self.voice}, Пища: {self.food}"


class Bird(Animal):
    def __init__(self, name, voice, food, plumage_color):
        super().__init__(name, voice, food)
        self.plumage_color = plumage_color

    def __str__(self):
        return f"Птица: {self.name}, Звук: {self.voice}, Пища: {self.food}, Цвет оперения: {self.plumage_color}"


class Mammal(Animal):
    def __init__(self, name, voice, food, hair_color):
        super().__init__(name, voice, food)
        self.hair_color = hair_color

    def __str__(self):
        return f"Млекопитающее: {self.name}, Звук: {self.voice}, Пища: {self.food}, Цвет шерсти: {self.hair_color}"


class Reptile(Animal):
    def __init__(self, name, voice, food, skin_color):
        super().__init__(name, voice, food)
        self.skin_color = skin_color

    def __str__(self):
        return f"Рептилия: {self.name}, Звук: {self.voice}, Пища: {self.food}, Цвет кожи: {self.skin_color}"


class Worker:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Сотрудник: {self.name}, Возраст: {self.age}, Пол: {self.gender}"


class ZooKeeper(Worker):
    def feed_animal(self):
        print(f"{self.name} кормит животное")

    def __str__(self):
        return f"Смотритель зоопарка: {self.name}, Возраст: {self.age}, Пол: {self.gender}"


class Veterinarian(Worker):
    def heal_animal(self):
        print(f"{self.name} лечит животное")

    def __str__(self):
        return f"Ветеринар: {self.name}, Возраст: {self.age}, Пол: {self.gender}"


class Zoo:
    def __init__(self):
        self.animals = []
        self.workers = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.remove(worker)

    def read_zoo(self):
        with open("zoo.txt", "r") as f:
            for line in f:
                line = line.strip().split()
                if line[0] == "animal":
                    if line[1] == "Bird":
                        animal = Bird(line[2], line[3], line[4], line[5])
                    elif line[1] == "Mammal":
                        animal = Mammal(line[2], line[3], line[4], line[5])
                    elif line[1] == "Reptile":
                        animal = Reptile(line[2], line[3], line[4], line[5])
                    self.add_animal(animal)
                elif line[0] == "worker":
                    if line[1] == "ZooKeeper":
                        worker = ZooKeeper(line[2], int(line[3]), line[4])
                    elif line[1] == "Veterinarian":
                        worker = Veterinarian(line[2], int(line[3]), line[4])
                    self.add_worker(worker)

    def write_zoo(self):
        with open("zoo.txt", "w") as f:
            for animal in self.animals:
                if isinstance(animal, Bird):
                    f.write(f"animal Bird {animal.name} {animal.voice} {animal.food} {animal.plumage_color}\n")
                elif isinstance(animal, Mammal):
                    f.write(f"animal Mammal {animal.name} {animal.voice} {animal.food} {animal.hair_color}\n")
                elif isinstance(animal, Reptile):
                    f.write(f"animal Reptile {animal.name} {animal.voice} {animal.food} {animal.skin_color}\n")
            for worker in self.workers:
                if isinstance(worker, ZooKeeper):
                    f.write(f"worker ZooKeeper {worker.name} {worker.age} {worker.gender}\n")
                elif isinstance(worker, Veterinarian):
                    f.write(f"worker Veterinarian {worker.name} {worker.age} {worker.gender}\n")


def animals_sound(animals):
    for animal in animals:
        print(animal.make_sound())


zoo = Zoo()
# Добавляем примеры животных и сотрудников для тестирования
owl = Bird("Сова", "Ухает", "Мыши", "Пестро-серый")
hawk = Bird("Ястреб", "Клекочет", "Утки", "Пестро-коричневый")
parrot = Bird("Попугай", "Разговаривает", "Фрукты", "Разноцветный")
tiger = Mammal("Тигр", "Рычит", "Мясо", "Оранжево-полосатый")
bear = Mammal("Медведь", "Ревёт", "Мясо", "Бурый")
elephant = Mammal("Слон", "Трубит", "Овощи", "Серый")
crocodile = Reptile("Крокодил", "Лает", "Мясо", "Зеленый")
varan = Reptile("Варан", "Сипит", "Рыба", "Серо-зеленый")
python = Reptile("Питон", "Шипит", "Лягушками", "Пятнистый")
zoo_keeper_1 = ZooKeeper("Николай", 43, "Мужской")
zoo_keeper_2 = ZooKeeper("Ольга", 45, "Женский")
veterinarian_1 = Veterinarian("Александр", 35, "Мужской")
veterinarian_2 = Veterinarian("Елена", 30, "Женский")

zoo.add_animal(owl)
zoo.add_animal(hawk)
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(bear)
zoo.add_animal(elephant)
zoo.add_animal(crocodile)
zoo.add_animal(varan)
zoo.add_animal(python)
zoo.add_worker(zoo_keeper_1)
zoo.add_worker(zoo_keeper_2)
zoo.add_worker(veterinarian_1)
zoo.add_worker(veterinarian_2)

# Записываем в файл
zoo.write_zoo()

# Очищаем текущий зоопарк
zoo.animals = []
zoo.workers = []

# Читаем из файла
zoo.read_zoo()

# Выводим прочитанные данные
print("Животные в зоопарке:")
for animal in zoo.animals:
    print(animal)

print("\nСотрудники зоопарка:")
for worker in zoo.workers:
    print(worker)

print("\nГолоса питомцев зоопарка:")
animals_sound(zoo.animals)
