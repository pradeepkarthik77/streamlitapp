import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Display Elements", page_icon="📑")

st.markdown("# Display Elements")
st.sidebar.header("Display Elements 📑")


st.header("These are the Display Elements in Streamlit:")

st.subheader("DataFrame")

st.write("A Python Dataframe is a editable table-like structure that is used for data-analysis")

st.write("**Code:**")

st.code("st.dataframe(df)")

st.write("**It's Output**")

df = pd.DataFrame(
   np.random.randn(10, 10),
   columns=('C %d' % i for i in range(10)))

st.dataframe(df)  # Same as st.write(df)

st.subheader("Table")

st.write("This differs from st.dataframe in that the table in this case is static: its entire contents are laid out directly on the page.")

st.write("**Code:**")

st.code("st.table(df)")

st.write("**It's Output**")

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)  # Same as st.write(df)
