"""creating a class describing about a car
    Args:
      car_title: name of the picture to which it related to
      poster_image: URL of an image displayed on the screen
      trailer_youtube:  link of the vedio to be palyed
    Methods:
      show_tariler: to play the vedio"""
# !/usr/bin/env python
import webbrowser


class Car():
    # creating a list of 4 elements
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]
    # This class created a new car object and sets its attributes

    def __init__(self, car_title, poster_image, trailer_youtube):
        self.title = car_title
        self.poster_img_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
