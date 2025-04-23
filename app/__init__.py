#importar, utilizar 
#una dependencia en python 

from flask import Flask , render_template

#crear la aplicacion 
#de flask 

app = Flask (__name__)

#utilizar  app 
#para crear una ruta 
@app.route('/prueba')
def prueb() :
    #defino la lista de paises
    paises = [
                {
                    'nombre': 'Argentina',
                    'capital': 'Buenos aires',
                    'moneda' : 'peso argentino',
                    "poblacion": '45.54M',
                    'superficie':'2.78km', 
                    'ciudades':'rosario'
                },

                {
                    'nombre': 'Ecuador',
                    'capital': 'Quito',
                    'moneda' : 'Dolar',
                    "poblacion": '17.98M',
                    'superficie':'283.561km', 
                    'ciudades':'guayaquil, cuenca, manta',
                },
                {
                    'nombre': 'Paraguay',
                    'capital': 'Asunción',
                    'moneda' : 'Guaraní',
                    "poblacion": '6.844M',
                    'superficie':'406.752km', 
                    'ciudades':'asuncion, ciudad del este, villarrica',
                },
                {
                    "nombre": "Brasil",
                    "capital": "Brasilia",
                    "moneda": "Real",
                    "poblacion": '211.1M',
                    'superficie':'8.51km', 
                    'ciudades':'rio de janeiro, sao paulo, recife',
                },
                {
                    "nombre": "Venezuela",
                    "capital": "Caracas",
                    "moneda": "Bolivar",
                    "poblacion":'28,3M',
                    'superficie':'916.445km', 
                    'ciudades':'Maracaibo, El tocuyo, Cumana',
                },


            ]
    #eviar la lista de paises 
    #a la vista 
    return render_template('paises.html', paises = paises, usuario= "cristian", ) 