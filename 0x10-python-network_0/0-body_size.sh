#!/usr/bin/env bash
# display the size of the response body in bytes
if [[ $# -ne 1 ]]; then
    exit 1;
else
    res=$(curl -s -I 0.0.0.0:5000 | grep "^Content-Length:" | cut -c17-)
    echo "$res"
fi
