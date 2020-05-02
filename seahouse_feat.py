import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='whitegrid')

df = pd.read_csv("/Users/brien/git_projects/seattle_housing/kc_house_data.csv")

# print(df.dtypes)

# this results in 0 null values for the entire df
# print(df.isna().sum())

# converting the date to the datetime format instead of an object
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

# price/sqft metric
df['price_sqft'] = df['price'] / df['sqft_living']

# price is lognormal, so normalizing for predictions
df['price_norm'] = np.log(df['price'])

# comparing house size to 15 closest homes average sqft_living and normalizing around 0
df['rel_size15'] = (df['sqft_living'] / df['sqft_living15'])

zip_avg = df.groupby('zipcode')['sqft_living'].aggregate(np.mean)
zip_avg = pd.DataFrame(zip_avg)
df = df.join(zip_avg, on='zipcode', how='outer', rsuffix='_zip_avg')

# comparing house size to average house size within the zip code and normalizing around 0
df['rel_sizezip'] = (df['sqft_living'] / df['sqft_living_zip_avg'])

# print(df.columns)

# df['yard_sqft'] =
# plt.hist(df['sqft_living'], bins=50, label='living space')
# plt.hist(df['sqft_living15'], bins=50, label='neighbors living space')
plt.hist(df['rel_size15'], bins=50, alpha=0.5, label='living space relative to neighbors')
plt.hist(df['rel_sizezip'], bins=50, alpha=0.5, label='living space relative to zipcode')
plt.legend()
plt.show()

# plt.show()
# df_date = df.groupby('date')['price_sqft'].aggregate(np.mean)
#
# plt.plot(
#     df_date.index,
#     df_date.values
# )
# plt.show()
