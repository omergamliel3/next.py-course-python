class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        """
        _x - x coordinate
        _y - y coordinate
        _red - a value between 0 and 255
        _green - a value between 0 and 255
        _blue - a value between 0 and 255
        """
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def __repr__(self):
        unique_value = self.getUniqueColor()
        return f'Coords: (X:{self._x}, Y:{self._y}) ' + \
            f'Color: ({self._red},{self._green},{self._blue}) {unique_value}'

    def getUniqueColor(self):
        zero_values = 0
        unique_value = ''
        colors = {'Red': self._red, 'Green': self._green, 'Blue': self._blue}
        for (key, value) in colors.items():
            if value == 0:
                zero_values += 1
            elif value > 50:
                unique_value = key
        if zero_values == 2 and unique_value != '':
            return unique_value
        else:
            return ''

    def set_coords(self, x=0, y=0):
        self._x = x
        self._y = y

    def set_colors(self, red=0, green=0, blue=0):
        self._red = red
        self._green = green
        self._blue = blue

    def set_grayscale(self):
        avarage = (self._red + self._green + self._blue) // 3
        self._red = avarage
        self._green = avarage
        self._blue = avarage


def main():
    pixel = Pixel(10, 10, 0, 51, 0)
    print(pixel)
    pixel.set_grayscale()


if __name__ == "__main__":
    main()
