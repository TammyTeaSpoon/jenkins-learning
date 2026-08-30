from app import greet


def test_greet():
    assert greet("Thomas") == "Hello, Thomas!"
