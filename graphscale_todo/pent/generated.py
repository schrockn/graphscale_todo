from graphscale.pent import Pent


class TodoUserGenerated(Pent):
    @property
    def obj_id(self):
        print(repr(self._data))
        return self._data['obj_id']

    @property
    def name(self):
        return self._data['name']


class TodoItemGenerated(Pent):
    @property
    def obj_id(self):
        return self._data['obj_id']

    @property
    def text(self):
        return self._data['text']


class QueryGenerated:
    pass


class MutationGenerated:
    pass
