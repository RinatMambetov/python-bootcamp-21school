from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [Extension('cyth.c_matrix_mul', ['cyth/c_matrix_mul.pyx'])]

setup(
    name='cyth',
    version='0.1',
    packages=['cyth'],
    ext_modules=cythonize(extensions),
    python_requires='>=3.6',
    zip_safe=False,
)
