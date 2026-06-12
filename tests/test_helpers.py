from dashi.helpers import prettify_title


def test_prettify_title():
    assert prettify_title("hello_world") == "Hello World"
    assert prettify_title("HELLO_WORLD_2") == "Hello World 2"
