import math


def paint_calc(height, width, coverage):
    """This function takes in the height and width of a rectangular area in centimeters and also the coverage
    a single can of paint covers. It calculates how many cans of spray are needed to cover the whole area."""

    area = height * width
    num_of_cans = math.ceil(area/coverage)
    print(f"You'll need {num_of_cans} of cans to paint this rectangular area.")


if __name__ == "__main__":
    paint_calc(8, 4, 10)

