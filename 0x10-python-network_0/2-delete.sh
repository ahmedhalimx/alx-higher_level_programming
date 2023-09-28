#!/bin/bash
# script that sends a DELETE request to the given URL and displays the body of the response
curl -s "$1" -X DELETE
