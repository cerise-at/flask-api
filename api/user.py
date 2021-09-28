class User():
    all = []

    def __init__(self, data):
        self._username = data['username']
        self._age = data['age']
        self._height = data['height']
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def username(self):
        return self._username

    @property
    def description(self):
        return self._age

    @property
    def height(self):
        return self._height

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]
