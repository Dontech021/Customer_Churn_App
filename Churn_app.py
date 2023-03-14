subprocess.call(['pip', 'install', '-r', 'requirement.txt'])
subprocess.call(['pip', 'show', 'dill')
import dill
import streamlit as st
import pandas as pd

st.write("""
# Churn Prediction App
choose your parameters from the sidebar and know if customer will **churn**
""")


st.sidebar.header('User Input Parameters ')

def user_input_features():
    age =st.sidebar.slider('Age of customer',5,200,50)
    Total_Purchase =st.sidebar.slider('Total_Purchase of customer',0,20000,10000)
    Account_Manager =st.sidebar.slider('Account_Manager of customer',0,1,0)
    Years =st.sidebar.slider('Years of customer',0,15,5)
    Num_Sites =st.sidebar.slider('Num_Sites of customer',1,20,8)

    u_data={'age':age,
            'Total_Purchase':Total_Purchase,
            'Account_Manager':Account_Manager,
            'Years':Years,
            'Num_Sites':Num_Sites
            }
    feature=pd.DataFrame(u_data,index=['valus'])
    return feature

df=user_input_features()

