import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
colors = sns.color_palette("husl", 4)
sns.set(style="dark")

def create_byweathersit_df(df, isweathersitint):
    byweathersit_df = hour_df.groupby(by="weathersit")['instant'].nunique().reset_index()
    byweathersit_df.rename(columns={
        "instant": "customer_count"
    }, inplace=True)

    plt.figure(figsize=(10, 5))

    sns.barplot(
        y="customer_count",
        x="weathersit",
        data=byweathersit_df.sort_values(by="customer_count", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by weathersit", loc="center", fontsize=15)
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunny', 'Clody', 'Foggy', 'Cold', 'Snowy', 'Stormy', 'Rainy'])
    plt.ylabel('jumlah')
    plt.xlabel('cuaca')
    plt.tick_params(axis='x', labelsize=12)
    plt.show()

    return byweathersit_df

def create_byweekday_df(df, isweekdaybyint):
    byweekday_df = df.groupby(by="weekday")['instant'].nunique().reset_index()
    byweekday_df.rename(columns={
        "instant": "customer_count"
    }, inplace=True)

    plt.figure(figsize=(10, 5))

    sns.barplot(
    y="customer_count",
    x="weekday",
    data=byweekday_df.sort_values(by="customer_count", ascending=False),
    palette=colors
    )
    plt.title("Number of Customer by weekday", loc="center", fontsize=15)
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    plt.ylabel('jumlah')
    plt.xlabel('day')
    plt.tick_params(axis='x', labelsize=12)
    plt.show()
    
    return byweekday_df

# Load datasets
hour_df = pd.read_csv("https://raw.githubusercontent.com/Nindakartika13/ML-24-Ninda-Kartika-Putri./16bd46235f159daf50719ee0e67ecd5c5630f830/Dashboard/hour.csv")
# Sort values and convert date column
column = "dteday"
hour_df.sort_values(by=column, inplace=True)
hour_df.reset_index(drop=True, inplace=True)

hour_df[column] = pd.to_datetime(hour_df[column])

# Get date range
min_date = hour_df[column].min()
max_date = hour_df[column].max()

with st.sidebar:
    st.image("https://raw.githubusercontent.com/Nindakartika13/ML-24-Ninda-Kartika-Putri./4b699e7715cc31fdd9ba529e3e230d51aab044d2/Dashboard/model.jpg")

    # Date input for selecting time range
    start_date, end_date = st.date_input(label="Time", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    
# Convert start_date and end_date to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataframes by selected date range
main_df = hour_df[(hour_df[column] >= start_date) & (hour_df[column] <= end_date)]

# Create dataframes for visualizations
byweathersit_df = create_byweathersit_df(main_df, 0)
byweekday_df = create_byweekday_df(main_df, 0)

# Dashboard content
st.header("Bikes")

col1, col2 = st.columns(2)

# Barplot for time of day analysis
st.subheader("Number of Customer by Weather")
fig3 = plt.figure(figsize=(10,5))
sns.barplot(
    y="customer_count",
    x="weathersit",
    data=byweathersit_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)
plt.title("Number of Customer by weathersit", loc="center", fontsize=15)
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunny', 'Clody', 'Foggy', 'Cold', 'Snowy', 'Stormy', 'Rainy'])
plt.ylabel('jumlah')
plt.xlabel('cuaca')
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig3)

st.subheader("Number of Customer by Weekday")
fig1 = plt.figure(figsize=(10,5))
sns.barplot(
    y="customer_count",
    x="weekday",
    data=byweekday_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)
plt.title("Number of Customer by weekday", loc="center", fontsize=15)
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
plt.ylabel('jumlah')
plt.xlabel('day')
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig1)