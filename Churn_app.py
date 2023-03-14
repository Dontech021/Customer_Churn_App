import os
import sys
import subprocess
import streamlit as st
name = 'main'
# Change the current working directory to the desired location
os.chdir('/home/appuser/.local/lib/python3.9/site-packages')

# Define your Streamlit app code
def main():
    
    import streamlit as st
    import pandas as pd
    import gzip
    import dill
    import numpy as np

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


    with gzip.open('churn_model.dill.gz', 'rb') as f:
        model =dill.load(f)

    with gzip.open('rescale.dill.gz', 'rb') as f:
        scale =dill.load(f)

    st.subheader('Predicted Parameters')
    st.write(df)



    u_value=scale.transform(df)
    pred= model.predict(u_value)
    pred_prob= model.predict_proba(u_value)

    st.subheader('Probability Display')
    st.write(pd.DataFrame({'won\'t churn':pred_prob[0][0],'churn':pred_prob[0][1]},index=['probability']))

    classes={0:'won\'t churn',1:'churn'}
    st.subheader('Predicted Action')
    st.write('**{}**'.format(classes[pred[0]]))
    
    st.title('My Streamlit App')
    # Add your Streamlit app code here

# Run your Streamlit app
if name == 'main':
    main()


