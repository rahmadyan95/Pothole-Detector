import pandas as pd
import detect

def save_csv(data) :
    
    data = detect.detect()
    df = pd.DataFrame.from_dict(data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)
    df.to_csv('nama_file.csv', index=True)


