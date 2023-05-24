def generate_otp(seed,taps,lenght):
    state = seed
    mask = (1<< lenght)-1
    otp=''

    for _ in range(lenght):
        xor_result=0
        for tap in taps:
            xor_result ^= (state>>tap) & 1
        state = (state << 1 | xor_result) & mask
        otp += str(xor_result)

    return otp

seed = int(input("시드 값을 입력하세요:" ))
taps = [5,3]
length = 6

otp = generate_otp(seed, taps, length)
print("otp:", otp)