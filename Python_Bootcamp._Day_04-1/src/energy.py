def modify_list(lst):
    return [i for i in lst if isinstance(i, str)]


# def fix_wiring(cs, ss, ps):
#     ps = modify_list(ps)
#     ss = modify_list(ss)
#     cs = modify_list(cs)
#     result = []
#     for i in range(len(cs)):
#         if len(ps) > i:
#             result.append(f"plug {cs[i]} into {ss[i]} using {ps[i]}")
#         else:
#             result.append(f"weld {cs[i]} to {ss[i]} without plug")
#     return result


def fix_wiring(cs, ss, ps): return [(f"plug {cs[i]} into {modify_list(ss)[i]} using {modify_list(ps)[i]}" if len(modify_list(ps)) > i else f"weld {cs[i]} to {ss[i]} without plug") for i in range(len(modify_list(cs)))]


def main(cables, sockets, plugs):
    for c in fix_wiring(cables, sockets, plugs):
        print(c)


def test_fix_wiring():
    cs1 = ['cable1', 'cable2', 'cable3', 'cable4']
    ss1 = ['socket1', 'socket2', 'socket3', 'socket4']
    ps1 = ['plug1', 'plug2', 'plug3']
    assert fix_wiring(cs1, ss1, ps1) == [
        'plug cable1 into socket1 using plug1',
        'plug cable2 into socket2 using plug2',
        'plug cable3 into socket3 using plug3',
        'weld cable4 to socket4 without plug'
    ]

    cs2 = ['cable2', 'cable1', False]
    ss2 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    ps2 = ['plugZ', None, 'plugY', 'plugX']
    assert fix_wiring(cs2, ss2, ps2) == [
        'plug cable2 into socket1 using plugZ',
        'plug cable1 into socket2 using plugY'
    ]


if __name__ == '__main__':
    # cables = ['cable1', 'cable2', 'cable3', 'cable4']
    # sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    # plugs = ['plug1', 'plug2', 'plug3']

    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    main(cables, sockets, plugs)

    test_fix_wiring()
