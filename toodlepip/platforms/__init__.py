from .python import PythonBuilder
from .default import DefaultBuilder


builders = {
    None: DefaultBuilder,
    "python": PythonBuilder,
}
