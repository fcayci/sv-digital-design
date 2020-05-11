# grade midterm 2020
# requirements:
#   python3
#   pip3 install boolean.py (boolean evaluation)
#   matplotlib for plotting
#   numpy - a couple small parts

import logging

# where do you wanna log? go to DEBUG / INFO / WARNING
#logging.basicConfig(filename='grading.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

# fixed values for problems
tsetup = 40
thold = 75
tffpq = 50
tffcq = 25

# question numbers and their relative points
quests = {
    'q4' : 1, 'q5' : 1, 'q6' :  1, 'q7' :  1, 'q8' : 1, 'q9' : 2,
    'q10': 1, 'q11': 2, 'q12':  1, 'q13':  2, 'q14': 1, 'q15': 2,
    'q16': 1, 'q17': 3, 'q18': 10, 'q19': 10, 'q20': 3, 'q21': 1,
    'q22': 3, 'q23': 1, 'q24':  5, 'q25':  4, 'q26': 4, 'q27': 5,
    'q28': 2, 'q29': 2, 'q30':  5, 'q31':  3, 'q32': 2, 'q33': 9,
    'q34': 2, 'q35': 3, 'q36':  4, 'q37':  2
}

# total number of questions
NUM_OF_QUESTIONS = len(quests)

# boolean dict for evaluation
bools = {
    '0' : '(~a & ~b & ~c & ~d)',
    '1' : '(~a & ~b & ~c &  d)',
    '2' : '(~a & ~b &  c & ~d)',
    '3' : '(~a & ~b &  c &  d)',
    '4' : '(~a &  b & ~c & ~d)',
    '5' : '(~a &  b & ~c &  d)',
    '6' : '(~a &  b &  c & ~d)',
    '7' : '(~a &  b &  c &  d)',
    '8' : '( a & ~b & ~c & ~d)',
    '9' : '( a & ~b & ~c &  d)',
    'a' : '( a & ~b &  c & ~d)',
    'b' : '( a & ~b &  c &  d)',
    'c' : '( a &  b & ~c & ~d)',
    'd' : '( a &  b & ~c &  d)',
    'e' : '( a &  b &  c & ~d)',
    'f' : '( a &  b &  c &  d)'
}

# sekil1
# shows the paths between ports
# will be used to calculate the paths
s1paths = {
    'ax' : 'tand + txor',
    'az' : 'tand + tnot',
    'xx' : 'tnot + txor',
    'xy' : 'tnot + tor',
    'xz' : 'tnot + tand + tnot',
    'yy' : 'tor + tnot + tor',
    'zx' : 'tand + txor',
    'zy' : 'tor + tnot + tor'
}


def boolean_compare(r, e):
    '''compare two boolean strings. First check if they are the same boolean expressions
    if not, boolean module does not provide an equality check. so just generate 16 different
    true false inputs, and feed into both equations to see if they produce the same results'''
    import boolean
    algebra = boolean.BooleanAlgebra()

    try:
        r = algebra.parse(r)
    except:
        # some other character is in use
        # auto fail
        return 0, 17

    e = algebra.parse(e)

    # lets try our luck
    if r == e:
        return 1, 0

    # damn
    a, b, c, d = algebra.symbols('a','b','c','d')
    t = algebra.TRUE
    f = algebra.FALSE
    hacks = {
        '0'  : [f, f, f, f],
        '1'  : [f, f, f, t],
        '2'  : [f, f, t, f],
        '3'  : [f, f, t, t],
        '4'  : [f, t, f, f],
        '5'  : [f, t, f, t],
        '6'  : [f, t, t, f],
        '7'  : [f, t, t, t],
        '8'  : [t, f, f, f],
        '9'  : [t, f, f, t],
        '10' : [t, f, t, f],
        '11' : [t, f, t, t],
        '12' : [t, t, f, f],
        '13' : [t, t, f, t],
        '14' : [t, t, t, f],
        '15' : [t, t, t, t]
    }
    # replace all the terms with true or false, then simplify them
    # simplification should return 0 or 1
    # do that for all input combinations, and count the number of mismatches
    err = 0
    for i in range(16):
        rres = r.subs({a:hacks[str(i)][0],
                       b:hacks[str(i)][1],
                       c:hacks[str(i)][2],
                       d:hacks[str(i)][3]}).simplify()

        eres = e.subs({a:hacks[str(i)][0],
                       b:hacks[str(i)][1],
                       c:hacks[str(i)][2],
                       d:hacks[str(i)][3]}).simplify()

        if eres != rres:
            err += 1

    if err == 0:
        return 1, err
    else:
        return 0, err

# all the question results return string

def q4(r):
    '''Rank inizi ikilik sistemde 16-bit gösteriniz. (0b kullanmayınız. Örn. 1100000000010010)'''
    return format(r, '016b')

def q5(r):
    '''Rank inizi onluk sistemde gösteriniz. (Örn. 49170)'''
    return str(r)

def q6(r):
    '''16-bit rank << 5, hex olarak yazınız. (0x kullanmayınız. Örn. C012)'''
    # make sure only 4 hex digits return
    return format(r << 5, '04x')[-4:]

def q7(r):
    '''16-bit rank >> 3, hex olarak yazınız. (0x kullanmayınız. Örn. C012)'''
    return format(r >> 3, '04x')

def q8(r):
    '''16-bit rank >>> 11, hex olarak yazınız. (0x kullanmayın. Örn. C012)'''
    # arithmetic shift is hacky
    # create a list of digits, then check the first item in the list
    a = list(str(format(r >> 11, '016b')))
    if (r & 0x8000):
        for i in range(11):
            a[i] = '1'

    # convert the list back to string, and format it back to hex
    return format(int(''.join(a), 2), '04x')

def q9(r):
    '''16-bit rank + 0x7F1A işleminin sonucunu hesaplayınız. (0x kullanmayınız. Örn. C012)'''
    # last four hex digits
    return format(r + 0x7F1A, '04x')[-4:]

def q10(r):
    '''16-bit rank + 0x7F1A işlemi sonucu NVC flaglarını hesaplayınız. (NVC sırasıyla giriniz. Örn. 010)'''
    # 17. bit will hold the carry
    x = format(r + 0x7F1A, '017b')
    r = format(r, '016b')
    c = x[0]
    # overflow check with 16.bits
    if r[0] == '0' and x[1] == '1':
        v = '1'
    else:
        v = '0'
    # negative check with 16.bit
    n = x[1]
    return n + v + c

def q11(r):
    '''16-bit rank + 0xC2F5 işleminin 16-bit sonucunu hesaplayınız. (0x kullanmayınız. Örn. C012)'''
    # last four hex digits
    return format(r + 0xC2F5, '04x')[-4:]

def q12(r):
    '''16-bit rank + 0xC2F5 işlemi sonucu NVC flaglarını hesaplayınız. (NVC sırasıyla giriniz. Örn. 010)'''
    # 17. bit will hold the carry
    x = format(r + 0xC2F5, '017b')
    r = format(r, '016b')
    c = x[0]
    # overflow check with 16.bits
    if r[0] == '1' and x[1] == '0':
        v = '1'
    else:
        v = '0'
    # negative check with 16.bit
    n = x[1]
    return n + v + c

def q13(r):
    '''16-bit rank - 0x4E3B işleminin 16-bit sonucunu hesaplayınız. (0x kullanmayınız. Örn. C012)'''
    x = r - 0x4E3B
    # negative is tricky. it will go -, so take mod 2**16
    if (x < 0):
        x = int(format(x % (1 << 16), '016b'), base=2)
    return format(x, '04x')

def q14(r):
    '''16-bit rank - 0x4E3B işlemi sonucu NVC flaglarını hesaplayınız. (NVC sırasıyla giriniz. Örn. 010)'''
    x = r - 0x4E3B
    # no carry if it is less than 0, (!borrow)
    if (x < 0):
        x = int(format(x % (1 << 16), '016b'), base=2)
        c = '0'
    else:
        c = '1'
    # reformat it to 16 bits
    x = format(x, '016b')
    r = format(r, '016b')

    # overflow check with 16.bits
    if r[0] == '1' and x[0] == '0':
        v = '1'
    else:
        v = '0'
    # negative check with 16.bits
    n = x[0]
    return n + v + c

def q15(r):
    '''16-bit rank - 0x9BD2 işleminin 16-bit sonucunu hesaplayınız. (0x kullanmayınız. Örn. C012)'''
    x = r - 0x9BD2
    # negative is tricky. it will go -, so take mod 2**16
    if (x < 0):
        x = int(format(x % (1 << 16), '016b'), base=2)
    return format(x, '04x')

def q16(r):
    '''16-bit rank - 0x9BD2 işlemi sonucu NVC flaglarını hesaplayınız. (NVC sırasıyla giriniz. Örn. 010)'''
    x = r - 0x9BD2
    # no carry if it is less than 0, (!borrow)
    if (x < 0):
        x = int(format(x % (1 << 16), '016b'), base=2)
        c = '0'
    else:
        c = '1'
    # reformat it to 16 bits
    x = format(x, '016b')
    r = format(r, '016b')

    # overflow check with 16.bits
    if r[0] == '0' and x[0] == '1':
        v = '1'
    else:
        v = '0'
    # negative check with 16.bits
    n = x[0]
    return n + v + c

def q17(r):
    '''Rank inizin odd parity sini hesaplayınız. (Örn. 1)'''
    x = format(r, '016b')
    p = 0
    # xor all digits and for odd parity invert the result (last xor)
    for i in x:
        p = p ^ int(i)
    return str(p ^ 1)

def q18(r):
    '''Rank inizin her hex digitini minterm olarak alıp, 4-giriş
    (ABCD), 1-çıkış (X) doğruluk tablosu çıkarınız.
    K-map ile en sade şeklini gerçekleştiriniz.
    SOP formunu SystemVerilog syntax ına uygun olarak giriniz.'''
    import boolean

    algebra = boolean.BooleanAlgebra()
    # minterm
    # read the rank as a hex digit list
    # bring the corresponding boolean expressions from the bools table
    # then create a SOP representation with | stiching
    r = list(format(r, '04x').lower())
    exp = ' | '.join(map(lambda x: bools[str(x)], r))
    # simplify and return the simplified expression
    e = algebra.parse(exp, simplify=True)
    return str(e)

def q19(r):
    '''Rank inizin her hex digitini maxterm olarak alıp, 4-giriş
    (ABCD), 1-çıkış (X) doğruluk tablosu çıkarınız.
    K-map ile en sade şeklini gerçekleştiriniz.
    SOP formunu SystemVerilog syntax ına uygun olarak giriniz.'''
    import boolean

    algebra = boolean.BooleanAlgebra()
    # maxterm
    # read the rank as a hex digit list
    # since this is max term, exclude the ones in the rank
    # bring the rest of the boolean expressions from the bools table
    # then create a SOP representation with | stiching
    r = list(format(r, '04x').lower())
    rb = [format(i, '1x').lower() for i in range(16) if format(i, '1x').lower() not in r]
    exp = ' | '.join(map(lambda x: bools[str(x)], rb))
    # simplify and return the simplified expression
    e = algebra.parse(exp, simplify=True)
    return str(e)

def q20(r):
    '''Şekil 1 de verilen devrenin propagation gecikmesini hesaplayınız.'''
    r = format(r, '04x')
    # 6x + 10 is the formula. waste to calculate for each problem,
    # but the problems are self contained this way
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    tnot = 6*int(r[3], 16) + 10
    # propagation delay
    # evaluate teh s1paths dict values with the given tand tor txor and tnot valus
    # return the max number
    x = {}
    for path, v in s1paths.items():
        x[path] = eval(v)

    return str(max(x.values()))

def q21(r):
    '''Şekil 1 de verilen devrenin propagation gecikmesinin hangi portlar arasında olduğunu giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    tnot = 6*int(r[3], 16) + 10
    # propagation delay paths
    # evaluate teh s1paths dict values with the given tand tor txor and tnot valus
    # return the paths as a list that give max numbers
    x = {}
    for path, v in s1paths.items():
        x[path] = eval(v)

    m = max(x.values())
    res = []
    for i, v in x.items():
        if v == m:
            res.append(i)
    return res

def q22(r):
    '''Şekil 1 de verilen devrenin contamination gecikmesini hesaplayınız.'''
    r = format(r, '04x')
    tand = (6*int(r[0], 16) + 10)//2
    tor = (6*int(r[1], 16) + 10)//2
    txor = (6*int(r[2], 16) + 10)//2
    tnot = (6*int(r[3], 16) + 10)//2
    # contamination delay
    # evaluate teh s1paths dict values with the given tand tor txor and tnot valus
    # return the min number
    x = {}
    for path, v in s1paths.items():
        x[path] = eval(v)

    return str(min(x.values()))

def q23(r):
    '''Şekil 1 de verilen devrenin contamination gecikmesinin hangi portlar arasında olduğunu giriniz.'''
    r = format(r, '04x')
    tand = (6*int(r[0], 16) + 10)//2
    tor = (6*int(r[1], 16) + 10)//2
    txor = (6*int(r[2], 16) + 10)//2
    tnot = (6*int(r[3], 16) + 10)//2
    # contamination delay paths
    # evaluate teh s1paths dict values with the given tand tor txor and tnot valus
    # return the paths as a list that give min numbers
    x = {}
    for path, v in s1paths.items():
        x[path] = eval(v)

    m = min(x.values())
    res = []
    for i, v in x.items():
        if v == m:
            res.append(i)
    return res

def q24(r):
    '''Şekil 1 de verilen devrenin çalıştırılabilir maximum frekansını hesaplayıp
    MegaHertz cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    tnot = 6*int(r[3], 16) + 10
    # max freq depend on the propagation delay (max)
    x = {}
    for path, v in s1paths.items():
        x[path] = eval(v)

    # append tffpq and tsetup, (no jitter)
    # convert tc to mhz (int) and return as string
    m = max(x.values())
    tc = m + tffpq + tsetup
    freq = int(1/tc * 10**6) # megaherz
    return str(freq)

def q25(r):
    '''Şekil 2 de verilen Full Adder devresini kullanarak Şekil 3 de
    verildiği gibi 3-bit toplayıcı / çıkarıcı devresi tasarladılar.
    Şekil 3a'da bu devrenin kendisi, 3b'de aynı devrenin giriş ve
    çıkışlarına register eklenmiş hali gösterilmektedir. Tablo 1 deki
    değerlere göre devrenin propagation gecikmesini hesaplayınız.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    # first FA
    # max will be y0 -> cout1 signal since it encapsulates
    # all others. Will be the same for all people
    m1 = txor + txor + tand + tor
    # second FA
    # max will be cin -> cout signal, since it will be longer than
    # y1 -> cout2 which is xor + xor + and + or
    m2 = tand + tor
    # third FA
    # max will be cin -> s signal, (we dont care about the cout)
    m3 = txor
    # total delay
    m = m1 + m2 + m3
    return str(m)

def q26(r):
    '''Şekil 3 de verilen devrenin contamination gecikmesini hesaplayınız.'''
    r = format(r, '04x')
    #tand = (6*int(r[0], 16) + 10)//2
    #tor = 6*int(r[1], 16) + 10)//2
    txor = (6*int(r[2], 16) + 10)//2
    #tnot = (6*int(r[3], 16) + 10)//2

    # contamination delay is shortest path,
    # which is min(c0 -> s0, x0 -> s0) since first is one xor,
    # that is faster (c0 -> s0)
    m = txor
    return str(m)

def q27(r):
    '''Şekil 3 de verilen devrenin çalıştırılabilir maximum frekansını
    hesaplayıp MegaHertz cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    m1 = txor + txor + tand + tor
    m2 = tand + tor
    m3 = txor
    m = m1 + m2 + m3

    # return the max freq
    tc = m + tffpq + tsetup
    freq = int(1/tc * 10**6) # megaherz
    return str(freq)

def q28(r):
    '''Şekil 3 de verilen devrenin throughput unu hesaplayıp
    Megabits per second cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    m1 = txor + txor + tand + tor
    m2 = tand + tor
    m3 = txor
    m = m1 + m2 + m3

    tc = m + tffpq + tsetup
    freq = int(1/tc * 10**6) # megaherz
    throuput = 3 * freq # 3 bits come out at this freq
    return str(throuput)

def q29(r):
    '''Şekil 3 de verilen devrenin latency sini hesaplayıp
    picosecond cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    m1 = txor + txor + tand + tor
    m2 = tand + tor
    m3 = txor
    m = m1 + m2 + m3
    tc = m + tffpq + tsetup
    # the incoming bits will wait 1 clock cycle to go out
    return str(tc)

def q30(r):
    '''Firmadaki bir mühendis, sistemi geliştirdiğini ileri
    sürerek Şekil 4 de gösterildiği gibi bir devre tasarımı yaptı.
    Yeni devrenin çalıştırılabilir maximum frekansını hesaplayıp
    MegaHertz cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    # max will be either from Y -> S which is 3 x xors
    #  or from Y -> cout which is 2 x xors + and + or
    m1 = txor + txor + txor
    m2 = txor + txor + tand + tor

    m = max(m1, m2)
    tc = m + tffpq + tsetup

    freq = int(1/tc * 10**6) # megaherz
    return str(freq)

def q31(r):
    '''Şekil 4 de verilen devrenin throughput unu hesaplayıp
    Megabits per second cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    m1 = txor + txor + txor
    m2 = txor + txor + tand + tor

    m = max(m1, m2)
    tc = m + tffpq + tsetup

    freq = int(1/tc * 10**6) # megaherz
    throuput = 3 * freq # 3 bits come out at this freq
    return str(throuput)

def q32(r):
    '''Şekil 4 de verilen devrenin latency sini hesaplayıp
    picosecond cinsinden tam sayı olarak giriniz.'''
    r = format(r, '04x')
    tand = 6*int(r[0], 16) + 10
    tor = 6*int(r[1], 16) + 10
    txor = 6*int(r[2], 16) + 10
    #tnot = 6*int(r[3], 16) + 10

    m1 = txor + txor + txor
    m2 = txor + txor + tand + tor

    m = max(m1, m2)
    tc = m + tffpq + tsetup

    # the incoming bits will wait 3 clock cycles to go out
    return str(3 * tc)


def q33(r):
    '''Şekil 5 te verilen SystemVerilog kod bloğunun ilk clk rising edge
    inde (t0) devreye rankinizi verdiğinizi varsayarsak, 25 clock rising
    edge sonrasında (t25) q çıkışını hesaplayınız.'''
    r = format(r, '016b')
    f = lambda r: str(int(r[0]) ^ int(r[3]) ^ int(r[7]) ^ int(r[10]))

    # that is lfsr. a random number generator
    # it will shift out the msb and shift in a new lsb in each clock cycle
    # the calculation depends on the formula in f function
    # do that for 25 cycles
    for i in range(25):
        n = f(r)
        r = r[1:] + n

    r = format(int(r, 2), '04x')

    return r

def q34(r):
    '''Şekil 6 da verilen SystemVerilog kod bloğunun a hesabi'''
    r = format(r, '016b')
    # simple concat
    return r[2:] + r[:2]

def q35(r):
    '''Şekil 6 da verilen SystemVerilog kod bloğunun b hesabi'''
    r = format(r, '016b')
    x = str(int(r[3]) & int(r[4]) & int(r[5]) & int(r[6]))
    return 4*x

def q36(r):
    '''Şekil 6 da verilen SystemVerilog kod bloğunun c hesabi'''
    r = format(r, '016b')
    # two conditional statements
    if r[2] == '1':
        x = r[0] + r[14:] + str(int(r[10]) & int(r[11]))
    elif r[12] == '1':
        x = str(int(r[7]) ^ int(r[8]) ^ int(r[9])) + r[14:] + r[0]
    else:
        x = r[7] + str(int(r[13]) | int(r[14]) | int(r[15])) + r[:2]

    return x

def q37(r):
    '''Şekil 6 da verilen SystemVerilog kod bloğunun d hesabi'''
    r = format(r, '016b')
    # if any of the xors produce a 1 or will produce a 1
    for i in range(8):
        if int(r[15-i]) ^ int(r[i]):
            return '1'
    return '0'


def read_csv(fname):
    '''generic csv read function. omit the first row
    return the rest as a list of rows'''
    import csv

    with open(fname, 'r') as f:
        n = []
        s = csv.reader(f, delimiter=',')
        for i, row in enumerate(s):
            # dont read the first row
            if i == 0:
                continue
            n.append(row)
        return n


def clean_exam(r):
    '''get rid of the points and feedback sections from the rows.
    this is specific to ms forms result format'''
    start = 7
    f = []
    for row in r:
        n = []
        for i, ir in enumerate(row[start:]):
            if i % 3 == 0:
                n.append(ir.strip()) # strip whitespace from the cells if there are any
        f.append(n)
    return f


def generate_answers(rname, fname, gennum=False):
    '''generate rank - answers sheet, optionally add student id.
    standalone function'''
    import csv

    ranks = read_csv(rname)
    ranks = {l[0] : l[1] for l in ranks} # convert ranks to dict

    with open(fname, 'w') as f:
        s = csv.writer(f, delimiter=',')
        if gennum:
            x = ['Ogrenci Numarasi', 'Rank']
        else:
            x = ['Rank']
        x.extend(list(quests.keys()))
        s.writerow(x)
        # iterate through ranks
        for num, r in ranks.items():
            rd = int(r, 16)
            if gennum:
                ans = [num, r]
            else:
                ans = [r]
            # evaluate the answers for a given rank
            for i, (q, p) in enumerate(quests.items()):
                ans.append(eval(q)(rd))
            s.writerow(ans)

class Student():

    def __init__(self, name, number, rank):
        '''one class to rule them all'''
        self.name = name.lower()
        self.number = number
        self.rank = int(rank, 16)
        self.exp = NUM_OF_QUESTIONS * [None]
        self.calculate_expected()
        self.ans = NUM_OF_QUESTIONS * [None]
        self.points = NUM_OF_QUESTIONS * [0]

    def calculate_expected(self):
        '''calculate the expected answers'''
        r = self.rank
        for i, (q, p) in enumerate(quests.items()):
            self.exp[i] = eval(q)(r)

    def evaluate_questions(self):
        r = self.rank
        logging.debug('Evaluating : %s with rank %s', self.name, format(self.rank, '04x'))
        for i, (q, p) in enumerate(quests.items()):
            # evaluate all questions, tho with different criteria
            if len(self.ans[i]):
                # exact matches with hex
                if i in [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 30, 31, 32, 33]:
                    # if exact match great!
                    if self.ans[i] == self.exp[i]:
                        self.points[i] = p
                    else:
                        try:
                            # this will also match 0 with 0000 but oh well. let the poor souls be happy
                            if int(self.ans[i], 16) == int(self.exp[i], 16):
                                self.points[i] = p
                                logging.debug('hex match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                            else:
                                logging.debug('hex NO match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                        except:
                            logging.debug('hex ERR: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])

                # exact matches with int
                elif i in [1, 16, 18, 21, 22]:
                    # if exact match great!
                    if self.ans[i] == self.exp[i]:
                        self.points[i] = p
                    else:
                        logging.debug('str NO match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])

                # %.05 tolerance on int conversions
                elif i in [20, 23, 24, 25, 26, 27, 28]:
                    # if exact match great!
                    if self.ans[i] == self.exp[i]:
                        self.points[i] = p
                    else:
                        e = int(self.exp[i])
                        try:
                            a = int(self.ans[i])
                            if  a < e+.05*e and a > e-.05*e:
                                self.points[i] = p
                                logging.debug('tilda match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                            else:
                                logging.debug('tilda NO match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                        except:
                            logging.debug('tilda ERR: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])

                # evaluate boolean
                elif i in [14, 15]:
                    logging.debug('boolean comparison: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                    # correct? and number of fails
                    crct, err = boolean_compare(self.ans[i], self.exp[i])
                    # 17 is special case where there is an alian character in the answer
                    if err == 17:
                        logging.debug('boolean ERR: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                    logging.debug(' ? %d, err: %d', crct, err)
                    if crct:
                        self.points[i] = p

                # any in the array is acceptable
                elif i in [17, 19]:
                    if self.ans[i] in self.exp[i]:
                        self.points[i] = p
                        logging.debug('array match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])
                    else:
                        logging.debug('array NO match: rank %s on quest: %s. cevap: %s, expected: %s', format(self.rank, '04x'), q, self.ans[i], self.exp[i])

                else:
                    # if any questions are left come here
                    # should not come here
                    print('WHERIS ', i)

            else:
                self.points[i] = 0

        logging.info('%s got: %d points', self.name, sum(self.points))
        logging.info('|--> point distribution: %s', self.points)


def create_answer_sheet(rankname):
    '''generates answers based on the ranks'''
    answers = 'elm234_arasinav2020_cevap_anahtari.csv'
    generate_answers(rankname, answers)


def create_score_sheet(studs, sname, detailed=False):
    '''create the grading sheet to hold the scores and answers and points'''
    import csv

    with open(sname, 'w', encoding='utf-8-sig',) as f:
        s = csv.writer(f, delimiter=',')

        # this is the order
        row = ['Ogrenci Adi', 'Ogrenci Numarasi', 'Rank']
        if detailed:
            for k in quests.keys():
                row.append(k + ' beklenen')
                row.append(k + ' cevap')
                row.append(k + ' puan')
        row.append('Toplam puan')

        s.writerow(row)
        # '\t' is just a hakc to excel to open normally
        # other programs might behave differently
        for i, st in enumerate(studs):
            row = [st.name, str(st.number) + '\t', format(st.rank, '04x') + '\t']
            if detailed:
                for e, a, p in zip(st.exp, st.ans, st.points):
                    row.append(str(e) + '\t')
                    row.append(str(a) + '\t')
                    row.append(p)
            row.append(sum(st.points))
            s.writerow(row)

def create_grade_figure(studs):
    '''plot grade histogram'''
    import matplotlib.pyplot as plt

    # points array
    pts = []
    for i, s in enumerate(studs):
        pts.append(sum(s.points))

    mnn = np.mean(pts)
    mdn = np.median(pts)

    fig = plt.figure()
    plt.hist(pts, bins=10, range=(0, 100))
    smn = 'mean:    {:.1f}\nmedian: {:.1f}'.format(mnn, mdn)
    plt.text(80, 13, smn)
    plt.ylabel('kişi sayısı')
    plt.xlabel('puan aralıkları')
    plt.title('ELM234 Ara sınav puan dağılımları')
    plt.show()
    #plt.savefig('elm234-arasinav-puan-dagilimi.png')


def create_questions_figure(studs):
    '''plot question correct answer freq'''
    import matplotlib.pyplot as plt
    import numpy as np

    qs = NUM_OF_QUESTIONS * [0]
    for s in studs:
        for i, p in enumerate(s.points):
            if p != 0:
                qs[i] += 1

    fig = plt.figure()
    plt.bar(quests.keys(), qs)
    plt.xticks(np.arange(NUM_OF_QUESTIONS), quests.keys(), rotation=60)
    plt.xlabel('soru numarası')
    plt.ylabel('çözüm sayısı')
    plt.title('ELM234 Ara sınav soru çözüm dağılımları')
    plt.show()
    #plt.savefig('elm234-arasinav-soru-cozum-dagilimi.png')


if __name__ == "__main__":
    import numpy as np

    # test and make sure points add up to 100
    if sum(quests.values()) != 100:
        raise ValueError('question points does not sum to 100')

    examname = 'elm234_sinav.csv'
    rankname = 'elm234_ranks.csv'

    # generate answers
    create_answer_sheet(rankname)

    # rest is for evaluation
    ranks = read_csv(rankname)
    exam2 = read_csv(examname)
    exam = clean_exam(exam2)
    ranks = {l[0] : l[1] for l in ranks} # convert ranks to dict
    studs = [] # master student array

    # test and make sure ranks match
    for i, s in enumerate(exam):
        if (ranks[s[1]][2:] != s[2].lower()):
            serr = s[0], s[1], s[2], ranks[s[1]], ranks[s[1]][2:], s[2].lower()
            raise ValueError('Ranks dont match: %s', serr)

    # add all the answers of the students
    for i, s in enumerate(exam):
        studs.append(Student(s[0], s[1], s[2]))
        for j, ans in enumerate(s[3:]):
            studs[i].ans[j] = ans.lower()
        # evaluate the questions for the student
        studs[i].evaluate_questions()

    create_grade_figure(studs)
    create_questions_figure(studs)

    #gradesname = 'elm234_sonuclar.csv'
    #create_score_sheet(studs, gradesname, True)