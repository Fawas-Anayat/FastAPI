"""here we are going to  create a project in which our role is to build APIs
and upon hitting them the user will get some information"""

from fastapi import FastAPI, Path, HTTPException
app=FastAPI()
data={
    'P001':"usman",
    'P002':"akber",
    'P003':"umer",
    'P004':"Abdullah"
}
def load_data(patient_id:str):
    return data[patient_id]

@app.get('/data/{patient_id}')
def pat_data(patient_id:str=Path(...,title='patient ID',description='this is the uniqu ID assigned to each patient eg(P001,P002 etc)')):
    l=data.keys()
    if patient_id in l:
        return {"patient ID": {patient_id},"patinet name":data[patient_id]}
    raise HTTPException(status_code=404,detail="patient record not found in the database")

@app.get('/view')
def view_all_patients():
    return data

@app.get('/informatin')
def info():
    return "this is the database of the patients having all the information about the patients having their names and other details"