from PIL import Image, ImageColor
from PIL import ImageDraw
from wavelength_to_rgb import wavelength_to_rgb as wl_to_rgb
from getting_wavelength import get_vector_wave_helium, get_vector_wave_hydrogen, get_vector_wave_lithium

width = 1000
height = 100

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)


for i in range(1000):
    x = int(i)
    draw.line((x, 0, x, height), fill=wl_to_rgb(i))

for i in get_vector_wave_lithium(1, 8):
    x = int(i)
    print(i)
    draw.line((x, 0, x, height), fill=(255, 255, 255))


# for i in get_vector_wave_lithium(1, 8):
#     x = int(i)
#     print(i)
#     draw.line((x, 0, x, height), fill=wl_to_rgb(i))

    # for i in get_vector_wave_lithium(2, 18):
    #     x = int(i)
    #     print(i)
    #     draw.line((x, 0, x, height), fill=wl_to_rgb(i))

elements_waves = [
    get_vector_wave_hydrogen,
    get_vector_wave_helium,
    get_vector_wave_lithium
]


# 1 –– Hydrogen
# 2 –– Helium
# 3 –– Lithium

# conter =
# for i in vec

image.save("empty.png", "PNG")
