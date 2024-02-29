#!/bin/bash
# display body size from sent request to a url
curl -s "$1" | wc -c
