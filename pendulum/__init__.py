VERSION = (0, 1, 6, 'pre4')

def version():
    return '%s.%s.%s-%s' % VERSION

def get_version():
    return 'Pendulum %s' % version()
