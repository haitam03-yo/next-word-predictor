import pytest
from src.utils.preprocess import clean_text

def test_clean_text():
    assert clean_text("Hello!  World?") == "hello world"
    assert clean_text("123abc") == "123abc"
    