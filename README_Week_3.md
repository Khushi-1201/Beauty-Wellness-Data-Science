# Week 3: Data Cleaning and Preprocessing Pipeline

## Project
Beauty & Wellness Appointment Dataset

## Files
- `Week_3_Data_Cleaning_Report.docx`: detailed assignment report
- `salon_appointments_dummy.csv`: original dataset (synthetic/dummy data)
- `cleaned_salon_appointments.csv`: processed output
- `Week_3_Data_Cleaning.ipynb`: Google Colab notebook, if downloaded separately
- `data_cleaning.py`: Python script version of the cleaning pipeline

## Observed results
- Dataset shape: 100 rows × 7 columns
- Missing values before cleaning: 0
- Exact duplicate rows: 0
- Duplicate appointment IDs: 0
- Invalid prices: 0
- Potential IQR price outliers: 0
- Final dataset shape: 100 rows × 7 columns

## Run
Install dependencies:
```bash
pip install pandas numpy
```
Place the input CSV in the same folder as `data_cleaning.py`, or update the input path. Then run:
```bash
python data_cleaning.py
```

## Notes
This is a small synthetic dataset intended for demonstrating data-cleaning methods. Outliers are flagged for review and are not automatically removed. No real customer trends should be inferred from this sample alone.
