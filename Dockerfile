FROM python:3.11
RUN apt-get update && apt-get install -y
#Install necessary dependencies
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY .. /app/
RUN mkdir -p /app/reports
EXPOSE 8000
CMD ["sh", "start.sh"]
