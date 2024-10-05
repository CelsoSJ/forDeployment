#!/bin/bash

# Update package list and install system dependencies
apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
