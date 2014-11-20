class Repo(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if initial:
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self.__dict__['_data'].get(name, None)

    def __setattr__(self, name, value):
        pass

    def to_dict(self):
        return self._data
