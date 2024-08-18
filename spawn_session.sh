#!/bin/bash

env_file=.env

while getopts ":he:" opt; do
    case "$opt" in
        h)
            echo "Usage: $0 [-h] [-e path_to_env_file]"
            exit 0
            ;;
        e)
            env_file="$OPTARG"
            ;;
        :)
            echo "Option -$OPTARG requires an argument."
            exit 1
            ;;
    esac
done

if [ ! -f "$env_file" ]; then
    echo "Error: Environment file '$env_file' not found."
    exit 1
else
    export $(cat $env_file | xargs)
fi

python alert.py --id $API_ID --hash $API_HASH --phone $PHONE_NUMBER --channel $CHANNEL_USERNAME --group $GROUP_USERNAME --keyword "$KEYWORDS"