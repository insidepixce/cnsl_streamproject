def lfsr(seed, taps):
    while True:
        feedback = seed[0]  # 첫 번째 비트를 피드백 비트로 사용
        new_bit = sum(seed[i] for i in taps) % 2  # 터치 위치의 비트들의 합을 계산
        seed = seed[1:] + [new_bit]  # 시드 값 업데이트
        yield feedback, seed

def generate_otp(seed, taps, length):
    otp = []
    generator = lfsr(seed, taps)
    for _ in range(length):
        feedback, seed = next(generator)
        otp.append(str(feedback))
    return ''.join(otp)

seed = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 초기 시드 값
taps = [11, 9, 8, 7]  # 터치 위치

otp = generate_otp(seed, taps, 12)
print("OTP:", otp)
