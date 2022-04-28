from generate_numbers import sorted_numbers

_count = 0


def findx(x, _numbers):
    global _count
    _first = 0
    _last = len(_numbers) - 1
    print(_first, _last)
    print(_first<_last)
    while _first <= _last:
        _count += 1
        _mid = (_first + _last) // 2
        if x == _numbers[_mid]:
            return f"index: {_mid} target: {x}"
        elif x < _numbers[_mid]:
            _last = _mid - 1
        else:
            _first = _mid + 1




print(_count)
print(findx(513, sorted_numbers))
