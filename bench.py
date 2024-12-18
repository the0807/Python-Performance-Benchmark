import time
from concurrent.futures import ThreadPoolExecutor

# 0부터 1억까지의 모든 정수를 더한 값을 반환
def compute(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

# 단일 스레드 테스트
start = time.time()
result = compute(0, 10**8)  # 범위를 1억으로 설정
end = time.time()

print(f"Python Single Thread: {end - start:.4f} seconds")

# 멀티 스레드 테스트
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    # 계산 범위를 4개로 나누어 각 스레드가 다른 범위에서 작업을 하도록 함
    ranges = [(i * (10**8 // 4), (i + 1) * (10**8 // 4)) for i in range(4)]
    results = list(executor.map(lambda r: compute(r[0], r[1]), ranges))

# 결과 합산
total_result = sum(results)
end = time.time()

print(f"Python Multi Thread: {end - start:.4f} seconds")
