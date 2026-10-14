# Import the required libraries
import streamlit as st
import pickle
import pandas as pd


# Create a title for sidebar
st.sidebar.title('Car Price Prediction')

# Create an HTML template to customize the main page title
# Create a div, set background colour, add title, set title colour and align the text
html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""

# Display the HTML template using the markdown method
# Set unsafe_allow_html = True to allow HTML rendering
st.markdown(html_temp, unsafe_allow_html=True)

# Get user inputs from the sidebar
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))  # Select the age of the car
hp=st.sidebar.slider("What is the hp_kw of your car?", 40, 300, step=5)  # Select the horsepower of the car
km=st.sidebar.slider("What is the km of your car", 0,350000, step=1000)  # Select the milage of the car
gearing_type=st.sidebar.radio('Select gear type',('Automatic','Manual','Semi-automatic'))  # Select the gearing type of the car
car_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))  # Select the model of the car

# Create a dictionary from the user inputs
my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gearing_Type':gearing_type,
    "make_model": car_model
    }

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame.from_dict([my_dict])

# Display a header for the car configuration
st.header("The configuration of your car is below")

# Display the DataFrame in a table format
st.table(df)

# Load the saved Random Forest
model=pickle.load(open("rf_model22","rb"))

# Load the saved column transformer
transformer = pickle.load(open('transformer22', 'rb'))

# Transform the DataFrame using the saved transformer
df2 = transformer.transform(df)

# Display a subheader prompting the user to make a prediction
st.subheader("Press predict if configuration is okay")

# Make a prediction when the user clicks the Predict button and display the result as a success message
if st.button("Predict"):
    prediction = model.predict(df2)
    st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))
