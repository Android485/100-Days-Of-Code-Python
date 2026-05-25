def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    name_join = name1 + name2
    T_count = 0
    R_count = 0
    U_count = 0
    E_count = 0
    
    for letter in name_join:
        if letter == "T":
            T_count += 1
        elif letter == "R":
            R_count += 1
        elif letter == "U":
            U_count += 1 
        elif letter == "E":
            E_count += 1
            
    print(f"T occurs {T_count} times")
    print(f"R occurs {R_count} times")
    print(f"U occurs {U_count} times")
    print(f"E occurs {E_count} times")
        
    Total = T_count + R_count + U_count + E_count
        
    print(f"Total = {Total}")
        
    L_count = 0
    O_count = 0
    V_count = 0
    E2_count = 0
        
    for letter in name_join:
        if letter == "L":
            L_count += 1
        elif letter == "O":
            O_count += 1
        elif letter == "V":
            V_count += 1 
        elif letter == "E":
            E2_count += 1
            
    print(f"L occurs {L_count} times")
    print(f"O occurs {O_count} times")
    print(f"V occurs {V_count} times")
    print(f"E occurs {E2_count} times")
        
    Total2 = L_count + O_count + V_count + E2_count
        
    print(f"Total = {Total2}")
        
    print(f"{Total}{Total2}")
        
calculate_love_score("Angela Yu", "Jack Bauer")