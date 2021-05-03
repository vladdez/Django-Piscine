#!/bin/sh
curl -s $* | grep --extended-regexp --only-matching '(http|https)://[^/"]+'