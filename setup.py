from setuptools import setup
readme = open('README').read()
setup(name='yt',
      version='0.2.0',
      author='Tyler Cone',
      author_email='herrflockig@gmial.com',
      license='WTFPL',
      description='A Youtube search curses client',
      long_description=readme,
      py_modules=['yt'])
