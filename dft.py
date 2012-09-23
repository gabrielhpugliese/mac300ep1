import math
from scipy.io.wavfile import read, write
from numpy import fft


def dft(x, inverse=False):
    N = len(x)
    inv = -1 if not inverse else 1
    X = [0] * N
    for k in xrange(N):
        print N - k
        for n in xrange(N):
            X[k] += x[n] * math.e ** (inv * 2j * math.pi * k * n / N)
        if inverse:
            X[k] /= N
    return X


def fft_CT(x, inverse=False):
    N = len(x) - 1
    inv = -1 if not inverse else 1
    if N % 2:
        return dft(x, inverse)
    x_e = x[::2]
    x_o = x[1::2]
    X_e = fft_CT(x_e, inverse)
    X_o = fft_CT(x_o, inverse)
    X = []
    M = N // 2
    for k in range(M):
        print M - k
        X += [X_e[k] + X_o[k] * math.e ** (inv * 2j * math.pi * k / N)]
    for k in range(M, N):
        X += [X_e[k - M] - X_o[k - M] * math.e ** (inv * 2j * math.pi * (k - M) / N)]
    if inverse:
        X = [j / 2 for j in X]

    return X


def main():
    rate, data = read('wavs/1notaA4_1seg.wav')
    write('wavs/1notaA4_m.wav', rate, fft_CT(data))


if __name__ == '__main__':
    main()
