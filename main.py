import streamlit as st
import pandas as pd


def calculate_survival_rate(data, age_min, age_max, pclass):
    age_group = data[(data['Age'] >= age_min) & (data['Age'] <= age_max) & (data['Pclass'] == pclass)]
    if len(age_group) > 0:
        survival_rate = age_group['Survived'].mean() * 100
    else:
        survival_rate = 0
    return survival_rate


data = pd.read_csv('titanic_train.csv').dropna(subset=['Age', 'Survived', 'Pclass'])

st.title("Процент выживших пассажиров Титаника")
p_class = st.selectbox("Выберите класс билета", options=sorted(data["Pclass"].unique()), index=0)

young_survival_rate = calculate_survival_rate(data, 0, 30, p_class)
old_survival_rate = calculate_survival_rate(data, 60, 100, p_class)

survival_data = {
    "Возрастная группа": ["0-30 лет", "60+ лет"],
    "Процент выживших": [young_survival_rate, old_survival_rate]
}
st.subheader(f"Процент выживших пассажиров в классе {p_class}:")
st.table(pd.DataFrame(survival_data))