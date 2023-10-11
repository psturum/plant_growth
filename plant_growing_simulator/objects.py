import pygame
from utils.constants import *

class Plant:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def simulate(self, arguments):
        plant_data = PLANT_DATA.get(self.name)
        points = [0,0,0,0,0,0]

        score = 0  # Initialize the score to 0
        # Check death criteria for each argument
        if arguments[0] < 5 or arguments[0] > 45:
            print("Temperature out of range")
            points[0] = -1  # Apply death criteria
        elif arguments[1] < 1 or arguments[1] > 22:
            print("Light out of range")
            points[1] = -1  # Apply death criteria
        elif (self.name in ["Mikroalge", "Makroalge"] and arguments[2] != 2) or \
            (self.name not in ["Mikroalge", "Makroalge"] and arguments[2] != 1):
            print("Water out of range")

            points[2] = -1
        elif arguments[3] < 5:
            print("N out of range")
            points[3] = -1  or arguments[5] < 5
        elif self.name not in ["Mikroalge", "Makroalge"] and (arguments[4] < 1):
            print("P  out of range")
            points[4] = -1
        elif self.name not in ["Mikroalge", "Makroalge"] and (arguments[5] < 1):
            print("K out of range")
            points[5] = -1
        

        for key, value in plant_data.items():
            if key == 'Gode egenskaber':
                continue
            elif key == 'Temperatur:':
                if value[0] <= arguments[0] <= value[1]:  # Check if the argument is within the range
                    points[0] = 1
            elif key == 'Vand:':
                if value == arguments[2]:  # Check if the argument matches the value
                    points[2] = 1
            elif key == 'Lys:':
                if isinstance(value, tuple):
                    if value[1][0] <= arguments[1] <= value[1][1]: # Check if the argument is within the first interval
                        points[1] = 2
                    elif value[0][0] <= arguments[1] <= value[0][1]:  # Check if the argument is within the second interval
                        points[1] = 1
            elif key == 'Næring:':
                if isinstance(value, dict) and 'Nitrogen' in value:
                    nitrogen_ranges = value['Nitrogen']
                    if nitrogen_ranges[1][0] <= arguments[3] <= nitrogen_ranges[1][1]: # Check if the argument is within the first interval
                        points[3] = 2
                    elif nitrogen_ranges[0][0] <= arguments[3] <= nitrogen_ranges[0][1]: # Check if the argument is within the second interval
                        points[3] = 1
                if isinstance(value, dict) and "Næring P:" in value:
                    næring_p_range = value['Næring P:']
                    if næring_p_range[0] <= arguments[4] <= næring_p_range[1]: # Check if the argument is within the range
                        points[4] = 1
                if isinstance(value, dict) and "Næring K:" in value:
                    næring_k_range = value['Næring K:']
                    if næring_k_range[0] <= arguments[5] <= næring_k_range[1]: # Check if the argument is within the range
                        points[5] = 1

        return sum(points), points





