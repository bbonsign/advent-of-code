timestamp = 1004345
_buses = '41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'
_buses = _buses.split(',')

stimestamp = 939
_sbuses = '7,13,x,x,59,x,31,19'
_sbuses = _sbuses.split(',')

buses = list(filter(lambda elem: elem != 'x', _buses))
sbuses = list(filter(lambda elem: elem != 'x', _sbuses))

buses2 = list(filter(lambda elem: elem[0]
                     != 'x', zip(_buses, range(len(_buses)))))
sbuses2 = list(
    filter(lambda elem: elem[0] != 'x', zip(_sbuses, range(len(_sbuses)))))


def parse_buses(s):
    _s = s.split(',')
    return list(filter(lambda elem: elem[0] != 'x', zip(_s, range(len(_s)))))
