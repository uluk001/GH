#! /usr/bin/env bash
# Get access to the secret link
secret_word=snickers
link=https://youtu.be/QtXby3twMmI?si=34W9pvRZDUQXV5xO

echo "Write the secret word: "
read user_input
while [ $secret_word != $user_input ]; do
	if [ $secret_word != $user_input ]; then
		echo "Secret is not correct, try one more time:"
		read user_input
	fi
done

echo "Oh! Great, you guessed the word, enjoy: $link"
