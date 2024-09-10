from fastapi import FastAPI
from pydantic import BaseModel
from src.predictory import PrediccionNacionalidad
app = FastAPI()

class Texts(BaseModel):
    texts: list[str]

predictor = PrediccionNacionalidad( "models/naive_bayes.pkl","models/nationality_vectorizer.pkl")

@app.post("/predict")
def predict_nationality(data: Texts):
    predictions = predictor.predict(data.texts)
    # Asegurarse de que las predicciones sean una lista de strings
    predictions_list = predictions.tolist() if hasattr(predictions, 'tolist') else predictions
    return {"predictions": predictions_list}
