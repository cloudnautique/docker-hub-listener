#!/usr/bin/env python2
import os
import json
import logging
import subprocess32

from flask import Flask, request, abort
from repo import Repo

app = Flask(__name__)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("docker_hub_webhook")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def get_repo_config(token=None):
    values = json.loads(os.environ.get('DOCKER_HUB_REPOS', '{}'))
    return Repo(values)


def get_docker_host():
    docker_host = os.environ.get('WEBHOOK_DOCKER_HOST',
                                 'unix:///var/run/docker.sock')
    return docker_host


@app.route('/')
def index():
    return "OK"


@app.route('/api/v1/webhooks/hub.docker.com/<token>', methods=['POST'])
def process_hook(token):
    '''
    Trust nothing from the data payload. The token if it gets out will only
    cause the configured repo to be pulled.
    '''
    if request.method == 'POST':
        repo_config = get_repo_config()
        repo = repo_config[token]

        if repo:
            logger.info('Webhook received for %s', repo)
            subprocess32.Popen(
                ['sudo', 'docker', '-H', get_docker_host(), 'pull', repo])

            return "OK"

        abort(401)
    else:
        abort(405)

if __name__ == '__main__':
    logger.info('Using Repos: %s', get_repo_config().to_dict())
    logger.info('Using DockerHost: %s', get_docker_host())

    app.run(debug=True)
