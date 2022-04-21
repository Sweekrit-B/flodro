from audioop import avg
from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# predicting humidity

data = pd.read_csv('/Users/kelvinj/Downloads/sample_data/yearly_monthly_averages.csv')

class Prediction:
    def predict(self):
        df = pd.DataFrame(data, columns=['month', 'avgtempC', 'rainMM'])
        print(df)
        # rainfall_and_temperature = df[['year', 'rainMM']][:5]
        avgtempC = (df['month'], df['avgtempC'], "r-")
        rainMM = (df['month'], df['rainMM'], "b-")
        meanRainMM = df['month'].mean()

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(df['month'], df['rainMM'], label='rainMM', color="blue")
        ax2.plot(df['month'], df['avgtempC'], label='avgtempC', color="#EE1289")

        ax1.set_xlabel('Months') 
        ax1.set_ylabel('rainMM', color='blue')
        ax2.set_ylabel('avgtempC', color="#EE1289")

        plt.grid(True)
        plt.legend()
        plt.show()

Prediction().predict()
        
