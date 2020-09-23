# Program classifies each color and outputs it to a file
from random import randint
from collections import Counter
import csv

dataset_filename = "colors.csv"

# A generator that loads CSV data and converts it into a format that is controllable
def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            line = "".join(line)
            line = line.split()
            label, hex_color = line
            yield (hex_to_rgb(hex_color), label)

def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i : i + 2], 16) for i in range(1, 6, 2))


def generate_colors(count=100):
    for i in range(count):
        yield (randint(0, 255), randint(0, 255), randint(0, 255))

def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
    return sum_distance_squared

def nearest_neighbors(model_colors, target_colors, num_neighbors=5):
    model_colors = list(model_colors)
    
    for target in target_colors:
        distances = sorted(
            ((color_distance(c[0], target), c) for c in model_colors)
        )
        yield target, distances[:5]
        
def name_colors(model_colors, target_colors, num_neighbors=5):
    for target, near in nearest_neighbors(
        model_colors, target_colors, num_neighbors=5
    ):
        print(target, near)
        name_guess = Counter(n[1] for n in near).most_common()[0][0]
        yield target, name_guess

def write_results(colors, filename="output.csv"):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for (r, g, b), name in colors:
            writer.writerow([name, f"#{r:02x}{g:02x}{b:02x}"])

def process_colors(dataset_filename="colors.csv"):
    model_colors = load_colors(dataset_filename)
    colors = name_colors(model_colors, generate_colors(), 5)
    write_results(colors)
    
if __name__ == "__main__":
    process_colors()