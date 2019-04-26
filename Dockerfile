FROM python:3.6
ENV LANG en_US.UTF-8

WORKDIR /usr/src/treasure-map-routing

ADD requirements.txt /usr/src/treasure-map-routing/requirements.txt

RUN pip install -r requirements.txt

COPY src /usr/src/treasure-map-routing/src

CMD python  src/pathfinder.py resources/treasure_maps.txt
