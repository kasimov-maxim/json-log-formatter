from setuptools import setup, find_packages

setup(
    name='json-log-formatter',
    version='0.0.1',
    description='JSON formatter for the standard python logging module',
    url='https://github.com/kasimov-maxim/json-log-formatter.git',
    author='Maxim Kasimov',
    author_email='kasimov.maxim@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    zip_safe=False
)

