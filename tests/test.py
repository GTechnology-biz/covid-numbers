from contextlib import contextmanager


@contextmanager
def not_raises(ExpectedException):
    try:
        yield

    except ExpectedException as error:
        raise AssertionError(f"Raised exception {error} when it should not!")

    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")


def good_func():
    print("hello")


def bad_func():
    raise ValueError("BOOM!")


def ugly_func():
    raise IndexError("UNEXPECTED BOOM!")


def test_ok():
    with not_raises(ValueError):
        good_func()


def test_bad():
    with not_raises(ValueError):
        bad_func()


def test_ugly():
    with not_raises(ValueError):
        ugly_func()
