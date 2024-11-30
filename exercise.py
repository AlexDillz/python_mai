import math
import random
import numpy as np



def calculate_target_data(x1, y1, x2, y2, heading):
    angle_to_target = math.atan2(y2 - y1, x2 - x1)

    heading_diff = angle_to_target - heading

    heading_diff = (heading_diff + math.pi) % (2 * math.pi) - math.pi

    distance = math.sqrt((y2 - y1)**2 + (x2 - x1)**2) #
    return heading_diff, distance


def calculate_control(heading_diff, distance):
    # 1 Вариант
    Kp_heading = 2.0
    max_velocity = 3.0  # Максимальная линейная скорость


    velocity = max_velocity * (1 - math.exp(-distance))


    angular_rate = Kp_heading * heading_diff

    return velocity, angular_rate

    # # 2 Вариант
    # Коэффициент пропорциональности для контроллеров
    # Kp_heading = 1
    # Kp_distance = 0.5
    
    # velocity = Kp_distance * distance  # Линейная скорость пропорциональна расстоянию
    # angular_rate = Kp_heading * heading_diff  # Угловая скорость пропорциональна разнице углов
    
    # return velocity, angular_rate



def check_target_reached(x1, y1, x2, y2):    
    distance_threshold = 0.5  # Пороговое расстояние для достижения контрольной точки
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance < distance_threshold