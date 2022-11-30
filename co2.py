import streamlit as st #web development
import numpy as np # np mean, np random
import pandas as pd  #read csv, df manipulation
import time #to simulate a real time data, time loop
import plotly.express as px #interactive charts


df = pd.read_csv('data/co2_data.csv')

st.set_page_config(
    page_title = 'Real-Time CO2 sensor data',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time CO2 sensor data")

# creating a single-element container.
placeholder = st.empty()

timestamps = df.timestamp
datadf = df.drop("timestamp", axis=1)
rows = len(datadf)

# near real-time / live feed simulation 

for i in range(rows):

    row = datadf.iloc[i].to_numpy()
    row = row.reshape((4,2))
    
    timestamp = timestamps.iloc[i]
    
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="CO2 Average", value=np.average(row))
        kpi2.metric(label="CO2 Minimum", value=row.min())
        kpi3.metric(label="CO2 Maximum", value=row.max())

        # create two columns for charts 

        #fig1 = st.columns(1)
        #with fig1:
        st.markdown(f"### CO2 Levels for {timestamp}")
        fig = px.imshow(row, labels=dict(x="Zone Number", y="Zone"), x=["1", "2"], y=['B', 'D', 'F', 'H'], text_auto=True, aspect="auto")
        st.write(fig)
        st.markdown("### Detailed Data View")
        st.dataframe(datadf.iloc[i])
        time.sleep(1)
    #placeholder.empty()