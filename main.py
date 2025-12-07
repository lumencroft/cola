import pandas as pd

def generate_user_matrix(limit=40):
    data = []
    
    # 작성자님이 제시한 순서대로 대장(Target)을 찾습니다.
    # 대장 조건: 누군가의 3x+1 결과가 되어야 함. (즉, 3의 배수가 아니어야 함)
    # 홀수 1, 3, 5, 7, 9... 중에서 3의 배수(3, 9, 15...)를 뺀 수들이 대장입니다.
    
    captains = [i for i in range(1, limit*3) if i % 2 != 0 and i % 3 != 0][:limit]

    for captain in captains:
        row = {}
        
        # 1. 대장 (Target)
        row["대장 (결과값)"] = captain
        
        # 2. 부하의 1번째 (Source, 홀수 부모 찾기)
        # 식: (captain * 2^k - 1) / 3 = parent
        # k를 늘려가며 정수가 되는 가장 작은 홀수 parent를 찾음
        parent = None
        for k in range(1, 10):
            numerator = captain * (2 ** k) - 1
            if numerator % 3 == 0:
                p = numerator // 3
                if p % 2 != 0: # 홀수여야 함
                    parent = p
                    break
                    
        # 3의 배수인지 확인하여 이모지 표시
        if parent is not None:
            if parent % 3 == 0:
                row["부하 1 (원인)"] = f"🌿{parent}" # 3의 배수 (핵심 잎사귀)
            else:
                row["부하 1 (원인)"] = f"🔗{parent}"
        else:
            row["부하 1 (원인)"] = "없음"

        # 3. 대장의 사슬 (4x+1 확장)
        current = parent
        for i in range(1, 4):
            current = current * 4 + 1
            row[f"사슬 {i} (4x+1)"] = current
            
        data.append(row)

    # 표 생성
    df = pd.DataFrame(data)
    print("-" * 80)
    print(" [작성자님 정의 Matrix] ")
    print(" * 대장: 3x+1 역연산이 가능한 수 (3의 배수 제외)")
    print(" * 부하 1: 대장을 만든 바로 그 홀수 (여기에 3의 배수가 나타남!)")
    print("-" * 80)
    print(df.to_string(index=False))

generate_user_matrix(40) # 10줄만 출력