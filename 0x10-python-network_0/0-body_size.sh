#!/bin/bash
# display the size of the response body in bytes
curl -s -I 0.0.0.0:5000 | grep "^Content-Length:" | cut -c17-
