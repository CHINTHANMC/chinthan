import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("C:/Users/SPTINT-26/Desktop/tested.csv")
print(data)

plt.scatter(data['PassengerId'],data['Pclass'])
plt.show
