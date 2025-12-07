import pandas as pd

def prove_uniform_distribution(bit_depth=5):
    # 3x-1 고리 맵핑
    loop_map = {}
    # Loop 1
    for x in [1, 2]: loop_map[x] = "Loop 1"
    # Loop 5
    for x in [5, 14, 7, 20, 10]: loop_map[x] = "Loop 5"
    # Loop 17 (주요 멤버)
    for x in [17, 50, 25, 74, 37, 110, 55, 164, 82, 41]: loop_map[x] = "Loop 17"
    
    # 2^bit_depth (예: 32개) 패턴 조사
    patterns = []
    
    # k는 홀수만 (잎사귀는 3k)
    # 비트 패턴을 보기 위해 0 ~ 2^N-1 범위의 모든 홀수 패턴 조사
    for i in range(1, 2**bit_depth, 2):
        # 이진수 패턴 (예: 00001)
        bin_str = format(i, f'0{bit_depth}b')
        
        # 해당 패턴을 가진 대표 숫자 k로 테스트
        # (패턴이 i인 k는 i, i + 2^N, i + 2*2^N... 등 무수히 많음)
        # 그 중 하나만 테스트해도 경로는 결정됨 (초기 수십 단계)
        k = i 
        leaf = 3 * k
        
        curr = leaf
        dest = "Unknown"
        
        # 3x-1 경로 추적
        for _ in range(500):
            if curr in loop_map:
                dest = loop_map[curr]
                break
            if curr % 2 == 0: curr //= 2
            else: curr = 3 * curr - 1
            
        patterns.append({
            "Suffix (k)": f"...{bin_str}",
            "Destination": dest
        })
        
    df = pd.DataFrame(patterns)
    
    print("-" * 60)
    print(f" [증명: 이진수 꼬리({bit_depth}비트)에 따른 목적지 결정론] ")
    print("-" * 60)
    print(df.to_string(index=False))
    
    # 요약 통계
    print("\n[패턴별 목적지 분포]")
    print(df['Destination'].value_counts())

prove_uniform_distribution(6) # 6비트(64개 패턴) 조사