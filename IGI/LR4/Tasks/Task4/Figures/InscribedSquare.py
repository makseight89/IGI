import math
from PIL import Image, ImageDraw, ImageFont
from Tasks.Task4.Figures.ShapeColor import ShapeColor
from Tasks.Task4.Figures.Shape import Shape
from Tasks.MyMixin import MyMixin


class InscribedSquare(Shape, MyMixin):
    def __init__(self, radius, color: ShapeColor, text=""):
        self._radius = radius
        self._color = color
        self._square_side = math.sqrt(2) * radius
        self._text = text
        self._image = Image.new('RGB', (10, 10), 'white')

    def get_area(self):
        return self._square_side ** 2

    def __str__(self):
        return f"{self.__class__.__name__} shape, color: {self._color}, size: {self._square_side}, area: {self.get_area()}"

    def draw(self):
        image = Image.new('RGB', (2 * (self._radius + 10), 2 * (self._radius + 10)), 'white')
        draw = ImageDraw.Draw(image)
        font = None
        if __name__ != "__main__":
            font = ImageFont.truetype('OpenSans-Regular.ttf', size=14)

        draw.ellipse((10, 10, 2 * self._radius + 10, 2 * self._radius + 10), fill="white", outline='black', width=5)
        center = self._radius + 10
        square_start_point = center - self._square_side / 2
        square_end_point = center + self._square_side / 2
        draw.rectangle((square_start_point, square_start_point, square_end_point, square_end_point),
                       fill=self._color.color, outline='black')
        draw.text((center - 50, center - 50), self._text, font=font, fill='black')

        image.show()
        self._image = image

    def save(self):
        self._image.save('Task4.jpg')