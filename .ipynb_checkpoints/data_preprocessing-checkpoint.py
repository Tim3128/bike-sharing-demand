import pandas as pd

dico_seasons = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}

def process(df_raw : pd.DataFrame):

    df_data = df_raw.drop('temp', axis=1)

    df_data['datetime'] = pd.to_datetime(df_data["datetime"])
    df_data['hour'] = df_data['datetime'].apply(lambda d: d.hour)

    df_data['season'] = df_data['season'].apply(lambda s: dico_seasons[s])

    df_data.set_index('datetime', inplace=True)

    df_data[['weather', 'season']] = df_data[['weather', 'season']].astype('category')

    df_data = pd.get_dummies(df_data)

    return df_data