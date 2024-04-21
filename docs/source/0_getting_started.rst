

Getting started
===============


Installation
------------


.. code-block:: console

    pip install zptimezone

Dependencies
------------

Main Dependencies:
``python3.9+``, ``timezonefinder``


(cf. ``pyproject.toml``)



Basic Usage
-----------



.. code-block:: python

    import ziptimezone as zpt

    zpt.get_lat_long_for_zip('02138') # returns a tuple (42.377, -71.1256)
    zpt.get_timezone_by_zip('02138') # returns 'Eastern' the timezone has been reduced to the more popular zones fo United States Regions
    zpt.get_timezone_for_many_zips(['02138', '85260']) # returns a dictionary, {'02138': 'Eastern', '85260': 'Mountain'}