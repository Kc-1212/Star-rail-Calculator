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
            print("reference : https://gameloid.com/speed-in-honkai-star-rail-how-to-calculate-and-increase/\n\n ")
            baseSPD=math.ceil(int(input("The speed of your character(without relics) :")))
            SPDpercent=float(input("The speed multiplyer ( percent ) from relics or buffs: "))
            FlatSPD=math.ceil(int(input("The speed from relics( flat speed without percentage) : ")))
            print("\n\n\n")
            Speed = math.ceil(baseSPD*((100+SPDpercent)/100)+FlatSPD)
            print("speed : ", Speed)

            BAV=10000/Speed
            print("Base Action Value : ", BAV ,"\n\n\n")

            MovePerRound=BAV/100
            print("average move per round :" , MovePerRound)
        
        elif choice == '3':
            print("reference : https://honkai-star-rail.fandom.com/wiki/Energy_Regeneration_Rate\n\n ")
            base_energy_regeneration = float(input("The regeneration rate of your character(without relics) :"))
            energy_regeneration_rate = float(input("The regeneration rate of relics (percentage) :"))
            real_energy_regeneration = base_energy_regeneration/100 * (1 + energy_regeneration_rate/100)
            print("Real Energy Regeneration:", real_energy_regeneration*100)
            maxenergy = math.ceil(int(input("your character max ult gauge : ")))
            SkillNum=real_energy_regeneration*30
            normalNum=real_energy_regeneration*20
            print("to regen ult : \n",
                  "Skill = ", maxenergy/SkillNum,
                   "normal = ", maxenergy/normalNum) 
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
