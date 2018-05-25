#!/usr/bin/env python
import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<html>
<head>
     <script src="https://code.jquery.com/jquery-1.12.3.min.js""
     "integrity="sha56-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css?family=Courgette""
        "rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/"
        "font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/"
        "css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/"
    "js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myVideo").modal("show");
        }
    </script>
    <title>Indian Sedon Cars</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 15%;
            /*justify-content: center;*/
        }
        body {
            margin: 20px;
        }

        header {
            color: #0000ff;
            background-color:  #ff6666;

            height: 1.5cm;
            margin: 0px, 0px, 0px, 0px;
            text-align: center;
            font-size: 40px;
            font-family: 'comic sans ms', cursive;
        }

        img {
            height: 400px;
            width: 400px;
        }
        .img1:hover,
        .img2:hover,
        .img3:hover,
        .img4:hover,
        .img5:hover,
        .img6:hover,
        .img7:hover,
        .img8:hover{
            background-color: #99ff99;
            visibility: visible;
            cursor: pointer;
            border-radius:3%;
        }
        .img1,.img2,.img3,.img4,.img5,.img6,.img7,.img8{
            float:left;
            margin-left:40px;
            padding:40px;
        }
    </style>
</head>

'''
main_page_content = '''
<body>
    <title>Indian Sedon Cars</title>
    <header><i> Indian Sedon Cars </i></header>
    <main>
        <div class="container">
            <div class="img1" onclick="changeVideo('8ORwzCqfkTo')">
                <img  src="http://www.loannow.in/wp-content/uploads/2015/01/"
                "next-generation-honda-city-2014.jpg" alt="Honda City">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <b>Honda City</b>
                </figcaption>
            </div>
            <div class="img2" onclick="changeVideo('JbA0u-OpoLw')">
                <img src="https://cars.usnews.com/static/images/Auto/izmo/"
                "i33960660/2018_mercedes_benz_e_class_angularfront.jpg""
                "alt="Mercedes Benz">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <b>Mercedes Benz</b>
                </figcaption>
            </div>
            <div class="img3" onclick="changeVideo('C0ktF5Ot1Ww')">
                <img src="https://images.cardekho.com/images/car-images/large/"
                "Hyundai/Verna/03.jpg" alt="Verna">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Verna</B>
                </figcaption>
            </div>
            <div class="img4" onclick="changeVideo('nGbFMRnlynw')">
                <img src="https://img.gaadicdn.com/images/car-images/large/"
                "Honda/Honda-Amaze/honda-amaze-urban-titanium-metallic.jpg""
                "alt="Amaze">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Amaze</B>
                </figcaption>
            </div>
            <div class="img5" onclick="changeVideo('wsGrHou5leU')">
                <img src="https://ymimg1.b8cdn.com/uploads/car_model/3994/"
                "logo/2018_Suzuki_Ciaz.jpg"alt="Ciaz">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Ciaz</B>
                </figcaption>
            </div>
            <div class="img6" onclick="changeVideo('8QraweGoIMs')">
                <img src="https://auto.ndtvimg.com/car-images/gallery/"
                "hyundai/xcent/exterior/hyundai-xcent-front.jpg"alt="Xcent">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Xcent</B>
                </figcaption>
            </div>
            <div class="img7" onclick="changeVideo('sl9zcOwTOpU')">
                <img src="https://auto.ndtvimg.com/car-images/colors/tata/"
                "zest/tata-zest-dune-beige.jpg?v="alt="Zest">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Zest</B>
                </figcaption>
            </div>
            <div class="img8" onclick="changeVideo('Ihsn6oLYegY')">
                <img src="https://img0.gaadicdn.com/images/car-images/"
                "large/Skoda/Skoda-Superb/047.jpg"alt=Skoda">
                <figcaption style="text-align: center; color: #cc33ff;">
                    <B>Skoda</B>
                </figcaption>
            </div>
        </div>
        <div class="modal fade" id="myVideo" tabindex="-1" role="dialog""
        "aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-body">
                        <iframe id="myframeY" width="550" height="350" src="""
                        "frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default""
                        "data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

'''
car_title_content = '''
<div class="modal fade" data-trailer-youtube-id="{trailer_youtube_id}""
"data-toggle="modal"data-transfer="#trailer">
    <img src="{poster_image_url}"width="220" height="342">
    <h2 style="color:white;">{car_title}</h2>
</div>
'''


def create_car_title_content(cars):
    content = ''
    for car in cars:
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', car.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', car.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        content += car_title_content.format(
            car_title=car.title,
            poster_image_url=car.poster_img_url,
            trailer_youtube_id=car.trailer_youtube_url
        )
    return content


def open_cars_page(cars):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    # Replace the car titles placeholder generated content
    rendered_content = main_page_content.format(car_title=create_car_title_content(cars))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # open the output file in the browser(in a new tab,if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
