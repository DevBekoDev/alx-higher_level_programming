#!/bin/bash
# send JSON request to url and display body response
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
