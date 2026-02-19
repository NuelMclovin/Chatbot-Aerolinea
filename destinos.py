import datetime

destinos = {
    "1": {
        "destino": "Monterrey",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=6, minute=30),
            datetime.time(hour=9, minute=30),
            datetime.time(hour=14, minute=15),
            datetime.time(hour=18, minute=45)
        ],
        "duracion_vuelo": "1h 30min",
        "precio_base": 1500
    },
    "2": {
        "destino": "California - Los Angeles",
        "pais": "USA",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=5, minute=40),
            datetime.time(hour=11, minute=20),
            datetime.time(hour=17, minute=30)
        ],
        "duracion_vuelo": "4h 15min",
        "precio_base": 8500
    },
    "3": {
        "destino": "Cancún",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=7, minute=0),
            datetime.time(hour=10, minute=30),
            datetime.time(hour=15, minute=45),
            datetime.time(hour=19, minute=20)
        ],
        "duracion_vuelo": "2h 45min",
        "precio_base": 3200
    },
    "4": {
        "destino": "Guadalajara",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=6, minute=0),
            datetime.time(hour=8, minute=30),
            datetime.time(hour=11, minute=45),
            datetime.time(hour=16, minute=10),
            datetime.time(hour=20, minute=30)
        ],
        "duracion_vuelo": "1h 15min",
        "precio_base": 1800
    },
    "5": {
        "destino": "Miami",
        "pais": "USA",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=6, minute=15),
            datetime.time(hour=13, minute=40),
            datetime.time(hour=18, minute=0)
        ],
        "duracion_vuelo": "3h 30min",
        "precio_base": 7800
    },
    "6": {
        "destino": "Nueva York",
        "pais": "USA",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=7, minute=30),
            datetime.time(hour=14, minute=20),
            datetime.time(hour=21, minute=10)
        ],
        "duracion_vuelo": "5h 0min",
        "precio_base": 9500
    },
    "7": {
        "destino": "Madrid",
        "pais": "España",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=10, minute=45),
            datetime.time(hour=22, minute=30)
        ],
        "duracion_vuelo": "10h 30min",
        "precio_base": 15000
    },
    "8": {
        "destino": "Tijuana",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=5, minute=50),
            datetime.time(hour=9, minute=15),
            datetime.time(hour=13, minute=30),
            datetime.time(hour=17, minute=45)
        ],
        "duracion_vuelo": "3h 45min",
        "precio_base": 2800
    },
    "9": {
        "destino": "Bogotá",
        "pais": "Colombia",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=8, minute=0),
            datetime.time(hour=16, minute=30)
        ],
        "duracion_vuelo": "4h 50min",
        "precio_base": 8200
    },
    "10": {
        "destino": "Buenos Aires",
        "pais": "Argentina",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=9, minute=30),
            datetime.time(hour=20, minute=0)
        ],
        "duracion_vuelo": "11h 20min",
        "precio_base": 16500
    },
    "11": {
        "destino": "Mérida",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=7, minute=20),
            datetime.time(hour=12, minute=0),
            datetime.time(hour=16, minute=40)
        ],
        "duracion_vuelo": "2h 10min",
        "precio_base": 2500
    },
    "12": {
        "destino": "Toronto",
        "pais": "Canadá",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=8, minute=30),
            datetime.time(hour=15, minute=45)
        ],
        "duracion_vuelo": "4h 40min",
        "precio_base": 9000
    },
    "13": {
        "destino": "París",
        "pais": "Francia",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=11, minute=15),
            datetime.time(hour=23, minute=0)
        ],
        "duracion_vuelo": "11h 0min",
        "precio_base": 17000
    },
    "14": {
        "destino": "Puerto Vallarta",
        "pais": "México",
        "tipo": "Nacional",
        "horarios": [
            datetime.time(hour=6, minute=45),
            datetime.time(hour=10, minute=0),
            datetime.time(hour=14, minute=30),
            datetime.time(hour=18, minute=15)
        ],
        "duracion_vuelo": "1h 50min",
        "precio_base": 2200
    },
    "15": {
        "destino": "Tokio",
        "pais": "Japón",
        "tipo": "Internacional",
        "horarios": [
            datetime.time(hour=13, minute=0),
            datetime.time(hour=22, minute=45)
        ],
        "duracion_vuelo": "14h 30min",
        "precio_base": 22000
    }
}


def imprimir_destinos():

    print("DESTINOS DISPONIBLES".center(80))

    # Separar destinos nacionales e internacionales
    nacionales = []
    internacionales = []

    for key, info in destinos.items():
        if info["tipo"] == "Nacional":
            nacionales.append((key, info))
        else:
            internacionales.append((key, info))

    # Imprimir destinos nacionales
    if nacionales:
        print("🛫 VUELOS NACIONALES (MÉXICO)".center(80))
        print("-"*80)
        for key, info in nacionales:
            print(f"\n[{key}] {info['destino']}")
            print(f"    📍 País: {info['pais']}")
            print(f"    ⏱️  Duración: {info['duracion_vuelo']}")
            print(f"    💰 Precio base: ${info['precio_base']:,} MXN")
            print(f"    🕐 Horarios disponibles: ", end="")
            horarios_str = ", ".join([h.strftime("%H:%M") for h in info['horarios']])
            print(horarios_str)

    # Imprimir destinos internacionales
    if internacionales:
        print("\n" + "="*80)
        print("✈️  VUELOS INTERNACIONALES".center(80))
        print("-"*80)
        for key, info in internacionales:
            print(f"\n[{key}] {info['destino']}")
            print(f"    📍 País: {info['pais']}")
            print(f"    ⏱️  Duración: {info['duracion_vuelo']}")
            print(f"    💰 Precio base: ${info['precio_base']:,} MXN")
            print(f"    🕐 Horarios disponibles: ", end="")
            horarios_str = ", ".join([h.strftime("%H:%M") for h in info['horarios']])
            print(horarios_str)

    print("\n" + "="*80 + "\n")


def imprimir_destino_individual(clave_destino):
    """
    Imprime la información detallada de un destino específico

    Args:
        clave_destino (str): La clave del destino a imprimir
    """
    if clave_destino in destinos:
        info = destinos[clave_destino]
        print("\n" + "="*60)
        print(f"INFORMACIÓN DE VUELO: {info['destino']}".center(60))
        print("="*60)
        print(f"\n📍 Destino: {info['destino']}")
        print(f"🌍 País: {info['pais']}")
        print(f"🎫 Tipo de vuelo: {info['tipo']}")
        print(f"⏱️  Duración estimada: {info['duracion_vuelo']}")
        print(f"💰 Precio base: ${info['precio_base']:,} MXN")
        print(f"\n🕐 Horarios disponibles:")
        for i, horario in enumerate(info['horarios'], 1):
            print(f"   {i}. {horario.strftime('%H:%M hrs')}")
        print("="*60 + "\n")
    else:
        print(f"\n❌ Error: No se encontró el destino con clave '{clave_destino}'")


def obtener_destinos_por_tipo(tipo):
    """
    Retorna una lista de destinos filtrados por tipo (Nacional o Internacional)

    Args:
        tipo (str): "Nacional" o "Internacional"

    Returns:
        dict: Diccionario con los destinos del tipo especificado
    """
    destinos_filtrados = {}
    for key, info in destinos.items():
        if info["tipo"].lower() == tipo.lower():
            destinos_filtrados[key] = info
    return destinos_filtrados


