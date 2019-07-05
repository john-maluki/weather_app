FROM python:3.7-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /dock

# Copy files
COPY . /dock

# Copy Pipfile
# COPY Pipfile /weather_app

# Install dependencies
RUN easy_install -U pip
RUN pip install --upgrade setuptools
RUN pip install virtualenv
RUN python -m venv myenv
Run . myenv/bin/activate 
RUN pip install -r requirements.txt


