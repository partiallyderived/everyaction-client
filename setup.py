from setuptools import setup

setup(
    name='everyaction-client',
    version='0.1.0',
    description='A client for EveryAction implemented in Python3.9+',
    author='Bobbey Reese',
    author_email='bobbeyreese@gmail.com',
    packages=['everyaction'],
    install_requires=[
        'makefun>=1.11.3',
        'requests>=2.25.1'
    ],
    python_requires='>=3.8',
    extras_require={'doc': 'sphinx>=3.4.3', 'test': ['pytest>=6.2.2', 'http-router>=2.0.3']}
)
