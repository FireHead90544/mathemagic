mathemagic
==========

.. image:: https://discord.com/api/guilds/710909601356447805/embed.png
   :target: https://discord.gg/dN66r3D
   :alt: Discord Server Invite
.. image:: https://img.shields.io/pypi/v/mathemagic.svg
   :target: https://pypi.python.org/pypi/mathemagic
   :alt: PyPI Version Info

A Module containing a lot of general and commonly used mathematical functions written in Python.

Key Features
-------------

- Commonly used and required mathematics operation in your finger tips.
- Many new functions are being added regularly.
- Proper error handling.
- Easy to use.
- Optimised in both speed and memory.

Installing
----------

**Python 3.x is recommended, but you can also install it on python2.x**

To install the module, you can just run the following command:

.. code:: sh

    # Linux/macOS (Replace python3 with python to install for python2.x)
    python3 -m pip install -U mathematics

    # Windows
    pip install -U mathematics


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/FireHead90544/mathemagic
    $ cd mathemagic
    $ python3 -m pip install -U .


Quick Example
--------------

.. code:: py

    import mathemagic

    mathemagic.pi(4) # Returns 3.1415, the value of pi till 4 digits after decimal.

    mathemagic.even(140) # Returns True, as 140 is an even number.

    mathemagic.calculate("100 + 200 - 150") # Returns 150, tries calculating the expression given.

    mathemagic.factorial(5) # Returns 120 as 5! = 120, returns the factorial of a given number.

    mathemagic.prime(20)  Returns False, as 20 is not a prime number, returns True/False based upon the number is prime or not.


You can find more examples in the documentation.

Links
------

- `Documentation <https://mathemagic.readthedocs.io/en/latest/index.html>`_
- `Official Discord Server <https://discord.gg/dN66r3D>`_
- `Author's Portfolio <https://www.rudranshjoshi.me/>`_

*README.md template taken from discord.py's README.rst*
