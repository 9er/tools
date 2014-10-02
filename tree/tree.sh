#!/bin/bash

pids=$(pgrep $1)

for pid in $pids; do
    echo $pid: `pstree -sA $pid`
done
