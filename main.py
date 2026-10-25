meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LMAO": "Respuesta a algo muy gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, Siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "BOMBOCLAP": "Respuesta a algo inesperado"
            }
for i in range(5):
    print("Este diccionario esta incompleto, Si la palabra no esta, busca a tu nieto para que lo ponga en el diccionario")
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("la palabra no esta en el diccionario, Buscalo y ponlo en el diccionario")
        key = input("¿Cual es la palabra/Meme?")
        value = input("¿Cual es el significado de la palabra?")
        meme_dict[key] = value

print(meme_dict)
