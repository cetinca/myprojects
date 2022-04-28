from generate_numbers import sorted_numbers

count = 0


def findx(x, _numbers):
    global count
    _first = 0
    _last = len(_numbers) - 1
    while _first <= _last:
        count += 1
        _mid = (_first + _last) // 2
        if x == _numbers[_mid]:
            return f"index: {_mid} target: {x}"
        elif x < _numbers[_mid]:
            _last = _mid - 1
        else:
            _first = _mid + 1
    return f"Not found!"


print(findx(33, sorted_numbers))
print(count)
