FROM python:3.6
ENV LANG en_US.UTF-8

WORKDIR /usr/src/treasure-map-routing

COPY . /usr/src/treasure-map-routing

RUN python -m unittest test/test_graph.py

CMD python src/pathfinder.py resources/treasure_maps.txt
