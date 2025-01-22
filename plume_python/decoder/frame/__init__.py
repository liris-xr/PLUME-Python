import importlib
import pkgutil
from pathlib import Path

def _register_all_decoders():

    path = Path(__file__).parent
    
    modules = pkgutil.iter_modules(path=[path])
    for module in modules:
        importlib.import_module(f"{__name__}.{module.name}")

_register_all_decoders()