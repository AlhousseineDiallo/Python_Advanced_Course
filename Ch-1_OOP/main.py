def afficher_information_personne(nom: str, age: int) -> None:
    print(f"La personne s'appelle {nom} et son age est: {age} ans.")


def demander_nom_personne() -> str:
    nom = input("Quel est votre nom: ").strip()
    return nom


def demander_age_personne() -> int:
    while True:
        saisie_age: str = input("Quel est votre age: ")
        try:
            age: int = int(saisie_age)
            if not 0 <= age <= 120:
                print("Veuillez entrer un age compris entre 0 et 120.")
                continue
            return age

        except ValueError:
            print("Veuillez entrer un age valide !")


def main():
    nom: str = demander_nom_personne()
    age: int = demander_age_personne()

    afficher_information_personne(nom=nom, age=age)


if __name__ == "__main__":
    main()
