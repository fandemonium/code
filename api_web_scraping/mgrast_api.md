1. searching by keyword:
```
http://api.metagenomics.anl.gov/search?all=neon&index=metagenome_index&limit=1000
```
default has a limit of 10. upper limit is 1000. But it has the next url at the bottom of the output. the limit tag in the url does not work on wget and curl. don't know why. 

for more options see: `http://api.metagenomics.anl.gov/`
