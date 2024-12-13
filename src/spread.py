################################################################
#
#    spread.py
#
################################################################

"""Helps position arrows around nodes in Tikz chaining diagrams"""

import math
import numpy as np
from trc import *

################################################################
#Spreading Algorithm
################################################################

def spread(angles: list[float], rho: float) -> list[float]:
    """
    Spread angles more evenly along the perimeter of a unit circle, with the 
    average angle fixed and maintaining relative position.

    Args:
        angles (list[float]): Angles, measured in radians, on the
            unit circle,
        rho (float): In [0.0, 1.0] where 0.0 = not spread out,
            1.0 = completely spread out, and any number in between
            = partially spread out

    Returns:
        list[float]: New angles on the unit circle.
    """
    #trc_enter(f"spread({angles},{rho})")
    # Compute delta = Length of the additional segment around each
    # point on the unrolled line.
    if rho >= 0.9999:
        # Ideally, we would special case rho = 1.0 to generate
        # perfect answers.  However, we don't use rho = 1.0
        # in our own application.
        rho = 0.9999
    n = len(angles)
    delta = 2.0 * math.pi * rho / ((1.0 - rho) * n)
    # Step 1: Trivial cases
    if len(angles) < 2:
        #trc_exit(f"spread -> {angles}")
        return angles
    # Step 2: Calculate the original angles for each point and sort them
    angles = np.array(angles)
    angles = np.mod(angles, 2 * np.pi)  # Ensure all angles are in (0, 2*pi]
    sorted_indices = np.argsort(angles)
    angles = angles[sorted_indices]
    # Step 3: Calculate the average angle
    avg_angle = spread_average_angle(angles)
    avg_angle = np.mod(avg_angle, 2 * np.pi)  # Ensure avg_angle in (0, 2*pi]
    # Step 4: Determine the alpha factor
    extended_angles = np.array([angles[-1] - 2 * np.pi] + angles.tolist() + [angles[0] + 2 * np.pi])
    avg_idx = np.searchsorted(extended_angles, avg_angle)
    if avg_angle < extended_angles[avg_idx]:
        # extended_angles[avg_idx - 1] < avg_angle < extended_angles[avg_idx]
        prev_angle = extended_angles[avg_idx - 1]
        next_angle = extended_angles[avg_idx]
        alpha = (avg_angle - prev_angle) / (next_angle - prev_angle)
    else:
        # avg_angle == extended_angles[avg_idx]
        left_idx = avg_idx
        right_idx = np.searchsorted(extended_angles, avg_angle, 'right') - 1
        # extended_angles[left_idx] == avg_angle == extended_angles[right_idx]
        avg_idx = (left_idx + right_idx) / 2
        alpha = 0.5
    # Step 5: Move avg_idx back to pointing into angles
    avg_idx = avg_idx - 1
    # Step 6: Unrolled angles padded with ((1 - alpha) * delta)-length line segments on
    # the left and (alpha * delta)-length line segments on the right.
    n = len(angles)
    unrolled_angles = [i * delta + (1 - alpha) * delta + angles[i] for i in range(n)]
    unrolled_avg_angle = avg_idx * delta + avg_angle
    # Step 7: Calculate perimeters and scaling factor
    old_perimeter = 2 * np.pi
    new_perimeter = old_perimeter + n * delta
    scaling = old_perimeter / new_perimeter
    # Step 8: Scale back each angle to the unit circle
    scaled_angles = [scaling * unrolled_angles[i] for i in range(n)]
    scaled_avg_angle = scaling * unrolled_avg_angle
    # Step 9: Shift to lock the average angle position
    avg_angle_shift = scaled_avg_angle - avg_angle
    shifted_angles = [spread_reduce_angle(angle - avg_angle_shift) for angle in scaled_angles]
    new_angles = np.empty_like(shifted_angles)
    new_angles[sorted_indices] = shifted_angles
    #trc_exit(f"spread -> {new_angles}")
    return new_angles

def spread_average_angle(angles):
    """
    Return average angle of the angles.  Compute the average point
    of the points on the unit circle corresponding to angles.  Define
    the average angle to be the angle of the average point on the
    unit circle.

    Args:
        angles (list[float]): A list of angles, measured in
        radians, representing points on the unit circle.

    Returns:
        float: The average angle, measured in radians, on the unit circle.
    """
    #trc_enter(f"spread_average_angle({angles})")
    points = [(np.cos(angle), np.sin(angle)) for angle in angles]
    avg_point = spread_average_point(points)
    avg_angle = np.arctan2(avg_point[1], avg_point[0])
    #trc_exit(f"spread_average_angle -> {avg_angle}")
    return avg_angle

def spread_average_point(points):
    avg = np.mean(points, axis=0)
    norm = np.sqrt(avg[0]**2 + avg[1]**2)
    if norm > 0.0:
        avg_point = avg_point = avg / norm
    else:
        avg_point = (1.0, 0.0)
    return avg_point

################################################################
#Angles and Compass Directions
################################################################

def spread_reduce_angle(angle: float) -> float:
    # Reduce angle to within (-pi, pi]
    #trc_enter(f"spread_reduce_angle({angle})")
    answer = ((angle + math.pi) % (2.0 * math.pi)) - math.pi
    #trc_exit(f"spread_reduce_angle -> {answer}")
    return answer

def spread_atan2(x: float, y: float) -> float:
    """
    Return math.atan2(y, x) in (-pi, pi].

    Args:
        x (float): x coordinate on the unit circle.
        y (float): y coordinate on the unit circle.

    Returns:
        list[float]: Angle, measured in radians, on the unit circle.
    """
    # Return angle in (-pi, pi]
    #trc_enter(f"spread_atan2({x}, {y})")
    angle = math.atan2(y, x)
    answer = spread_reduce_angle(angle)
    #trc_exit(f"spread_atan2 -> {answer}")
    return answer

def spread_compass_direction(angle: float) -> str:
    """
    Map angle, measured in radians, to closest of 8 compass direction strings:
    "west", "south west", "south", "south east", "east", "north east", "north",
    "north west".

    Args:
        angle (list[float]): Angles, measured in radians, on the unit circle.

    Returns:
        list[float]: New angles on the unit circle.
    """
    #trc_enter(f"spread_compass_direction({angle})")
    # Reduce the angle to the interval (-pi, pi]
    angle = spread_reduce_angle(angle)
    # Compute "compass" by:
    compass = (8.0 / math.pi) * angle
    # Determine the compass direction based on the reduced angle
    if compass <= -7:
        answer = "west"
    elif compass <= -5:
        answer = "south west"
    elif compass <= -3:
        answer = "south"
    elif compass <= -1:
        answer = "south east"
    elif compass <= 1:
        answer = "east"
    elif compass <= 3:
        answer = "north east"
    elif compass <= 5:
        answer = "north"
    elif compass <= 7:
        answer = "north west"
    else:
        answer = "west"
    #trc_exit(f"spread_compass_direction -> {answer}")
    return answer
