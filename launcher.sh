#!/bin/bash

echo "MacGoalNC Version-1.0 (C)Sayan Das(2015)"
echo "Update you with live soccer match score from goal.com. You have to just enter the URL of the match"
echo "NOTE: Support only goal.com links"
echo "eg.http://www.goal.com/en-india/match/wellington-phoenix-vs-melbourne-victory/1697681?ICID=LS"
echo "Enter the URL:"

read URL
python main.py $URL