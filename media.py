#!/usr/bin/env python
import webbrowser


class Car():
    # creating a class with 4 elements
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]
    # This class created a new car object and sets its attributes

    def __init__(self, car_title, poster_image, trailer_youtube):
        self.title = car_title
        self.poster_img_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
