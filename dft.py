from decorators import time_measure
from math import e, pi, log
from numpy import fft, array, zeros, arange, append
from pylab import plot, savefig, xlabel, ylabel
from scipy.io.wavfile import read, write
import sys
from midiutil.MidiFile import MIDIFile


def plot_amplitude(x, rate):
    time = 1.0 / rate
    t = append(arange(0, 1, time), 0)
    plot(t, x)
    xlabel('Tempo')
    ylabel('Amplitude')


def get_frequency(n, rate):
    i = arange(n)
    T = n / rate
    frequency = i / T
    frequency = frequency[range(n / 2)]

    return abs(frequency)


def plot_freq(n, frequency, a_fft):
    Y = a_fft / n
    Y = Y[range(n / 2)]

    plot(frequency, abs(Y), 'r')
    xlabel('Frequencia')
    ylabel('abs(Y(Frequencia))')


def create_midi(frequency):
    MyMIDI = MIDIFile(1)
    track = 0
    channel = 0
    pitch = 69 + 12 * log(frequency[len(frequency) - 1] / 440, 2)
    time = 0
    duration = 1
    volume = 100

    MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    binfile = open("output.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()


def dft(x):
    ''' Algoritmo DFT ingenuo '''
    N = len(x)
    X = zeros(N, dtype=complex)
    E = e
    P = pi

    for k in xrange(N):
        for n in xrange(N):
            X[k] += x[n] * E ** (-1 * 2j * P * k * n / N)

    return X


def run(filename):
    ''' Roda o que foi pedido no EP '''
    rate = 0
    data = []

    rate, data = read(filename)
    wav_array = array(data)

    plot_amplitude(wav_array, rate)
    savefig('amp_fft.png')

    fft_resp = time_measure(fft.fft)(wav_array)

    frequency = get_frequency(len(wav_array), rate)
    plot_freq(len(wav_array), frequency, fft_resp)
    savefig('freq_fft.png')

    create_midi(frequency)
#    dft_resp = time_measure(dft)(wav_array)
#
#    write_file = filename[:-4] + '.midi'
#    write(write_file, rate, resp)


if __name__ == '__main__':
    filename = ''
    try:
        filename = sys.argv[1]
    except IndexError as error:
        raise IndexError('Passe um arquivo .wav como parametro')

    if filename.endswith('.wav'):
        run(filename)

