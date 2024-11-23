from src.math_operations import add,sub


def test_add():
    assert add(2,3)==5
    assert add(5,3)==8


def test_sub():
    assert sub(6,2)==4
    assert sub(5,2)==3
    assert sub(9,5)==4
    assert sub(7,5)==2
