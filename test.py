import pandas as pd

data = {
    3: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    18: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    22: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    27: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    0: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    37: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'},
    43: {'Latitude': -6.2146, 'Longitude': 106.8451, 'Day': 'Tuesday', 'Date': '5,9,2023', 'Time': '14:41:59'}
}

# Konversi dictionary menjadi dataframe Pandas
df = pd.DataFrame.from_dict(data, orient='index')
df.reset_index(inplace=True)
df.rename(columns={'index': 'id'}, inplace=True)
df.to_csv('nama_file.csv', index=True)
# Menampilkan dataframe
print(df)
