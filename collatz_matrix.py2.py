import pandas as pd
import numpy as np

def generate_sovereign_matrix(limit=20):
    captains = (lambda n: n[(n % 2 != 0) & (n % 3 != 0)][:limit])(np.arange(1, limit * 3))
    
    r = 1 - 2 * (captains % 3 == 1)
    parents = captains + (captains + r) // 3 * r
    df = pd.DataFrame({"대장 (결과값)": captains})
    fmt = lambda x: np.where(x % 3 == 0, "🌿", "🔗") + x.astype(str)
    df["부하 1 (원인)"] = fmt(parents)
    curr = parents
    for i in range(1, 6):
        curr = curr * 4 - 1
        df[f"사슬 {i} (4x-1)"] = fmt(curr)
    print(df.to_string(index=False))

generate_sovereign_matrix(20)