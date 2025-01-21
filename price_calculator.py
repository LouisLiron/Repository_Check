import streamlit as st

def calculate_price(days, hours_per_day):
    rate_per_hour = 80  # Your hourly rate in cedis
    base_price = days * hours_per_day * rate_per_hour
    price_with_negotiation = base_price * 1.30  # Adding a 30% increase for negotiation
    
    # Round to the nearest hundred
    base_price = round(base_price, -2)
    price_with_negotiation = round(price_with_negotiation, -2)
    
    return base_price, price_with_negotiation

# Streamlit app
st.title("Project Price Calculator")

# Input fields
days = st.number_input("Number of days to work on the project:", min_value=1, step=1)
hours_per_day = st.number_input("Number of hours you'd work per day:", min_value=1, step=1)

if st.button("Calculate"):
    base_price, price_with_negotiation = calculate_price(days, hours_per_day)
    st.write(f"Base Price: {base_price} cedis")
    st.write(f"Negotiable Price (with 30% increase): {price_with_negotiation} cedis")
