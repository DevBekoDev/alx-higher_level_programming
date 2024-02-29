#!/usr/bin/env bash
# display body size from sent request to a url

curl -sw '%{size_download}\n' -o /dev/null "$1"
