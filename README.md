# Hospital IQ

## Healthcare Analytics Dashboard

Hospital IQ is an interactive healthcare analytics dashboard built with Python, Pandas, Matplotlib and Streamlit.

The dashboard provides a clear view of patient demographics, medical conditions, treatment utilisation, patient outcomes and hospital length of stay.

---

## Project Overview

Healthcare datasets can contain large amounts of patient information that are difficult to interpret from raw tables alone.

Hospital IQ transforms patient-level data into an interactive analytical dashboard that allows users to:

- Explore patient demographics
- Filter patients by gender, region and admission type
- Analyse patient outcomes
- Compare medical conditions by patient count
- Examine average hospital length of stay
- Explore treatment utilisation
- Identify key patterns within the dataset

The dashboard is designed to support descriptive healthcare analytics and data-driven exploration.

---

## Key Features

### Interactive Patient Filters

Users can dynamically filter the dashboard by:

- Gender
- Region
- Admission Type

All visualisations and KPI values update according to the selected filters.

### KPI Dashboard

The dashboard displays four key metrics:

- Total Patients
- Improved Patients
- Average Age
- Average Length of Stay

### Patient Outcomes

A bar chart compares the number of patients across:

- Improved
- Stable
- Worsened

### Medical Condition Analysis

The dashboard compares patient counts across different medical conditions.

### Hospital Length of Stay

Average length of stay is analysed across:

- Patient outcomes
- Medical conditions

### Treatment Analysis

Treatment utilisation is visualised across multiple treatment categories.

### Key Insights

The dashboard automatically identifies:

- Most common patient outcome
- Medical condition with the highest patient count
- Medical condition with the longest average hospital stay

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualisation |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Exploratory data analysis |
| Power BI | Additional business intelligence visualisation |

---

## Project Structure

```text
HospitalIQ/
│
├── data/
│   ├── processed/
│   └── raw/
│       └── medical_data.csv
│
├── images/
│
├── models/
│
├── notebooks/
│   └── hospital_iq_analysis.ipynb
│
├── powerbi/
│   └── HospitalIQ_Healthcare_Analytics.pbix
│
├── streamlit/
│   └── app.py
│
├── README.md
├── requirements.txt
└── .gitignore
Author

Vaishnavi Krishna Priya Uppala

Master of Data Science & Artificial Intelligence
University of Newcastle, Australia