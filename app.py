from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Renderiza templates/index.html si existe
    return render_template("index.html")

if __name__ == "__main__":
    # Escucha en 0.0.0.0:8080 para que el IDE pueda mostrarlo
    app.run(host="0.0.0.0", port=8080, debug=True)
