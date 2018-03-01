from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext


ext_modules = cythonize('pure_cython3.pyx')

setup(
    name='types cython',
    cmdclass={'buile_ext': build_ext},
    ext_modules=ext_modules
)