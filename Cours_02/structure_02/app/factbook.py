from flask import Flask
from .config import Config

app = Flask(__name__.split('.')[1]) #REF-1 du cours 1. Nom du module changé afin de changer la valeur de __name__.
# normalement, cela devrait afficher app.factbook. Afin de n'avoir que factbook, je fais un split sur le point afin de ne garder que factbook.


version = "0.0.1" #APP-2 séance 1. Je donne ici une valeur à ma variable version
template_folder='templates'
app.config.from_object(Config)

@app.route('/home/<string:id>') 
def personne (id): 
    return 'Hello' + ' ' + id

@app.route('/division/<int:int1>/<int:int2>') #REV-2 du cours 2. ma route prend en entrée 2 arguments optionnels de type int
def division (int1, int2): #mon décorateur amène une fonction division qui prend en entrée les deux arguments optionnels.
    resultat = int1 / int2 #Je fais l'opération de division entre les deux arguments optionnels.
    return str(resultat) #Je retourne sur la page web le résultat de la division entre les deux arguments optionnels

"""
    Si on fait plusieurs routes pour une seule fonction, il faut veiller à ce que chaque route ai le même nombre d'arguments que la fonction
"""

