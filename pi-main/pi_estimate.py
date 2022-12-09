"""Estimate the value of Pi with Monte Carlo simulation.
Author:  Arya Krishnagiri
Credits:  TBD
"""
import random
import doctest
import points_plot


GOOD_PI = 3.141592653589793  # A very good estimate, from math.pi
SAMPLES = 5000   # More =>  more precise, but slower


def in_unit_circle(x: float, y: float) -> bool:
    """Returns True if and only if (x,y) lies within the circle
    with origin (0,0) and radius 1.0.
    """
    return (x*x + y*y) < 1.0


def  rand_point_unit_sq() -> tuple[float, float]:
    x = random.random()
    y = random.random()
    return x, y


def plot_random_points(n_points: int = 5000):
    points_plot.init()
    for i in range(n_points):
        x, y = rand_point_unit_sq()
        points_plot.plot(x, y, color_rgb=(255, 10, 10))
    points_plot.wait_to_close()
        

def relative_error(est: float, expected: float) -> float:
    abs_error = est - expected
    rel_error = abs(abs_error / expected)
    return rel_error


def pi_approx() -> float:
    total_tried = 0
    total_in_circle = 0
    for i in range(SAMPLES):
        x, y = rand_point_unit_sq()
        total_tried += 1
        if in_unit_circle(x,y) == True:
            points_plot.plot(x, y, color_rgb=(255, 10, 10))
            total_in_circle += 1
        else:
             points_plot.plot(x, y, color_rgb=(240, 240, 240))
    ratio_t = (total_in_circle / total_tried)*4
    return ratio_t
    

def main():
    doctest.testmod()
    # points_plot.init() # Enables plotting
    points_plot.init()
    estimate = pi_approx()
    print(f"Pi is approximately {estimate}")
    points_plot.wait_to_close()


if __name__ == "__main__":
    main()
