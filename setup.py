from setuptools import setup

setup(
    name='MyApp',
    version='1.0',
    long_description=__doc__,
    packages=['myapp', 'myapp.main', 'myapp.admin'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=1.1',
        'pymongo>=3.11',
        'Flask-PyMongo>=2.3'
    ]
)