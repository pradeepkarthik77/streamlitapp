import streamlit as st
import time

st.set_page_config(page_title="Input Widgets", page_icon="📑")

st.markdown("# Input Widgets")
st.sidebar.header("Input Widgets 📑")

st.header("These are the Input Widgets in Streamlit")

with st.expander("**Button**"):

    st.write("Display a Button Widget")

    st.write("**Code:**")

    st.code("st.button('Click Me!')")

    st.write("**Its output:**")

    if st.button("Click Me!"):
        st.balloons()
    else:
        pass

with st.expander("**CheckBox**"):

    st.write("Display a CheckBox widget")

    st.write("**Code:**")

    st.code("st.checkbox('Click here!')")

    st.write("**Its output:**")

    progress_bar = st.empty()

    if st.checkbox('Click here!'):
        progress_bar = st.progress(0)

        for i in range(11):
            progress_bar.progress(i*10)
            time.sleep(0.3)
        
        progress_bar.empty()
        st.write("Thank you for clicking me!!!")


with st.expander("**Radio Buttons**"):

    st.write("Display Radio Button Widget")

    st.write("**Code:**")

    st.code("genre = st.radio('Which OS Do you like?',('Windows', 'Linux', 'macOS'))")

    st.write("**Its output:**")

    genre = st.radio('Which OS Do you like?',('Windows', 'Linux', 'macOS'))

with st.expander("**SelectBox**"):

    st.write("Display Select Widget")

    st.write("**Code:**")

    st.code("value = st.selectbox('Choose Your Favorite:',['Pizza🍕','Burger🍔','Sandwich🥪'])")

    st.write("**Its output:**")

    value = st.selectbox('Choose Your Favorite:',['Pizza🍕','Burger🍔','Sandwich🥪'])

with st.expander("**Multi-Select**"):

    st.write("Display Multi-Select Widget")

    st.write("**Code:**")

    st.code("options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])")

    st.write("**Its output:**")

    options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])

    st.write("You selected: ",",".join(options))

with st.expander("**Slider**"):

    st.write("Display Slider Widget")

    st.write("**Code:**")

    st.code("temperature = st.slider('Choose the temperature value:',0,100,25)")

    st.write("**Its output:**")

    temperature = st.slider('Choose the temperature value:',0,100,25)

    st.metric("Temperature", f"{temperature} °C", f"{temperature-25} °C")

with st.expander("**Text-Input**"):

    st.write("Display Text Input Box")

    st.write("**Code:**")

    st.code("name=st.text_input('Enter your name:')")

    st.write("**Its output:**")

    name = ""

    name=st.text_input('Enter your name:')

    if name!="":
        st.write(f"Thank you: {name}")
