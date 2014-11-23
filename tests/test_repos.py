import repo
import json


def get_set_repo():
    value = json.loads(
        '{"good_token": "good_repo", "other_token": "other_repo"}')
    return repo.Repo(value)


def test_repo_init():
    repo0 = repo.Repo()
    assert repo0.to_dict() == {}
    del(repo0)

    repo0 = get_set_repo()
    expected = {'good_token': 'good_repo', 'other_token': 'other_repo'}
    assert repo0.to_dict() == expected


def test_getattr():
    repo = get_set_repo()
    assert repo.good_token == 'good_repo'
    assert repo.bad_repo is None


def test_getitem():
    repo = get_set_repo()
    assert repo['good_token'] == 'good_repo'
    assert repo.bad_repo is None


def test_setattr():
    # Do not allow setting repos post init
    repo = get_set_repo()
    repo.not_real = 'not_working'
    assert repo.not_real is None
