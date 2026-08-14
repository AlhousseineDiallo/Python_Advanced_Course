class Person:
    MIN_AGE: int = 0
    MAX_AGE: int = 120

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Personne: name={self.name} et age={self.age}"

    def __repr__(self) -> str:
        return f"Person({self.name!r}, {self.age!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented

        return self.name == other.name and self.age == other.age

    def sepresenter(self) -> str:
        return f"Bonjour je m'appelle: {self.name} et j'ai: {self.age}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(
                f"name doit etre une chaine de caracteres, recu: {type(name).__name__}"
            )
        self.__name = name

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"value doit etre un entier, recu: {type(value)}")

        if not (self.MIN_AGE < value < self.MAX_AGE):
            raise ValueError(
                f"Veuillez renseigner un age raisonnable, entre: {self.MIN_AGE} et {self.MAX_AGE}"
            )
        self.__age = value


p1: Person = Person(name="Jean", age=22)
p2: Person = Person(name="Albert", age=32)
p3: Person = Person(name="Jean", age=22)

p1.name: str = 282983
# print(p1.name)
print(p1.sepresenter())
print(repr(p1))
print(p1 == p2)
print(p1 == p3)
print(p1.__dict__)
# print(p1.__dir__())
print(p1)
