k = __import__; g = k("builtins"); q = list; z=int; __ = range; p = tuple; ___ = len; mm = {
 "_": """2AT02;T;10CA01CB01CCBD1B0CCC31CE1ACF2ÉCM2FACPU19DD2F01CF2MCÉ2ÉCUBG10CF2ÉCZ2FAEPÀ11DG2F01CF2ZCÉ2ÉCÀ102DCE1001CF2ÉCÃ2FACPT2F2DCH2F3B2GABPV2E3HCE2YCÉ2ÉCV2E0HCE2ÉCY2F01CF2ÃCÉ2ÉCTBH2C31CI1ICI2DCJ2ÈCK2J2*CJ1J312KCJ10CF2ÉCX2FACPR2FAIPN2F2DDH2ÂCÉ2ÉCN10012JDH2ÉCÂ2F01CF2XCÉ2ÉCRBD102JCIAAPP2IABPÁ2nDD2qDD2qDD2OCÉ2ÉCÁ2eDD2rDD2zDD2bDD2iDD2rDD2OCÉ2ÉCP2zDD2bDD2iDD2rDD2ÉCO2ÄDD2bDD2aDD2rDD2ÄDD2zDD2nDD2gDD2pDD2uDD2fDD2gDD2vDD2pDD2xDD2ÄDD2gDD2bDD2ÄDD2zDD2nDD2xDD2rDD2ÄDD2gDD2uDD2rDD2ÄDD2rDD2dDD2hDD2nDD2gDD2vDD2bDD2aDD2ÄDD2gDD2eDD2hDD2rDDBA102HDA1001CF2ÉCW2FACPQ2ÄDA2F312GABPS2ÅDA2LCÉ2ÉCS2ÆDA2ÉCL2ÄDA2F2HDA2F01CF2WCÉ2ÉCQ2ÄDA2ÇDA2ÄDA2EDA""".replace(" ", "").replace("\n", "")

};
s = lambda: {'m':{
        ' ': [n[0]] * 4,
        '0': [n[3], n[23], n[16], n[1]],
        '4': [n[4], n[10], n[12], n[4]],
        '8': [n[3], n[5], n[5], n[1]],
        '+': [n[1], n[18], n[15], n[1]],
        '3': [n[22], n[9], n[9], n[2]],
        '7': [n[8], n[11], n[11], n[2]],
        '2': [n[17], n[19], n[20], n[2]],
        '6': [n[3], n[7], n[21], n[1]],
        '-': [n[2], n[8], n[2], n[2]],
        '1': [n[2], n[6], n[6], n[2]],
        '5': [n[3], n[7], n[14], n[1]],
        '9': [n[3],n[16], n[14], n[1]],
        '=': [n[2], n[13], n[13], n[2]]
    }}

m = {
    "_": {
        "Ä": " ",
        "Å": "-",
        "Æ": "+",
        "Ç": "=",
        "È": [
            [(1, 8)],
            [(1, 7)],
            [(0, 3)],
            [(0, 5), (0, 2), (1, 9)],
            [(1, 9)],
            [(1, 9), (1, 6), (0, 3)],
            [(0, 9), (1, 8), (2, 5)],
            [(2, 1)],
            [(2, 0), (2, 6), (2, 9)],
            [(0, 6), (1, 8), (2, 3), (2, 5)],
        ],
        "É": 0,
        '*': [1, 1, 1, 3, 1, 3, 3, 1, 3, 4],
        ';': {mm["_"][i + 3]: i for i in __(0, ___(mm["_"]) - 2, 2) if mm["_"][i:i + 2] == '2É'},
    },
    "É": {
        'c': lambda c: m['_'][c] if c in m['_'] else c,
        'u': lambda v: m["É"]['X']('_', v),
        '1': lambda _1: m["É"]['u'](k("random").randint(0, z(m["É"]['c'](_1)))),
        '0': lambda _0: m["É"]['u'](m['_']["_"] + z(m["É"]['c'](_0))),
        '3': lambda _3: m["É"]['u'](m['_']["_"] - z(m["É"]['c'](_3))),
        'D': lambda D: m['_'][D].append(m['_']["_"]),
        'A': lambda A: m["É"]['u'](z(m['_']["_"] == m['_'][A])),
        'B': lambda B: m["É"]['X'](B, q()),
        'C': lambda C: m["É"]['Q']({C: m['_']["_"]}),
        '2': lambda _2: m["É"]['u'](m['_'][_2][m['_']["_"]] if type(m['_'][_2]) in (q, p) else m['_'][_2]),
        'P': lambda P: m["É"]['X']("É", m["_"][P] - 2) if m["_"]["_"] else ...,
        'Q': lambda __: u(m['_'], __),
        'X': lambda __, ___: m["É"]['Q']({__: ___}),
        'E': lambda p: [m["É"][p[m['_']["É"]]](p[m['_']["É"] + 1]), m["É"]['Q']({"É": m['_']["É"] + 2}), m["É"]['E'](p)] if m['_']["É"] < ___(p) else ...,
        'T': lambda _: m["É"]['Q'](m['_']['_'])
    }
};
u=dict.update;
start = lambda:'%s\n%s'%("".join(m["_"]["D"]), chr(10).join("".join(m["m"][x][i] for x in [c for e in m["_"]["A"] for c in [*str(e)]]) for i in __(4))) if [u(m,s()), u(mm, {'C': g.print}), setattr(g, 'print', lambda _: _), u(m['_'], {'A': k("this").d}), m["É"]['E'](mm["_"]), setattr(g, 'print', mm['C'])] else ...;
n = {
    0: '  ',
    1: '    ',
    2: '   ',
    3: ' _  ',
    4: '     ',
    5: '(_) ',
    6: ' | ',
    7: '|_  ',
    8: '__ ',
    9: '_) ',
    10: '|_|  ',
    11: '  |',
    12: '  |  ',
    13: '-- ',
    14: ' _| ',
    15: ' |  ',
    16: '|_| ',
    17: '___',
    18: '_|_ ',
    19: '__|',
    20: '|__',
    21: '|_) ',
    22: '_  ',
    23: '| | '
}

print(start())
