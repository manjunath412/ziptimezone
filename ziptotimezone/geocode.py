import pgeocode

def get_lat_long_for_zip(zip_code, country='US'):
    """
    Retrieve the latitude and longitude for a given ZIP code.

    Parameters:
        zip_code (str): The ZIP code for which geographic coordinates are requested.
        country (str): Country code to refine the search, default is 'US'.

    Returns:
        tuple: A tuple containing latitude and longitude (float, float) if found, otherwise (None, None).

    Raises:
        ValueError: If the zip_code is not recognized.
    """
    nomi = pgeocode.Nominatim(country)
    location = nomi.query_postal_code(zip_code)
    
    if location is not None and not location.latitude is None and not location.longitude is None:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"ZIP code {zip_code} not recognized.")
