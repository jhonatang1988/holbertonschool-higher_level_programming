#!/bin/bash
# display all available methods
curl -s -I -X OPTIONS "$1" | grep "^Allow:" | cut -c8-
