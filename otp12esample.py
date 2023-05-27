def lfsr(seed, taps):
    while True:
        feedback = sum(seed[i] for i in taps) % 2
        seed = [feedback] + seed[:-1]
        yield seed[-1]

def generate_otp(seed, taps, length):
    otp = []
    generator = lfsr(seed, taps)
    for _ in range(length):
        otp.append(str(next(generator)))
    return ''.join(otp)

seed = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 초기 시드 값
taps = [11, 9, 8, 7]  # 터치 위치

otp = generate_otp(seed, taps, 12)
print("OTP:", otp)
