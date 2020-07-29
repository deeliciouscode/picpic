#!/bin/sh
PATH=${PATH}:/usr/bin/pip3
echo installing...
pip3 install wheel
pip3 install flask
pip3 install matplotlib
pip3 install numpy
pip3 install colormath
pip3 install flask_restful
pip3 install flask_cors
pip3 install requests
pip3 install pillow
pip3 install instagram-scraper
echo done.