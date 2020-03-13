#!/bin/bash

raspivid -n -w 1280 -h 720 -b 4500000 -fps 25 -vf -hf -t 0 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! gdppay ! tcpserversink host=127.0.0.1 port=5000