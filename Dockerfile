FROM python:3.9

WORKDIR /repos/payoneer

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 80 for the Flask app
EXPOSE 80

CMD [ "python3", "counter-service.py" ]
