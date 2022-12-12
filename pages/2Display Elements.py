import streamlit as st
import time

st.set_page_config(page_title="Display Elements", page_icon="📑")

st.markdown("# Display Elements")
st.sidebar.header("Display Elements 📑")


st.header("These are the Display Elements in Streamlit")

with st.expander("**st.write**"):

    st.write("Display text in your webpage")

    st.write("**Code:**")

    st.code("st.write('Hello everyone Im st.write')")

    st.write("**Its output:**")

    st.markdown("st.write('Hello everyone I'm st.write')")

with st.expander("**Title**"):

    st.write("Display string formatted as a Title")

    st.write("**Code:**")

    st.code("st.title('Welcome to my App')")

    st.write("**Its output:**")

    st.title('Welcome to my App')


with st.expander("**Markdown**"):

    st.write("Display string formatted as MarkDown")

    st.write("**Code:**")

    st.code("st.markdown('Hello **ACM**')")

    st.write("**Its output:**")

    st.markdown("Hello **ACM**")

with st.expander("**Header**"):

    st.write("Display text in Header formatting")

    st.write("**Code:**")

    st.code("st.header('I am a Header')")

    st.write("**Its output:**")

    st.header('I am a Header')

with st.expander("**Subheader**"):

    st.write("Display text in Sub-Header formatting")

    st.write("**Code:**")

    st.code("st.subheader('I am a Sub-Header')")

    st.write("**Its output:**")

    st.subheader('I am a Sub-Header')

with st.expander("**Code**"):

    st.write("Display text in a Code Block")

    st.write("**Code:**")

    st.code("st.code('st.slider(\"Enter a value\",0,100)')")

    st.write("**Its output:**")

    st.code("st.slider('Enter a value',0,100)")

with st.expander("**SideBar**"):

    st.write("Display the SideBar widget")

    st.write("**Code:**")

    st.code("btn = st.sidebar.button('Click to celebrate')")

    st.write("**Its output:**")

    button = st.button("Add a button to sidebar")

    if button:
        btn = st.sidebar.button('Here I am!!!')