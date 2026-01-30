import math
def circle_coverage(radius1, radius2):
    if radius1<0 or radius2<0:
        return "Error, one or both radii invalid. Radius must be greater than zero."
    area1 = math.pi * (radius1**2)
    area2 = math.pi * (radius2**2)

    larger_area = max(area1, area2)
    smaller_area = min(area1, area2)

    percentage_covered = (smaller_area / larger_area) * 100
    return percentage_covered






