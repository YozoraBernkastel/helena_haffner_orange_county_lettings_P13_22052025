FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY . /code
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "-e", "/code/entrypoint.sh"]

EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "oc_lettings_site.asgi:application"]
