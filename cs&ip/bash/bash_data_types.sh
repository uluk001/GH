#! /bin/bash/
first_name="Erlich"
last_name="Bakhman"
full_name="$first_name $last_name"

echo "Hello, $full_name"

num1=5
num2=10
sum=$((num1+num2))
product=$((num1*num2))

echo "$product"


fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
  echo $fruit
done



declare -A colors
colors[apple]="red"
colors[banana]="yellow"
colors[grape]="purple"
unset colors[banana]
echo ${colors[apple]} # red
echo ${colors[grape]} # purple

