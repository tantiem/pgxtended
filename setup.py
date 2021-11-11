from setuptools import setup

setup(
   name='pgx',
   version='1.0',
   license='MIT',
   description='A wrapper for pygame which is a wrapper for SDL2. Makes it a lot easier to draw stuff.',
   author='Levi Reynolds',
   author_email='lereynolds776@gmail.com',
   packages=['pgx'],  #same as name
   install_requires=['pygame'], #external packages as dependencies
)