#!/bin/bash
# display allowed headers from the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
