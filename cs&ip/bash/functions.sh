#! /usr/bin/env bash
# Get access to the secret link
secret_word="snickers"
link="https://youtu.be/QtXby3twMmI?si=34W9pvRZDUQXV5xO"

check_secret_with__retry() {
    local expected="$1"
    echo "Write the secret word: "
    read -r user_input
    while [ "$expected" != "$user_input" ]; do
        echo "Secret is not correct, try one more time:"
        read -r user_input
    done
    local result="$user_input"
    echo "$result"
}

check_secret_with__retry "$secret_word"

echo "Oh! Great, you guessed the word, enjoy: $link"
