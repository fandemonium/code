args<-commandArgs(TRUE)

env<-read.delim(args[1], sep='\t', header=T)
map<-read.delim(args[2], sep='\t', header=F)

names(map)<-c("ID_Miseq_ID", "SAMPLES")

env_16s<-merge(env, map, "ID_Miseq_ID")

write.table(env_16s, file=args[3], sep='\t', row.names=F, quote=F)
