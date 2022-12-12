import streamlit as st
import time

st.set_page_config(page_title="Plotting Demo", page_icon="✔")

st.markdown("# Installation")
st.sidebar.header("Installation ✔")

install_type = st.selectbox("Select your Operating System",["Windows","macOS/Linux"])

if install_type == "macOS/Linux":

    st.subheader("Installation in macOS/Linux")

    st.write("Open your Terminal")

    st.write("Type the following command in the CLI")

    st.code("pip3 install streamlit")

    st.write("To run your file type the following command:")

    st.code("streamlit run filename.py")

    st.write("or else you can use:")

    st.code("python -m streamlit run your_script.py")
    

else:
    st.subheader("Installation in Windows")

    st.write("Install the anaconda enviroment")

    st.write("Then Open the root anaconda environment and click 'Open Terminal'")

    st.write("Type the following command in the CLI")

    st.code("pip3 install streamlit")

    st.write("To run your file type the following command:")

    st.code("streamlit run filename.py")

    st.write("or else you can use:")

    st.code("python -m streamlit run your_script.py")