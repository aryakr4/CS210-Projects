"""Summarize a path in a map, using the standard Ramer-Douglas-Peucher (aka Duda-Hart)
split-and-merge algorithm.
Author: Arya Krishnagiri
Credits: TBD
"""

import csv
import doctest

import geometry
import map_view
import config

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def read_points(path: str) -> list[tuple[float, float]]:
    final = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for x in reader:
            easting = float(x["Easting"])
            northing = float(x["Northing"])
            final.append((easting, northing))
        
    return final
    


def summarize(points: list[tuple[float, float]],
              tolerance: int = config.TOLERANCE_METERS,
              ) -> list[tuple[float, float]]:
    summary: list[tuple[float, float]] = [points[0]]
    epsilon = float(tolerance * tolerance)
    """>>> path = [(0,0), (1,1), (2,2), (2,3), (2,4), (3,4), (4,4)]
     >>> expect = [(0,0), (2,2), (2,4), (4,4)]
     >>> simple = summarize(path, tolerance=0.5)
     >>> simple == expect
     True"""
    def simplify(start: int, end: int):
        """Add necessary points in (start, end] to summary."""
        if end - start > 2:
            map_view.scratch(points[start], points[end])

        worst = 0
        bad_index = 0
        for x in range(start, end):
            d = geometry.deviation_sq(points[start], points[end], points[x])
            if d > worst:
                bad_index = x
                worst = d
        if worst > epsilon:
            simplify(start, bad_index)
            simplify(bad_index, end)
        if worst <= epsilon:
            summary.append(points[end])
    simplify(0, len(points) - 1)
    return summary
    


def main():
    points = read_points(config.UTM_CSV)
    map_view.init()
    for point in points:
        map_view.plot_to(point)
    map_view.clean_scratches()
    print(f"{len(points)} raw points")
    summary = summarize(points, config.TOLERANCE_METERS)
    print(f"{len(summary)} points in summary")
    map_view.wait_to_close()


if __name__ == "__main__":
    doctest.testmod()
    print("Tested")
    main()



