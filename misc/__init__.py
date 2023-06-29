def _ConfigAttr(*args, **kwargs):
    for arg in args:
        arg.config(**kwargs)
