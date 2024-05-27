# Use official image for AWS Lambda environment
FROM public.ecr.aws/lambda/python:latest

# Install dependencies using requirements.txt from your project folder.
COPY requirements.txt  .
RUN python -m pip install --upgrade pip
# RUN  yum install gcc -y

# ${LAMBDA_TASK_ROOT} is an environment variable set by AWS Lambda
# to the /var/task directory, which is the default working directory.

# RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
# Copy model and tokenizer artifacts to a dir in the Lambda tmp
COPY artifacts /tmp/artifacts
RUN pip install --upgrade -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY lambda_function_local.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function_local.lambda_handler" ]
