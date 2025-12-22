import pandas as pd
import numpy as np

def generate_simple_tree_matrix(limit=20):
    """
    Collatz Inverse Tree Matrix
    """
    
    # 1. Seed: The start of a new branch (Odd numbers)
    seeds = (lambda n: n[(n % 2 != 0) & (n % 3 != 0)][:limit])(np.arange(1, limit * 3))
    
    # 2. stems: The node that generated the seed via inverse mapping
    r = 1 - 2 * (seeds % 3 == 2)
    stems = seeds + (seeds - r) // 3 * r
    
    # DataFrame Setup (English Only)
    df = pd.DataFrame({"Seed": seeds})
    
    # Formatter: Tree Status
    # 🍃 (Leaf): Divisible by 3 (Terminal node)
    # 🪵 (Branch): Not divisible by 3 (Active node)
    fmt = lambda x: np.where(x % 3 == 0, "🍃", "🪵") + x.astype(str)
    
    df["Stems"] = fmt(stems)
    
    # 3. Chain: Linear extension (4x+1 path)
    curr = stems
    for i in range(1, 6):
        curr = curr * 4 + 1
        df[f"Chain {i}"] = fmt(curr)
    
    # Display Options
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    
    print(df.to_string(index=False))

# Execute the simulation
generate_simple_tree_matrix(20)