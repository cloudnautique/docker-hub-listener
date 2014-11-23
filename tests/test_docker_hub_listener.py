import subprocess32
import docker_hub_listener

app = docker_hub_listener.app.test_client()


def test_index():
    response = app.get('/')
    assert response.status_code == 200


def test_process_hook_post_no_token():
    # POST method with no token will 404
    response = app.post('/api/v1/webhooks/hub.docker.com/')
    assert response.status_code == 404


def test_process_hook_non_post():
    # Get method 405
    response = app.get('/api/v1/webhooks/hub.docker.com/bad_token')
    assert response.status_code == 405


def test_process_hook_post_bad_token():
    # Post Method with bad token (401)
    response = app.post('/api/v1/webhooks/hub.docker.com/bad_token')
    assert response.status_code == 401


def test_process_hook_with_good_token(mocker):
    # Post with valid URL and token return(200)
    mocker.patch('subprocess32.Popen')
    response = app.post('/api/v1/webhooks/hub.docker.com/good_token')

    assert response.status_code == 200
    subprocess32.Popen.assert_called_once_with(
        ['sudo', 'docker', '-H', 'unix:///var/run/docker.sock', 'pull', 'good_repo'])
