import re
import time
from datetime import datetime, date, timedelta


# Lenguaje Natural por expresiones regulares
Promo_RE = r"[pP]romociones?|[Pp]romos?|[dD]escuentos?|[oO]fertas?|[eE]special(es)?|[qQ]uiero (ver |las |los )?(promociones?|descuentos?|ofertas?|promos?)|[hH]ay (promociones?|descuentos?|ofertas?)|[mM]uest(ra|ren)(me)? (las |los )?(promociones?|ofertas?)|[qQ]u[eé] (promociones?|ofertas?|descuentos?) (hay|tienen|ofrecen)"

Asis_Re = r"[aA]yuda|[aA]sistencia|[eE]quipaje|[mM]aletas?|[cC]argar|[pP]eso|[kK]ilos?|[dD]imensiones?|[lL]levar|[nN]ecesito (ayuda|apoyo|asistencia) (con|sobre|para) (mi|mis|el|la) (equipaje|maletas?)|[cC]u[aá]nto (puedo|debo) (llevar|cargar)|[cC]u[aá]ntas? maletas?|[qQ]u[eé] (puedo|debo) (llevar|cargar)|[lL][ií]mite (de )?equipaje"

InfoDest_RE = r"[iI]nfo(rmaci[oó]n)?( (de|del|sobre|para))? (destino|viaje|vuelo|ciudad)|[dD]estino|[vV]iajar (a |hacia )?|[cC][oó]mo (es|est[aá]) |[qQ]u[eé] (hay|ver|hacer|visitar) (en )?|[cC]iudad(es)?|[dD][oó]nde (puedo|debo) (ir|viajar)|[hH]oteles?|[tT]ransporte|[rR]ecomendaciones?|[lL]ugares? (para|de) (visita|turismo|inter[eé]s)|[mM]e interesa (viajar|conocer)|[hH]abla(me)? (de|sobre)|[cC]u[eé]ntame (de|sobre)"

Dudas_Re = r"[dD]udas?|[pP]reguntas?|[cC]onsultas?|[iI]nformaci[oó]n|[aA]claraci[oó]n|[nN]o (entiendo|comprendo|s[eé])|[pP]uedes? (ayudar|explicar|aclarar)(me)?|[tT]engo (una )?(duda|pregunta|consulta)|[qQ]uisiera (saber|preguntar)|[mM]e (gustar[ií]a|interesa) (saber|preguntar)|[cC][oó]mo (funciona|se hace|puedo)|[nN]ecesito (informaci[oó]n|saber)|[qQ]u[eé] (es|significa|quiere decir)|[pP]ol[ií]tica(s)?|[rR]equisitos?|[dD]ocumento(s)?|[pP]asaporte|[vV]isa"

Estadovuelo_RE = r"[eE]sta(do|tus) (de |del )?vuelo|[vV]uelo|[eE]st[aá] (retrasado|a tiempo|cancelado)|[hH]ora (de )?(salida|llegada|abordaje)|[pP]uerta (de )?(abordaje|embarque)?|[nN][uú]mero (de )?vuelo|[cC]onsultar (mi )?vuelo|[vV]erificar vuelo|[dD][oó]nde (est[aá]|se encuentra) (mi )?vuelo|[sS]eguimiento (de |del )?vuelo|[rR]astrear vuelo|[aA]terrizar|[dD]espegar|[dD]espegue|[aA]terrizaje|[mM]i vuelo (es|sale|llega)|[cC]hec(k|ar) vuelo"

afirmacion_RE = r"[Ss][íi|] ([Cc]laro|[Gg]racias)|[Cc]laro|[dD]efinitivamente|[Pp]or supuesto|[Gg]racias|[Pp]or favor|[sS][íi]"
salir_RE = r"[sS]alir|[mM]e equivoque|[pP]erd[oó]n|[aA]di[óo]s|[lL]a cague|[uU]ps|[sS]orry|[eE]rror|[Nn]o|[fF]all[ao]|[sS]kype|[dD]eseo (salir|interrumpir)|[nN]op|[nN]el "

# Lenguaje natural para promodicones
Promo2x1_RE = r"[dD]os (x|por) [uU]no|2x1|[vV]uelos [iI]nternacionales|[iI]nternacionales|[eE]xtranjero|[fF]uera (de|del) pais"
PromoNac_RE = r"[vV]uelos [nN]acionales|[nN]acionales|[iI]nternos|[dD]entro|"
PromoEst_RE = r"[eE]studiantes|[aA]lumnos|20[%|[pP]orciento])|[eE]educaci[o|ó]n"
PromoEqp_RE = r"[eE]quipaje|[gG]ratis|[mM]aleta"

# Lenguaje natural para menu de asistencia equipaje
equipMano_RE = r"[eE]quipaje de [mM]ano|[mM]ano"
equipDoc1_RE = r"[pP]rime[r|ra ] [mM]aleta|[dD]ocumentad[a|o]|[eE]quipaje principal"
equipExt_RE = r"[eE]xtr[a|as]|[aA]dicional"
equipEsp_RE = r"[aA]rticul[o|os]|[eE]specia[l|les]"

state = 0
salida = 1

saludo =("Soy capaz de informarte de nuestras promociones, darte informacion para algun destino,"
         "\nasistirte con tu equipaje, consultar el estatus de tu vuelo o resolverte alguna duda.\n")


while salida:
    if state == 0:
        print("Hola soy el chatbot de Vivaerobus ¿En qué te puedo ayudar?\n")
        time.sleep(1)
        opcion = input(saludo + "\n\t")
        if re.findall(Promo_RE, opcion, flags=0) != []:
            state = 1
        elif re.findall(Asis_Re, opcion, flags=0) != []:
            state = 6
        elif re.findall(InfoDest_RE, opcion, flags=0) != []:
            state = 11
        elif re.findall(Dudas_Re, opcion, flags=0) != []:
            state = 16
        elif re.findall(Estadovuelo_RE, opcion, flags=0) != []:
            state = 21
        elif re.findall(salir_RE, opcion, flags=0) != []:
            state = 99
        else:
            state = 100

    # opcion de promociones
    if state == 1:
        print("PROMOCIONES VIVAEROBUS")

        promociones = {
            "1": {
                "nombre": "Vuelos Nacionales desde $599",
                "detalle": "Viaja por México desde $599 pesos. Aplica en rutas seleccionadas.",
                "vigencia": "Válido hasta el 28 de febrero 2026"
            },
            "2": {
                "nombre": "2x1 en vuelos internacionales",
                "detalle": "Compra un vuelo internacional y lleva a un acompañante gratis.",
                "vigencia": "Válido para viajes entre marzo y junio 2026"
            },
            "3": {
                "nombre": "20% de descuento para estudiantes",
                "detalle": "Presenta tu credencial vigente y obtén 20% de descuento.",
                "vigencia": "Válido todo el año 2026"
            },
            "4": {
                "nombre": "Equipaje documentado gratis",
                "detalle": "Añade hasta 25kg de equipaje sin costo adicional en vuelos seleccionados.",
                "vigencia": "Válido hasta el 31 de marzo 2026"
            }
        }

        # Mostrar lista de promociones
        for key, promo in promociones.items():
            print(f"\n{key}. {promo['nombre']}")

        # Preguntar si quiere ver detalles
        time.sleep(0.5)
        opcion_promo = input("\nQué promoción es de la que te gustaría tener más detalles \n\t\t").strip()

        if re.findall(Promo2x1_RE, opcion_promo, flags=0) != []:
            for valor in promociones["2"]:
                print(f"{promociones["2"][valor]}")
        elif re.findall(PromoNac_RE, opcion_promo, flags=0) != []:
            for valor in promociones["1"]:
                print(f"{promociones["1"][valor]}")
        elif re.findall(PromoEst_RE, opcion_promo, flags=0) != []:
            for valor in promociones["3"]:
                print(f"{promociones["3"][valor]}")
        elif re.findall(PromoEqp_RE, opcion_promo, flags=0) != []:
            for valor in promociones["4"]:
                print(f"{promociones["4"][valor]}")


        state = 2

    # opcion de asistencia con equipaje
    if state == 6:
        print("ASISTENCIA CON EQUIPAJE")

        # Información de equipaje
        info_equipaje = {
            "1": {
                "tipo": "Equipaje de Mano",
                "peso_max": "10 kg",
                "dimensiones": "55 x 40 x 20 cm (largo x ancho x alto)",
                "detalles": [
                    "Debe caber en el compartimento superior o debajo del asiento",
                    "Incluye 1 artículo personal (bolso, mochila pequeña)",
                    "Sin costo adicional",
                    "Permitido en todas las tarifas"
                ],
                "restricciones": [
                    "No puede contener líquidos mayores a 100ml",
                    "Líquidos deben ir en bolsa transparente"
                ]
            },
            "2": {
                "tipo": "Equipaje Documentado (Primera maleta)",
                "peso_max": "25 kg",
                "dimensiones": "158 cm lineales (suma de largo + ancho + alto)",
                "detalles": [
                    "Se documenta en el mostrador o en línea",
                    "Costo depende de la tarifa y ruta",
                    "Tarifa Light: $600 - $800 (aproximado)",
                    "Tarifa Plus/Viva: Incluida sin costo"
                ],
                "restricciones": [
                    "Peso máximo 25 kg por maleta",
                    "Exceso de peso: $150 por cada 5 kg adicionales"
                ]
            },
            "3": {
                "tipo": "Equipaje Adicional (Segunda maleta o más)",
                "peso_max": "25 kg por maleta",
                "dimensiones": "158 cm lineales por maleta",
                "detalles": [
                    "Segunda maleta: $800 - $1,200 (aproximado)",
                    "Tercera maleta: $1,200 - $1,500 (aproximado)",
                    "Los precios varían según ruta y temporada"
                ],
                "restricciones": [
                    "Máximo 5 maletas por pasajero",
                    "Sujeto a disponibilidad de espacio en la aeronave"
                ]
            },
            "4": {
                "tipo": "Artículos Especiales",
                "peso_max": "Variable según artículo",
                "dimensiones": "Variable según artículo",
                "detalles": [
                    "Instrumentos musicales: pueden ir como equipaje de mano si caben",
                    "Bicicletas: $800 - $1,500 (deben ir en caja)",
                    "Tablas de surf: $800 - $1,500",
                    "Equipo deportivo: $600 - $1,200",
                    "Mascotas: consultar políticas especiales"
                ],
                "restricciones": [
                    "Deben empacarse adecuadamente",
                    "Algunos requieren notificación previa"
                ]
            }
        }

        print("\nTipos de equipaje disponibles:\n")
        time.sleep(2)
        for key, equip in info_equipaje.items():
            print(f"{key}. {equip['tipo']}")
            print(f"Peso máximo: {equip['peso_max']}")
            print(f"Dimensiones: {equip['dimensiones']}\n")

        # Preguntar qué información necesita
        time.sleep(2)
        opcion_equip = input("\nNecesitas más informacion de alguna de ellas? \n\t\t").strip()
        if re.findall(afirmacion_RE, opcion_equip, flags=0) != []:
            opcion = input("\n De cual de ellas? \n\n\t")
            #if re.findall(equipMano_RE, opcion, flags=0) != []:
                #for carac in


        #else


        # Información general adicional
        if state == 6:  # Si no cambió el estado, mostrar tips generales
            print("CONSEJOS ÚTILES PARA TU EQUIPAJE")
            print("""
            1. Etiqueta tu equipaje con tu nombre y contacto
            2. Usa candados certificados por TSA
            3. Toma fotos de tu equipaje antes de documentar
            4. Pesa tu maleta en casa para evitar cargos por exceso
            5. Lleva artículos valiosos en tu equipaje de mano
            6. Medicamentos deben ir en su empaque original
            7. Baterías de litio solo en equipaje de mano
            8. Descarga la app Vivaerobus para rastrear tu equipaje
            """)

            # Preguntar si quiere calcular equipaje
            time.sleep(0.5)
            calcular = input("\n¿Deseas calcular cuánto equipaje puedes llevar según tu tarifa? \n\t\t").strip()
            if re.findall(afirmacion_RE, calcular, flags=0) != []:
                state = 8  # Estado para calcular equipaje
            else:
                state = 2

    # Ver otro tipo de equipaje
    if state == 7:

        info_equipaje = {
            "1": {"tipo": "Equipaje de Mano"},
            "2": {"tipo": "Equipaje Documentado (Primera maleta)"},
            "3": {"tipo": "Equipaje Adicional"},
            "4": {"tipo": "Artículos Especiales"}
        }

        print("Tipos de equipaje:\n")
        for key, equip in info_equipaje.items():
            print(f"{key}. {equip['tipo']}")

        opcion = input("\nIndicame el numero de la opcion que deseas consultar\n\t\t ").strip()
        if opcion in ["1", "2", "3", "4"]:
            state = 6  # Regresar al estado 6 para mostrar la info
        else:
            print("\nOpción no válida.")
            state = 2

    # Calcular equipaje según tarifa
    if state == 8:
        tarifas_info = {
            "1": {
                "nombre": "Light",
                "equipaje_mano": "1 maleta de mano (10 kg) + 1 artículo personal",
                "equipaje_documentado": "No incluido (se compra por separado)",
                "costo_primera": "$600 - $800 aproximado"
            },
            "2": {
                "nombre": "Plus",
                "equipaje_mano": "1 maleta de mano (10 kg) + 1 artículo personal",
                "equipaje_documentado": "1 maleta documentada (25 kg) incluida",
                "costo_adicional": "$800 - $1,200 por maleta adicional"
            },
            "3": {
                "nombre": "Viva",
                "equipaje_mano": "1 maleta de mano (10 kg) + 1 artículo personal",
                "equipaje_documentado": "1 maleta documentada (25 kg) incluida",
                "extras": "Asiento preferente y abordaje prioritario incluidos",
                "costo_adicional": "$800 - $1,200 por maleta adicional"
            }
        }


        print("\nCALCULADORA DE EQUIPAJE POR TARIFA")

        print("\n¿Qué tarifa compraste?\n")
        print("1. Light (la más económica)")
        print("2. Plus (incluye equipaje documentado)")
        print("3. Viva (todo incluido)")

        tarifa = input("\nSelecciona el numero de tu tarifa \n\t\t").strip()
        if tarifa in tarifas_info:
            info = tarifas_info[tarifa]
            print(f"\nTarifa {info['nombre']}")
            print(f"\nEquipaje de mano: {info['equipaje_mano']}")
            print(f"Equipaje documentado: {info['equipaje_documentado']}")
            if 'costo_primera' in info:
                print(f"Costo primera maleta documentada: {info['costo_primera']}")
            if 'costo_adicional' in info:
                print(f"Maletas adicionales: {info['costo_adicional']}")
            if 'extras' in info:
                print(f"Extras: {info['extras']}")

        else:
            print("\nOpción no válida.")

        state = 2

    # info destinos
    #if state == 11:


    # Estado de continuación después de ejecutar acción
    if state == 2:

        time.sleep(0.5)
        opcion_continuar = input("\n¿Te puedo ayudar en algo más?\n\t\t").strip()

        if re.findall(afirmacion_RE, opcion_continuar, flags=0) != []:
            state = 0
        elif re.findall(salir_RE, opcion_continuar, flags=0) != []:
            state = 99
        else:
            state = 0

    # Estado de Despedida
    if state == 99:
        print("Gracias por usar Vivaerobus Chatbot, ")
        print("Que tengas un excelente dia")
        salida = 0

    #Estado de error
    if state == 100:
        print("\nLo siento, no entendí tu solicitud.")
        print("Por favor, intenta reformular tu pregunta o elige una de las opciones disponibles.\n")
        time.sleep(1)
        state = 0