FROM python:3.8
RUN apt-get update && apt-get upgrade
RUN apt-get install -y supervisor nginx gdal-bin python3-gdal

CMD supervisord
ENV DJANGO_SETTINGS_MODULE=config.settings.base

WORKDIR /app
COPY requirements.txt /app/requirements/
COPY ci/rootfs /
RUN pip install -r requirements/base.txt

COPY . /app
RUN ./manage.py collectstatic --settings config.settings.base --no-input
