
import csv
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
#Módulos para la regresión lineal
from scipy.stats import linregress

data_list = [["Dia_x", "Casos_y"],
             [1, 0],
             [2, 0],
             [3, 0],
             [4, 0],
             [5, 0],
             [6, 0],
             [7, 1],
             [8, 0],
             [9, 0],
             [10, 3],
             [11, 0],
             [12, 9],
             [13, 0],
             [14, 16],
             [15, 35],
             [16, 45],
             [17, 57],
             [18, 65],
             [19, 102],
             [20, 128],
             [21, 158],
             [22, 210],
             [23, 235]
             ]
with open('covid19_SURAMERICA.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)

#Lee el archivo
df = pd.read_csv('./covid19_SURAMERICA.csv', sep='|', engine='python')
 
#Generamos el gráfico
fig = px.line(df, x = 'Dia_x', y = 'Casos_y', title='Evolución de casos reportados COVID-19 Colombia')

fig.show()

#Modelo predictivo
#Primero leo los datos del dataset
dataframe = pd.read_csv("covid19_SURAMERICA.csv", sep='|', engine='python')
#Leo los datos en cada variable, para este caso, días y casos
x = dataframe.Dia_x
y = dataframe.Casos_y
#Intercepción de la línea de regresión será a partir de los valores en x e y
stats = linregress(x, y)

m = stats.slope #pendiente de la línea de regresión
b = stats.intercept
e = stats.rvalue #coeficiente de correlación
#es = stats.stderr
#rmse = np.sqrt(mean_squared_error(y_predict, y_test))

print("r-value: coeficiente de correlación:",e)
print("r-value: coeficiente de determinación R^2:",e**2)
#print("Error estandar de la estimación:",es)
#print("Intercepción de la línea de regresión:",inter)


#Dibujo la gráfico con los datos y la línea de regresión
plt.figure(figsize=(6,6))
plt.scatter(x, y, marker='x')
plt.plot(x, m * x + b, color="red", linewidth=3)   # I've added a color argument here
# Add x and y lables, and set their font size
plt.xlabel("Días desde el 1 de marzo de 2020", fontsize=15)
plt.ylabel("Personas reportadas con COVID-19", fontsize=15)
#Creo el archivo y lo guardo
plt.savefig("python-reg-lineal.covid19-colombia.png")

#Mido el error


plt.show()
