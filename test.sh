# to read a line
file_name="definitions.txt"
line_number=2
line=$(sed "${line_number}!d" "$file_name")
read -a text <<< "$line"
echo ${text[*]}
