import imp
import os
import pkgutil
import sys


_cached_namespaces = {}


def _handle(path, namespace):
    importer = pkgutil.get_importer(path)
    if importer is None:
        return
    loader = importer.find_module(namespace)
    if loader is None:
        return
    module = loader.load_module(namespace)
    _cached_namespaces[namespace].append(module.__path__[0])


def declare(namespace):
    if namespace in _cached_namespaces:
        return
    _cached_namespaces[namespace] = []

    extra_path = ""
    if '.' in namespace:
        declare(namespace.rsplit('.', 1)[-2])
        extra_path, _module = namespace.rsplit(".", 1)
        extra_path.replace(".", "/")

    for path in sys.path:
        _handle(os.path.join(path, extra_path), namespace)
    sys.modules[namespace].__path__ = _cached_namespaces[namespace]
