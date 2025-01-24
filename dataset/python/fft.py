import cmath

def fft(x):
    N = len(x)  
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def fft__cp(x):
    N = len(x)
    if N <= 1:
        return x  
    even_indices = x[0::2]
    odd_indices = x[1::2]
    even = fft(even_indices)
    odd = fft(odd_indices)
    twiddle_factors = [cmath.exp(-2j * cmath.pi * k / N) for k in range(N // 2)]
    T = [twiddle_factors[k] * odd[k] for k in range(N // 2)]
    first_half = [even[k] + T[k] for k in range(N // 2)]
    second_half = [even[k] - T[k] for k in range(N // 2)]
    return first_half + second_half

def fft__cf(x):
    PI = cmath.pi
    N = len(x)  
    Ns = range(N // 2)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * PI * k / N) * odd[k] for k in Ns]
    return [even[k] + T[k] for k in Ns] + [even[k] - T[k] for k in Ns]


def fft__cp__cf(x):
    N = len(x)
    if N <= 1:
        return x  
    PI = cmath.pi
    even_indices = x[0::2]
    odd_indices = x[1::2]
    even = fft(even_indices)
    odd = fft(odd_indices)
    Ns = range(N // 2)
    twiddle_factors = [cmath.exp(-2j * PI * k / N) for k in Ns]
    T = [twiddle_factors[k] * odd[k] for k in Ns]
    Ns2 = Ns
    first_half = [even[k] + T[k] for k in Ns2]
    second_half = [even[k] - T[k] for k in Ns2]
    return first_half + second_half