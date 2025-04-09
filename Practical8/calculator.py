def calculate_volume(weight, strength):
    # The recommended dose of paracetamol for children up to 18 years old is 15 mg/kg
    recommended_dose = 15  
    # Check if the weight is within the expected range (10 - 100 kg)
    if not (10 <= weight <= 100):
        print("Weight should be between 10 and 100 kg")
        return None
    # Check if the strength of paracetamol is one of the expected concentrations
    if strength not in ["120 mg/5 ml", "250 mg/5 ml"]:
        print("Invalid paracetamol strength. Expected '120 mg/5 ml' or '250 mg/5 ml'")
        return None
    # Calculate the required dose in milligrams based on the weight and recommended dose
    required_dose_mg = weight * recommended_dose
    # Determine the concentration of paracetamol per milliliter based on the strength
    if strength == "120 mg/5 ml":
        concentration = 120 / 5  
    else:
        concentration = 250 / 5  
    # Calculate the required volume of paracetamol in milliliters
    volume_ml = required_dose_mg / concentration
    return volume_ml
weight = int(input("weight: "))
strength = input("strength: ")
volume = calculate_volume(weight, strength)
if volume is not None:
    print(f"The required volume of paracetamol is {volume} ml")
# Example of how to call the function
weight0 = 30  
strength0 = "120 mg/5 ml"  
volume = calculate_volume(weight0, strength0)
if volume is not None:
    print(f"The required volume of paracetamol is {volume} ml")