import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='whitegrid')

df = pd.read_csv("~/git_projects/seattle_housing/data/seahouse_data.csv.tar.bz2")

df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

# price/sqft metric
df['price_sqft'] = df['price'] / df['sqft_living']

# price is lognormal, so normalizing for predictions
df['price_norm'] = np.log(df['price'])

# comparing house size to 15 closest homes average sqft_living
df['rel_size15'] = (df['sqft_living'] / df['sqft_living15'])

# looking at average house size within each zip code and comparing to each home
zip_avg = df.groupby('zipcode')['sqft_living'].aggregate(np.mean)
zip_avg = pd.DataFrame(zip_avg)
df = df.join(zip_avg, on='zipcode', how='outer', rsuffix='_zip_avg')

df['rel_sizezip'] = (df['sqft_living'] / df['sqft_living_zip_avg'])

df.loc[:, 'is_renovated'] = 0
df.loc[df['yr_renovated'] != 0, 'is_renovated'] = 1

# calculating yard size using sqft logic
mask = (df['floors'] == 1)
df['yard_size'] = df.loc[mask, 'sqft_lot'] - df.loc[mask, 'sqft_above']