import glue
import pytest  # noqa


def test_glue_version() -> None:
    """Test that the glue version is correct."""
    assert glue.__version__ == "0.1.0"
