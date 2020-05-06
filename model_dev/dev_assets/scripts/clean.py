import pandas as pd

df = pd.read_csv("~/git_projects/seattle_housing/data/kc_house_data.csv")

df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

df.to_csv(
    "~/git_projects/seattle_housing/data/seahouse_data.csv.tar.bz2",
    compression='bz2',
    index=False
)