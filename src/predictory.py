import joblib

class PrediccionNacionalidad:
    def __init__(self, modelo_path, vectorizer_path):
        self.modelo = self.load_model(modelo_path)
        self.vectorizer =  self.load_model(vectorizer_path)

    def load_model(self, path):
        with open(path, "rb") as file:
            return joblib.load(file)
    def predict(self, texts):
        transformed_texts = self.vectorizer.transform(texts)
        predictions = self.modelo.predict(transformed_texts)
        return predictions

