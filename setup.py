# Choose your output methods.

#from distutils.core import setup
# COMMANDS: python setup.py sdist

from setuptools import setup
# COMMANDS: python setup.py bdist_egg


setup(
    name='jcspygm',
    author='Jen-Chieh Shen',
    author_email='jcs090218@gmail.com',
    version='1.0.0',
    description='Library to make the game using PyGame API.',
    url='https://github.com/jcs090218/JCSPyGm_Lib',
    license='MIT',
    
    
    packages=['jcspygm', 
              'jcspygm.core', 
              'jcspygm.gui', 
              'jcspygm.managers', 
              'jcspygm.util', 
              'jcspygm.util.collider'],
)
