import csv
from datetime import datetime

import matplotlib.pyplot as plt

from os import scandir, getcwd
from os.path import abspath


# ---------------- Function to generate a directory of files------------------------------
def dictArchivos(ruta = '.'):
    """Retorna un diccionario archivos de un directorio.
    nombre del archivo como key y ruta como value """
    rutas = {}  # Dictionary
    for arch in scandir(ruta):
        key = arch.name
        value = abspath(arch.path)
        rutas[key] = value
    return rutas
# ---------------- Function to select a file from a list of files------------------------------

def selectFile(indice, archivos):
    """Seleccionamos el archivo de un grupo de archivos
    Retorna filename = nombre del archivo y directFile = Directorio del archivo"""
    for index, key in enumerate(archivos):
        if indice == index:
            filename = key
            directFile = archivos[key]
    return filename, directFile

# --------------- Function to Analize and plot data sets-------------------------------

def plotDataSetTemperature(filename, directory):
    """Ingreso el nombre de archivo y del directorio
    Analizo los datos del directorio
    Retorno el grafico"""
    with open(directory) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            if column_header == 'DATE':
                date = index
            elif column_header == 'TMAX':
                tMax = index
            elif column_header == 'TMIN':
                tMin = index
            elif column_header == 'TAVG':
                tAvg = index

        # Get dates, and high and low temperatures from this file.
        dates, highs, lows, avgs = [], [], [], []
        for row in reader:
            current_date = datetime.strptime(row[date], '%Y-%m-%d')  # convect date information to a datetime object
            # I use a block try/except/else because there are values in blank and appear the following error by console
            # ValueError: invalid literal for int() with base 10: ''
            try:
                avg = float(row[tAvg])  # Agrego temperatura media
                high = float(row[tMax])
                low = float(row[tMin])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)  # Append date
                highs.append(high)  # Append high temperature
                lows.append(low)  # Append low temperature
                avgs.append(avg)  # Append average temperature
    
    # Plot the high and low temperatures and its dates.
    plt.style.use('seaborn')
    fig = plt.subplot()
    ax = plt.subplot()
    ax.plot(dates, highs, c='red', alpha=0.5)  # I pass the dates and the high temperature values to plot()
    ax.plot(dates, lows, c='blue', alpha=0.5)  # alpha controls a color's transparency
    ax.plot(dates, avgs, c='yellow', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

    # Format plot
    title = f"Daily high and low temperatures from \n{filename}"
    plt.title(title, fontsize=20)
    plt.xlabel('Dates', fontsize=10)
    plt.xticks(rotation=30)  # Rotate x ticks 30º
    plt.ylabel("Temperature(ºC)", fontsize=10)
    plt.tick_params(axis='both', which=None, labelsize=10)
    plt.show()

# ----------------------------------------------

# Directory where the files are stored.
directory = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_csv_files/data/data_argentina'

# List and select file that I want it. 
print(f'Se listaran todos los archivos del directorio {directory}')
archivos = dictArchivos(directory)
for index, key in enumerate(archivos):
    print(index, key)
seleccion = int(input('Que archivo quieres? Elige un numero: '))


caso_estudio = selectFile(seleccion, archivos)
print(caso_estudio[0])
plotDataSetTemperature(caso_estudio[0], caso_estudio[1])

