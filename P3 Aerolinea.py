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
salir_RE = r"[sS]alir|[mM]e equivoque|[pP]erd[oó]n|[aA]di[óo]s|[lL]a cague|[uU]ps|[sS]orry|[eE]rror|[Nn]o|[fF]all[ao]|[sS]kype|[dD]eseo (salir|interrumpir)| "


state = 0
salida = 1

saludo =("Soy capaz de informarte de nuestras promociones, darte informacion para algun destino,"
         "\nasistirte con tu equipaje, consultar el estatus de tu vuelo o resolverte alguna duda.\n")


while salida:
    if state == 0:
        print("Hola soy el chatbot de Vivaerobus ¿En qué te puedo ayudar?\n")
        time.sleep(1)
        opcion = input(saludo + "\t")
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

    if state == 1: #opcion de promociones
        print("PROMOCIONES VIVAEROBUS")
        from promociones import promociones

        # Mostrar lista de promociones
        for key, promo in promociones.items():
            print(f"\n{key}. {promo['nombre']}")

        # Preguntar si quiere ver detalles
        time.sleep(0.5)
        opcion_promo = input("\nSi te gustaria revisar algun detalle de alguna promocion, solo indicame el numero de la misma \n\t\t").strip()

        if opcion_promo in promociones:
            promo_seleccionada = promociones[opcion_promo]
            print(f"{promo_seleccionada['nombre']}")
            print(f"\nDetalle: {promo_seleccionada['detalle']}")
            print(f"Vigencia: {promo_seleccionada['vigencia']}")
            print("\nPara reservar, visita https://www.vivaaerobus.com/es-mx/ o llama al 818-215-0000")
        elif opcion_promo.lower() not in ['no', 'n', 'salir']:
            print("\nLo siento, no existe esa opcion")

        state = 2
    if state == 6: #opcion de asistencia con equipaje
        print("ASISTENCIA CON EQUIPAJE")

        # Información de equipaje
        from info_equipaje import info_equipaje

        print("\nTipos de equipaje disponibles:\n")
        time.sleep(2)
        for key, equip in info_equipaje.items():
            print(f"{key}. {equip['tipo']}")
            print(f"Peso máximo: {equip['peso_max']}")
            print(f"Dimensiones: {equip['dimensiones']}\n")


        # Preguntar qué información necesita
        time.sleep(2)
        opcion_equip = input("\nIndicame sobre que numero de opcion quieres obtener detalle o si de todos los casos \n\t\t").strip()

        if opcion_equip.lower() == 'todo' or opcion_equip.lower() == 'todos':
            # Mostrar toda la información
            print("INFORMACIÓN COMPLETA DE EQUIPAJE")
            for key, equip in info_equipaje.items():
                print(f"\n{key}. {equip['tipo']}")
                print(f"Peso máximo: {equip['peso_max']}")
                print(f"Dimensiones: {equip['dimensiones']}")
                print("\nInformación importante:")
                for detalle in equip['detalles']:
                    print(f"      • {detalle}")
                if equip.get('restricciones'):
                    print("\nRestricciones:")
                    for restriccion in equip['restricciones']:
                        print(f"      • {restriccion}")


        elif opcion_equip in info_equipaje:
            # Mostrar información específica
            equip_seleccionado = info_equipaje[opcion_equip]
            print(f"{equip_seleccionado['tipo']}")
            print(f"\nPeso máximo permitido: {equip_seleccionado['peso_max']}")
            print(f"Dimensiones máximas: {equip_seleccionado['dimensiones']}")

            print("\nInformación importante:")
            for detalle in equip_seleccionado['detalles']:
                print(f"   • {detalle}")

            if equip_seleccionado.get('restricciones'):
                print("\n⚠Restricciones:")
                for restriccion in equip_seleccionado['restricciones']:
                    print(f"   • {restriccion}")


            # Ofrecer ayuda adicional
            time.sleep(0.5)
            ayuda_extra = input("\n¿Necesitas información sobre otro tipo de equipaje? \n\t\t").strip()
            if re.findall(afirmacion_RE, ayuda_extra, flags=0) != []:
                state = 7  # Estado para ver otro tipo de equipaje
            else:
                state = 2  # Continuar al menú de seguimiento

        elif opcion_equip.lower() not in ['no', 'n', 'salir']:
            print("\nOpción no válida.")
            state = 2
        else:
            state = 2

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

    if state == 7:  # Ver otro tipo de equipaje

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

    if state == 8:  # Calcular equipaje según tarifa
        print("\nCALCULADORA DE EQUIPAJE POR TARIFA")

        print("\n¿Qué tarifa compraste?\n")
        print("1. Light (la más económica)")
        print("2. Plus (incluye equipaje documentado)")
        print("3. Viva (todo incluido)")

        tarifa = input("\nSelecciona el numero de tu tarifa \n\t\t").strip()

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





    if state == 2:
        # Estado de continuación después de ejecutar accion
        time.sleep(0.5)
        opcion_continuar = input("\n¿Te puedo ayudar en algo más?\n\t\t").strip()

        if re.findall(afirmacion_RE, opcion_continuar, flags=0) != []:
            state = 0
        elif re.findall(salir_RE, opcion_continuar, flags=0) != []:
            state = 99
        else:
            state = 0

    if state == 99:
        print("Gracias por usar Vivaerobus Chatbot, ")
        print("Que tengas un excelente dia")
        salida = 0

    if state == 100:
        print("\nLo siento, no entendí tu solicitud.")
        print("Por favor, intenta reformular tu pregunta o elige una de las opciones disponibles.\n")
        time.sleep(1)
        state = 0