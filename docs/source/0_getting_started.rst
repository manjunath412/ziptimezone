

Getting started
===============


Installation
------------


.. code-block:: python

    pip install ziptimezone

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
    
    zpt.get_lat_long_for_many_zips(['02138', '85260']) # returns a dictionary, {'02138': (42.377, -71.1256), '85260': (33.6013, -111.8867)}
    
    zpt.calculate_time_difference(['02138', '72201']) # returns a string, '02138 is ahead of 72201 by 1.00 hours."}
    
    get_sunrise_sunset("02138") # returns a dictionary, for 5/30/24 {'sunrise_time': '05:11:13', 'sunset_time': '20:13:31'}

    get_sunrise_sunset("02138", datetime(2024, 7, 4).date()) # returns {'sunrise_time': '05:13:42', 'sunset_time': '20:24:10'}