#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
import numpy as np
from numpy.lib.nanfunctions import nancumprod
import sounddevice as sd
import matplotlib as plt
import soundfile as sf
from suaBibSignal import *
from funcoes_LPF import *

audio, samplerate = sf.read('audio/musicamuitofoda.wav')

audio = audio[:132300]

freqDeAmostragem = 44100
duracao = 3
numAmostras = freqDeAmostragem*duracao

inicio = 0
fim = 4
numPontos = numAmostras

t = np.linspace(inicio,fim,numPontos)
# plot do gravico  áudio vs tempo!
plt.title('Audio normalizado')
plt.plot(t, audio[:,0])
plt.show()

signal= signalMeu()
fs = freqDeAmostragem


filtrado = filtro(audio[:,0], samplerate, 4000)
sd.play(filtrado, samplerate)
sd.wait()

# plot do gravico  áudio vs tempo!
plt.plot(t, filtrado)
plt.title('Audio filtrado')
plt.show()

xf, yf = signal.calcFFT(filtrado, fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio filtrado')
plt.show()


y, x = signal.generateSin(14000, 1, duracao, freqDeAmostragem)

X=filtrado
sd.play(X, samplerate)
sd.wait()

plt.plot(t, X)
plt.title('Audio modulado')
plt.show()

xf, yf = signal.calcFFT(X, fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio modulado')
plt.show()

sf.write('audio/teste.wav', X, samplerate)