# pull official base image
FROM python:3.10.4-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variablesч]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# copy entrypoint.sh
COPY amo_connect/entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/amo_connect/entrypoint.sh"]