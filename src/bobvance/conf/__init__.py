# Do not load tests from the conf/ dir.
# see https://docs.python.org/3.9/library/unittest.html#load-tests-protocol
def load_tests(*args):
    return None
