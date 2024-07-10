import time
import streamlit as st
import requests
from random import randrange

# Initialize state (once per app/user session)
if 'first_run' not in st.session_state:
    # API Gateway URL format- https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}
    # {restapi_id} for API Gateway REST API
    # {region} AWS region
    # {stage_name} deployment stage (e.g., prod, dev, etc.)
    # {resource_path} the endpoint that triggers the Lambda function
    st.session_state.API_URL = 'https://ud4rhytiik.execute-api.us-west-1.amazonaws.com/'
    st.session_state.first_run = False


'### Fake News Detector'
'Version 0.0.1'

article = st.text_area("Paste a news article here.*", height=200)

if st.button('Detect'):
        r = None
        if article == "":
            st.error("Please enter some text, then click Detect.")

        else:
            # with st.status("Fetching data from server..."):
            messages = ['Sending the JSON request to Lambda Function',
                        'Tokenizing',
                        'Running real-time inference',
                        'This model is performing complex calculations with 100 million parameters!',
                        'Doing some dishes while I wait',
                        'Waiting for a response',
                        'Almost done...',
                        'Do you know any good jokes?',
                        'AI hasn\'t learned how to tell (funny) jokes yet. <crickets>',
                        ]
            message = messages[randrange(0, len(messages))]
            with st.spinner(message):
                post_start = time.monotonic()
                r = requests.post(st.session_state.API_URL+'predict', json={'Text':article})
                lambda_runtime = time.monotonic() - post_start
 
            if r is not None and r.status_code == 200:
                # print(r.headers['Content-Type']) #application/json
                # print('headers:\n', r.headers) #{'Date': 'Wed, 29 May 2024 03:50:21 GMT', 'Content-Type': 'application/json', 'Content-Length': '48', 'Connection': 'keep-alive', 'Apigw-Requestid': 'Yg7eoiIWSK4EJ8Q='}
                # print(r.encoding) #utf-8
                pred = r.json()[0]
                label = pred['label']
                score = pred['score']
                '**Label:**', label
                f'**Score:** {score:.2%}'
                f"Total: {lambda_runtime:.2f} seconds to send and receive the request from AWS Lambda"
                st.caption('*The model was fine-tuned on a training set of only 5,000 articles (about 10 MB). It also has a limited vocabulary size of 50,000 of the most common words. RoBERTa models have a maximum input size of 512 byte-pair encodings (bpe), which is about 300-400 words. The tokenizer will truncate articles that are too long for the model. RoBERTA has 125 million parameters.\n\nFor comparison, GPT-3 has 175 billion parameters, with a context (maximum input) of 2048 tokens. The model\'s parameters, alone, require 350GB of space, so no single GPU currently has enough memory to load the full model. GPT-4 has 100 trillion parameters!')

            else:
                f"Failed to trigger AWS Lambda function. Status code: {r.status_code}"
                if r is not None:
                    f"Status code: {r.status_code}"

if st.button('Get model info'):
    with open("README.md", "r") as f:
        mdf = f.read()
        mdf
