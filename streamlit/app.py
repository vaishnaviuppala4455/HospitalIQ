from pathlib import Path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
# ============================================================
# GLOBAL CHART STYLE
# ============================================================


plt.rcParams.update({
    "figure.facecolor": "#0f1117",
    "axes.facecolor": "#171a23",
    "axes.edgecolor": "#303642",
    "axes.labelcolor": "#c9d1d9",
    "axes.titlecolor": "#f2f4f7",
    "xtick.color": "#9aa4b2",
    "ytick.color": "#9aa4b2",
    "text.color": "#f2f4f7",
    "grid.color": "#303642",
    "grid.alpha": 0.45,
    "axes.grid": True,
    "font.size": 10,
    "axes.titlesize": 15,
    "axes.titleweight": "600",
    "axes.labelsize": 10,
    "legend.facecolor": "#171a23",
    "legend.edgecolor": "#303642",
    "legend.labelcolor": "#c9d1d9",
})
# ============================================================
# CHART THEME
# ============================================================

CHART_BG = "#171a23"
CHART_TEXT = "#d8dee9"
CHART_MUTED = "#8f98a8"
CHART_GRID = "#2a303d"

PRIMARY = "#6ea8fe"
SECONDARY = "#8b9bb4"



# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hospital IQ",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DATA LOADING
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "medical_data.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


df = load_data()


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>
        /* -------------------------------------------------------
       CARD INTERACTIONS
    ------------------------------------------------------- */

    .kpi-card,
    .insight-card {
        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease;
    }

    .kpi-card:hover,
    .insight-card:hover {
        transform: translateY(-3px);
        border-color: #6ea8fe;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.20);
    }

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background-color: #0f1117;
        color: #e8eaed;
    }

    .main {
        background-color: #0f1117;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }


    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */
section[data-testid="stSidebar"] {
    background-color: #141820;
    border-right: 1px solid #252c37;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] h2 {
    color: #eef1f5;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.01em;
    margin-bottom: 1.4rem;
}

section[data-testid="stSidebar"] label {
    color: #98a6b8 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}


    /* -------------------------------------------------------
       SELECT BOXES
    ------------------------------------------------------- */

    div[data-baseweb="select"] > div {
        background-color: #10131a;
        border: 1px solid #303644;
        border-radius: 8px;
        transition: border-color 0.2s ease,
                    box-shadow 0.2s ease;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #64748b;
    }/* -------------------------------------------------------
   FILTER SELECT BOXES
------------------------------------------------------- */

div[data-baseweb="select"] > div {
    background-color: #11151d;
    border: 1px solid #303744;
    border-radius: 8px;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease,
        background-color 0.2s ease;
}

/* Hover */
div[data-baseweb="select"] > div:hover {
    background-color: #151a23;
    border-color: #52657d;
}

/* Focus / active */
div[data-baseweb="select"] > div:focus-within {
    border-color: #6ea8fe !important;
    box-shadow: 0 0 0 2px rgba(110, 168, 254, 0.12);
}

/* Selected text */
div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p {
    color: #e5e9ef !important;
}

/* Dropdown text */
div[role="option"] {
    transition:
        background-color 0.15s ease,
        color 0.15s ease;
}

/* Dropdown hover */
div[role="option"]:hover {
    background-color: #202733 !important;
}

/* Dropdown container */
div[data-baseweb="popover"] {
    border: 1px solid #303744;
    border-radius: 8px;
}


    /* -------------------------------------------------------
       PAGE HEADER
    ------------------------------------------------------- */

    .page-title {
        font-size: 2.25rem;
        font-weight: 700;
        letter-spacing: -0.035em;
        color: #f4f6f8;
        margin-bottom: 0.2rem;
    }

    .page-subtitle {
        color: #8f98a8;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }

/* -------------------------------------------------------
   KPI CARDS
------------------------------------------------------- */

div[data-testid="stMetric"] {
    background: #171a23;
    border: 1px solid #2d3542;
    border-radius: 12px;
    padding: 1.15rem 1.25rem;
    min-height: 115px;

    transition:
        transform 0.2s ease,
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    border-color: #52657d;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.18);
}

div[data-testid="stMetricLabel"] {
    color: #8fa4bd !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

div[data-testid="stMetricValue"] {
    color: #f2f4f7 !important;
    font-size: 2rem !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricDelta"] {
    color: #8fa4bd !important;
    font-size: 0.75rem !important;
}

    /* -------------------------------------------------------
       SECTION HEADINGS
    ------------------------------------------------------- */

    .section-title {
        color: #f1f3f5;
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
    }


    /* -------------------------------------------------------
       INSIGHT CARDS
    ------------------------------------------------------- */

    .insight-card {
        background: #171a23;
        border: 1px solid #292f3b;
        border-radius: 10px;
        padding: 1.1rem 1.2rem;
        height: 100%;
        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }

    .insight-card:hover {
        transform: translateY(-2px);
        border-color: #4b5565;
    }

    .insight-title {
        color: #e8eaed;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.45rem;
    }

    .insight-text {
        color: #9aa3b2;
        font-size: 0.82rem;
        line-height: 1.55;
    }


    /* -------------------------------------------------------
       ANALYTICAL NOTE
    ------------------------------------------------------- */

    .note-box {
        background: #141820;
        border: 1px solid #2b313d;
        border-radius: 10px;
        padding: 1.2rem 1.3rem;
        margin-top: 1.5rem;
    }

    .note-title {
        color: #e8eaed;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.55rem;
    }

    .note-text {
        color: #929baa;
        font-size: 0.82rem;
        line-height: 1.65;
    }


    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #626b7b;
        font-size: 0.72rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #242a34;
    }


    /* -------------------------------------------------------
       CHART CONTAINERS
    ------------------------------------------------------- */

    div[data-testid="stImage"] {
        border-radius: 10px;
    }


    /* -------------------------------------------------------
       BUTTONS
    ------------------------------------------------------- */

    button {
        transition:
            transform 0.15s ease,
            opacity 0.15s ease;
    }

    button:hover {
        opacity: 0.92;
    }

    button:active {
        transform: scale(0.98);
    }


    /* -------------------------------------------------------
       REMOVE STREAMLIT DECORATIVE ELEMENTS
    ------------------------------------------------------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background-color: transparent;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "<h2>Patient Filters</h2>",
    unsafe_allow_html=True
)

gender_options = ["All"] + sorted(
    df["Gender"].dropna().unique().tolist()
)

region_options = ["All"] + sorted(
    df["Region"].dropna().unique().tolist()
)

admission_options = ["All"] + sorted(
    df["Admission_Type"].dropna().unique().tolist()
)


selected_gender = st.sidebar.selectbox(
    "Gender",
    gender_options
)

selected_region = st.sidebar.selectbox(
    "Region",
    region_options
)

selected_admission = st.sidebar.selectbox(
    "Admission Type",
    admission_options
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df.copy()

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_admission != "All":
    filtered_df = filtered_df[
        filtered_df["Admission_Type"] == selected_admission
    ]


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    """
    <div class="page-title">
        Hospital IQ
        <span style="
            color:#7d8798;
            font-size:1.15rem;
            font-weight:400;
            letter-spacing:-0.01em;
        ">
            (Healthcare Analytics Dashboard)
        </span>
    </div>

    <div class="page-subtitle">
        Interactive exploration of patient demographics,
        medical conditions, treatment utilisation,
        outcomes, and hospital length of stay.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_patients = len(filtered_df)

improved_patients = (
    filtered_df["Outcome"]
    .eq("Improved")
    .sum()
)

average_age = (
    filtered_df["Age"].mean()
    if total_patients > 0
    else 0
)

average_stay = (
    filtered_df["Length_of_Stay"].mean()
    if total_patients > 0
    else 0
)
# ============================================================
# KPI DISPLAY FUNCTION
# ============================================================

def display_kpi(label, value, suffix=""):

    if isinstance(value, float):
        formatted_value = f"{value:.2f}"
    else:
        formatted_value = f"{value:,}"

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-label">
                {label}
            </div>

            <div class="kpi-value">
                {formatted_value}
                <span class="kpi-unit">
                    {suffix}
                </span>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# ANIMATED KPI NUMBER
# ============================================================

def animated_kpi(label, value, suffix=""):

    if isinstance(value, float):
        target_value = f"{value:.2f}"
    else:
        target_value = f"{value:,}"

    components.html(
        f"""
        <html>
        <head>
            <style>
                * {{
                    box-sizing: border-box;
                }}

                body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                    font-family: Arial, sans-serif;
                }}

                .kpi-card {{
                    height: 115px;
                    padding: 18px 20px;
                    background: #171a23;
                    border: 1px solid #2d3542;
                    border-radius: 12px;

                    transition:
                        transform 0.2s ease,
                        border-color 0.2s ease,
                        box-shadow 0.2s ease;
                }}

                .kpi-card:hover {{
                    transform: translateY(-3px);
                    border-color: #52657d;
                    box-shadow:
                        0 8px 22px rgba(0, 0, 0, 0.18);
                }}

                .kpi-label {{
                    color: #8fa4bd;
                    font-size: 12px;
                    font-weight: 500;
                    margin-bottom: 12px;
                }}

                .kpi-value {{
                    color: #f2f4f7;
                    font-size: 30px;
                    font-weight: 600;
                    line-height: 1;
                    letter-spacing: -0.5px;
                }}

                .kpi-unit {{
                    color: #8fa4bd;
                    font-size: 13px;
                    font-weight: 400;
                    margin-left: 5px;
                }}
            </style>
        </head>

        <body>

            <div class="kpi-card">

                <div class="kpi-label">
                    {label}
                </div>

                <div class="kpi-value">
                    <span id="number">0</span>
                    <span class="kpi-unit">{suffix}</span>
                </div>

            </div>

            <script>

                const target = "{target_value}";
                const numberElement =
                    document.getElementById("number");

                const numericTarget =
                    parseFloat(target.replace(/,/g, ""));

                const hasDecimal =
                    target.includes(".");

                const duration = 900;
                const startTime = performance.now();

                function animate(currentTime) {{

                    const progress = Math.min(
                        (currentTime - startTime) / duration,
                        1
                    );

                    const eased =
                        1 - Math.pow(1 - progress, 3);

                    const current =
                        numericTarget * eased;

                    if (hasDecimal) {{

                        numberElement.textContent =
                            current.toFixed(2);

                    }} else {{

                        numberElement.textContent =
                            Math.floor(current)
                            .toLocaleString();

                    }}

                    if (progress < 1) {{

                        requestAnimationFrame(animate);

                    }} else {{

                        numberElement.textContent =
                            target;

                    }}
                }}

                requestAnimationFrame(animate);

            </script>

        </body>
        </html>
        """,
        height=125,
        scrolling=False
    )
# ============================================================
# KPI CARDS
# ============================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    animated_kpi(
        "Total Patients",
        total_patients
    )

with kpi2:
    animated_kpi(
        "Improved Patients",
        improved_patients
    )

with kpi3:
    animated_kpi(
        "Average Age",
        average_age
    )

with kpi4:
    animated_kpi(
        "Average Length of Stay",
        average_stay,
        "days"
    )
# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "No patients match the selected filters. "
        "Try changing one or more filters."
    )

    st.stop()


# ============================================================
# PATIENT OUTCOMES
# ============================================================

st.markdown(
    '<div class="section-title">Patient Outcomes</div>',
    unsafe_allow_html=True
)

outcome_counts = (
    filtered_df["Outcome"]
    .value_counts()
    .reindex(
        ["Improved", "Stable", "Worsened"],
        fill_value=0
    )
)


fig1, ax1 = plt.subplots(figsize=(10, 4.8))

ax1.bar(
    outcome_counts.index,
    outcome_counts.values,
    width=0.55
)

ax1.set_title(
    "Patient Outcomes",
    fontsize=15,
    pad=15
)

ax1.set_ylabel("Number of Patients")

ax1.grid(
    axis="y",
    alpha=0.15
)

ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

plt.tight_layout()

st.pyplot(
    fig1,
    use_container_width=True
)

plt.close(fig1)


# ============================================================
# TWO-COLUMN ANALYSIS
# ============================================================

left_col, right_col = st.columns(2)


# ============================================================
# PATIENTS BY MEDICAL CONDITION
# ============================================================

with left_col:

    st.markdown(
        '<div class="section-title">Patients by Medical Condition</div>',
        unsafe_allow_html=True
    )

    condition_counts = (
        filtered_df["Medical_Condition"]
        .value_counts()
        .sort_values()
    )

    fig2, ax2 = plt.subplots(
        figsize=(8, 7)
    )

    ax2.barh(
        condition_counts.index,
        condition_counts.values
    )

    ax2.set_xlabel("Number of Patients")
    ax2.set_ylabel("")

    ax2.set_title(
        "Patients by Medical Condition",
        fontsize=14,
        pad=12
    )

    ax2.grid(
        axis="x",
        alpha=0.15
    )

    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig2,
        use_container_width=True
    )

    plt.close(fig2)


# ============================================================
# AVERAGE LENGTH OF STAY BY OUTCOME
# ============================================================

with right_col:

    st.markdown(
        '<div class="section-title">Average Length of Stay</div>',
        unsafe_allow_html=True
    )

    stay_by_outcome = (
        filtered_df
        .groupby("Outcome")["Length_of_Stay"]
        .mean()
        .reindex(
            ["Worsened", "Stable", "Improved"]
        )
    )

    fig3, ax3 = plt.subplots(
        figsize=(8, 7)
    )

    ax3.bar(
        stay_by_outcome.index,
        stay_by_outcome.values,
        width=0.55
    )

    ax3.set_title(
        "Average Length of Stay by Patient Outcome",
        fontsize=14,
        pad=12
    )

    ax3.set_ylabel("Average Stay (days)")

    ax3.grid(
        axis="y",
        alpha=0.15
    )

    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig3,
        use_container_width=True
    )

    plt.close(fig3)


# ============================================================
# AVERAGE LENGTH OF STAY BY MEDICAL CONDITION
# ============================================================

st.markdown(
    '<div class="section-title">Length of Stay by Medical Condition</div>',
    unsafe_allow_html=True
)

los_by_condition = (
    filtered_df
    .groupby("Medical_Condition")["Length_of_Stay"]
    .agg(
        Patient_Count="count",
        Average_Stay="mean"
    )
    .round(2)
    .sort_values(
        "Average_Stay",
        ascending=False
    )
)


fig4, ax4 = plt.subplots(
    figsize=(12, 6)
)

ax4.bar(
    los_by_condition.index,
    los_by_condition["Average_Stay"]
)

ax4.set_title(
    "Average Length of Stay by Medical Condition",
    fontsize=15,
    pad=15
)

ax4.set_ylabel("Average Stay (days)")
ax4.set_xlabel("Medical Condition")

ax4.tick_params(
    axis="x",
    rotation=55
)

ax4.grid(
    axis="y",
    alpha=0.15
)

ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)

plt.tight_layout()

st.pyplot(
    fig4,
    use_container_width=True
)

plt.close(fig4)


# ============================================================
# TREATMENT PATTERNS
# ============================================================

st.markdown(
    '<div class="section-title">Treatment Patterns by Patient Outcome</div>',
    unsafe_allow_html=True
)

treatment_outcome = pd.crosstab(
    filtered_df["Treatment"],
    filtered_df["Outcome"]
)

for outcome in ["Improved", "Stable", "Worsened"]:

    if outcome not in treatment_outcome.columns:
        treatment_outcome[outcome] = 0


treatment_outcome = treatment_outcome[
    ["Improved", "Stable", "Worsened"]
]


# Convert counts to percentages within treatment

treatment_percentage = (
    treatment_outcome
    .div(
        treatment_outcome.sum(axis=1),
        axis=0
    )
    .mul(100)
)


fig5, ax5 = plt.subplots(
    figsize=(14, 6)
)

treatment_percentage.plot(
    kind="bar",
    ax=ax5,
    width=0.78
)

ax5.set_title(
    "Treatment Patterns by Patient Outcome",
    fontsize=15,
    pad=15
)

ax5.set_xlabel("Treatment")
ax5.set_ylabel("Percentage of Patients")

ax5.tick_params(
    axis="x",
    rotation=45
)

ax5.legend(
    title="Outcome"
)

ax5.grid(
    axis="y",
    alpha=0.15
)

ax5.spines["top"].set_visible(False)
ax5.spines["right"].set_visible(False)

plt.tight_layout()

st.pyplot(
    fig5,
    use_container_width=True
)

plt.close(fig5)


# ============================================================
# KEY INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">Key Insights</div>',
    unsafe_allow_html=True
)

# Most common outcome
if not outcome_counts.empty:
    most_common_outcome = outcome_counts.idxmax()
    most_common_outcome_count = int(outcome_counts.max())
else:
    most_common_outcome = "N/A"
    most_common_outcome_count = 0

# Most common medical condition
condition_counts_full = (
    filtered_df["Medical_Condition"]
    .value_counts()
)

if not condition_counts_full.empty:
    highest_condition = condition_counts_full.idxmax()
    highest_condition_count = int(condition_counts_full.max())
else:
    highest_condition = "N/A"
    highest_condition_count = 0

# Highest average stay
if not los_by_condition.empty:
    highest_los_condition = los_by_condition.index[0]
    highest_los = float(
        los_by_condition.iloc[0]["Average_Stay"]
    )
else:
    highest_los_condition = "N/A"
    highest_los = 0


insight1, insight2, insight3 = st.columns(3)


with insight1:
    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-title">Most Common Outcome</div>'
        f'<div class="insight-text">'
        f'{most_common_outcome} was the most frequently observed '
        f'outcome, with {most_common_outcome_count:,} patients '
        f'in the current selection.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with insight2:
    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-title">Highest Patient Count</div>'
        f'<div class="insight-text">'
        f'{highest_condition} had the highest number of patients '
        f'in the current selection, with '
        f'{highest_condition_count:,} recorded patients.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with insight3:
    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-title">Longest Average Stay</div>'
        f'<div class="insight-text">'
        f'{highest_los_condition} had the highest observed '
        f'average length of stay at {highest_los:.2f} days.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )
# ============================================================
# ANALYTICAL NOTE
# ============================================================

st.markdown(
    '<div class="note-box">'
    '<div class="note-title">Analytical Note</div>'
    '<div class="note-text">'
    'This dashboard provides descriptive analysis of the available '
    'patient dataset. The results show observed patterns across '
    'patient characteristics, medical conditions, treatments, '
    'outcomes and hospital length of stay.'
    '<br><br>'
    'Differences between groups describe patterns within this '
    'dataset and should not be interpreted as evidence that a '
    'particular treatment caused a specific patient outcome.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Hospital IQ | Healthcare Analytics Dashboard
        <br>
        Built with Python, Pandas, Matplotlib and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)