from flask import Flask, jsonify, render_template_string
from calculadora import *

app = Flask(__name__)

@app.route("/")
def inicio():
    html = """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculadora Interactiva</title>
        <style>
            body {font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #f4f4f4;}
            .calculator {background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);}
            input {padding: 12px; font-size: 18px; width: 100%; margin-bottom: 15px; border: 2px solid #ddd; border-radius: 8px;}
            .buttons {display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;}
            button {padding: 15px; font-size: 18px; background: #007bff; color: white; border: none; border-radius: 8px; cursor: pointer;}
            button:hover {background: #0056b3;}
            #resultado {margin-top: 20px; padding: 15px; font-size: 22px; background: #e9ffe9; border-radius: 8px; min-height: 30px;}
            .error {background: #ffe9e9; color: red;}
        </style>
    </head>
    <body>
        <div class="calculator">
            <h1>🧮 Calculadora Interactiva</h1>
            
            <label>Número 1:</label>
            <input type="number" id="num1" placeholder="Primer número" value="5">
            
            <label>Número 2:</label>
            <input type="number" id="num2" placeholder="Segundo número" value="3">
            
            <div class="buttons">
                <button onclick="calcular('sumar')">➕ Sumar</button>
                <button onclick="calcular('restar')">➖ Restar</button>
                <button onclick="calcular('multi')">✖️ Multiplicar</button>
                <button onclick="calcular('divi')">➗ Dividir</button>
            </div>
            
            <div id="resultado">Resultado aparecerá aquí...</div>
        </div>

        <script>
            async function calcular(operacion) {
                const num1 = document.getElementById('num1').value;
                const num2 = document.getElementById('num2').value;
                const resultadoDiv = document.getElementById('resultado');
                
                if (!num1 || !num2) {
                    resultadoDiv.innerHTML = "Por favor ingresa ambos números";
                    resultadoDiv.className = "error";
                    return;
                }
                
                resultadoDiv.className = "";
                resultadoDiv.innerHTML = "Calculando...";
                
                try {
                    const response = await fetch(`/${operacion}/${num1}/${num2}`);
                    const data = await response.json();
                    
                    if (response.ok) {
                        resultadoDiv.innerHTML = `<strong>${data.operacion.toUpperCase()}</strong><br>Resultado: <strong>${data.resultado}</strong>`;
                    } else {
                        resultadoDiv.innerHTML = `Error: ${data.error || 'Error desconocido'}`;
                        resultadoDiv.className = "error";
                    }
                } catch (error) {
                    resultadoDiv.innerHTML = "Error de conexión";
                    resultadoDiv.className = "error";
                }
            }
        </script>
    </body>
    </html>"""
    return render_template_string(html)

@app.route("/sumar/<int:a>/<int:b>")
def suma(a,b):
    return jsonify({
        "operacion":"suma",
        "resultado": sumar(a,b)
    })

@app.route("/restar/<int:a>/<int:b>")
def resta(a, b):
    return jsonify({
        "operacion": "resta",
        "resultado": restar(a, b)
    })

@app.route("/multi/<int:a>/<int:b>")
def multiplica(a, b):
    return jsonify({
        "operacion": "multiplicación",
        "resultado": multi(a, b)
    })
   
@app.route("/divi/<int:a>/<int:b>")
def divide(a, b):
    try:
        return jsonify({
            "operacion": "división",
            "resultado": divi(a, b)
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True)