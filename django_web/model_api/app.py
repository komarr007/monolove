import json
from flask import Flask, request
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pymongo

MODEL_PATH = "C:\\Users\\Mario\\Documents\\dating data analysis\\saved_model\\model_v5"
model = tf.keras.models.load_model(MODEL_PATH)

app = Flask(__name__)


def read_data() -> pd.DataFrame:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["dating_dump"]
    collection = db["dating"]

    data = list(collection.find())
    df = pd.DataFrame(data)
    df_training = df.dropna()

    return df_training[['gender', 'race_o', 'age_o', 'pf_o_sin', 'pf_o_int', 'pf_o_fun', 'pf_o_amb', 'pf_o_sha', 'sinc_o', 'intel_o', 'fun_o', 'amb_o', 'shar_o', 'like_o', 'prob_o', 'met_o', 'age', 'field_cd', 'race', 'imprace', 'imprelig', 'income', 'date', 'go_out', 'career_c', 'sports', 'tvsports', 'exercise', 'dining', 'museums','match']]

def merge_data(data) -> pd.DataFrame:
    
    df = read_data()
    user_df = pd.DataFrame([data])
    
    merged_data = pd.concat([df, user_df])

    return merged_data

def pca(df) -> pd.DataFrame:


    pca_pf_o_attribute = PCA(n_components=1, random_state=123)
    pca_pf_o_attribute.fit(df[['pf_o_sin', 'pf_o_int', 'pf_o_fun', 'pf_o_amb', 'pf_o_sha']])
    df['dimension_pf'] = pca_pf_o_attribute.transform(df.loc[:, ('pf_o_sin', 'pf_o_int', 'pf_o_fun', 'pf_o_amb', 'pf_o_sha')]).flatten()
    output = df.drop(['pf_o_sin', 'pf_o_int', 'pf_o_fun', 'pf_o_amb', 'pf_o_sha'], axis=1)
    
    return output

def normalisasi(df) -> pd.DataFrame:


    scaler = StandardScaler()
    scaler = scaler.fit(df.drop(["match",'iid','pid'],axis=1))
    df_training_scaled = scaler.transform(df.drop(["match",'iid','pid'],axis=1))
    df_training_scaled = pd.DataFrame(df_training_scaled, columns=df.drop(["match",'iid','pid'],axis=1).columns)
    df_training_scaled_full = pd.concat([df_training_scaled.reset_index(drop=True), df['match'].reset_index(drop=True), df['iid'].reset_index(drop=True), df['pid'].reset_index(drop=True)],axis=1)

    return df_training_scaled_full

def preprocessing(data) -> pd.DataFrame:

    pca_data = pca(data)
    normalisasi_data = normalisasi(pca_data)

    user_data = normalisasi_data[normalisasi_data['pid'] == 99]
    return user_data

@app.route("/")
def index():
    response_json = {
        "output": "API KONEK"
    }

    return json.dumps(response_json)


@app.route("/predict", methods=["POST"])
def predict():
    
    request_json = request.json

    data = request_json.get("data")

    data['pid'] = 99
    data['iid'] = 99

    raw_df = merge_data(data)

    user_df = preprocessing(raw_df).drop(["match",'iid','pid'],axis=1)

    prediction = model.predict([user_df[col] for col in user_df.columns])
    
    prediction_serialize = float(prediction[0][0])

    print(prediction_serialize)

    response_json = {
        "prediction": prediction_serialize
    }

    return json.dumps(response_json)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
