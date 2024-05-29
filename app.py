import streamlit as st
import requests
import json

# API Gateway URL format- https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}
# {restapi_id} for API Gateway REST API
# {region} AWS region
# {stage_name} deployment stage (e.g., prod, dev, etc.)
# {resource_path} the endpoint that triggers the Lambda function
API_URL = 'https://ud4rhytiik.execute-api.us-west-1.amazonaws.com/'

st.title('Fake News Detector')
st.write('Version 0.0.1')

article = st.text_input("Paste a news article here.")

if st.button('Predict'):
        if article == "":
            st.error("Please enter some text, then click Predict.")

        else:
            r = requests.post(API_URL+'predict', json={'Text':article})
            # print(r.headers['Content-Type']) #application/json
            # print('headers:\n', r.headers) #{'Date': 'Wed, 29 May 2024 03:50:21 GMT', 'Content-Type': 'application/json', 'Content-Length': '48', 'Connection': 'keep-alive', 'Apigw-Requestid': 'Yg7eoiIWSK4EJ8Q='}
            # print(r.encoding) #utf-8
            
            if r.status_code == 200:
                pred = r.json()[0]
                label = pred['label']
                score = pred['score']
                st.write('Label:', label)
                st.write(f'Score: {score:14%}')
            else:
                st.write(f"Failed to trigger AWS Lambda function. Status code: {r.status_code}")

if st.button('Get model info'):
    r = requests.post(API_URL+'info')
    
    if r.status_code == 200:
        # st.write(r.content.decode('utf-8'))
        with open("README.md", "r") as f:
            mdf = f.read()
        st.markdown(mdf)
    else:
        st.write(f"Failed to trigger AWS Lambda function. Status code: {r.status_code}")