FROM python:3.7
ENV LANG en_US.UTF-8

WORKDIR /usr/src/treasure-map-routing
ENV PYTHONPATH /usr/src/treasure-map-routing

COPY . /usr/src/treasure-map-routing

RUN python -m unittest

CMD python src/pathfinder.py resources/treasure_maps.txt
