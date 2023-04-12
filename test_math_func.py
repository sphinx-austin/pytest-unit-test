import math_func
import pytest
import sys


@pytest.mark.number
@pytest.mark.skipif(sys.version_info < (3, 7), reason='do not run')
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(6, 5) == 11
    assert math_func.add(7) >= 9
    assert math_func.add(3) == 5
    print(math_func.add(6, 4), '--------------------------')


@pytest.mark.number
def test_product():
    assert math_func.product(3) == 6
    assert math_func.product(3, 3) == 9
    assert math_func.product(5, 5) == 25
    assert math_func.product(7) != 10


# Using options with pytest
@pytest.mark.strings
@pytest.mark.skipif(sys.version_info > (3, 10), reason='do not run')
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result
    assert 'ksahACAC' not in result


@pytest.mark.skip(reason='do not run')
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


# Parameterizing tests

# def test_add():
#     assert math_func.add(7, 3) == 10

# def test_add():
#     result = math_func.add('Hello', ' World')
#     assert result == 'Hello World'

# def test_add():
#     result = math_func.add(10.5, 25.5)
#     assert result == 36

# as below


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
    # result = math_func.add('Hello', ' World')
    # assert result == 'Hello World'
    # result = math_func.add(10.5, 25.5)
    # assert result == 36
