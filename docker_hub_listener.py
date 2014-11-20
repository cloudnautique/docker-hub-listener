import os
import json
import logging
from docker import Client

from flask import Flask, request, abort
from repos import Repo

app = Flask(__name__)
logger = logging.getLogger()


def get_repos():
    values = json.loads(os.environ.get('DOCKER_HUB_REPOS', '{}'))
    return Repo(values)


def get_client():
    docker_host = os.enviorn.get('WEBHOOK_DOCKER_HOST',
                                 'unix://var/run/docker.sock')
    return Client(base_url=docker_host)


@app.route('/')
def index():
    return "OK"


@app.route('/api/v1/webhooks/hub.docker.com/<token>', methods=['POST'])
def process_hook(token):
    if request.method == 'POST':

        repo_dict = get_repos()
        repo = getattr(repo_dict, token, None)

        if repo:
            docker_client = get_client()
            docker_client.pull(repo)
            return "OK"

        abort(401)
    else:
        abort(405)

if __name__ == '__main__':
    app.run(debug=True)
