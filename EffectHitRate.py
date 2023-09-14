# Prompt the user to enter six numbers
Real_Effect_Probability=0; 

print("Real Effect Probability = Base Effect Probability x (1 + Attacker’s EHR) x (1 – Target’s Effect RES) x (1 – Target’s Debuff RES)\n\n\n\n",
      "reference : https://honkai-star-rail.fandom.com/wiki/Effect_RES \n",
      "Enemy Hit Res can be found in the website\n\n\n")

Base_Effect_Probability = float(input("Enter the Base_Effect_Probability (Hit rate listed in skill description): "))
Attacker_EHR = float(input("Enter the Attacker_EHR(states the character): "))
Target_Effect_RES = float(input("Enter the Target_Effect_RES (Enemy's res state): "))
Target_Debuff_RES = float(input("Enter the Target_Debuff_RES: "))

Real_Effect_Probability =Base_Effect_Probability*(1 + Attacker_EHR/100)*(1-Target_Effect_RES/100)*( 1-Target_Debuff_RES/100)

# Display the result
print("Probability of taking effect :", Real_Effect_Probability)