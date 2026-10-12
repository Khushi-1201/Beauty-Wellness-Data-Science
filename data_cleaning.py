import pandas as pd
from pathlib import Path

input_file = Path("salon_appointments_dummy.csv")
output_file = Path("cleaned_salon_appointments.csv")

df = pd.read_csv(input_file)
print("Original shape:", df.shape)
print("Missing values before cleaning:\n", df.isna().sum())
print("Exact duplicate rows:", df.duplicated().sum())
print("Duplicate appointment IDs:", df["appointment_id"].duplicated().sum())

cleaned_df = df.copy()

for column in ["service_name", "customer_id", "staff_member_id"]:
    cleaned_df[column] = cleaned_df[column].astype("string").str.strip()

cleaned_df["appointment_date"] = pd.to_datetime(
    cleaned_df["appointment_date"], format="%d-%m-%Y", errors="coerce"
)
cleaned_df["appointment_time"] = pd.to_datetime(
    cleaned_df["appointment_time"], format="%H:%M", errors="coerce"
).dt.strftime("%H:%M")
cleaned_df["price"] = pd.to_numeric(cleaned_df["price"], errors="coerce")

invalid_prices = cleaned_df["price"].isna() | (cleaned_df["price"] <= 0)

q1 = cleaned_df["price"].quantile(0.25)
q3 = cleaned_df["price"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
potential_outliers = cleaned_df[
    (cleaned_df["price"] < lower_bound) |
    (cleaned_df["price"] > upper_bound)
]

cleaned_df.to_csv(output_file, index=False)
print("Final shape:", cleaned_df.shape)
print("Missing values after conversion:\n", cleaned_df.isna().sum())
print("Invalid prices:", int(invalid_prices.sum()))
print("Potential price outliers:", len(potential_outliers))
print("Saved to:", output_file)
