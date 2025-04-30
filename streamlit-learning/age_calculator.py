import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# Set allowable range for DOB input
min_dob = date(1900, 1, 1)
max_dob = date.today()

# Input for Date of Birth
DOB = st.date_input("Enter your Date of Birth", min_value=min_dob, max_value=max_dob)

# Today's date
today = date.today()

# Calculate age in years, months, and days
if DOB:
    age = relativedelta(today, DOB)
    st.write(f"Your age is {age.years} years, {age.months} months, and {age.days} days according to your Birth Date: {DOB}")
