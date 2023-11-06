def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        _tulpe = (0, None)
        return _tulpe
    else:
        first_element = sentence[0]
        _tulpe = (length, first_element)
        return _tulpe
