#!/bin/bash
# send POST request with parameters
curl -s -X POST "$1" -d "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD"
