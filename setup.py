from setuptools import setup, find_packages

setup(name="ski-calculator",
      packages=find_packages(exclude=['tests']),
      entry_points={'console_scripts': [
          'ski_calculator = ski_calculator.main:main',
      ]},
      install_requires=['pytest'])
