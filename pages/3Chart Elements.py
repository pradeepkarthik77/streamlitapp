import streamlit as st
import pandas as pd
import numpy as np
import time
st.set_page_config(page_title="Chart Elements", page_icon="📑")

st.markdown("# Chart Elements")
st.sidebar.header("Display Elements 📑")

st.header("These are the Chart Elements in Streamlit:")

st.subheader("Line Chart")

st.write("Used to Draw a Line Chart of a Data Source")

st.write("**Code**")

st.code("line_chart = st.line_chart(df)")

st.write("**It's Output:**")

progress_bar = st.progress(0)
status_text = st.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.01)

progress_bar.empty()


st.button("Run me again!")

st.subheader("Bar Chart")

st.write("Used to Draw a Bar Chart of a Data Source")

st.write("**Code**")

st.code("bar_chart = st.bar_chart(df)")

st.write("**It's Output:**")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.subheader("Map Chart")

st.write("Used to Draw a Map Chart of a Data Source")

st.write("**Code**")

st.code("map_chart = st.bar_chart(df)")

st.write("**It's Output:**")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [11.016, 76.9558],
    columns=['lat', 'lon'])

st.map(df)