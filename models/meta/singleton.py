
class Singleton(type):
    """Metaclass ensuring only one instance of the same class exists"""

    """Dictionnary of the singleton instances"""
    __instances = {}

    def __call__(cls, *args, **kwargs):
        """Register a new class into the singleton instances dictionnary"""
        if cls not in cls.__instances:
            print('Creating class ' + cls.__name__)
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
