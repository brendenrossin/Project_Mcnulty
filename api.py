import numpy as np
import pickle

decision_tree = pickle.load(open('./model/model.pkl', 'rb'))

example = {
    'Flight_Purpose_Aerial Application': 0.0,
    'Flight_Purpose_Business': 0.0,
    'Flight_Purpose_Ferry': 0.0,
    'Flight_Purpose_Instructional': 0.0,
    'Flight_Purpose_Other': 0.0,
    'Flight_Purpose_Personal': 1.0,
    'Flight_Purpose_Positioning': 0.0,
    'Weather_Condition_IMC': 0.0,
    'Weather_Condition_VMC': 1.0,
    'Broad_Phase_of_Flight_INFLIGHT': 1.0,
    'Broad_Phase_of_Flight_LANDING': 0.0,
    'Broad_Phase_of_Flight_TAKEOFF': 0.0,
    'Broad_Phase_of_Flight_TAXI': 0.0,
    'Commercial_Flight_No': 1.0,
    'Commercial_Flight_Yes': 0.0,
}


def make_prediction(features):
    X = np.array([features['Flight_Purpose_Aerial Application'], features['Flight_Purpose_Business'],
                  features['Flight_Purpose_Ferry'], features['Flight_Purpose_Instructional'],
                  features['Flight_Purpose_Other'], features['Flight_Purpose_Personal'],
                  features['Flight_Purpose_Positioning'], features['Weather_Condition_IMC'],
                  features['Weather_Condition_VMC'], features['Broad_Phase_of_Flight_INFLIGHT'],
                  features['Broad_Phase_of_Flight_LANDING'], features['Broad_Phase_of_Flight_TAKEOFF'],
                  features['Broad_Phase_of_Flight_TAXI'], features['Commercial_Flight_No'],
                  features['Commercial_Flight_Yes']]).reshape(1, -1)
    prob_fatal = decision_tree.predict_proba(X)[0, 0]

    result = {
        'prediction': int(prob_fatal < 0.5),
        'prob_fatal': np.round(prob_fatal, 4)
    }
    return result


if __name__ == '__main__':
    print(make_prediction(example))
