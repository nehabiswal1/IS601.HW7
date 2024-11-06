FROM python:3.9.12-slim
WORKDIR /app
COPY homework7.py /app/
RUN pip install qrcode[pil]
CMD ["python", "homework7.py"]


