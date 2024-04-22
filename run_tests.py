import unittest

if __name__ == "__main__":
    tests = unittest.TestLoader().discover("tests")  # run from 'tests' directory
    result = unittest.TextTestRunner().run(tests)
    if result.failures or result.errors:
        exit(1)

# python -m unittest tests
