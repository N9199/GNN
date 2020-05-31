#!/bin/sh
echo "1" >> WL/in
python3 WL/ConstructCounter.py < WL/in > WL/test
python3 WL/BuildSubGraphs.py < WL/test > WL/temp
python3 WL/WeisfelerLehman.py < WL/temp > WL/out
python3 WL/test.py < WL/out >> WL/out2
sed -i '.bu' '$d' WL/in
echo "2" >> WL/in