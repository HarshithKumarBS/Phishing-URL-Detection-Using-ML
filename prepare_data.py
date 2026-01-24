import pandas as pd
from feature_extraction import extract_features

df = pd.read_csv("data/urls.csv")

features = df['url'].apply(lambda x: pd.Series(extract_features(x)))
final_df = pd.concat([features, df['label']], axis=1)

final_df.to_csv("data/processed_urls.csv", index=False)

print("Processed dataset created successfully ✅")
