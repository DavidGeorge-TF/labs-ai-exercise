from importlib import metadata

__version__ = metadata.version(__name__)
PACKAGE_NAME = __name__

__all__ = ["__version__", "PACKAGE_NAME"]
