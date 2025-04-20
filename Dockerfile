# Stage 1: Install dependencies
FROM python:3.13-slim as builder

WORKDIR /app

# Install FastAPI and other dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --target /app/python --no-cache-dir

# Stage 2: Lambda runtime
FROM public.ecr.aws/lambda/python:3.13

# Copy dependencies first (into /var/task)
COPY --from=builder /app/python ${LAMBDA_TASK_ROOT}

# Then copy only your app files (main.py, etc.)
COPY main.py ${LAMBDA_TASK_ROOT}

# Lambda entrypoint
CMD [ "main.handler" ]
