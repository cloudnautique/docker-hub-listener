### Brain Dead Simple Dockerhub webhook listener for pulling images.

=============

This app is extremely simple and does only one thing, pull repositories when it recieves webhook. Currently, it does not trust the payload contents.

To run:

   ```   
   $ docker build -t <imagename> .
   $docker run -d -v /var/run/docker.sock:/var/run/socker.sock -e "NGINX_SERVER_NAME=<listening address> -e 'DOCKER_HUB_REPOS={"repo_token":"repo_name"}' -p <host_port>:80 <image>
   ```
   

   
