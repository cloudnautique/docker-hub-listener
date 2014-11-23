FROM ubuntu:14.04.1

MAINTAINER Bill Maxwell '<bill@rancher.com>'

VOLUME /app
COPY ./ /app/

RUN /app/scripts/bootstrap
RUN pip install -r /app/requirements.txt

RUN apt-get install -y nginx
COPY ./tools/nginx_docker_hub_listener.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx_docker_hub_listener.conf /etc/nginx/sites-enabled/

RUN useradd -m -G docker,users gunicorn

RUN echo "%docker ALL=NOPASSWD: /usr/bin/docker" >> /etc/sudoers


EXPOSE 80

CMD ["/app/tools/start_server"]
