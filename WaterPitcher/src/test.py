

from agent import testing

def test():
    assert testing([2,4],6) == 4
    assert testing([3,5],16) == 8
    assert testing([2,5,6,72],143) == 8
    print('all passed!')
def test_impossible():
    assert testing([2,4],1) == -1
    assert testing([2],13) == -1
    print('all passed!')

test()
test_impossible()
