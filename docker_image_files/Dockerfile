# Use AWS image for AWS Lambda environment
FROM public.ecr.aws/lambda/python:latest

RUN python -m pip install --upgrade pip

# ${LAMBDA_TASK_ROOT} is an environment variable set by AWS Lambda
# to /var/task/, the default working directory.
COPY requirements.txt  .
RUN pip install --upgrade -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy model and tokenizer artifacts to a dir in the Lambda tmp
COPY artifacts /tmp/artifacts

# Copy function code. /var/task/ is read-only.
COPY lambda_function_local.py ${LAMBDA_TASK_ROOT}

# Use CMD to run the handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function_local.lambda_handler" ]