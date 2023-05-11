#Importe todas as bibliotecas
import numpy as np
from numpy.lib.nanfunctions import nancumprod
from scipy.signal.ltisys import freqresp
import sounddevice as sd
import matplotlib as plt
import soundfile as sf
from suaBibSignal import *
from funcoes_LPF import *

audio, samplerate = sf.read('audio/teste.wav')
signal= signalMeu()
duracao = 4
freqDeAmostragem = samplerate
y, x = signal.generateSin(14000, 1, duracao, freqDeAmostragem)

audio_demo = audio*x[:102665]
xf, yf = signal.calcFFT(audio_demo, samplerate)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio demodulado')
plt.show()
sd.play(audio_demo,samplerate)
sd.wait()


filtrado = filtro(audio_demo, samplerate, 4000)
xf, yf = signal.calcFFT(filtrado, samplerate)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio demodulado')
plt.show()
sd.play(filtrado, samplerate)
sd.wait()