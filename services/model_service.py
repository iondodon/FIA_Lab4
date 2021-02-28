from ml.model import ValuePredictModel
import numpy
import pandas as pd

MODEL = ValuePredictModel()


def predict_apartment_value(test_data_json: str) -> list:
    pd_test_data = pd.read_json(test_data_json)
    prediction: numpy.ndarray = MODEL.predict(pd_test_data)
    return prediction.flatten().tolist()
