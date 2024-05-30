import streamlit as st
import requests
from random import randrange

# API Gateway URL format- https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}
# {restapi_id} for API Gateway REST API
# {region} AWS region
# {stage_name} deployment stage (e.g., prod, dev, etc.)
# {resource_path} the endpoint that triggers the Lambda function
API_URL = 'https://ud4rhytiik.execute-api.us-west-1.amazonaws.com/'



'### Fake News Detector'
'Version 0.0.1'

article = st.text_area("Paste a news article here.*", height=200)

if st.button('Detect'):
        r = None
        if article == "":
            st.error("Please enter some text, then click Detect.")

        else:
            # with st.status("Fetching data from server..."):
            messages = ['Sending the JSON request to Lambda Function', 'Pulling a Docker image', 'Probably still pulling the Docker image', 'Tokenizing', 'Running real-time inference', 'This model is performing complex calculations with 100 million parameters!', 'Doing some dishes while I wait', 'Waiting for a response', 'Does anyone feel like we\'re getting ghosted?', 'Almost done...', 'Does you know any good jokes?', 'AI hasn\'t learned how to tell (funny) jokes yet. <crickets>', 'Really almost done.', 'Almost really done.']
            message = messages[randrange(0, len(messages))]
            with st.spinner(message):
                r = requests.post(API_URL+'predict', json={'Text':article})
            # print(r.headers['Content-Type']) #application/json
            # print('headers:\n', r.headers) #{'Date': 'Wed, 29 May 2024 03:50:21 GMT', 'Content-Type': 'application/json', 'Content-Length': '48', 'Connection': 'keep-alive', 'Apigw-Requestid': 'Yg7eoiIWSK4EJ8Q='}
            # print(r.encoding) #utf-8
 
            if r.status_code == 200:
                pred = r.json()[0]
                st.balloons()
                label = pred['label']
                score = pred['score']
                '**Label:**', label
                f'**Score:** {score:14%}'
                st.caption('*The model was fine-tuned on a training set of only 5,000 articles (about 10 MB). It also has a limited vocabulary size of 50,000 of the most common words. RoBERTa models have a maximum input size of 512 byte-pair encodings (bpe), which is about 300-400 words. The tokenizer will truncate articles that are too long for the model.\n\nFor comparison, GPT 3 has 175 billion parameters, with a context of 2048 tokens. The model\'s parameters, alone, require 350GB of space, so no single GPU currently has enough memory to load the full model. GPT-4 has 100 trillion parameters!')

            else:
                f"Failed to trigger AWS Lambda function. Status code: {r.status_code}"

if st.button('Get model info'):
    with st.spinner("Waiting for server response..."):
        r = requests.post(API_URL+'info')
    
    if r.status_code == 200:
        # st.write(r.content.decode('utf-8'))
        with open("README.md", "r") as f:
            mdf = f.read()
        mdf
    else:
        f"Failed to trigger AWS Lambda function. Status code: {r.status_code}"