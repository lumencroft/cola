import pandas as pd
from collections import deque

def get_horizontal_family(start_node):
    """
    한 숫자가 주어졌을 때, 가로로(같은 촌수) 파생되는 모든 형제들을 찾음
    규칙: 3의 배수가 아닐 때만 파생(Spawning) 가능
    반환: (가족 리스트, 유효 시드 개수)
    """
    family = [start_node]
    valid_seed_count = 0
    
    # 시작 노드가 시드 자격이 있는지 확인 (단, 시작 노드는 외부에서 들어온 것이므로 체크 필요)
    # 로직상 외부에서 Vertical로 들어온 놈을 큐에 넣고 시작
    
    queue = deque([start_node])
    visited = {start_node}
    
    # 3의 배수가 아니면 시드 인정
    if start_node % 3 != 0:
        valid_seed_count += 1
        # 파생 가능하므로 자식 계산 시도
        curr = start_node
        while True:
            # 공식 적용
            is_rem_2 = (curr % 3 == 2)
            r = 1 - 2 * int(is_rem_2)
            spawn = curr + (curr - r) // 3 * r
            
            # 이미 본 놈이면 루프 방지
            if spawn in visited:
                break
            
            visited.add(spawn)
            family.append(spawn)
            
            # 파생된 놈이 시드 자격이 있는지 확인
            if spawn % 3 != 0:
                valid_seed_count += 1
                curr = spawn # 이 놈이 또 낳을 수 있으므로 curr 갱신해서 계속
            else:
                # 3의 배수면 여기서 가로 확장은 멈춤 (하지만 리스트에는 포함되어 다음 세대로 넘어감)
                break
                
    return family, valid_seed_count

def count_generations(max_gen):
    print(f"{'Gen':<5} | {'Line (4^n)':<12} | {'Main Num':<10} | {'Valid Seeds':<12}")
    print("-" * 50)
    
    # 0세대 (1)
    current_gen_nodes = [1] 
    
    for gen in range(1, max_gen + 1):
        line_name = 4**gen
        main_num_label = ""
        
        next_gen_nodes = []
        total_valid_seeds_in_gen = 0
        
        # 1. 이전 세대의 모든 노드들이 4x+1로 성장하여 이번 세대의 '시작점'들이 됨
        vertical_inputs = [x * 4 + 1 for x in current_gen_nodes]
        
        if len(vertical_inputs) > 0:
            main_num_label = vertical_inputs[0] # 대표 숫자 (5, 21, 85...)
        
        # 2. 각 시작점으로부터 가로로 파생하며 가족을 형성
        # 중복 처리를 위해 set 사용 (같은 촌수 내에서 합류할 수도 있으므로)
        unique_nodes_in_gen = set()
        
        for start_node in vertical_inputs:
            if start_node in unique_nodes_in_gen:
                continue
                
            family, count = get_horizontal_family(start_node)
            
            total_valid_seeds_in_gen += count
            
            for member in family:
                if member not in unique_nodes_in_gen:
                    unique_nodes_in_gen.add(member)
                    next_gen_nodes.append(member) # 순서 유지를 위해 리스트에도 추가
        
        print(f"{gen:<5} | {line_name:<12,} | {main_num_label:<10,} | {total_valid_seeds_in_gen:<12,}")
        
        # 다음 세대를 위해 현재 세대 노드 리스트 갱신
        current_gen_nodes = next_gen_nodes

# 15단계까지 확인
count_generations(18)