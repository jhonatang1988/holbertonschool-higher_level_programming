#!/bin/bash
# sends a json post request using curl and get the response body
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
