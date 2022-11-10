FROM python:3.11-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /code folder as a directory where the source code is stored.
WORKDIR /code

# Copy the source code of the project into the container.
COPY . .
