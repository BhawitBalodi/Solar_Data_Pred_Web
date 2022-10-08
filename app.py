# from sys import float_repr_style
from tkinter.ttk import Style
from turtle import color
import tensorflow as tf
import numpy as np
from tensorflow import keras
from flask import *
app = Flask(__name__)

model = tf.keras.models.load_model('NeuralN_try8.h5')


@app.route('/')
def home():
    #result =''
    return render_template('ekor.html')



@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Air_Temp = request.form.get('Air_Temp')
    Wind_speed = request.form.get('Wind_speed')
    Pannel_temp = request.form.get('Pannel_temp')
    Array_Voltage = request.form.get('Array_Voltage')
    Array_Current = request.form.get('Array_Current')
    Solar_Radiation = request.form.get('Solar_Radiation')
    model_input = tf.strings.to_number([Air_Temp,Wind_speed, Pannel_temp,Array_Voltage,Array_Current,Solar_Radiation])
    model_input = tf.expand_dims(model_input, axis=0)
    # model_input = tf.expand_dims(model_input, axis=1)
    result = model.predict(model_input)
    return render_template('ekor.html',prediction_text = "The Power Generated is: {} Watt".format(result))


if __name__ == "__main__":
    app.run(debug=True)
