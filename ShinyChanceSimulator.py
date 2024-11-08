import random

def check_chance():
    encounters = 0
    Shiny = 0
    while True:  
        random_number = random.randint(1, 30000)
        r = random.randint(1, 30000)
        
        if random_number == r and encounters <= 1:
            Shiny += 1
            encounters += 1
            print(f"Shiny!! After {encounters} attempts!!!")
            print(f"{Shiny} shiny in total")
            return ""

        if random_number == r:
            Shiny += 1
            print(f"Shiny!! After {encounters} attempts.")
            encounters = 0
            
        else:
            encounters += 1

# Example usage
result = check_chance()
print(result)