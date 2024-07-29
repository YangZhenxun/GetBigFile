from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = [Extension("c_usn_journal",
                sources=["c_usn_journal.pyx"],
                language="c++")]
setup(ext_modules=cythonize(ext, language_level=3))
