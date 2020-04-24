# generate test vectors for alu2020

BIT_WIDTH = 32
INT_MAX  =  2**(BIT_WIDTH-1)-1
INT_MIN  = -2**(BIT_WIDTH-1)
UINT_MAX =  2**(BIT_WIDTH)-1

ALU_OPS = {
    'ALU_ADD' : '0000',
    'ALU_SUB' : '1000',
    'ALU_AND' : '0111',
    'ALU_OR'  : '0110',
    'ALU_XOR' : '0100',
    'ALU_LSL' : '0001',
    'ALU_LSR' : '0101',
    'ALU_ASR' : '1101',
    'ALU_CMP' : '0010',
    'ALU_CMPU': '0011'
}

models = [
    'alu_add_model',
    'alu_sub_model',
    'alu_and_model',
    'alu_or_model',
    'alu_xor_model',
    'alu_lsl_model',
    'alu_lsr_model',
    'alu_asr_model',
    'alu_cmpu_model',
    'alu_cmp_model'
]

def alu_add_model(a, b):
    '''ALU ADD model'''
    r = a + b

    # check if r is bigger than 32 bits, if so trim it
    # and set carry flag
    if r > (UINT_MAX):
        r = r % (1 << BIT_WIDTH)
        c = '1'
    else:
        c = '0'

    # check for overflow, + + > - or - - > +
    if a <= INT_MAX and b <= INT_MAX:
        if r > INT_MAX:
            v = '1'
        else:
            v = '0'
    elif a > INT_MAX and b > INT_MAX:
        if r <= INT_MAX:
            v = '1'
        else:
            v = '0'
    else:
        v = '0'

    z = '1' if r == 0 else '0'
    n = '1' if r > INT_MAX else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_ADD'], format(r, '032b'), n, z, v, c


def alu_sub_model(a, b):
    '''ALU SUB model'''

    r = a - b

    # check if r is smaller than 0, if so trim it
    # and set carry flag
    if r < 0:
        r = int(format(r % (1 << 32), '032b'), base=2)
        c = '0'
    else:
        c = '1'

    # check for overflow, + - > - or - + > +
    if a <= INT_MAX and b > INT_MAX:
        if r > INT_MAX:
            v = '1'
        else:
            v = '0'
    elif a > INT_MAX and b <= INT_MAX:
        if r <= INT_MAX:
            v = '1'
        else:
            v = '0'
    else:
        v = '0'

    z = '1' if r == 0 else '0'
    n = '1' if r > INT_MAX else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_SUB'], format(r, '032b'), n, z, v, c


def alu_and_model(a, b):
    '''ALU AND model'''

    r = a & b
    c = '0'
    v = '0'
    z = '1' if r == 0 else '0'
    n = '1' if r > INT_MAX else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_AND'], format(r, '032b'), n, z, v, c


def alu_or_model(a, b):
    '''ALU OR model'''

    r = a | b
    c = '0'
    v = '0'
    z = '1' if r == 0 else '0'
    n = '1' if r > INT_MAX else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_OR'], format(r, '032b'), n, z, v, c


def alu_xor_model(a, b):
    '''ALU XOR model'''

    r = xor(a, b)
    c = '0'
    v = '0'
    z = '1' if r == 0 else '0'
    n = '1' if r > INT_MAX else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_XOR'], format(r, '032b'), n, z, v, c


def alu_lsl_model(a, b):
    '''ALU LSL model'''

    shamt = b % 32
    rs = format(a << shamt, '033b')

    c = rs[-1*(BIT_WIDTH+1)]
    rs = rs[-1*BIT_WIDTH:]
    v = '0'
    z = '0' if '1' in rs else '1'
    n = rs[0]

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_LSL'], rs, n, z, v, c

def alu_lsr_model(a, b):
    '''ALU LSR model'''

    shamt = b % 32
    if shamt > 0:
        r = a >> (shamt-1)
        c = format(r, '032b')[-1]
        rs = format(r >> 1, '032b')
    else:
        rs = format(a, '032b')
        c = '0'

    v = '0'
    z = '0' if '1' in rs else '1'
    n = rs[0]

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_LSR'], rs, n, z, v, c


def alu_asr_model(a, b):
    '''ALU ASR model'''

    shamt = b % 32
    amsb = 1 if a > INT_MAX else 0

    if shamt > 0:
        r = a >> (shamt-1)
        c = format(r, '032b')[-1]
        rs = format(r >> 1, '032b')

        if amsb == 1:
            rsl = list(rs)
            for i in range(shamt):
                rsl[i] = '1'
            rs = ''.join(rsl)
    else:
        rs = format(a, '032b')
        c = '0'

    v = '0'
    z = '0' if '1' in rs else '1'
    n = rs[0]

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_ASR'], rs, n, z, v, c


def alu_cmpu_model(a, b):
    '''ALU CMPU model: unsigned compare'''

    r = 1 if a > b else 0

    c = '0'
    v = '0'
    n = '0'
    z = '1' if r == 0 else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_CMPU'], format(r, '032b'), n, z, v, c



def alu_cmp_model(a, b):
    '''ALU CMP model: signed compare'''

    if a > INT_MAX:
        anew = a - UINT_MAX -1
    else:
        anew = a

    if b > INT_MAX:
        bnew = b - UINT_MAX -1
    else:
        bnew = b

    r = 1 if anew > bnew else 0

    c = '0'
    v = '0'
    n = '0'
    z = '1' if r == 0 else '0'

    return format(a, '032b'), format(b, '032b'), ALU_OPS['ALU_CMP'], format(r, '032b'), n, z, v, c


def xor(a, b):
    return (a & (~b)) | ((~a) & b)


def test_randoms(f, n=100):
    for _ in range(n):
        tvf.write(','.join(eval(f)(randint(0, UINT_MAX), randint(0, UINT_MAX))))
        tvf.write('\n')


def test_edges(f):
    import itertools

    alist = [0, 1, UINT_MAX, UINT_MAX-1, INT_MAX, INT_MAX+1, INT_MAX-1]
    blist = [0, 1, UINT_MAX, UINT_MAX-1, INT_MAX, INT_MAX+1, INT_MAX-1]
    for a, b in list(itertools.product(*[alist,blist])):
        tvf.write(','.join(eval(f)(a, b)))
        tvf.write('\n')

if __name__ == "__main__":
    from random import randint
    with open('lab4_p3_testvector.txt', 'w') as tvf:
        for f in models:
            test_randoms(f, 100)
            test_edges(f)

