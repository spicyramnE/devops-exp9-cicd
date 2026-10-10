"""Automated unit tests. The CI pipeline runs these before packaging.
If any test fails, the build halts and no image is pushed to ECR."""
from app import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2
