FROM python:3.9-slim

WORKDIR /code

# Copy the requirements file to the container
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code
COPY . /code

# The default command will run uvicorn, but Celery will override it in the docker-compose file
CMD ["uvicorn", "fastapi.app:app", "--host", "0.0.0.0", "--port", "8000"]
