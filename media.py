#!/usr/bin/env python
import webbrowser


class Car():
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]
    # This class created a new car object and sets its attributes

    def __init__"
    "(self, car_title, car_storyline, poster_image, trailer_youtube):
        self.title = car_title
        self.storyline = car_storyline
        self.poster_img_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
