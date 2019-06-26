1. to use bwa for mapping, create a bwa index: 
	```
	bwa index -p /PATH/TO/DIR/index_prefix full_length_derep.fasta
	```

2. bwa mapping:  
	```
	bwa mem /PATH/TO/DIR/index_prefix a_seq_file.fq | grep 'NM:i:0' | cut -f 1,3,4,6,13 > /PATH/TO/STORE/no_mismatch/a_seq_file_mapped.bwa
	```

3. then need to split the cigar and evaluate the hanging position. I did this in R originally. But could be modified in python... maybe easier... 
	```
	R
	library(dplyr)
	bwa <- read.delim("/A/FILE/FROM/STEP2", header = F)
	names(bwa) <- c("seq_name", "strain_id", "clip_index", "cigar", "mismatch_position")
	bwa_m <- subset(bwak grepl("M$", cigar))
	if (dim(bwa_m)[[1]] == 0) {
		print("No desired matched found!")
	} else {
	test <- data.frame(do.call('rbind', strsplit(as.character(bwa_m$cigar), "[A-Z")))
	test <- mutate_all(test, function(x) as.numeric(as.character(x)))
	test[, 3:4] <- data.frame(do.call('rbind', gregexpr(pattern="[A-Z]", as.character(bwa_m$cigar))))
	names(test) <- c("first_len", "match_len", "first_index", "match_index")
	
	test$first_len <- ifelse(test$first_index == test$match_index, 0, as.numeric(as.character(test$first_len)))
	test$match_len <- as.numeric(as.character(test$match_len))
	
	bwa_m <- data.frame(bwa_m, test)
	
	bwa_m_perfect <- subset(bwa_m, clip_index==1 | first_index==match_index) %>% filter(match_len>= 100)
	##
	## then one can adjust the length of the overhang and match as needed or save to file"
	```


