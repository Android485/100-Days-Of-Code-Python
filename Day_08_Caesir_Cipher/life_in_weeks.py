def life_in_weeks(age):
    
    number_of_years = []
    
    for years in range(age, 90):
        number_of_years.append(years)
        
    count = len(number_of_years)
    x = count * 52
    
    print(f"You have {x} weeks left.")
    


life_in_weeks(56)
    