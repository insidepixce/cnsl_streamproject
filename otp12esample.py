import time

class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps

    def step(self):
        nextbit = sum([self.state[i] for i in self.taps]) % 2
        self.state.append(nextbit)
        return self.state.pop(0)

def lfsr_otp(length):
    seed = int(time.time() * 1000)  #밀리세컨드까지 사용
    seed = [int(i) for i in bin(seed)[-16:].zfill(16)]  
    lfsr = LFSR(seed, [15, 13, 12, 10])  
    return ''.join(str(lfsr.step()) for _ in range(length))

print(lfsr_otp(int(input("OTP 길이: "))))  

