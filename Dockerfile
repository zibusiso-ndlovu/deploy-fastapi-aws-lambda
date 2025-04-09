FROM public.ecr.aws/lambda/python:3.11
# Copy function code
COPY . ${LAMBDA_TASK_ROOT}
# Install the function's dependencies using file requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" -U --no-cache-dir
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]


aws-vault exec zibusiso -- \
    aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin 851725207187.dkr.ecr.us-east-1.amazonaws.com

    851725207187.dkr.ecr.us-east-1.amazonaws.com/lambda_code/fastapi_lambda