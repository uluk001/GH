#! /usr/bin/env bash
# Get access to the secret link
secret_word="snickers"
link=https://youtu.be/QtXby3twMmI?si=34W9pvRZDUQXV5xO

check_secret_with__retry() {
	echo "Write the secret word: "
	read user_input
	while [ $1 != $user_input ]; do
	        if [ $1 != $user_input ]; then
	                echo "Secret is not correct, try one more time:"
	                read user_input
	        fi
	done
	local result=$1=$user_input
	echo $result
}

(check_secret_with__retry $secret_word)

echo "Oh! Great, you guessed the word, enjoy: $link"
