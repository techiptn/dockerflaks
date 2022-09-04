# Use the linux alpine container image
FROM python:3.9

RUN mkdir /code
WORKDIR /code
ADD . /code/
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Test and checking excute flask app alone
# CMD python run.py

# Run the command to start gunicorn
CMD gunicorn --bind 0.0.0.0:5000 -w 3 run:app