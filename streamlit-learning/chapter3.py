import streamlit as st

st.title("Chai test column")

col1,col2 = st.columns(2)

with col1:
    st.header("Mashala Cahi")
    st.image("https://goqii.com/blog/wp-content/uploads/shutterstock_1024718095-1024x682.jpg", width=250)
    vote1 = st.button("Vote for mashala Cahi")

with col2:
    st.header("Adrak Cahi")
    st.image("https://shorturl.at/m2DlR", width=250)
    vote2 = st.button("Vote for Adrak Cahi")

if vote1:
    st.success('Thanks For Voting Masala cahi')
elif vote2:
    st.success("Thanks For Voting Adrak cahi")

name = st.sidebar.text_input("Enter Your Name")
flavor = st.sidebar.selectbox("Choose a Cahi : " ,["Adrak" , "Iletchi" , "kesar" , "Tulsi"])
if name:
    st.write(f"Welcome, {name} ! Your {flavor} Cahi is Ready")

with st.expander("show Cahi making instructions"):
    st.write("""
     1. Boil water
     2. add spices and milk
     3. ready to Go. serve it.
""")