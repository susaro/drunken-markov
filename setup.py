from setuptools import setup

setup(name='drunken-markov',
      version='0.1',
      description='Markov chain analysis / estimation pipeline',
      url='https://github.com/nebw/drunken-markov',
      packages=['drunkenmarkov', 'drunkenmarkov.clustering'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
