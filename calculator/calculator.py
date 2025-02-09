def calculate_bmi(height, weight):
    return weight / (height * height)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "red"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "green"
    elif 25 <= bmi < 30:
        return "Overweight", "red"
    elif 30 <= bmi < 35:
        return "Obesity Class I", "red"
    elif 35 <= bmi < 40:
        return "Obesity Class II", "red"
    else:
        return "Obesity Class III", "red"
