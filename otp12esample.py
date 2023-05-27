class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps

    def step(self):
        nextbit = sum([self.state[i] for i in self.taps]) % 2
        self.state.append(nextbit)
        return self.state.pop(0)

def lfsr_otp(seed, length):
    seed = [int(i) for i in bin(seed)[2:].zfill(16)] 
    lfsr = LFSR(seed, [15, 13, 12, 10]) 
    return ''.join(str(lfsr.step()) for _ in range(length))

print(lfsr_otp(12345, 12)) 
