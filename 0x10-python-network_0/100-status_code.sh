#!/bin/bash
# display only status code of response using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
