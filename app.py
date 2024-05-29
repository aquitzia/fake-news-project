import streamlit as st
import requests

# API Gateway URL format- https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}
# {restapi_id} for API Gateway REST API
# {region} AWS region
# {stage_name} deployment stage (e.g., prod, dev, etc.)
# {resource_path} the endpoint that triggers the Lambda function
API_URL = 'https://ud4rhytiik.execute-api.us-west-1.amazonaws.com/'

if st.button('Test Prediction'):
    response = requests.post(API_URL+'predict', json={'Text':'Test any string.'})
    
    if response.status_code == 200:
        st.write(response.content)
        # label = response.get('label')
        # score = response.get('score')
        # st.write('label:', label, 'score:', score)
    else:
        st.write(f"Failed to trigger AWS Lambda function. Status code: {response.status_code}")

if st.button('Get model info'):
    info = requests.get(API_URL+'info')

    if response.status_code == 200:
        st.write(response.content)
    else:
        st.write(f"Failed to trigger AWS Lambda function. Status code: {response.status_code}")