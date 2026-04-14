import pandas as pd

# Example dataset
df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai']
})

# One-Hot Encoding
df_encoded = pd.get_dummies(df, drop_first=True)

print(df_encoded)