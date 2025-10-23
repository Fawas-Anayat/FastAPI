# practice_project_1

"""from fastapi import FastAPI

app=FastAPI()
@app.get('/')

def hello():
    return {'home':'hello world'}

@app.get("/about")
def about():
    return {'message' : "this is the first fastapi code"}

@app.get('/info')
def info():
    return "this is the new adding in the web page"

    

# practice_project_2

from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Simple GET endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

# GET with path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# POST endpoint - using dict instead of class
@app.post("/items")
def create_item(name: str, price: float, quantity: int = 1):
    total = price * quantity
    return {"item": name, "total_cost": total, "quantity": quantity}

# GET with query parameters
@app.get("/search")
def search_items(keyword: str, max_price: float = 100.0):
    return {"searching_for": keyword, "max_price": max_price}


    """

from fastapi import FastAPI, Path, HTTPException
app=FastAPI()
data={
    'P001':"usman",
    'P002':"akber"
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