class Musician:

    def __repr__(self):
        if isinstance(self, Guitarist):
            return f"Guitarist instance. Name = {self.name}"
        elif isinstance(self, Drummer):
            return f"Drummer instance. Name = {self.name}"
        elif isinstance(self, Bassist):
            return f"Bassist instance. Name = {self.name}"
        else:
            return "Unknown instance"


class Band(Musician):
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    @staticmethod
    def get_instrument():
        return 'guitar'

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = 'bass'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'


    @staticmethod
    def get_instrument():
        return 'bass'

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = 'drums'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    @staticmethod
    def get_instrument():
        return 'drums'

    @staticmethod
    def play_solo():
        return "rattle boom crash"


if __name__ == '__main__':
    Guitarist(),
    Bassist("Krist Novoselic"),
    Drummer("Dave Grohl"),
    joan = Guitarist('joan')
    sheila = Drummer('sheila')
    meshell = Bassist('meshell')
    nirvana = Band('nirvana')
    jimi = Guitarist('jimi')
    jimi.get_instrument('jimi')
    print(joan.__str__())
    print(joan.__repr__())

