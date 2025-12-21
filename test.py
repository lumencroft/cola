import collections
import time

def prove_collatz_filling_fixed(target_limit=100000, buffer_ratio=10):
    """
    target_limit: 우리가 찾고 싶은 범위 (예: 10만)
    buffer_ratio: 중간 경로를 위해 허용할 탐색 범위 배수 (예: 10배 -> 100만까지 허용)
    """
    search_limit = target_limit * buffer_ratio
    
    print(f"\n⚡ 시뮬레이션 재시작: 목표 1 ~ {target_limit} (탐색 허용: ~{search_limit})")
    print("-" * 70)
    print(f"{'Step':<6} | {'Found Odds':<12} | {'Coverage':<10} | {'Queue Size':<12} | {'Note'}")
    print("-" * 70)

    found_odds_in_target = {1}  # 목표 범위 내의 홀수들
    visited = {1}               # 전체 방문 기록 (탐색 범위 포함)
    queue = collections.deque([1])
    
    total_target_odds = target_limit // 2
    step = 0
    
    start_time = time.time()
    
    while queue:
        step += 1
        current_gen_size = len(queue)
        
        for _ in range(current_gen_size):
            curr = queue.popleft()
            
            # 역-콜라츠 로직 (curr에서 파생되는 이전 숫자 찾기)
            # 조건: (curr * 2^k - 1) / 3 = prev
            k = 1
            while True:
                val = curr * (1 << k) # 비트 연산으로 2^k 가속
                
                # 가망 없으면 탈출 (탐색 한계를 넘어서면 가지치기)
                if (val - 1) // 3 > search_limit:
                    break
                
                if (val - 1) % 3 == 0:
                    prev_node = (val - 1) // 3
                    
                    # 홀수이고, 1보다 크며, 아직 안 가본 곳이라면
                    if prev_node % 2 != 0 and prev_node > 1:
                        if prev_node not in visited:
                            visited.add(prev_node)
                            queue.append(prev_node)
                            
                            # 우리가 찾는 '목표 범위' 안의 놈이면 카운트
                            if prev_node <= target_limit:
                                found_odds_in_target.add(prev_node)
                
                k += 1

        # 통계 계산
        count = len(found_odds_in_target)
        coverage = (count / total_target_odds) * 100
        
        # 로그 출력 (너무 자주는 말고, 변화가 크거나 일정 주기마다)
        if step % 2 == 0 or coverage >= 99.0:
            elapsed = time.time() - start_time
            note = ""
            if coverage > 99.9: note = "🔥 Almost!"
            print(f"{step:<6} | {count:<12,} | {coverage:.2f}%{'':<4} | {len(queue):<12,} | {note}")
        
        if count >= total_target_odds:
            print("-" * 70)
            print(f"🎉 증명 성공! {step} Step 만에 {target_limit} 이하 모든 홀수 정복.")
            print(f"⏱ 소요 시간: {time.time() - start_time:.2f}초")
            break
            
    if count < total_target_odds:
        print(f"\n💀 실패... 버퍼({buffer_ratio}배)가 부족했거나, 정말 반례가 있거나.")

# 실행: 버퍼를 넉넉하게 20배 줘보자. (10만 찾기 위해 200만까지 경유 허용)
prove_collatz_filling_fixed(100000, buffer_ratio=20)