from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import sympy as sp
# Después de inicializar tu app Flask

app = Flask(__name__)
CORS(app)

# Descargar recursos necesarios de nltk
nltk.download('punkt')
nltk.download('stopwords')

# Información de la institución
institucion = {
    "nombre": "José Gálvez",
    "ubicacion": "Jr las Begonias, Rio negro, Perú",
    "telefono": "01-234-5678",
    "horario": "Lunes a viernes de 8am a 3pm"
}

# Funciones de operaciones matemáticas
def calcular_expresion(expresion):
    try:
        resultado = sp.sympify(expresion)
        return f"El resultado de {expresion} es {resultado}."
    except Exception as e:
        return f"Error: {str(e)}"

# Función para resumir texto
def resumir_texto(texto, num_oraciones=2):
    oraciones = sent_tokenize(texto, language="spanish")
    palabras = word_tokenize(texto.lower())
    stop_words = set(stopwords.words('spanish'))
    palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in stop_words]
    frecuencia = Counter(palabras_filtradas)

    puntuacion_oraciones = {}
    for oracion in oraciones:
        for palabra in word_tokenize(oracion.lower()):
            if palabra in frecuencia:
                if oracion not in puntuacion_oraciones:
                    puntuacion_oraciones[oracion] = 0
                puntuacion_oraciones[oracion] += frecuencia[palabra]

    oraciones_resumidas = sorted(puntuacion_oraciones, key=puntuacion_oraciones.get, reverse=True)[:num_oraciones]
    return ' '.join(oraciones_resumidas)

# Función para extraer contenido de una página web
def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = [tag.get_text() for tag in soup.find_all(['p', 'h1', 'h2', 'h3'])]
        return ' '.join(content)
    except requests.RequestException as e:
        return f"Error al acceder a la web: {e}"

# Función del chatbot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    userInput = request.json.get('message', '')
    response = ""

    try:
        # Evaluar expresiones matemáticas simples
        if userInput.lower().startswith("calcular "):
            expression = userInput[9:].strip()  # Extraer la expresión
            response = calcular_expresion(expression)
        else:
            # Respuestas predefinidas
            if 'ubicacion' in userInput.lower():
                response = "La ubicación del colegio José Gálvez es Jr. Las Begonias (secundaria) y Jr. Las Orquídeas (primaria) Río Negro-Satipo."
            elif 'hola' in userInput.lower():
                response = "Hola mucho gusto, soy tu chatbot personal 😊, estoy aquí para contestar tus preguntas."
            elif 'como estas' in userInput.lower():
                response = "Estoy bien y feliz de ser tu chatbot personal 😁."
            elif 'que haces' in userInput.lower():
                response = "Puedo contestar tus preguntas sobre la información del colegio José Galvez y también puedo resolver problemas matemáticos básicos."
            elif 'nombre' in userInput.lower():
                response = "José Galvez"
            elif 'niveles' in userInput.lower():
                response = "El colegio José Galvez cuenta con 2 niveles Primaria y Secundaria."
            elif 'telefono' in userInput.lower():
                response = "El teléfono es 964073785."
            elif 'director' in userInput.lower():
                response = "El director del colegio José Galvez es Melgar Quispe José Fernando."
            elif 'correo' in userInput.lower():
                response = "El correo es ieijosegalvez@gmail.com."
            elif 'horario' in userInput.lower():
                response = "El horario es de lunes a viernes de 8am a 3pm."
            elif 'historia' in userInput.lower():
                response = "La Institución Educativa José Gálvez, fue creada con la Resolución Directoral-005-82-La Merced, jurisdicción de la tercera Región de Educación de Junín, el 02 de mayo de 1982, en tanto la Escuela Rural PRE vocacional N°5204 del anexo de Rio Negro, Distrito de Satipo, fue creado mediante una R.D.N° 97458 del 09 de junio de 1942. La iniciativa de la integración por parte del presidente de APAFA del nivel primaria señor Victor Astoray Castillo, en coordinación con la Dirección del nivel primaria y el nivel secundaria el presidente de APAFA el señor Hernan Garcia, siendo el director el profesor Gilberto Bendezú Montero, en una reunión de docentes y directivos se logra la aceptación por parte de su mayoría. Obteniéndose una primera R.D. en el mes de febrero de 1994, comenzando la unificación como Centro Educativo Integrado de los niveles de primaria y secundaria. Desde entonces somos una Institución Educativa Integrado, con las especialidades de Industrias Alimentarias y Computación."
            else:
                response = "Lo siento, no entiendo esa operación o pregunta."

    except Exception as e:
        response = f"Ocurrió un error: {str(e)}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
