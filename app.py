from flask import Flask, render_template, request
import huma

app = Flask(__name__, template_folder='./templates')

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def run_command():
    if request.method == "POST":
        komut = request.form["komut"]
        result, error = huma.run('<stdin>', komut)

        if error:
            sonuc_html = f"<p class='error'>{error.as_string()}</p>"
        elif result:
            if len(result.elements) == 1:

                sonuc_html = f"<p>{repr(result.elements[0])}</p>"
            else:

                sonuc_html = f"<p>{repr(result)}</p>"
        else:
            sonuc_html = "<p>Komut çalıştırılamadı.</p>"

        return render_template("index.html", sonuc=sonuc_html)

if __name__ == "__main__":
    app.run(debug=True)
