1. in docker, to run redbiom
```
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```

2. context list changes! get a list of context by this:
```
redbiom summarize contexts | cut -f 1,2,3 | grep 16S-v4 | sort -k 2 -n | cut -f 1 > ctx_list.txt
```

2. loop through different "context" (database of sequencing methods)
```
while read ctx; do redbiom search metadata "us|usa|USA|america" | redbiom fetch sample-metadata --context $ctx --output ${ctx//Pick_closed-reference_OTUs-/}.txt; done < ctx_list.txt
```

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

3. biom files do not contain sequences... don't even bother...
if you need the sequences, aka the biom files, do
```
redbiom search metadata "soil & europe where ph" | redbiom fetch samples --context Pick_closed-reference_OTUs-illumina-16S-v4-66f541 --output illumina-16S-v4-66f541_initial_pull.biom
``` 

4. usually, when I need to mine emp is becuase I need specific samples from a state of a country. not all sample metadata contain gps coordiantes. but many do. A quick way to find out if any of the metadata table pulled out form the context list contain log and lat:
```
grep "longitude" * | cut -d ":" -f 1 > files_with_lon_lat.txt
```

5. get a shape file for the specific region, states or countries. like this:
##State   longitude       latitude
##Alabama -88.473227      31.893856
##Alabama -88.468879      31.930262
##Alabama -88.46887438    31.93032335
##Alabama -88.46887426    31.93032507

6. run overlay script:
```
while read line; do Rscript /efs/home/fyang3/repos/R_code/rscripts/overlay_gps.R redbiom_context_meta/$line usa_gps_coord_state.txt "State" gps_overlay_meta/$line.us.overplayed.txt; done < files_with_lon_lat.txt 
```

