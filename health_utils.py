def calculate_bmi(height: float, weight: float) -> float:
    """Calcule le BMI avec validation des entrées"""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values")
    return weight / (height ** 2)


def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """Calcule le BMR avec validation des paramètres"""
    if any([val <= 0 for val in [height, weight, age]]):
        raise ValueError("All values must be positive")
    
    height_cm = height * 100  # Conversion mètre -> cm
    
    # Vérification du genre
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Use 'male' or 'female'")

# def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
#     """Calcule le BMR avec validation des paramètres"""
#     if any([val <= 0 for val in [height, weight, age]]):
#         raise ValueError("All values must be positive")
    
#     height_cm = height * 100  # Conversion mètre -> cm
    
#     if gender == 'male':
#         return 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
#     else:
#         return 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)