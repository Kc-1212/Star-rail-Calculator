import math
while True:
    try:
        print("Menu:")
        print("1. Calculate Real Effect Probability")
        print("2. Speed vs AV per Round")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            Real_Effect_Probability = 0

            print("Real Effect Probability = Base Effect Probability x (1 + Attacker’s EHR) x (1 – Target’s Effect RES) x (1 – Target’s Debuff RES)\n\n\n\n",
                "reference : https://honkai-star-rail.fandom.com/wiki/Effect_RES \n",
                "Enemy Hit Res can be found on the website\n\n\n")

            Base_Effect_Probability = float(input("Enter the Base_Effect_Probability (Hit rate listed in skill description): "))
            Attacker_EHR = float(input("Enter the Attacker_EHR (states the character): "))
            Target_Effect_RES = float(input("Enter the Target_Effect_RES (Enemy's res state): "))
            Target_Debuff_RES = float(input("Enter the Target_Debuff_RES: "))

            Real_Effect_Probability = Base_Effect_Probability * (1 + Attacker_EHR / 100) * (1 - Target_Effect_RES / 100) * (1 - Target_Debuff_RES / 100)

            print("Probability of taking effect:", Real_Effect_Probability)


        elif choice == '2':

            baseSPD=math.ceil(int(input("The speed of your character(without relics) :")))
            SPDpercent=math.ceil(int(input("The speed percent from relics or buffs: ")))
            FlatSPD=math.ceil(int(input("The speed from relics( flat speed without percentage) : ")))
            Speed = math.ceil(baseSPD*((100+SPDpercent)/100)+FlatSPD)
            print("speed : ", Speed)
        
        
        
        else:
            print("Invalid choice. Please select a valid option (1 or 2).")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

    user_input = input("Press 'q' to quit or empty to continue: ")
    if user_input.lower() == 'q':
        break

print("Program ended.")
