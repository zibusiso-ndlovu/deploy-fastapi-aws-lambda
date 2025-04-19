FROM python:3.13-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --target /app/python

FROM public.ecr.aws/lambda/python:3.11
COPY --from=builder /app/python ${LAMBDA_TASK_ROOT}
COPY . ${LAMBDA_TASK_ROOT}
CMD [ "main.handler" ]
