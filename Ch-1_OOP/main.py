def afficher_information_personne(nom: str, age: int) -> None:
    print(f"La personne s'appelle {nom} et son age est: {age} ans")


def demander_nom_personne() -> str:
   name = input("Quel est votre nom: ")
   return name


def demander_age_personne() -> int:
    age: str = input("Quel est votre age: ")
    try:
        age: int = int(age)
        return age

    except ValueError:
        print("Conversion failed, please check the value !")


if __name__ == "__main__":
    nom1 = demander_nom_personne()
    age1 = demander_age_personne()

    afficher_information_personne(nom=nom1, age=age1)
