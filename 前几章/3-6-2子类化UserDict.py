import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    # self.data 是 dict 的实例
    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item