# Handle missing values
df = df.fillna(df.median(numeric_only=True))

# Drop unnecessary columns (if any)
# df = df.drop(['column_name'], axis=1)
