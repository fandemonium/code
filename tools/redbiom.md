1. in docker, to run redbiom
```
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```

2. loop through different "context" (database of sequencing methods)
```
while read context; do redbiom search metadata "soil & europe where ph" | redbiom fetch sample-metadata --output ${context//Pick_closed-reference_OTUs-/}.txt --context $context; done < ctx_list.txt 
```

####ctx_list.txt:
####Pick_closed-reference_OTUs-illumina-16S-v45-66f541
####Pick_closed-reference_OTUs-flx-16S-v4-66f541
####Pick_closed-reference_OTUs-ls454-16S-v4-66f541
####Pick_closed-reference_OTUs-titanium-16S-v46-66f541
####Pick_closed-reference_OTUs-titanium-16S-v4-66f541
####Pick_closed-reference_OTUs-illumina-16S-v4-66f541

3. if you need the sequences, aka the biom files, do
```
redbiom search metadata "soil & europe where ph" | redbiom fetch samples --context Pick_closed-reference_OTUs-illumina-16S-v4-66f541 --output illumina-16S-v4-66f541_initial_pull.biom
``` 
