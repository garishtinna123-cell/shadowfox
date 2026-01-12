# 1. Format function
def format_number(num, fmt):
    return format(num, fmt)

print(format_number(145, 'o'))   # octal representation


# 2. Area of circular pond and total water
pi = 3.14
radius = 84

area = pi * radius * radius
print(int(area))                 # area without decimal

water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter
print(int(total_water))          # total water without decimal


# 3. Speed calculation
distance = 490                   # meters
time = 7 * 60                    # seconds

speed = distance / time
print(int(speed))                # speed without decimal