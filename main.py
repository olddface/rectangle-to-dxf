import ezdxf
import matplotlib.pyplot as plt

val1, val2 = int(input("masukan nilai pertama: ")), int(input("masukan nilai kedua: "))

#ask for length and width
length = max(val1, val2)
width = min(val1, val2)

print(f'width: {width}, length: {length}')


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.doc = ezdxf.new(dxfversion='R2010')
        self.msp = self.doc.modelspace()

    def get_coordinates(self):
        x0, y0 = 0, 0
        x1, y1 = x0 + self.length, y0 + self.width
        return x0, y0, x1, y1

    def preview_rectangle(self):
        x0, y0, x1, y1 = self.get_coordinates()
        x = [x0, x1, x1, x0, x0]
        y = [y0, y0, y1, y1, y0]

        plt.figure()
        plt.plot(x, y, "-k")
        plt.fill(x, y, alpha=0.2)
        plt.axis("equal")
        plt.title(f"Rectangle {width}x{length}")
        plt.savefig(f"./result/rectangle_{width}x{length}.png", dpi=300, bbox_inches="tight")
        plt.show()

    def export_to_dxf(self):

        x0, y0, x1, y1 = self.get_coordinates()
        self.msp.add_lwpolyline(
            [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
            close=True
        )
        self.doc.saveas(f"./result/rectangle_{self.width}x{self.length}.dxf")
        self.preview_rectangle()






rectObj = Rectangle(width, length)
rectObj.export_to_dxf()