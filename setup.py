from setuptools import setup

with open("README.rst", "r") as fh:
    readme = fh.read()

setup(name='mathemagic',
      version='1.0',
      description='Module containing a lot of general and commonly used mathematical functions.',
      long_description=readme,
      long_description_content_type="text/x-rst",
      url='http://github.com/FireHead90544/mathemagic',
      project_urls={
        "Documentation": "https://mathemagic.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/FireHead90544/mathemagic/issues",
      },
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      license='GNU GPL v3',
      packages=['mathemagic'],
      zip_safe=False,
      install_requires=[])