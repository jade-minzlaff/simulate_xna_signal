import unittest
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from simulate_xna_signal import plot  

class TestPlotFunction(unittest.TestCase):

    def test_plot_generates_plot(self):
        # Test case to check if the plot function generates a plot

        # Arrange
        x = [1, 2, 3, 4, 5]
        y = [0.1, 0.2, 0.3, 0.4, 0.5]
        expected_image_path = 'expected_plot.png'

        # Act
        fig, ax = plt.subplots()
        plot(x, y)
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        plt.savefig(expected_image_path)

        # Assert
        # Load the expected image
        expected_image = plt.imread(expected_image_path)
        plt.close(fig)

        # Render the actual image
        fig, ax = plt.subplots()
        plot(x, y)
        canvas = FigureCanvasAgg(fig)
        canvas.draw()

        # Compare the images
        actual_image = canvas.renderer.buffer_rgba()
        plt.close(fig)

        self.assertTrue((expected_image == actual_image).all(), msg="The generated plot does not match the expected result")

if __name__ == '__main__':
    unittest.main()
