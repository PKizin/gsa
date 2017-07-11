import os
import csv
import gmpy2
from gmpy2 import mpfr, mpc, mpz
from gmpy2 import sqrt
from gmpy2 import norm
from gmpy2 import const_pi as pi
from gmpy2 import floor

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, xlim, ylim
from numpy import arange


class GSParams:
    def __init__(self):
        pass

    alphabet = ['-1', '0', '+1']    # coding alphabet
    bits = 400                      # precision for gmpy2 library
    find_inf_step = 0.001           # fixed step in GSCoding.find_strip method
    find_gap_step = 0.001           # fixed step in GSCoding.find_strip method
    frequency = 32                  # number of nodes in one periodic well
    gap = 1                         # number of gap
    initial_strip = 1               # boundary for initial search [-initial_strip; initial_strip]
    left_tail = 3                   # number of zero wells from the left
    mu = 1.0                        # parameter mu
    periods = 10                    # number of periodic wells
    right_tail = 3                  # number of zero wells from the right
    thread_state = False            # thread controller
    v0 = 3.0                        # parameter V0
    path = os.getcwd()              # path to working directory

    @staticmethod
    def get_h():
        return GSConst.pi / mpfr(str(GSParams.frequency), GSParams.bits)

    @staticmethod
    def get_initial_strip():
        return mpfr(str(GSParams.initial_strip), GSParams.bits)

    @staticmethod
    def get_l():
        return GSConst.pi * mpfr(str(GSParams.periods), GSParams.bits)

    @staticmethod
    def get_mu():
        return mpfr(str(GSParams.mu), GSParams.bits)

    @staticmethod
    def get_v0():
        return -mpfr(str(GSParams.v0), GSParams.bits)

    @staticmethod
    def update():
        ctx = gmpy2.get_context()
        ctx.precision = GSParams.bits
        gmpy2.set_context(ctx)


class GSConst:
    def __init__(self):
        pass

    c = [mpfr('0.0')] * 51
    e = [mpfr('0.0')] * 51
    e_ = [mpfr('0.0')] * 51
    pi = pi()

    @staticmethod
    def update():
        for i in range(51):
            GSConst.c[i] = mpfr(str(float(i)), GSParams.bits)
        for i in range(51):
            GSConst.e[i] = mpfr('1' + i * '0' + '.0', GSParams.bits)
        for i in range(1, 51):
            GSConst.e_[i] = mpfr('0.' + (i-1) * '0' + '1', GSParams.bits)
        GSConst.pi = pi(GSParams.bits)


class GSGrid:
    def __init__(self):
        pass

    # Add 50 to GSParams!
    x = [[]] * 50
    v1 = [[]] * 50
    v2 = [[]] * 50
    v3 = [[]] * 50

    @staticmethod
    def update():
        h = GSParams.get_h()
        mu = GSParams.get_mu()
        v0 = GSParams.get_v0()
        c0 = GSConst.c[0]
        c2 = GSConst.c[2]
        pi = GSConst.pi
        for i in range(50):
            ci = GSConst.c[i + 1]
            GSGrid.x[i] = GSCalc.lin_space(c0, ci * pi, h)
            GSGrid.v1[i] = GSCalc.sub(GSCalc.mul(v0, GSCalc.cos(GSCalc.mul(c2, GSGrid.x[i]))), mu)
            GSGrid.v2[i] = GSCalc.sub(GSCalc.mul(v0, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(GSGrid.x[i], h/c2)))), mu)
            GSGrid.v3[i] = GSCalc.sub(GSCalc.mul(v0, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(GSGrid.x[i], h)))), mu)


class GSCalc:
    def __init__(self):
        pass

    @staticmethod
    def abs(arg):
        if arg > GSConst.c[0]:
            return arg
        else:
            return -arg

    @staticmethod
    def add(arg_list, val):
        return [arg + val for arg in arg_list]

    @staticmethod
    def cos(arg_list):
        return [gmpy2.cos(arg) for arg in arg_list]

    @staticmethod
    def lin_space(l, r, h):
        res = []
        if h > 0:
            while l < r + h / GSConst.c[2]:
                res.append(l)
                l += h
        else:
            while l > r + h / GSConst.c[2]:
                res.append(l)
                l += h
        return res

    @staticmethod
    def max(val, *args):
        for arg in args:
            if arg > val:
                val = arg
        return val

    @staticmethod
    def min(val, *args):
        for arg in args:
            if arg < val:
                val = arg
        return val

    @staticmethod
    def mul(val, arg_list):
        return [val * arg for arg in arg_list]

    @staticmethod
    def sign(arg):
        if arg >= GSConst.c[0]:
            return GSConst.c[1]
        else:
            return -GSConst.c[1]

    @staticmethod
    def sub(arg_list, val):
        return [arg - val for arg in arg_list]

    @staticmethod
    def sum(arg_list):
        res = GSConst.c[0]
        for arg in arg_list:
            res += arg
        return res

    @staticmethod
    def zeros(n):
        return [GSConst.c[0]] * int(n)


class GSCalcAdvanced:
    def __init__(self):
        pass

    @staticmethod
    def eig2(mat):
        a1 = mat[0][0]
        a2 = mat[0][1]
        a3 = mat[1][0]
        a4 = mat[1][1]

        c1 = GSConst.c[1]
        c2 = GSConst.c[2]
        c4 = GSConst.c[4]

        b = -(a1 + a4)
        c = a1*a4 - a2*a3
        d = b*b - c4*c
        l1 = (-b - sqrt(d)) / c2
        l2 = (-b + sqrt(d)) / c2
        k1 = a2 / (l1 - a1)
        k2 = a2 / (l2 - a1)
        v12 = c1 / sqrt(c1 + k1*k1)
        v11 = k1 * v12
        v22 = c1 / sqrt(c1 + k2*k2)
        v21 = k2 * v22
        if norm(l1) < norm(l2):
            return [[[v12, v11], [v22, v21]], [l1, l2]]
        else:
            return [[[v22, v21], [v12, v11]], [l2, l1]]

    @staticmethod
    def monodromy_maxabs(h):
        e1 = [GSConst.c[1], GSConst.c[0]]
        e2 = [GSConst.c[0], GSConst.c[1]]

        v1 = GSCalcAdvanced.runge_linear(e1, [GSConst.c[0], GSConst.pi], h)
        v2 = GSCalcAdvanced.runge_linear(e2, [GSConst.c[0], GSConst.pi], h)

        m1 = [v1[0][-1], v1[1][-1]]
        m2 = [v2[0][-1], v2[1][-1]]

        p, j = GSCalcAdvanced.eig2([m1, m2])

        if abs(j[0]) > abs(j[1]):
            return [p[0], j[0]]
        else:
            return [p[1], j[1]]

    @staticmethod
    def monodromy_simple(h):
        e1 = [GSConst.c[1], GSConst.c[0]]
        e2 = [GSConst.c[0], GSConst.c[1]]

        v1 = GSCalcAdvanced.runge_linear(e1, [GSConst.c[0], GSConst.pi], h)
        v2 = GSCalcAdvanced.runge_linear(e2, [GSConst.c[0], GSConst.pi], h)

        m1 = [v1[0][-1], v1[1][-1]]
        m2 = [v2[0][-1], v2[0][-1]]

        p, j = GSCalcAdvanced.eig2([m1, m2])

        return [p[1], j[1]]

    @staticmethod
    def runge_full(v0, t, h):
        n = int(GSCalc.abs(t[1] - t[0]) / GSCalc.abs(h)) + 1

        mu = GSParams.get_mu()
        v = GSParams.get_v0()

        c2 = GSConst.c[2]
        c6 = GSConst.c[6]

        x = GSCalc.lin_space(t[0], t[1], GSCalc.abs(h))
        y1 = GSCalc.zeros(n)
        y2 = GSCalc.zeros(n)

        v1 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, x))), mu)                       # A*cos(2*x) - w
        v2 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(x, h/c2)))), mu)     # A*cos(2*(x+he/2)) - w
        v3 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(x, h)))), mu)        # A*cos(2*(x+he)) - w

        a = v0[0]
        b = v0[1]

        for i in range(n):
            y1[i] = a
            y2[i] = b

            k11 = b
            k12 = v1[i]*a + a*a*a

            k21 = b + k12*h/c2
            k22 = v2[i]*(a+k11*h/c2) + (a+k11*h/c2)*(a+k11*h/c2)*(a+k11*h/c2)

            k31 = b + k22*h/c2
            k32 = v2[i]*(a+k21*h/c2) + (a+k21*h/c2)*(a+k21*h/c2)*(a+k21*h/c2)

            k41 = b + k32*h
            k42 = v3[i]*(a+k31*h) + (a+k31*h)*(a+k31*h)*(a+k31*h)

            a += (h/c6) * (k11 + c2*k21 + c2*k31 + k41)
            b += (h/c6) * (k12 + c2*k22 + c2*k32 + k42)

            if GSCalc.abs(a) > GSConst.e[6]:
                y1[-1] = GSCalc.sign(a) * GSConst.e[50]
                y2[-1] = GSCalc.sign(b) * GSConst.e[50]
                break

        return [y1, y2]

    @staticmethod
    def runge_linear(v0, t, h):
        n = int(GSCalc.abs(t[1] - t[0]) / GSCalc.abs(h)) + 1

        mu = GSParams.get_mu()
        v = GSParams.get_v0()

        c2 = GSConst.c[2]
        c6 = GSConst.c[6]

        x = GSCalc.lin_space(GSCalc.abs(t[0]), GSCalc.abs(t[1]), GSCalc.abs(h))
        y1 = GSCalc.zeros(n)
        y2 = GSCalc.zeros(n)

        v1 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, x))), mu)                       # A*cos(2*x) - w
        v2 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(x, h/c2)))), mu)     # A*cos(2*(x+he/2)) - w
        v3 = GSCalc.sub(GSCalc.mul(v, GSCalc.cos(GSCalc.mul(c2, GSCalc.add(x, h)))), mu)        # A*cos(2*(x+he)) - w

        a = v0[0]
        b = v0[1]

        for i in range(n):
            y1[i] = a
            y2[i] = b

            k11 = b
            k12 = v1[i]*a

            k21 = b + k12*h/c2
            k22 = v2[i]*(a+k11*h/c2)

            k31 = b + k22*h/c2
            k32 = v2[i]*(a+k21*h/c2)

            k41 = b + k32*h
            k42 = v3[i]*(a+k31*h)

            a += (h/c6) * (k11 + c2*k21 + c2*k31 + k41)
            b += (h/c6) * (k12 + c2*k22 + c2*k32 + k42)

        return [y1, y2]

    @staticmethod
    def runge_short(v0, t, h):
        n = int(GSCalc.abs(t[1] - t[0]) / GSCalc.abs(h)) + 1
        m = int(GSCalc.abs(t[1] - t[0]) / GSCalc.abs(pi())) - 1
        c2 = GSConst.c[2]
        c6 = GSConst.c[6]

        a = v0[0]
        b = v0[1]

        y1 = GSConst.c[0]
        y2 = GSConst.c[0]

        for i in range(n):
            y1 = a
            y2 = b

            k11 = b
            k12 = GSGrid.v1[m][i]*a + a*a*a

            k21 = b + k12*h/c2
            k22 = GSGrid.v2[m][i]*(a+k11*h/c2) + (a+k11*h/c2)*(a+k11*h/c2)*(a+k11*h/c2)

            k31 = b + k22*h/c2
            k32 = GSGrid.v2[m][i]*(a+k21*h/c2) + (a+k21*h/c2)*(a+k21*h/c2)*(a+k21*h/c2)

            k41 = b + k32*h
            k42 = GSGrid.v3[m][i]*(a+k31*h) + (a+k31*h)*(a+k31*h)*(a+k31*h)


            a += (h/c6) * (k11 + c2*k21 + c2*k31 + k41)
            b += (h/c6) * (k12 + c2*k22 + c2*k32 + k42)

            if GSCalc.abs(a) > GSConst.e[6]:
                y1 = GSCalc.sign(a) * GSConst.e[50]
                y2 = GSCalc.sign(b) * GSConst.e[50]
                break

            if not GSParams.thread_state:
                return GSConst.c[0], GSConst.c[0]

        return y1, y2


class GSCoding:
    def __init__(self):
        pass

    @staticmethod
    def cur_bounds(l, r, n, code, sign, alphabet):
        result = []
        for ch1, ch2 in zip(alphabet, alphabet[::-1]):
            a, b = GSCoding.find_strip(l, r, n)
            if not GSParams.thread_state:
                return 0

            if len(ch1) > 1:
                ch1 = '(' + ch1 + ')'
            if len(ch2) > 1:
                ch2 = '(' + ch2 + ')'

            msg = ''
            if sign > 0:
                msg = 'Strip H_{' + code + ch1 + '}'
            else:
                msg = 'Strip H_{' + code + ch2 + '}'
            GSWriter.print_strip(msg, a, b)

            l = b
            result.append(a)
            result.append(b)

        return result

    @staticmethod
    def find_bounds_from_gap(p0, p1, hp, n):
        eps = GSConst.e[1]
        M = GSConst.e[6]
        m = GSConst.c[0]
        n = int(n)

        count = 0
        h = GSParams.get_h()

        v0, j = GSCalcAdvanced.monodromy_maxabs(h)
        y = GSCalcAdvanced.runge_short(GSCalc.mul(p0, v0), [GSConst.c[0], GSConst.c[n] * GSConst.pi], h)
        m0 = y[0]

        is_enter = 0
        mc = 0

        while GSCalc.abs(M - GSCalc.abs(m)) > eps:
            p0 = p0+hp

            y = GSCalcAdvanced.runge_short(GSCalc.mul(p0, v0), [GSConst.c[0], GSConst.c[n] * GSConst.pi], h)
            if not GSParams.thread_state:
                return

            m = y[0]

            condition1 = GSCalc.sign(m) == GSCalc.sign(m0)
            condition2 = GSCalc.abs(m) < GSConst.e[10]
            condition3 = GSCalc.abs(m0) < GSConst.e[10]
            condition4 = GSCalc.abs(m-m0) < GSConst.e[3]
            if condition1 and condition2 and condition3 and condition4:
                hp = GSConst.c[2] * hp

            if GSCalc.abs(hp) < GSConst.e_[50] * GSConst.e_[30]:
                break

            if GSCalc.abs(m) < GSConst.e[10]:
                if_inf = 0

            condition1 = (GSCalc.abs(m) > M) and (is_enter == 0)
            condition2 = (GSCalc.abs(m) < M) and (is_enter == 1)
            condition3 = m*mc < GSConst.c[0]
            if condition1 or condition2 or condition3:
                hp /= -GSConst.e[1]
                if is_enter == 0:
                    is_enter = 1
                else:
                    is_enter = 0

            mc = m

            count += 1

            if count >= 150:
                hp *= GSConst.e[1]
                count = 0

        return p0

    @staticmethod
    def find_bound_from_inf(p0, p1, hp, n):
        eps = GSConst.e[1]
        M = GSConst.e[6]
        m = GSConst.c[0]
        n = int(n)
        h = GSParams.get_h()

        v0, j = GSCalcAdvanced.monodromy_maxabs(h)

        y = GSCalcAdvanced.runge_short(GSCalc.mul(p0 + hp*hp*hp, v0), [GSConst.c[0], GSConst.c[n] * GSConst.pi], h)
        m0 = y[0]

        is_inf = 1
        is_enter = 0
        mc = m0
        count = 0

        while GSCalc.abs(M - GSCalc.abs(m)) > eps:
            p0 += hp

            y = GSCalcAdvanced.runge_short(GSCalc.mul(p0, v0), [GSConst.c[0], GSConst.c[n] * GSConst.pi], h)
            if not GSParams.thread_state:
                return -1, ''

            m = y[0]

            if GSCalc.abs(m) < GSConst.e[10]:
                is_inf = 0

            condition1 = (GSCalc.abs(m) < M) and (is_enter == 0)
            condition2 = (GSCalc.abs(m) > M) and (is_enter == 1)
            condition3 = (mc*m < GSConst.c[0]) and (GSCalc.abs(m) > GSConst.e[10] or GSCalc.abs(mc) > GSConst.e[10])
            if condition1 or condition2 or condition3:
                hp /= -GSConst.e[1]

            if GSCalc.abs(m) < GSConst.e[10]:
                is_enter = 1
            else:
                is_enter = 0

            if GSCalc.abs(hp) < GSConst.e_[50] * GSConst.e_[30]:
                break

            mc = m

            count += 1

            if count >= 100:
                hp *= GSConst.e[1]
                count = 0

        if is_inf == 1:
            side = 'm'
        elif GSCalc.sign(m0) * GSCalc.sign(m) > 0:
            side = 'l'
        else:
            side = 'r'

        return p0, side

    @staticmethod
    def find_strip(l, r, n):
        hp = (r - l) * GSParams.find_inf_step
        b1 = l
        s = 'm'
        while s == 'm':
            b1, s = GSCoding.find_bound_from_inf(b1, r, hp, n)
            if not GSParams.thread_state:
                return 0, 0

        if s == 'r':
            b2 = b1
            b1 = GSCoding.find_bounds_from_gap(b1, l, -hp * GSParams.find_gap_step, n)
            if not GSParams.thread_state:
                return 0, 0

            return b1, b2

        b2 = GSCoding.find_bounds_from_gap(b1, r, hp * GSParams.find_gap_step, n)
        if not GSParams.thread_state:
            return 0, 0

        return b1, b2

    @staticmethod
    def make_state(code):
        GSParams.update()
        GSConst.update()
        GSGrid.update()

        GSWriter.print_info('.' * 165)
        bracket_code = ''.join(code)
        for ch in GSParams.alphabet:
            if len(ch) > 1:
                bracket_code = bracket_code.replace(ch, '(' + ch + ')')
        GSWriter.print_info('Soliton ' + bracket_code + ' will be assembled')
        GSWriter.print_info('.' * 165)

        h = GSParams.get_h()
        c0 = GSConst.c[0]
        c2 = GSConst.c[2]
        strip = GSParams.get_initial_strip()
        alphabet = GSParams.alphabet

        b = GSCoding.cur_bounds(-strip, strip, c2, '00', -1, alphabet)
        if not GSParams.thread_state:
            GSWriter.print_fail('Computation has been stopped')
            return 0
        GSWriter.print_info('.' * 165)

        n = 2
        r = '00'
        for ch in code[1:]:
            v0, j = GSCalcAdvanced.monodromy_maxabs(h)
            y = GSCalcAdvanced.runge_short(GSCalc.mul(b[-1], v0), [c0, GSConst.c[n] * GSConst.pi], h)
            n += 1

            keys = alphabet
            sign = 1
            if y[0] < 0:
                keys = keys[::-1]
                sign = -1

            for elem in zip(keys, b[0::2], b[1::2]):
                if ch == elem[0]:
                    if len(ch) > 1:
                        ch = '(' + ch + ')'
                    b = GSCoding.cur_bounds(elem[1], elem[2], n, r + ch, sign, alphabet)
                    if not GSParams.thread_state:
                        GSWriter.print_fail('Computation has been stopped')
                        return 0
                    break
                sign *= -1

            r += ch
            GSWriter.print_info('.' * 165)

        r = r[1:]

        n = len(code)
        b = GSCoding.reach_stable_manifold(b[len(alphabet) - 1], b[len(alphabet)], n)
        if not GSParams.thread_state:
            GSWriter.print_fail('Computation has been stopped')
            return 0, 0

        p, j = GSCalcAdvanced.monodromy_maxabs(h)
        n = len(code) - 1
        y = GSCalcAdvanced.runge_full(GSCalc.mul(b, p), [c0, GSConst.c[n] * GSConst.pi], h)

        x = GSCalc.lin_space(c0, GSConst.c[n] * GSConst.pi, h)
        y = y[0]

        GSWriter.save_csv(x, y, r)
        GSWriter.save_figure(x, y, r)

        GSParams.thread_state = False
        GSWriter.print_success('Soliton ' + r + ' has been successfully assembled')
        return [x, y]

    @staticmethod
    def reach_stable_manifold(p0, p1, n):
        GSWriter.print_info('Reaching stable manifold')
        h = GSParams.get_h()
        n = int(n)

        v1, j1 = GSCalcAdvanced.monodromy_simple(h)
        v2, j2 = GSCalcAdvanced.monodromy_maxabs(h)

        i = GSConst.e_[3]
        while 1:
            hp = i*(p1-p0)
            min_p = p0
            min_norm = GSConst.e[10]

            GSWriter.print_asympt(p0, p1, hp)

            for p in GSCalc.lin_space(p0, p1, hp):
                y = GSCalcAdvanced.runge_short(GSCalc.mul(p, v2), [0, GSConst.c[n] * GSConst.pi], h)
                if not GSParams.thread_state:
                    return -1

                vl = y
                cur_norm = GSCalc.abs(vl[0]/v1[0] - vl[1]/v1[1])

                if cur_norm < GSConst.e_[6]:
                    return p
                if cur_norm < min_norm:
                    min_norm = cur_norm
                    min_p = p
            p0 = min_p - hp
            p1 = min_p + hp

        return -1


class GSWriter:
    def __init__(self):
        pass

    fig = plt.figure()
    ax = fig.add_subplot(111)

    @staticmethod
    def format(num):
        s = ''
        si = ''
        if num < GSConst.c[0]:
            num = -num
            si = '-'

        num1 = mpz(floor(num))
        while 1:
            s = str(num1 % 10) + s
            num1 -= num1 % 10
            num1 /= 10
            if num1 <= 0:
                break
        s += '.'
        num1 = num - floor(num)
        for i in range(100):
            num1 *= 10
            s += str(mpz(floor(num1)))
            num1 -= floor(num1)

        s = si + s
        return s

    @staticmethod
    def print_asympt(left, right, step):
        print '\n'.join(('<asympt>', GSWriter.format(left), GSWriter.format(right), GSWriter.format(step)))

    @staticmethod
    def print_fail(msg):
        print '\n'.join(('<fail>', str(msg)))

    @staticmethod
    def print_info(msg):
        print '\n'.join(('<info>', str(msg)))

    @staticmethod
    def print_strip(name, left, right):
        print '\n'.join(('<strip>', str(name), GSWriter.format(left), GSWriter.format(right)))

    @staticmethod
    def print_success(msg):
        print '\n'.join(('<success>', str(msg)))

    @staticmethod
    def save_csv(x, y, s):
        gap = GSParams.gap
        path = GSParams.path + '\\result\\'
        filename = path + 'gap' + str(gap) + '   ' + s + '.csv'
        with open(filename, 'w') as csv_file:
            wr = csv.writer(csv_file, delimiter=';', lineterminator='\n')
            for xy in zip(x, y):
                wr.writerow(xy)

    @staticmethod
    def save_figure(x, y, s):
        n = len(s) - 1

        GSWriter.fig.set_size_inches(7, 3)

        GSWriter.fig.patch.set_facecolor('b')
        GSWriter.fig.patch.set_alpha(0.0)

        GSWriter.ax.set_xticks(arange(0, float(n * GSConst.pi), float(GSConst.pi)))
        GSWriter.ax.set_xticklabels((r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$',
                                     r'$7\pi$', r'$8\pi$', r'$9\pi$', r'$10\pi$', r'$11\pi$', r'$12\pi$', r'$13\pi$',
                                     r'$14\pi$', r'$15\pi$', r'$16\pi$', r'$17\pi$', r'$18\pi$', r'$19\pi$', r'$20\pi$',
                                     r'$21\pi$', r'$22\pi$', r'$23\pi$', r'$24\pi$', r'$25\pi$', r'$26\pi$', r'$27\pi$',
                                     r'$28\pi$', r'$29\pi$', r'$30\pi$', r'$31\pi$', r'$32\pi$', r'$33\pi$', r'$34\pi$'))
        GSWriter.ax.set_yticks(range(-10, 10))
        GSWriter.ax.set_yticklabels((r'$-10$', r'$-9$', r'$-8$', r'$-7$', r'$-6$', r'$-5$', r'$-4$', r'$-3$', r'$-2$', r'$-1$',
                                     r'$0$', r'$1$', r'$2$', r'$3$', r'$4$', r'$5$', r'$6$', r'$7$', r'$8$', r'$9$', r'$10$'))

        [i.set_linewidth(2) for i in GSWriter.ax.spines.itervalues()]
        [i.label.set_fontsize(16) for i in GSWriter.ax.xaxis.get_major_ticks()]
        [i.label.set_fontsize(16) for i in GSWriter.ax.yaxis.get_major_ticks()]
        GSWriter.ax.tick_params(width=2)
        GSWriter.ax.xaxis.tick_bottom()
        GSWriter.ax.yaxis.tick_left()

        GSWriter.ax.set_xlabel(r'$x$', fontsize=24)
        GSWriter.ax.set_ylabel(r'$u$', fontsize=24, rotation='horizontal')
        GSWriter.ax.yaxis.set_label_coords(-0.075, 0.45)

        GSWriter.ax.patch.set_facecolor((0.992, 0.917, 0.739))
        GSWriter.ax.patch.set_alpha(1.0)

        m = float(str(GSCalc.max(GSCalc.abs(GSCalc.min(*y)), GSCalc.abs(GSCalc.max(*y)))))
        xlim(float(str(x[0])), float(str(x[-1])))
        ylim(-1.2 * m, 1.2 * m)
        plot(x, y, color=(0.5, 0, 0.5), linewidth=4)

        GSWriter.fig.tight_layout(pad=0.4)

        gap = GSParams.gap
        path = GSParams.path + '\\result\\'
        filename = path + 'gap' + str(gap) + '   ' + s + '.png'

        if os.path.exists(filename):
            os.remove(filename)

        plt.savefig(filename, dpi=100, facecolor=GSWriter.fig.get_facecolor(), edgecolor='none')
        GSWriter.ax.lines[0].remove()