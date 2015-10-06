# find files by size range (c behind numbers indicate bites)
find . -size +640c -a -size -650c -print
find . -size +640c -a  -size -650c -exec ls -lh {} \;

# find files that are 0bites and delete
find . -type f -size 0b -delete
