### Brain Dead Simple Dockerhub webhook listener for pulling images.

=============

This app is extremely simple and does only one thing, pull docker repos when it recieves webhook. Currently, it does not trust the payload contents.

To run:

```   
$ docker build -t <imagename> .
$docker run -d -v /var/run/docker.sock:/var/run/socker.sock -e "NGINX_SERVER_NAME=<listening address> -e 'DOCKER_HUB_REPOS={"repo_token":"repo_name"}' -p <host_port>:80 <image>
   ```

The DOCKER_HUB_REPOS variable is a json object in the following format:

```
{"token":"org/reponame"}
```

The URLS will be:
http://<listening address>/api/v1/webhooks/hub.docker.com/<token>

You can craft the token however you want. Currently, the app only respects the repo in the key value pair. So if the URL is hit by not docker hub it will not pull random images to your server.