try:
    from .local import *
except:
    try:
        from .production import *
    except:
        pass
