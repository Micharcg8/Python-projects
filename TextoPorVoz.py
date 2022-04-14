import speech_recognition as sr       #importamos la libreria

r = sr.Recognizer()

#se usa la clase microphone, para que el microfono por defecto de nuestro sistema sea la fuente de datos que capture la palabras

with sr.Microphone() as source:
    print("Say Something...") #avisamos al usuario que ya estamos listo para recibir las palabras con el metodo listen
    audio = r.listen(source)

#se usa el bloque try - except, para controlar aquellos casos donde exista un error para capturar o entender que dice el usuario

    try:
        text = r.recognize_google(audio)
        print("What did you say: {}".format(text))
    except:
        print("I'm sorry! I can't understand!")