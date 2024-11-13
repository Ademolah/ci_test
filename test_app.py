from app import add

def test():
    assert add(3, 5) == 8
    assert add(4, 5) == 9
    assert add(-7 , 5) == -2

