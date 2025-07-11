FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY . /code
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["daphne", "c_lettings_site.asgi:application"]
