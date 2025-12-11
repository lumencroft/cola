import pandas as pd

def generate_user_matrix(limit=40):
    data = []
    
    captains = [i for i in range(1, limit*3) if i % 2 != 0 and i % 3 != 0][:limit]

    for captain in captains:
        row = {}
        row["대장 (결과값)"] = captain
        r = 1 - 2*(captain % 3==1)
        parent = captain + (captain + r) // 3 * r
        
        if parent % 3 == 0:
            row["부하 1 (원인)"] = f"🌿{parent}"
        else:
            row["부하 1 (원인)"] = f"🔗{parent}"

        current = parent
        for i in range(1, 6):
            current = current * 4 - 1
            row[f"사슬 {i} (4x+1)"] = current
            if current % 3 == 0:
                row[f"사슬 {i} (4x+1)"] = f"🌿{current}" 
            else:
                row[f"사슬 {i} (4x+1)"] = f"🔗{current}"
            
        data.append(row)

    df = pd.DataFrame(data)
    print(df.to_string(index=False))

generate_user_matrix(40)