# converting python 2 to python 3 code:
1. can do it in batch as an entire folder
```
mkdir DIR
2to3 -o DIR -W -n PY2DIR
```

2. can be used with find for any py2 scripts: the below code will find any file ending with ".py", then convert them to py3 code written to new file with "py3" as suffix. Note: it is a bit of dumb... you will end up with files end with ".pypy3". 
```
find . -type f -name "*.py" | xargs 2to3 -n -W --add-suffix="py3" {}
```
