import matplotlib.pyplot as plt
import numpy as np

def simulate_recursive_explosion(limit=100000):
    # 전체 홀수 개수 (목표치)
    total_odds = limit // 2
    
    # 방문한(점령한) 숫자들 집합
    occupied = set()
    
    # 탐색 큐 (대장들의 리스트)
    # 초기값: 1번 대장 단 한 명
    captains_queue = [1]
    occupied.add(1)
    
    # 통계 저장용
    history_count = [1]
    history_percent = [1 / total_odds * 100]
    
    depth = 0
    
    print(f"--- [시뮬레이션 시작] 목표: 1 ~ {limit} 홀수 정복 ---")
    
    while captains_queue:
        depth += 1
        next_gen_captains = []
        
        # 현재 세대의 대장들이 각자 사슬을 뻗음
        for cap in captains_queue:
            
            # 1. 4x+1 사슬 확장 (가로 폭발)
            curr = cap
            while curr <= limit:
                if curr not in occupied:
                    occupied.add(curr)
                
                # 2. 이 숫자가 새로운 대장을 낳을 수 있는지 확인 (세로 폭발)
                # 역연산: (curr * 2^k - 1) / 3 = parent
                # 가능한 모든 k에 대해 부모(새 대장)를 찾음
                # 범위 제한을 위해 k는 적당히 (숫자가 limit 넘으면 의미 없으므로)
                
                # 최적화를 위해 k=1,2,3... 시도
                temp_val = curr * 2
                while True: # k 루프
                    numerator = temp_val - 1
                    
                    # limit을 너무 초과하면 중단 (부모가 범위 밖이면 무의미)
                    if numerator // 3 > limit:
                        break
                        
                    if numerator % 3 == 0:
                        parent = numerator // 3
                        if parent % 2 != 0: # 홀수 부모만
                            if parent not in occupied and parent <= limit:
                                occupied.add(parent)
                                next_gen_captains.append(parent) # 다음 세대 대장 등록
                    
                    temp_val *= 2 # 다음 k (2^k)
                    if temp_val - 1 > limit * 3: break

                # 사슬의 다음 칸으로 이동
                curr = curr * 4 + 1
        
        # 통계 기록
        count = len(occupied)
        percent = count / total_odds * 100
        history_count.append(count)
        history_percent.append(percent)
        
        print(f"Depth {depth:02d}: {count:>6}개 점령 ({percent:6.2f}%) - 신규 대장 {len(next_gen_captains)}명 탄생")
        
        if percent >= 99.99: # 100% 가까이 되면 중단
            break
            
        captains_queue = next_gen_captains

    return history_percent

# 실행
y_values = simulate_recursive_explosion(100000)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(range(len(y_values)), y_values, marker='o', color='red', linewidth=2)
plt.title("Recursive Explosion of '4x+1' Fractal Structure", fontsize=15)
plt.xlabel("Recursion Depth (Generation)")
plt.ylabel("Occupied Territory (%)")
plt.grid(True)
plt.axhline(y=100, color='blue', linestyle='--', label='100% Saturation')
plt.legend()
plt.text(len(y_values)/2, 50, "Explosion!", fontsize=20, color='red', fontweight='bold', rotation=45)
plt.show()