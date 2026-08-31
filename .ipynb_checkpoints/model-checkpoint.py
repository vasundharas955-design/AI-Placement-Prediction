import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("placementdata.csv")
print(df)        
print(df.dtypes)
print(df.isnull().sum())


#                                     label encoding(string data---->integers)
PlacementTraining_encoder=LabelEncoder()
PlacementStatus_encoder=LabelEncoder()
df['PlacementTraining']=PlacementTraining_encoder.fit_transform(df['PlacementTraining'])
df['PlacementStatus']=PlacementStatus_encoder.fit_transform(df['PlacementStatus'])


#                                     Feature scaling(integers---->scaler)
scaler=MinMaxScaler()
columns=['CGPA','Projects','Certifications','Internships','AptitudeTestScore','SoftSkillsRating']
df[columns]=scaler.fit_transform(df[columns])
print(df[columns])


#                                     seperating x and y
x=df[['CGPA','Projects','Certifications','Internships', 'AptitudeTestScore','SoftSkillsRating','PlacementTraining']]
y=df['PlacementStatus']
print(x)
print(y)


#                                      train test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


#                                       logistic reagression
lr=LogisticRegression()
lr.fit(x_train,y_train)


#                                           prediction
lr_prediction=lr.predict(x_test)
lr_accuracy=accuracy_score(y_test,lr_prediction)
print(lr_accuracy) 


#                                         decision tree classifier
dt=DecisionTreeClassifier(random_state=42)
dt.fit(x_train,y_train)
dt_prediction=dt.predict(x_test)
dt_accuracy=accuracy_score(y_test,dt_prediction)
print(dt_accuracy)


#                                         comparing model
best_model=lr

#                                        confusion matrix
prediction=best_model.predict(x_test)
print(confusion_matrix(y_test,prediction))

#                                       classification report
print(classification_report(y_test,prediction))


#                                        taking user input
CGPA=float(input(' Enter the CGPA:'))
Projects=int(input(' Enter the number of Projects that students have done so far:'))
Certifications=int(input(' Enter the number of Certifications that students have done so far:'))
Internships=int(input('Enter the number of Internships that students have done so far:'))
AptitudeTestScore=float(input(' Provide Aptitude Score:'))
SoftSkillsRating=float(input(' Provide Soft Skills Rating:'))
PlacementTraining=input('Placement Training:(Yes/NO):').strip().capitalize()


#                                           encoding input
PlacementTraining=PlacementTraining_encoder.transform([PlacementTraining])[0]



#                                          scaling numeric values
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
    'SoftSkillsRating',
    ]
new_student[columns]=scaler.transform(new_student[columns])



#                                                  prediction
result = best_model.predict(new_student)
probability = best_model.predict_proba(new_student)
print("Prediction:",result[0])
print("Probability:",probability)


#                                                   results
if result[0] == 1:
    print('student is placed')
else:
    print('student is not placed')

#                                              model_save
joblib.dump(best_model ,"placement_model.pkl")
joblib.dump(scaler,"scaler.pkl")
joblib.dump(PlacementTraining_encoder,"PlacementTraining_encoder.pkl")
print("model saved successfully")

