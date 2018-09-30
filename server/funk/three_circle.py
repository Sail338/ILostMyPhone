import math

def three_circle_intersection(x0, y0, r0, x1, y1, r1, x2, y2, r2):
    # skipped some shit
    i = math.sqrt(2)
    d = 1
    j = 1
    x = ((r0**2) - (r1**2) + (d**2)) / (d*2)
    y = (((r0**2) - (r2**2) + (i**2) + (j**2)) / ((2*j) - (i*x))) / j
    return (x,y)

def get_user_location_by_response(rssia, rssib, rssic):

    return three_circle_intersection(0, 0, abs(rssia)/90, 1, 0, abs(rssib)/90, 0, 1, abs(rssic)/90)