def unpack(zipped):
    for unzip in zipped:
        try:
            yield from unzip
        except TypeError:
            yield unzip
