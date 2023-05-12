import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
#Importe todas as bibliotecas
import numpy as np
from numpy.lib.nanfunctions import nancumprod
#from scipy.signal.ltisys import freqresp
import sounddevice as sd
import matplotlib as plt
import soundfile as sf
from suaBibSignal import *
from funcoes_LPF import *

# Carrega o arquivo de áudio
fs, audio = wavfile.read('audio/teste.wav')

# Normaliza o sinal de áudio
audio = audio / np.max(np.abs(audio))

# Frequência da portadora
fc = 14000

# Tempo do sinal de áudio
t = np.arange(len(audio)) / fs

# Sinal portadora
carrier = np.cos(2 * np.pi * fc * t)

# Multiplica o sinal de áudio pela portadora
modulated = audio * carrier

# Filtro passa-baixa
fcutoff = 4000
b, a = signal.butter(8, 2 * fcutoff / fs)

# Demodulação do sinal
demodulated = signal.filtfilt(b, a, modulated)

# Plota os sinais
plt.figure(figsize=(10, 6))
plt.plot(t, audio, label='Áudio original')
plt.plot(t, demodulated, label='Áudio demodulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Reproduz o áudio original
sd.play(demodulated, fs)
sd.wait()

# Transformada rápida de Fourier do sinal modulado
modulated_fft = np.fft.fft(modulated)

# Frequências correspondentes à FFT
freq = np.fft.fftfreq(len(modulated), 1/fs)

# Espectro de magnitude do sinal modulado
plt.figure()
plt.plot(freq, np.abs(modulated_fft))
plt.title('Sinal de áudio modulado - domínio da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Transformada rápida de Fourier do sinal demodulado
demodulated_fft = np.fft.fft(demodulated)

# Frequências correspondentes à FFT
freq = np.fft.fftfreq(len(demodulated), 1/fs)

# Espectro de magnitude do sinal demodulado
plt.figure()
plt.plot(freq, np.abs(demodulated_fft))
plt.title('Sinal de áudio demodulado - domínio da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Filtro passa-baixa
fcutoff = 4000
b, a = signal.butter(8, 2 * fcutoff / fs)

# Filtragem do sinal demodulado
demodulated_filtered = signal.filtfilt(b, a, demodulated)

# Transformada rápida de Fourier do sinal demodulado e filtrado
demodulated_filtered_fft = np.fft.fft(demodulated_filtered)

# Frequências correspondentes à FFT
freq = np.fft.fftfreq(len(demodulated_filtered), 1/fs)

# Espectro de magnitude do sinal demodulado e filtrado
plt.figure()
plt.plot(freq, np.abs(demodulated_filtered_fft))
plt.title('Sinal de áudio demodulado e filtrado - domínio da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Sinal de áudio demodulado e filtrado - domínio do tempo
plt.figure()
plt.plot(t, demodulated_filtered)
plt.title('Sinal de áudio demodulado e filtrado - domínio do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()
