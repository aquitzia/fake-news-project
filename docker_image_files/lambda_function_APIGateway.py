# import mlflow
# import json

MY_TRACKING_SERVER= "http://ec2-54-241-146-233.us-west-1.compute.amazonaws.com:5000"
MY_REGISTERED_MODEL = "fake-news-binary-classification"
MY_ALIAS = "best"

PREDICT_PATH = '/predict'    #this line is lambda-specific
RETRAIN_PATH = '/retrain'    #this line is lambda-specific

def predict(articles):
    mlflow.set_tracking_uri(MY_TRACKING_SERVER)
    model = mlflow.pyfunc.load_model(f"models:/{MY_REGISTERED_MODEL}@{MY_ALIAS}")
    return model.predict(articles)

def lambda_handler(event, context):
    print(event)

    if event['rawPath'] == PREDICT_PATH:
        decodedEvent = json.loads(event['body'])
        articles = decodedEvent['text']
        results = predict(articles)
        print('Model output:', results)
        return results

    elif event['rawPath'] == RETRAIN_PATH:
        # re_train()
        return "model retrained"

    else:
        return "Please provide a valid parameter"
