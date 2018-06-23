fwd=$1
rev=$2

echo "grep -o -P '(?<="$fwd").*(?="$rev")' $3" 
