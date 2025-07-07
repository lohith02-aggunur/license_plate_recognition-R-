#!/bin/bash
apt-get update
apt-get install -y tesseract-ocr
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:$PORT
