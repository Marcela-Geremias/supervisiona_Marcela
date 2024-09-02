from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route("/predict", methods=["POST"])
def predict_attrition():
    resultado = None
    try:
        age = int(request.form["Age"])
        distance_from_home = int(request.form["DistanceFromHome"])
        environment_satisfaction = int(request.form["EnvironmentSatisfaction"])
        job_involvement = int(request.form["JobInvolvement"])
        job_satisfaction = int(request.form["JobSatisfaction"])
        gender_ajustado = int(request.form["gender_ajustado"])  


        if ((environment_satisfaction <= 2 and job_satisfaction <= 2) or 
            (environment_satisfaction <= 2 and job_involvement <= 2) or
            (job_satisfaction <= 2 and job_involvement <= 2)):
            resultado = "Sim"  
        else:
            resultado = "Não" 

    except Exception as e:
        print(f"Erro: {e}")
        resultado = "Erro na predição"

    return render_template("result.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
