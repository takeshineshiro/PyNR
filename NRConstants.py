"""NR constants

3GPP 38.101-1 V.16.2.0 and 38.101-2 V.16.2.0
"""

import pandas as pd

# 3GPP 38.101-1 Table 5.1-1 V.16.2.0
FR1_LOW = 410e6
FR1_HIGH = 7125e6
FR2_LOW = 24250e6
FR2_HIGH = 52600e6

# 3GPP 38.101-1 Table 5.4.3.3-1 V.16.2.0
ss_raster = pd.DataFrame({
    'NR Operating Band': [
        'n1',
        'n2',
        'n3',
        'n5',
        'n5',
        'n7',
        'n8',
        'n11',
        'n14',
        'n18',
        'n20',
        'n25',
        'n28',
        'n29',
        'n30',
        'n34',
        'n38',
        'n39',
        'n40',
        'n41',
        'n41',
        'n48',
        'n50',
        'n51',
        'n65',
        'n66',
        'n66',
        'n70',
        'n71',
        'n74',
        'n75',
        'n76',
        'n77',
        'n78',
        'n79',
        'n90',
        'n90',
        'n91',
        'n92',
        'n93',
        'n94',
        'n257',
        'n257',
        'n258',
        'n258',
        'n260',
        'n260',
        'n261',
        'n261',
    ],
    'SS Block SCS': [
        15e6,
        15e6,
        15e6,
        15e6,
        30e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        30e6,
        30e6,
        15e6,
        15e6,
        15e6,
        15e6,
        30e6,
        15e6,
        15e6,
        15e6,
        15e6,
        15e6,
        30e6,
        30e6,
        30e6,
        15e6,
        30e6,
        15e6,
        15e6,
        15e6,
        15e6,
        120e6,
        240e6,
        120e6,
        240e6,
        120e6,
        240e6,
        120e6,
        240e6,
    ],
    'SS Block pattern': [
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case B',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case C',
        'Case C',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case B',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case C',
        'Case C',
        'Case C',
        'Case A',
        'Case C',
        'Case A',
        'Case A',
        'Case A',
        'Case A',
        'Case D',
        'Case E',
        'Case D',
        'Case E',
        'Case D',
        'Case E',
        'Case D',
        'Case E',
    ],
    'Range of GSCN First': [
        5279,
        4829,
        4517,
        2177,
        2183,
        6554,
        2318,
        1828,
        1901,
        2156,
        1982,
        4829,
        1901,
        1798,
        5879,
        5030,
        6431,
        4706,
        5756,
        6246,
        6252,
        7884,
        3584,
        3572,
        5279,
        5279,
        5285,
        4993,
        1547,
        3692,
        3584,
        3572,
        7711,
        7711,
        8480,
        6246,
        6252,
        3572,
        3584,
        3572,
        3584,
        22388,
        22390,
        22257,
        22258,
        22995,
        22996,
        22446,
        22446,
    ],
    'Range of GSCN Step': [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        16,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
    ],
    'Range of GSCN Last': [
        5419,
        4969,
        4693,
        2230,
        2224,
        6718,
        2395,
        1858,
        1915,
        2182,
        2047,
        4981,
        2002,
        1813,
        5893,
        5056,
        6544,
        4795,
        5995,
        6717,
        6714,
        7982,
        3787,
        3574,
        5494,
        5494,
        5488,
        5044,
        1624,
        3790,
        3787,
        3574,
        8329,
        8051,
        8880,
        6717,
        6714,
        3574,
        3787,
        3574,
        3787,
        22558,
        22556,
        22443,
        22442,
        23166,
        23164,
        22492,
        22490,
    ],
})



# ss_raster = pd.DataFrame(columns=['NR Operating Band', 'SS Block SCS', 'SS Block pattern', 'Range of GSCN First', 'Range of GSCN Step', 'Range of GSCN Last'])
