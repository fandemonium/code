#!/bin/bash

url1='some_api_url_1'
url2='some_api_url_2'
url3='some_api_url_3'

header="authorization: Bearer "

usage () {
	echo "Usage: $0 [-d <text1|text2|text3>] [-b <token>] [-i <some_id|some_cat?]"
	}

while getopts ":d:b:i:" opt; do
	case $opt in
		d)
			if [ $OPTARG = "text1" ]; then
				domain="$url1"
			elif [ $OPTARG = "text2" ]; then
				domain="$url2"
			elif [$OPTARG = "text3" ]; then
				domain="$url3"
			else
				echo "unknown option"
				exit 1
			fi
			;;
		b)
			token=$OPTARG
			oauth=$header$token
			;;
		i)
			input=${OPTARG// /%20}
			;;
		\?)
			echo "Invalid option: -$OPTARG"
			exit 1
			;;
		:)
			echo "Option -$OPTARG requires an argument"
			exit 1
		;;
	esac
done

url=$domain$input

curl --request GET \
	--url $url \
	--header "$oauth"

