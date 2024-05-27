import streamlit as st
import requests

# API Gateway URL format- https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}
# {restapi_id} for API Gateway REST API
# {region} AWS region
# {stage_name} deployment stage (e.g., prod, dev, etc.)
# {resource_path} the endpoint that triggers the Lambda function
API_URL = ''

if st.button('Get Model Details'):
    response = requests.post(API_URL, json={'Action':'info'})
    
    if response.status_code == 200:
        st.write(response.content)
    else:
        st.write(f"Failed to trigger AWS Lambda function. Status code: {response.status_code}")

# label = response.get('label')
# score = response.get('score')
# st.write('label: ', label, 'score: ', score)