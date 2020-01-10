"""
Flask-FHIR
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-FHIR',
    version='1.0',
    url='http://github.com/jiaola/flask-fhir',
    license='BSD',
    author='Dazhi Jiao',
    author_email='djiao@jhu.edu',
    description='A FLASK extension to provide FHIR API',
    long_description=__doc__,
    packages=['flask_fhir'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    python_requires='>=3.7',
    # extra_require={
    #     'test': tests_require,
    #     'doc': doc_require,
    #     'dev': dev_require,
    # },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)