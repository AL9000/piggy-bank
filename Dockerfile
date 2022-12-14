FROM python:3.11-slim-buster

# Add user that will be used in the container.
RUN useradd al9000

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "al9000" user
RUN chown al9000:al9000 /app

# Copy the source code of the project into the container.
COPY --chown=al9000:al9000 . .

# Use user "al9000" to run the build commands below and the server itself.
USER al9000

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Run code coverage.
#   3. Show code coverage.
#   4. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   piggybank instance can be started with a simple "docker run" command.
CMD set -xe; python manage.py migrate --noinput; python -m coverage run --source='./savings' manage.py test savings; python -m coverage report; gunicorn piggybank.wsgi:application;
