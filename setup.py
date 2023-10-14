"""Install missing modules"""
import pip


def import_or_install(module, package = None):
    """install module if unable to import"""
    if package is None:
        package = module
    try:
        __import__(module)
    except ImportError:
        print("Installing {package}")
        pip.main(['install', package])

import_or_install("infisical")
import_or_install("flask")
import_or_install("pandas")
import_or_install("pandas")
import_or_install("requests")
