import random

# Definicion de personajes, locaciones y armas
personajes = {
    "Sr. Green": "Empresario",
    "Sra. Peacock": "Politica",
    "Profesor Plum": "Cientifico",
    "Srta. Scarlett": "Actriz",
    "Coronel Mustard": "Militar"
}

locaciones = {
    "Salon": {
        "descripcion": "El salon principal de la mansion es un lugar donde se celebran muchas reuniones sociales. La gente se reune aqui para discutir negocios, politica y chismes.",
        "desarrollo": "Se rumorea que en el salon se llevaron a cabo discusiones acaloradas entre los invitados durante la noche del crimen. Algunos testigos afirman haber escuchado voces elevadas y amenazas."
    },
    "Cocina": {
        "descripcion": "La cocina es el corazon de la mansion, donde se preparan deliciosas comidas para los huespedes. Sin embargo, tambien es un lugar donde se pueden encontrar ingredientes peligrosos.",
        "desarrollo": "En la cocina, se encontraron restos de una cena elegante, pero tambien habia evidencia de un desorden inusual. Algunos utensilios parecian haber sido manipulados recientemente."
    },
    "Biblioteca": {
        "descripcion": "La biblioteca es un lugar tranquilo donde los habitantes de la mansion vienen a estudiar, leer y relajarse. Pero tambien es un lugar donde se guardan secretos oscuros.",
        "desarrollo": "La biblioteca es conocida por sus estantes llenos de libros antiguos y documentos raros. Se dice que algunos de estos documentos podrian contener informacion comprometedora."
    },
    "Sala de estar": {
        "descripcion": "La sala de estar es un espacio acogedor donde los invitados se reunen para conversar, jugar juegos y disfrutar de la compania de los demas. Sin embargo, tambien puede ser el escenario de intrigas y conspiraciones.",
        "desarrollo": "En la sala de estar, se descubrieron pistas que indicaban que algunos de los invitados estaban conspirando en secreto. Se encontraron notas escritas y objetos misteriosos."
    },
    "Comedor": {
        "descripcion": "El comedor es donde se sirven las elegantes cenas en la mansion. Aqui, los invitados pueden disfrutar de exquisitos platos mientras discuten asuntos importantes. Pero tambien puede ser un lugar de confrontacion y rivalidades.",
        "desarrollo": "Durante la cena en el comedor, se produjeron tensiones evidentes entre algunos de los invitados. Algunos testigos informaron sobre intercambios de miradas hostiles y comentarios agresivos."
    }
}

armas = [
    "Candelabro",
    "Cuerda",
    "Llave inglesa",
    "Cuchillo",
    "Revolver"
]

# Historias de los personajes
historias = {
    "Sr. Green": "El Sr. Green ha estado actuando de manera sospechosa ultimamente, y los rumores dicen que tiene un secreto oscuro relacionado con un negocio ilegal.",
    "Sra. Peacock": "La Sra. Peacock es conocida por su ambicion politica despiadada, y se rumorea que esta dispuesta a hacer cualquier cosa para ascender en la jerarquia.",
    "Profesor Plum": "El Profesor Plum es un brillante cientifico con un pasado turbio. Se dice que tiene acceso a sustancias peligrosas que podrian utilizarse como veneno.",
    "Srta. Scarlett": "La Srta. Scarlett es una actriz famosa, pero hay quienes afirman que su exito se debe mas a sus conexiones oscuras que a su talento.",
    "Coronel Mustard": "El Coronel Mustard es un veterano militar con un temperamento explosivo. Se rumorea que tiene enemigos que estarian dispuestos a eliminarlo."
}

def generar_juego():
    # Se elige aleatoriamente el culpable, el arma y la locacion
    culpable = random.choice(list(personajes.keys()))
    arma = random.choice(armas)
    locacion = random.choice(list(locaciones.keys()))

    # Se muestra la historia del culpable
    print("HISTORIA DEL CULPABLE:")
    print(historias[culpable])
    print()

    # Se muestra la locacion y su descripcion
    print("CRIMEN COMETIDO:")
    print("Locacion: ", locacion)
    print("Descripcion de la locacion: ", locaciones[locacion]["descripcion"])
    print()

    # Se muestra el desarrollo adicional de la historia segun la locacion
    print("DESARROLLO DE LA HISTORIA:")
    print(locaciones[locacion]["desarrollo"])
    print()

    # Se muestra el arma usada
    print("Arma: ", arma)
    print()

# Funcion principal del programa
def main():
    while True:
        print("BIENVENIDO AL SIMULADOR DE CLUE")
        print("1. Generar nuevo juego")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            generar_juego()
        elif opcion == "2":
            print("Gracias por jugar. Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
