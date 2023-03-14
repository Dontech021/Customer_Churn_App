import os
import streamlit as st
name ='main'

# Change the current working directory to the desired location
os.chdir('/home/appuser/.local/lib/python3.9/site-packages')

# Define your Streamlit app code
def main():

    import subprocess
    import streamlit as st
    import dill
    import pandas as pd
    subprocess.call(['pip', 'install', 'joblib'])
    subprocess.call(['pip', 'list'])

   

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
    st.title('Churn App')
    # Add your Streamlit app code here

# Run your Streamlit app
if name == 'main':
    main()
