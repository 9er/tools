#! /bin/bash
#
# usage: backup.sh output gpg_id [FILE]...
#
# Backups files by stuffing them into a .tar.gz and encrypting it
# with your gpg key. If "output" is a directory, the filename will
# be "backup-$DATE.tar.gz.gpg".


# make sure we have enough params
if [ $# -lt 3 ]
then
    echo "usage: $0 output gpg_id [FILE]..."
    exit
fi

# output file
if [ -d "$1" ] ; then
    DATE=$(date "+%Y-%m-%d")
    BACKUP_FILE=`printf '%s\n' "${1%/}/backup-$DATE.tar.gz.gpg"`
else
    BACKUP_FILE="$1"
fi

shift


# gpg pubkey id for encryption (privkey needed for decryption)
GPG_ID="$1"

shift # get rid of the the gpg_id in the arguments


# files to backup: all remaining arguments
FILES=""
while test ${#} -gt 0
do
    FILES="$FILES $1"
    shift
done


# make sure tar is installed
if which tar > /dev/null; then
    TAR=`which tar`
else
    echo "tar not found"
    exit
fi


# make sure gpg is installed
if which gpg > /dev/null; then
    GPG=`which gpg`
else
    echo "gpg not found"
    exit
fi


# some status output
echo "settings:"
echo " - files to backup: $FILES"
echo " - gpg-id: $GPG_ID"
echo " - output-file: $BACKUP_FILE"


# go go go
echo "creating backup..."
$TAR -cz $FILES | $GPG --batch -e -r $GPG_ID -o $BACKUP_FILE
echo "done"
echo $(ls -lh "$BACKUP_FILE")
