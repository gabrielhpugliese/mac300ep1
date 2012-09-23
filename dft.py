import math
from scipy.io.wavfile import read, write
from numpy import fft, array, zeros
from decorators import time_measure


def dft(x):
    N = len(x)
    X = zeros(N, dtype=complex)
    E = math.e
    P = math.pi

    for k in xrange(N):
        for n in xrange(N):
            X[k] += x[n] * E ** (-1 * 2j * P * k * n / N)

    return X


def main():
    rate, data = read('wavs/1notaA4_1seg.wav')
    write('1notaA4_1seg_m.wav', rate, time_measure(dft)(array(data)))


if __name__ == '__main__':
    main()
