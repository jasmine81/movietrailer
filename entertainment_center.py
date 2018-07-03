#!/usr/bin/env python
import media  # importing packages
import fresh_tomatoes  # importing packages
# creating variables
hondacity = media.Car("Honda City", "luxury",
                      "http://www.loannow.in/wp-content/uploads"
                      "/2015/01/next-gen"
                      "eration-honda-city-2014.jpg",
                      "https://www.youtube.com/embed/8ORwzCqfkTo")
mercedesbenz = media.Car("Mercedes Benz", "comfort",
                         "https://cars.usnews.com/static/images/Auto/izmo/i33"
                         "960660/2018_mercedes_benz_e_class_angularfront.jpg",
                         "https://www.youtube.com/embed/JbA0u-OpoLw")
verna = media.Car("Verna", "happiness",
                  "https://images.cardekho.com/images/car-images/large"
                  "/Hyundai/Verna/03.jpg",
                  "https://www.youtube.com/embed/HmIBqEW3B8o")
amaze = media.Car("Amaze", "smilingface car",
                  "https://img.gaadicdn.com/images/car-images/large/Honda/"
                  "Honda-Amaze/honda-amaze-urban-titanium-metallic.jpg",
                  "https://www.youtube.com/embed/DasUUC2eCD8")
ciaz = media.Car("Ciaz", "posh",
                 "https://ymimg1.b8cdn.com/uploads/car_model/3994/logo/"
                 "2018_Suzuki_Ciaz.jpg",
                 "https://www.youtube.com/embed/wsGrHou5leU")
xcent = media.Car("Xcent", "enjoyment",
                  "https://auto.ndtvimg.com/car-images/gallery/hyundai/xcent/"
                  "exterior/hyundai-xcent-front.jpg",
                  "https://www.youtube.com/embed/8QraweGoIMs")
zest = media.Car("Zest", "tour",
                 "https://auto.ndtvimg.com/car-images/colors/tata/zest/tata"
                 "-zest-dune-beige.jpg?v=",
                 "https://www.youtube.com/embed/sl9zcOwTOpU")
skoda = media.Car("Skoda", "stylish",
                  "https://img0.gaadicdn.com/images/car-images/large/Skoda/"
                  "Skoda-Superb/047.jpg",
                  "https://www.youtube.com/embed/Ihsn6oLYegY")
cars = [hondacity, mercedesbenz, verna, amaze, ciaz, xcent, zest, skoda]
# creating a list
fresh_tomatoes.open_cars_page(cars)
# calling function by passing cars as parameters
