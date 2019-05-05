FROM python:3.7-slim
USER root
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
