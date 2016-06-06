# @Author: Tian Qiao <qiaotian>
# @Date:   2016-06-06T10:54:12+08:00
# @Email:  qiaotian@me.com
# @Last modified by:   qiaotian
# @Last modified time: 2016-06-06T10:58:35+08:00
# @License: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE



import numpy as np
from timeit import default_timer as timer

def VectorAdd(a, b, c):
    for i in xrange(a.size):
        c[i] = a[i] + b[i]

def main():
    N = 32000000

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    VectorAdd(A, B, C)
    vectoradd_time = timer() - start

    print("VectorAdd took %f seconds" % vectoradd_time)

if __name__ == '__main__':
    main()
