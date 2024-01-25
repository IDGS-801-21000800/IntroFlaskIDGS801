from flask import Flask, render_template, request #importe de las librerias

app=Flask(__name__)

 #definicion de rutas
 #por defecto, los metodos son de tipo post
@app.route("/") #Pagina principal 
def index():
    return render_template("index.html") #importe de archivos html

@app.route("/alumnos") #Pantalla de alumnos
def alumnos():
    titulo="Alumnos UTL"
    nombres=["mario", "pedro", "juan", "Angel"]
    return render_template("alumnos.html",titulo=titulo, nombres=nombres)
    '''
        Para envio de informacion de variable, 
        se puede enviar a traves de render_template haciendo referencia a las variables
    '''

@app.route("/maestros") #Pantalla de maestros
def maestros():
    return render_template("maestros.html")

@app.route("/test")
def test():
    return "<h1>texto</h1>"

@app.route("/prueba")
def prueba():
    return "<h6>mm</h6>"

 #uso de variables
@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "tu nombre es "+nom

@app.route("/numero/<int:num>")
def numeros(num):
    return "tu número es {}".format(num)

@app.route("/user/<int:num>/<string:nom>")
def validate(num, nom):
    return "ID {} <br> Nombre {}".format(num, nom)

@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    res = num1+ num2
    return "El resultado de {} + {} es: {}".format(num1,num2,res)

@app.route("/default") # valores default
@app.route("/default/<string:nom>")
def default(nom="null"):
    return "Su nombre es " + nom

@app.route("/calcular", methods=["GET", "POST"]) #asigancion de los tipos de metodos
def calcular():
    if request.method=="POST": # verificacion del tipo del metodo
        num1 = request.form.get("n1")
        num2 = request.form.get("n")

        return "La multiplicacion {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
    else :
        return '''
            <form action="/calcular" method="POST">
                <label>N1:</label>
                <input type="text" name="n1"><br>
                <label>N2:</label>
                <input type="text" name="n2"><br>
                
                <input type="submit" />
            </form>
    '''

@app.route("/operasBas")
def operasBas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method=="POST": # verificacion del tipo del metodo
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        res = int(num1)*int(num2)
        return "La multiplicacion {} x {} = {}".format(num1,num2,res)

if __name__=="__main__":
    app.run(debug=True) #Activar modo de debug, recarga la aplicacion