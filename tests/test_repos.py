import repos
import json

def get_set_repo():
    value = json.loads('{"good_token": "good_repo", "other_token": "other_repo"}')
    return repos.Repo(value)

def test_repo_init():
    repo = repos.Repo()
    assert repo.to_dict() == {}
    del(repo)

    repo = get_set_repo()
    expected = {'good_token':'good_repo', 'other_token':'other_repo'}
    assert repo.to_dict() == expected

def test_getattr():
    repo = get_set_repo()
    assert repo.good_token == 'good_repo'
    assert repo.bad_repo == None

def test_setattr():
    # Do not allow setting repos post init
    repo = get_set_repo()
    repo.not_real = 'not_working'
    assert repo.not_real == None
