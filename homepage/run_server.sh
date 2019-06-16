#!/bin/bash

sudo iptables -t nat -A PREROUTING -i enp2s0 -p tcp --dport 80 -j REDIRECT --to-port 5000

./app.py
