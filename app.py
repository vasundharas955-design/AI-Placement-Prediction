from flask import Flask, render_template, request
import joblib
import pandas as pd

app=Flask(__name__)

 #                                            load the files
model=joblib.load('placement_model.pkl')
scaler=joblib.load('scaler.pkl')
PlacementTraining_encoder=joblib.load('PlacementTraining_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    CGPA=float(request.form['CGPA'])
    Projects=int(request.form['Projects'])
    Certifications=int(request.form['Certifications'])
    Internships=int(request.form['Internships'])
    AptitudeTestScore=float(request.form['AptitudeTestScore'])
    SoftSkillsRating=float(request.form['SoftSkillsRating'])
    PlacementTraining=request.form['PlacementTraining']

    PlacementTraining=PlacementTraining_encoder.transform([PlacementTraining])[0]

    new_student=pd.DataFrame({
    'CGPA':[CGPA],
    'Projects':[Projects],
    'Certifications':[Certifications],
    'Internships':[Internships],
    'AptitudeTestScore':[AptitudeTestScore],
    'SoftSkillsRating':[SoftSkillsRating],
    'PlacementTraining':[PlacementTraining]
})
    columns=[
    'CGPA',
    'Projects',
    'Certifications',
    'Internships',
    'AptitudeTestScore',
    'SoftSkillsRating'
    ]
    new_student[columns]=scaler.transform(new_student[columns])

    result = model.predict(new_student)

    if result[0] == 1:
        prediction='student is likely to be placed'
    else:
        prediction='student is not likely to be placed'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


    


