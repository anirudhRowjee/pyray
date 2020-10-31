"""
PPM (Portable Pixel Map) Image Utilities
Author: Anirudh Rowjee
1. Create a file
2. Write list of list of pixel vectors to a file
3. Save the file
4. Read the file
"""


class ImageWriter:
    """
    ImageWriter Class
    write an image (MxN Vector Array) to a PPM file
    @param height => height of the image
    @param width => width of the image
    @param limit => maximum strength of a color (i.e 255, etc)
    """

    # TODO implement this function
    def normalize():
        pass

    def __init__(self, height=1, width=1, limit=255):
        """
        constructor method
        """
        self.height = height
        self.width = width
        self.limit = limit
        self.header = f"P3 {self.width} {self.height}\n{self.limit}\n"
