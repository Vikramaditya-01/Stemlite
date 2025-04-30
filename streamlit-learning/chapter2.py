import streamlit as st

st.title("Chai maker App")

if st.button("Make Chai"):
    st.success("your Cahi is being brewed")


add_mashala = st.checkbox("add mashala")

if add_mashala:
    st.write("Mashala added in chai ")

tea_type = st.radio("pick up your chai base : " , ["milk" , "lemon" , "water" , "Almond Milk"])

st.write(f"Selected Base is {tea_type}")

flavor = st.selectbox("choose your flavour: " , ["Adrak" , "Iletchi" , "kesar" , "Tulsi"])

st.write(f"Selected flavour is {flavor}")

suger = st.slider("suger level(spoon)" , 0,10,3)
st.write(f"suger level is {suger} spoon ")

cups = st.number_input("How many cups of Tea do you want ? " ,min_value=2 , max_value = 20 , step = 2)
st.write(f"You are ordering tea for  {cups} of Tea")

name = st.text_input("Enter your name :")
if name:
    st.write(f"Welcome, {name} ! Your Tea is on the way!")

doo = st.date_input("Enter the date for your order : ")

if doo : 
    st.write(f"your selected date is {doo}")


