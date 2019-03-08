"""
module for predefined setlX functions
"""

import sys
import time
import math
import inspect
import multiprocessing
import random as _random
import typing

_print = print
_str = str
_abs = abs
_int = int
_max = max
_min = min
_pow = pow
_range = range


def abort(*args):
    raise Exception('abort is not implemented yet')


def abs(value):
    return _abs(value)


def appendFile(*args):
    raise Exception('appendFile is not implemented yet')


def arb(*args):
    raise Exception('arb is not implemented yet')


def args(*args):
    raise Exception('args is not implemented yet')


def ask(*args):
    raise Exception('ask is not implemented yet')


def atan2(*args):
    raise Exception('atan2 is not implemented yet')


def cacheStats(*args):
    raise Exception('cacheStats is not implemented yet')


def canonical(*args):
    raise Exception('canonical is not implemented yet')


def ceil(value):
    return math.ceil(value)


def char(value):
    return chr(value)


def clearCache(*args):
    raise Exception('clearCache is not implemented yet')


def collect(*args):
    raise Exception('collect is not implemented yet')


def compare(*args):
    raise Exception('compare is not implemented yet')


def deleteFile(*args):
    raise Exception('deleteFile is not implemented yet')


def domain(*args):
    raise Exception('domain is not implemented yet')


def double(value):
    return float(value)


def endsWith(*args):
    raise Exception('endsWith is not implemented yet')


def eval(*args):
    raise Exception('eval is not supported')


def evalTerm(*args):
    raise Exception('evalTerm is not supported')


def execute(*args):
    raise Exception('execute is not supported')


def fct(*args):
    raise Exception('fct is not implemented yet')


def first(*args):
    raise Exception('first is not implemented yet')


def floor(value):
    return math.floor(value)

# This is the setlx from function. renamed because "from" is a python keword


def v_from(*args):
    raise Exception('v_from is not implemented yet')


def fromB(*args):
    raise Exception('fromB is not implemented yet')


def fromE(*args):
    raise Exception('fromE is not implemented yet')


def get(*args):
    raise Exception('get is not implemented yet')


def getOsID(*args):
    raise Exception('getOsID is not implemented yet')


def getScope(*args):
    raise Exception('getScope is not implemented yet')


def getTerm(*args):
    raise Exception('getTerm is not implemented yet')


def hypot(*args):
    raise Exception('hypot is not implemented yet')


def int(value):
    return _int(value)


def isBoolean(value):
    return isinstance(value, bool)


def isClass(value):
    return inspect.isclass(value)


def isDouble(value):
    return isinstance(value, float)


def isError(*args):
    raise Exception('isError is not implemented yet')


def isInfinite(value):
    return value == math.inf


def isInteger(value):
    return isinstance(value, _int)


def isList(*args):
    """
    checks if list of arguments is a list
    """
    for a in args:
        if not isinstance(a, list):
            return False
    return True


def isMap(*args):
    """
    checks if list of arguments is a map(aka dict in Python)
    """
    for a in args:
        if not isinstance(a, dict):
            return False
    return True


def isNumber(value):
    return isInteger(value) or isDouble(value)


def isObject(*args):
    raise Exception('isObject is not implemented yet')


def isPrime(n):
    if not isInteger(n):
        return False
    else:
        # Sieve of Eratosthenes.
        # see https://stackoverflow.com/a/17377939
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(math.sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True


def isProbablePrime(n, k=15):
    """
    based on https://gist.github.com/Ayrx/5884790
    """
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in _range(k):
        a = _random.randrange(2, n - 1)
        x = _pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in _range(r - 1):
            x = _pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def isProcedure(*args):
    raise Exception('isProcedure is not implemented yet')


def isRational(*args):
    raise Exception('isRational is not implemented yet')


def isSet(*args):
    raise Exception('isSet is not implemented yet')


def isString(value):
    return isinstance(value, _str)


def isTerm(*args):
    raise Exception('isTerm is not supported')


def isVariable(*args):
    raise Exception('isVariable is not implemented yet')


def join(*args):
    raise Exception('join is not implemented yet')


def la_cond(*args):
    raise Exception('la_cond is not implemented yet')


def la_det(*args):
    raise Exception('la_det is not implemented yet')


def la_eigenValues(*args):
    raise Exception('la_eigenValues is not implemented yet')


def la_eigenVectors(*args):
    raise Exception('la_eigenVectors is not implemented yet')


def la_hadamard(*args):
    raise Exception('la_hadamard is not implemented yet')


def la_isMatrix(*args):
    raise Exception('la_isMatrix is not implemented yet')


def la_isVector(*args):
    raise Exception('la_isVector is not implemented yet')


def la_matrix(*args):
    raise Exception('la_matrix is not implemented yet')


def la_pseudoInverse(*args):
    raise Exception('la_pseudoInverse is not implemented yet')


def la_solve(*args):
    raise Exception('la_solve is not implemented yet')


def la_svd(*args):
    raise Exception('la_svd is not implemented yet')


def la_vector(*args):
    raise Exception('la_vector is not implemented yet')


def last(*args):
    raise Exception('last is not implemented yet')


def load(*args):
    raise Exception('load is not implemented yet')


def loadLibrary(*args):
    raise Exception('loadLibrary is not implemented yet')


def logo(*args):
    raise Exception('logo is not implemented yet')


def makeTerm(*args):
    raise Exception('makeTerm is not implemented yet')


def matches(*args):
    raise Exception('matches is not implemented yet')


def mathConst(*args):
    raise Exception('mathConst is not implemented yet')


def max(collection):
    return _max(collection)


def min(collection):
    return _min(collection)


def multiLineMode(*args):
    raise Exception('multiLineMode is not implemented yet')


def nCPUs(*args): 
    return multiprocessing.cpu_count()


def nDecimalPlaces(*args):
    raise Exception('nDecimalPlaces is not implemented yet')


def nPrint(*args):
    return _print(*args, end="")


def nPrintErr(*args):
    _print(*args, sep=" ", end="", file=sys.stderr)


def nextPermutation(*args):
    raise Exception('nextPermutation is not implemented yet')


def nextProbablePrime(*args):
    raise Exception('nextProbablePrime is not implemented yet')


def now():
    return int(round(time.time() * 1000))


def parse(*args):
    raise Exception('parse is not implemented yet')


def parseStatements(*args):
    raise Exception('parseStatements is not implemented yet')


def permutations(*args):
    raise Exception('permutations is not implemented yet')


def pow(*args):
    raise Exception('pow is not implemented yet')


def print(*args):
    _print(*args, sep=" ")


def printErr(*args):
    _print(*args, sep=" ", file=sys.stderr)


def random(n=1.0):
    return _random.random()*n

# TODO maybe escape this?


def range(*args):
    raise Exception('range is not implemented yet')


def rational(*args):
    raise Exception('rational is not implemented yet')


def read(*args):
    raise Exception('read is not implemented yet')


def readFile(*args):
    raise Exception('readFile is not implemented yet')


def replace(*args):
    raise Exception('replace is not implemented yet')


def replaceFirst(*args):
    raise Exception('replaceFirst is not implemented yet')


def resetRandom():
    _random.seed(0)


def reverse(*args):
    raise Exception('reverse is not implemented yet')


def rnd(*args):
    raise Exception('rnd is not implemented yet')


def round(*args):
    raise Exception('round is not implemented yet')


def run(*args):
    raise Exception('run is not implemented yet')


def shuffle(*args):
    raise Exception('shuffle is not implemented yet')


def sleep(milliseconds):
    time.sleep(milliseconds*1000)


def sort(*args):
    raise Exception('sort is not implemented yet')


def split(*args):
    raise Exception('split is not implemented yet')


def startsWith(*args):
    raise Exception('startsWith is not implemented yet')


def stop(*args):
    raise Exception('stop is not implemented yet')


def str(arg):
    return _str(arg)


def throw(e):
    raise Exception(e)


def toLowerCase(*args):
    raise Exception('toLowerCase is not implemented yet')


def toUpperCase(*args):
    raise Exception('toUpperCase is not implemented yet')


def trace(*args):
    raise Exception('trace is not implemented yet')


def trim(*args):
    raise Exception('trim is not implemented yet')


def writeExamples(*args):
    raise Exception('writeExamples is not implemented yet')


def writeFile(*args):
    raise Exception('writeFile is not implemented yet')


def writeLibrary(*args):
    raise Exception('writeLibrary is not implemented yet')
