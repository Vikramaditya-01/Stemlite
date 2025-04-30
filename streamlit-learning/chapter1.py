import streamlit as st

st.title("Hello World!")
st.subheader("brewed wit Streamlite")
st.text("welcome to your first Interactive Application ")
st.write("choose your favourite programming language")

lan = st.selectbox("choose your favourite programming lanaguage : " ,["C" , "C++" , "JAVA" , "Python" ,"JavaScript"])
st.write(f"You Choose {lan}")
st.success(f"{lan} is Exellence Choices")