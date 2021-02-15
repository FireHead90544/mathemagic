from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mathemagic',
      version='1.0',
      description='Module containing a lot of general and commonly used mathematical functions.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/FireHead90544/mathemagic',
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      license='GNU GPL v3',
      packages=['mathemagic'],
      zip_safe=False,
      install_requires=['random',
                        'math'])