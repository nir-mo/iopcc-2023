# IOPCC-2023

## Obfuscated Python Matchstick Puzzles Generator :fire: (August/2023)
This project serves as my submission for the IOPCC 2023 competition. 
It combines my passion for puzzles, coding, and obfuscation, offering a unique and entertaining experience.

The following Python script is a Matchstick Riddles Generator, a playful Python program that creates intriguing 
matchstick riddles. This project was crafted with a touch of whimsy, drawing inspiration from the "Zen of Python" while 
celebrating the art of obfuscation.

```python
k=__import__;g=k("builtins");q=list;z=int;__=range;p=tuple     ;___=len;mm={ "_" :"""2AT02;T;10
CA01CB01CCBD1B0CCC31CE1ACF2ÉCM2FACPU19DD2F01CF2MCÉ2ÉCUBG1      0CF2ÉCZ2FAEPÀ11DG2F01CF2ZCÉ2ÉCÀ1
02DCE1001CF2ÉCÃ2FACPT2F2DCH2F3B2GABPV2E3HCE2YCÉ2ÉCV2E0HCE      2ÉCY2F01CF2ÃCÉ2ÉCTBH2C31CI1ICI2D
CJ2ÈCK2J2*CJ1J312KCJ10CF2ÉCX2FACPR2FAIPN2F2DDH2ÂCÉ2ÉCN100      12JDH2ÉCÂ2F01CF2XCÉ2ÉCRBD102JCIA
APP2IAB     PÁ2nDD2      qDD2qDD                  2OCÉ2ÉC                               Á2eDD2r
DD2zDD2     bDD2iDD      2rDD2OC                  É2ÉCP2z                               DD2bDD2
iDD2rDD     2ÉCO2ÄD      D2bDD2a      DD2rDD2     ÄDD2zDD      2nDD2gDD2pDD2uDD2fDD     2gDD2vD
D2pDD2x     DD2ÄDD2      gDD2bDD      2ÄDD2zD     D2nDD2x      DD2rDD2ÄDD2gDD2uDD2r     DD2ÄDD2
rDD2dDD     2hDD2nD      D2gDD2v      DD2bDD2     aDD2ÄDD      2gDD2eDD2hDD2rDDBA10     2HDA100
1CF2ÉCW     2FACPQ2      ÄDA2F31      2GABPS2     ÅDA2LCÉ      2ÉCS2ÆDA2ÉCL2ÄDA2F2H     DA2F01C
F2WCÉ2É     CQ2ÄDA2                   ÇDA2ÄDA                  2EDA""".                 replace
(" ",       "").                      replace(                 "\n","")                  }; s= \
lambda:     { 32: [n[0 ]]* 4,48 :[n[3 ], n [23],n [16],n[1]],49:[n[ 4        ],n[10],n[12],n[4]]
, 56: [     n[3] ,n [5],n[5],n[1]],43:[n[1],n[18],n[15],n[1]],51:[n [        22],n[9],n[9],n[2]]
, 55: [     n[ 8], n[11],n[11],n[2]],50:[n[17],n[19],n[20],n[2]],54 :        [n[3],n[7],n[21],n[
1]], 45     :[n[2], n[8],n[2],n[2]], 49:[n[2],n[6],n[6],n[2]] ,53:[ n        [3],n[7],n[14],n[1]
], 57 :                  [n[3],n                               [16],n[       14],n[1     ] ], 61
:[n[2],                  n[13],n                               [13],n[       2]] };      m={"_"
:{  "Ä"                  :" "  ,                               "Å":"-",      "Æ":"+"     , "Ç" :
"=","È"     :[ [(1      ,8)], [(1,7)], [(0,3)], [(0,5),(       0,2),(1       ,9)], [      (1,9)],
 [(1,9)     ,(1,6),      (0,3)], [(0,9),(1,8),(2,5)], [(2      ,1)], [       (2,0),(     2,6),(2
,9)], [     (0,6),(      1,8),(2,3),(2,5)], ], "É":0, '*'      :[1,1,1       ,3,1,3,     3,1,3,4
], ';':     {mm["_"      ][i+3]:i for i in __(0,___(mm["_"     ]) -2,2       ) if mm     ["_"][i
:i+2]==     '2É'},                                             }, "É":                   { 'c' :
lambda      c:m['_'                                            ][c] if                   c in  m
['_'  ]     else c,'u': lambda v:m["É"]['X'](      '_',v), '1': lambda _1:m["É"]['u'     ](k("ra"
"ndom")     .randint(0,z(m["É"]['c'](_1))) ),     '0': lambda _0:m["É"]['u'](m['_'][     "_"]+z (
m["É"][     'c'](_0))), '3': lambda _3:m["É"]     ['u'](m['_']["_"]-z(m["É"]['c'] (     _3))), 'D'
:lambda     D: m['_'][D].append(m['_']  [ "_"     ]), 'A': lambda A:m["É"]['u'](z(m     ['_']["_"
]  ==m[     '_'][A]                   )), 'B'     :lambda                               B: m ["É"
]  ['X'     ](B,q()                   ), 'C':      lambda                               C : m["É"
""]['Q'     ]({C:m[      '_']["_"     ] }), '2': lambda _2      :m["É"]['u'](m['_'][_2][m['_'][""
"_"]]if     type( m      ['_'][       _2]) in (q,p) else m      ['_'][_2]), 'P': lambda P:m["É" ]
['X'](     "É",m["_"     ][P]-2       ) if  m[ "_" ] ["_"]      else ..., 'Q': lambda __:u(m['_'],
__),'X'     :lambda      __,___       :m["É"]['Q']({__:         ___}), 'E': lambda p:[m["É"][p[ m
['_'] [     "É"]]](p     [ m['_']     ["É"]+1                  ]),m["É"                 ][ 'Q'  ]
({"É":m     ['_'] [      "É"]+2})     ,m["É"]                  ['E'] (p                 )]   if m
['_'][      "É"]<___     ( p)else     ...,                      'T'   :                 lambda _:
m["É"][     'Q'](m[      '_'] ['_'    ]) } }    ; u =dict.update; start     =lambda     :'%s\n%s'\
     %(     "".join      (m[ "_" ]    ["D"])    ,chr(10).join(  "".join     (m[  "m"    ][x][i  ]
for x       in [  c      for     e    in   m    [ "_"]["A"] for  c in [     *str(e)]    ])for i in
 __(4))     )if[u(m      ,{"m":{chr   (v):s(    )[v]for v in s()}}),u (     mm,{'C':    g.print}),
setattr     (  g   ,     'print' ,    lambda    _:_),u(m['_'] ,{'A': k(     "this").    d}),m["É"]
['E'] (     mm["_"])     ,setattr(                                         g,'print'    ,mm['C'])
] else      ...;n= [      bytes( (                                          v>>i*8)     &255 for i
in __(5)).split(bytes(1), bool(...))[z(....__ne__(...))].decode() for v in  [  8224,    538976288,
2105376, 538992416,     137977929760,   539582248,   2128928,  538992508, 2121567 ,     2107743 ,
137983975292,  8134688,137983959072, 2108717,  545021728,   538999840,   545021820,     6250335 ,
543128671, 8150879, 6250364, 539582332, 2105439, 545005692]]; " -------> START HERE -^^         "


if __name__ == "__main__":
    print(start())
```

## Usage
To correctly run the obfuscated Python script, run the script using this amazing command (use Python 3.8+):

```bash
python3 submission/nirmo.py
```

Each time you run it, you get a brand-new matchstick riddle.
Here's a sneak peek at the kind of puzzles this mysterious script generates:

```
move one matchstick to make the equation true
_          _           _               
_)   __   | |   _|_   |_|   --    |  | 
_)        |_|    |     _|   --    |  | 
                                       
```

## Files
 - [/submission](/submission) The actual submission: `nirmo.py` + `remarks.md`.
 - [/original_code](/original_code) The original code before obfuscation.
 - [/obfuscation_steps](/obfuscation_steps) All the intermediate obfuscation steps and some utils.
