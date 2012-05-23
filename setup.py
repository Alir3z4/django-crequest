from setuptools import setup, find_packages

setup(
    name='django-crequest',
    version=".".join(map(str, __import__('crequest').__version__)),
    description='Middleware to make current request always available.',
    long_description=open('README').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='https://github.com/Alir3z4/django-crequest',
    packages=find_packages(exclude=['django_crequest']),
    install_requires=['django>=1.2'],
    keywords=[
        'django',
        'request',
        'web'
    ],
    platforms='OS Independent',
    provides=['crequest',],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)
