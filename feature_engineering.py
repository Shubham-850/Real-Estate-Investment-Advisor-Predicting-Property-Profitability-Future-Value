def create_features(df):
    df = df.copy()

    # Price per sqft
    df["Price_per_SqFt"] = (df["Price_in_Lakhs"] * 100000) / df["Size_in_SqFt"]

    # Property Age
    df["Age_of_Property"] = 2026 - df["Year_Built"]

    # Classification target
    median_price = df["Price_in_Lakhs"].median()
    df["Good_Investment"] = (df["Price_in_Lakhs"] < median_price).astype(int)

    return df