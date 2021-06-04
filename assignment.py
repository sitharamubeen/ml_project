from logging import info
from os import access
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st

import matplotlib
import seaborn as sns 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Dataset of accident death in USA monthly")
df=pd.read_csv('accidents.csv')
df=df.dropna()
new = df["Month"].str.split("-", n = 1, expand = True)
df['month']=new[1]
df['year']=new[0]
df=df.drop(columns=['Month'])
st.table(df.head(10))
st.header("Visualization using seaborn ")
st.subheader("heatmap")
accidents=df.pivot_table(values='Accident_death',index='month',columns='year')
sns.heatmap(accidents)
st.pyplot()
st.subheader("barplot based on year")
sns.barplot(y='Accident_death',x='year',data=df)
st.pyplot()
st.subheader("barplot based on month")
sns.barplot(y='Accident_death',x='month',data=df)
st.pyplot()
st.subheader("mean of accient death in each year")
st.table(df.groupby("year").mean())
st.subheader("Standard deviation of accient death in each year")
st.table(df.groupby("year").std())