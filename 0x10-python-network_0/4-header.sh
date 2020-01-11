#!/bin/bash
# sends a GET requests with a custom header
curl -s -X GET "$1" -H "X-HolbertonSchool-User-Id:98"
