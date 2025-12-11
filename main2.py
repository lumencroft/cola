import pandas as pd

def generate_user_matrix_3x_minus_1(limit=10):
    data = []
    
    # Target condition: T must be congruent to 2 mod 3 (not a multiple of 3, but specifically 3k+2 type)
    captains = [i for i in range(1, limit*3) if i % 2 != 0 and i % 3 == 2][:limit]

    for captain in captains:
        row = {}
        
        row["대장 (결과값)"] = captain
        
        # Inverse rule: P = (T * 2^k + 1) / 3
        parent = None
        for k in range(1, 10):
            numerator = captain * (2 ** k) + 1
            if numerator % 3 == 0:
                p = numerator // 3
                if p % 2 != 0:
                    parent = p
                    break
        
        if parent is not None:
            if parent % 3 == 0:
                row["부하 1 (원인)"] = f"🌿{parent}"
            else:
                row["부하 1 (원인)"] = f"🔗{parent}"
        else:
            row["부하 1 (원인)"] = "없음"

        # Chain Expansion: P -> 4P - 1 (Inverse of 3x-1 structure)
        current = parent
        for i in range(1, 4):
            current = current * 4 - 1
            row[f"사슬 {i} (4x-1)"] = current
            
        data.append(row)

    df = pd.DataFrame(data)
    print("-" * 80)
    print(" [작성자님 정의 Anti-Collatz Matrix (3x-1)] ")
    print(" * 대장: 3x-1 역연산이 가능한 수 (3k+2 형태의 홀수)")
    print(" * 부하 1: 대장을 만든 바로 그 홀수")
    print("-" * 80)
    print(df.to_string(index=False))

generate_user_matrix_3x_minus_1(100)