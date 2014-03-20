#!/bin/bash
#
# usage: ping.sh target
#
# Pings a target once a second. As soon as the target replies, it plays a
# *pling* sound and exits.
#
# *pling*-sound is from jobro on freesound.org
# http://freesound.org/people/jobro/sounds/180894/


# check if a target is specified
if [ $# -eq 0 ]
then
    echo "usage: $0 target"
    exit
fi

# action on ^C
control_c()
{
    exit
}

trap control_c SIGINT


# which audio player?
if which mpv > /dev/null; then
    PLAYER="mpv --really-quiet"
elif which mplayer > /dev/null; then
    PLAYER="mplayer -really-quiet"
elif which cvlc > /dev/null; then
    PLAYER="cvlc --quiet --play-and-exit"
else
    echo "please install mpv, mplayer or vlc"
    exit
fi


cd "$(dirname "$0")"

# main loop
while true
do
    # ping once every second
    if ping -c 1 -w 1 $1 > /dev/null
    then
        # play a sound when the target respons
        $PLAYER sound/180894_35187-lq.mp3
        break
    fi
done
