#!/bin/bash
# display status code from a response
curl -s -o /dev/null -w "%{http_code}" "$1"
