def find_complementary_color(HEX_color):
    red = int(HEX_color[1:3], 16)
    green = int(HEX_color[3:5], 16)
    blue = int(HEX_color[5:7], 16)
    complementary_red = 255 - red
    complementary_green = 255 - green
    complementary_blue = 255 - blue
    complementary_hex_color = '#{:02x}{:02x}{:02x}'.format(complementary_red, complementary_green, complementary_blue)

    return complementary_hex_color


color = "#00a3a6"
complementary_color = find_complementary_color(color)
print(complementary_color)
