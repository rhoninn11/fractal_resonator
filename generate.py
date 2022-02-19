from recursive_H_fractal import fractal_gen, DR
from proj_const import header,tail
import util


origin = {"x": 100, "y": 100}
fractal_points = []
fractal_points.append(fractal_gen(origin, 75, 4, DR["N"]))
svg = []
svg.append(header())
svg.append(util.points_2_path(fractal_points))
svg.append(tail())

result_svg = "".join(svg);

with open('result.svg', 'w') as file:
    file.write(result_svg)

fractal_len = util.calculate_path_length(fractal_points)
print(f'Fractal lines total length {fractal_len}')

