#!/bin/bash
# display the size of the response body in bytes
curl -s -I $1 | grep "^Content-Length:" | cut -c17-
