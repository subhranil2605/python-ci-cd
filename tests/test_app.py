from src.app import index
import pytest


def test_index():
    assert index() == "Hello World"

