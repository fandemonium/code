####################################################################
#### RAST annotation plot was done in R 3.2+              ##########
#### 3 steps: 						  ##########
#### 1. finalize RAST annotation table			  ##########
#### 2. finalize RAST taxonomy table     		  ##########
#### 3. plot using ggplot2 				  ##########
####################################################################
library(plyr)
library(ggplot2)

####################################################################
#### 1. finalize RAST annotation table			  ##########
####################################################################
## determine the unique subsystem level 1 annotations and compare them to subsystem level 1 from Json file to eliminate inconsistant annotation namings
unique(rast$T1)
rast$T1<-gsub("^Virulence$", "Virulence, Disease and Defense", rast$T1)
rast$T1<-gsub("^Cell Division$", "Cell Division and Cell Cycle", rast$T1)
rast$T1<-gsub("^Prophage$", "Phages, Prophages, Transposable elements, Plasmids", rast$T1)
rast$T1<-gsub("^Phages, Prophages, Transposable elements$", "Phages, Prophages, Transposable elements, Plasmids", rast$T1)
## to confirm all subsystem level 1 inconsistance are corrected
unique(rast$T1)

## rast annotations contain lots of duplicated information due to inconsistant naming that should be combined to eliminate false counts.
## first, remove any duplicated rows where fig id (gene id) and gene names are repeated
rast_derep_fig_gene<-rast[!duplicated(rast[, c("fig", "gene")]), ]
## then, remove any duplicated rows where fig id and annotation descriptions are repeated
rast_derep_fig_gene_desc<-rast_derep_fig_gene[!duplicated(rast_derep_fig_gene[, c("fig", "desc")]), ]
## finally, remove any duplicated rows where fig id and subsystem level 1 (T1) annotation are repeated
rast_derep_fig_gene_desc_T1<-rast_derep_fig_gene_desc[!duplicated(rast_derep_fig_gene_desc[, c("fig", "T1")]), ]
## finally check the dimension of the annotation table
## the number of rows should be much closer to the number of unique fig id
dim(rast_derep_fig_gene_desc_T1)


####################################################################
#### 2. finalize RAST taxonomy table     		  ##########
####################################################################
## read in taxonomy table
## because the taxonomy was taken directly from genbank file, some rows have more columns appears later in the taxonomy file
## R read.table determines the number of columns by the first 5 rows, unless specified
## first find out the longest line in your file and determine the most number of columns needed
## to specify the number of columns, we assign each column with names
cn<-paste("V", 1:12, sep="")
## because the first columns are rast.id, R read.table automatically considers it number, which changes the original RAST id slightly (eg., XXX.10 becomes XXX.1). To avoid any complication, we declare the column class for the first column as character
taxa<-read.table("refsoil_v1.1_rastID_to_gb_taxonomy.txt", sep="\t", header=F, comment.char="", quote="", fill=T, col.names=cn, colClasses=c("V1"="character"))
## check the read-in taxa table's dimension
dim(taxa)
## check the structure of the first column
str(taxa$V1)
## rename the columns that are consistant across all rows, column names start with "V" need to be fixed downstream
names(taxa)<-c("rast_id", "ncbi_acc", "ncbi_desc", "strain", "Domain", "Phylum", "Class", "Order", "Family", "V10", "V11", "V12")

## find all rows with empty V10 cells, and the non-empty V10 cells
test<-subset(taxa, V10=="")
taxa.1<-subset(taxa, V10!="")
## check dimension
dim(taxa.1)
dim(taxa)
dim(test)
## rows with non-empty V10 cells have extra columns of bacteria group/complex information
## identify misclassified hierarchy levels (in this case, "XXXales" in Class level
test.1<-subset(test, grepl("ales$", Class))
dim(test.1)
test.2<-subset(test, !grepl("ales$", Class))
dim(test.2)
## Class identification for these rows are also missing. Renaming one of the empty column as Class for this particular group
colnames(test.1)[7:9]<-c("Order", "Family", "Class")
test.1$Class<-NULL
colnames(test.1)[9]<-"Class"
## directly obtain genus and species information from strain description
test$Genus<-data.frame(do.call('rbind', strsplit(as.character(test.1$strain), " ", fixed=T)))[, 1]
test$Species<-data.frame(do.call('rbind', strsplit(as.character(test.1$strain), " ", fixed=T)))[, 2]
test.1$Genus<-data.frame(do.call('rbind', strsplit(as.character(test.1$strain), " ", fixed=T)))[, 1]
test.1$Species<-data.frame(do.call('rbind', strsplit(as.character(test.1$strain), " ", fixed=T)))[, 2]
## remove columns that may contain misleading information
test.1<-test.1[, -c(10:11)]
dim(test.1)
head(test.1)
## for the rows that do not have missing Class, identify any organisms that do not have complete taxonomy infomation
test.2[test.2$Class=="", ]
## in this case, they were all Thermobaculum
taxa[taxa$Phylum=="Thermobaculum", ]
subset(taxa, grepl("Thermobaculum", strain))
## subset to fix again
test.3<-test.2[test.2$Class=="", ]
test.3
dim(test.2)
test.2<-test.2[test.2$Class!="", ]
dim(test.2)
## manually fix the classification
test.3$Phylum<-"Chloroflexi"
names(test.1)
test.3$V12<-NULL
test.3
colnames(test.3)[10:11]<-c("Genus", "Species")
test.3
test.3$Genus<-data.frame(do.call('rbind', strsplit(as.character(test.3$strain), " ", fixed=T)))[, 1]
test.3$Species<-data.frame(do.call('rbind', strsplit(as.character(test.3$strain), " ", fixed=T)))[, 2]
test.3
## check all dimensions of subset tables
dim(taxa.1)
dim(test.1)
dim(test.2)
dim(test.3)
dim(test)
head(test.2)
test.2$V12<-NULL
colnames(test.2)[10:11]<-c("Genus", "Species")
test.2$Genus<-data.frame(do.call('rbind', strsplit(as.character(test.2$strain), " ", fixed=T)))[, 1]
test.2$Species<-data.frame(do.call('rbind', strsplit(as.character(test.2$strain), " ", fixed=T)))[, 2]
## recombine parts
test<-rbind(test.1, test.2, test.3)
dim(test)
colnames(taxa.1)[10:11]<-c("Genus", "Species")
taxa.1$V12<-NULL
taxa.1$Genus<-data.frame(do.call('rbind', strsplit(as.character(taxa.1$strain), " ", fixed=T)))[, 1]
taxa.1$Species<-data.frame(do.call('rbind', strsplit(as.character(taxa.1$strain), " ", fixed=T)))[, 2]
## recombine parts to full taxa table
taxa<-rbind(taxa.1, taxa.2)
dim(taxa)
## make sure no empty Phylum cells
taxa[taxa$Phylum=="", ]
## write fixed taxa data.frame to file
write.table(taxa, "refsoil_v1.1_rastID_to_gb_taxonomy_fixed.txt", sep="\t", row.names=F, quote=F)

## merge taxa information onto rast annotations
rast_derep_fig_gene_desc_T1_w_taxa<-merge(rast_derep_fig_gene_desc_T1, taxa, "rast_id")
dim(rast_derep_fig_gene_desc_T1_w_taxa)
dim(rast_derep_fig_gene_desc_T1)

## because RAST subsystem level 1 contains categories that are not informative, such as "NA", "cluster based" etc, we need to construct a different data.frame for plotting
names(rast_derep_fig_gene_desc_T1_w_taxa)
to_plot<-rast_derep_fig_gene_desc_T1_w_taxa[, c("rast_id", "fig", "TaxID", "T1", "Phylum", "strain")]

## consider each row as one gene count, do not use "1", which would make it a character
to_plot$count<-1
## condense data.frame by Phylum to identify the percentage of genes were identified with multiple annotations
refsoil_phyla<-ddply(to_plot, .(Phylum), summarize, total_uniq_genes=length(unique(fig)), total_genes=sum(count))
refsoil_phyla$percent_multifunction<-100*(refsoil_phyla$total_genes-refsoil_phyla$total_uniq_genes)/refsoil_phyla$total_uniq_genes
## reorder Phylum by total # of unique genes in reverse order
refsoil_phyla$Phylum<-reorder(refsoil_phyla$Phylum, -refsoil_phyla$total_uniq_genes)

## condense data.frame by subsystem level 1, and eliminate unwanted categories
refsoil_T1<-ddply(to_plot, .(T1), summarize, total_genes=sum(count))
refsoil_T1
to_plot<-subset(to_plot, !grepl("Clustering-based subsystems|Experimental Subsystems|Experimental Subsystems|Miscellaneous", T1) & !is.na(T1))
unique(to_plot$T1)


## Final rast plot is consisted of two pannels: A. the phylum distribution of subsystem level 1 genes; B. the phylum distribution of RefSoil genes (database)
to_plot.a<-ddply(to_plot, .(T1, Phylum), summarize, gene_counts=sum(count))
########### frame A ##########
## Add total gene counts for each subsystem level 1 category and calculate the percent phylum abundance in each category
to_plot.a<-merge(to_plot.a, refsoil_T1, "T1")
to_plot.a$percent<-100*(to_plot.a$gene_counts/to_plot.a$total_genes)
## Define the plotting frame A
to_plot.a$frame<-"A"
########### frame B ##########
## frame B is the phyla distribution of RefSoil dataset
to_plot.b<-refsoil_phyla
## Define the plotting frame B
to_plot.b$frame<-"B"
## Define an arbutrary T1 category for RefSoil so frame A and frame B can be combined into one data frame.
to_plot.b$T1<-"RefSoil"
## Calculate the percent gene abundance of each phya in RefSoil dataset 
to_plot.b$percent<-100*(to_plot.b$total_uniq_genes/sum(to_plot.b$total_uniq_genes))
head(to_plot.b)
########### combine frame A and frame B ##########
to_plot.final<-rbind(to_plot.a[, c("T1", "Phylum", "percent", "frame")], to_plot.b[, c("T1", "Phylum", "percent", "frame")])
## check dimensions
dim(to_plot.final)
dim(to_plot.a)
dim(to_plot.b)


####################################################################
#### 3. plot using ggplot2 				  ##########
####################################################################
## to plot with specific order, data frame factors must be reordered based on a previously defined order. 
to_plot.final$Phylum<-factor(to_plot.final$Phylum, levels=levels(refsoil_phyla$Phylum))
## from refsoil_phyla, we can identify Proteobacteria is the most abundant phyla
## sort subssystem level 1 display order by their abundance in Proteobacteria
proteo_T1<-subset(to_plot.final, grepl("Proteobac", Phylum))
proteo_T1<-ddply(proteo_T1, .(T1), summarize, proteo_genes=sum(count))
proteo_T1$T1<-reorder(proteo_T1$T1, -proteo_T1$percent)
to_plot.final$T1<-factor(to_plot.final$T1, levels=c(levels(proteo_T1$T1), "RefSoil"))
## check structure of the data frame to be plotted
str(to_plot.final)

## define customized color pallete
colors<-c("#3E4627", "#6A96CD", "#824625", "#C84456", "#7B3472", "#C3C3CD", "#578D6E", "#413D67", "#D050B9", "#5CF933", "#C755DF", "#D44D2A", "#596C76", "#D2478A", "#CBC590", "#5BF5FB", "#562732", "#618935", "#CD953C", "#D0D548", "#766CCE", "#7EDB95", "#C8877E", "#C98EC3")

## Reordering factor levels is sufficient for ggplot2 version<2.0. However, ggplot2 version 2.0+ removed the ordering functions. When using geom_bar(stat="identity"), only legend display would be reordered, while the stacked bars would be left as how they were displayed in data.frame

## work around: specify data.frame item order according to the levels using "dplyr", ie., sort character items as numberic items 
library(dplyr)
p1<-to_plot.final %>% ungroup() %>% arrange(as.integer(Phylum)) %>% ggplot(aes(x=T1, y=percent, fill=Phylum, color=Phylum, order=Phylum))
p2<-p1+geom_bar(stat="identity")+theme_bw()
p3<-p2+scale_fill_manual(values=colors)+scale_color_manual(values=colors)
p4<-p3+facet_grid(~frame, scales="free", space="free")+guides(fill = guide_legend(reverse=TRUE), color=guide_legend(reverse=T))
p5<-p4+theme(axis.text.x=element_text(angle=90, hjust=1, vjust=0.5, size=12), axis.text.y=element_text(size=12))
p6<-p5+scale_x_discrete(name="") + scale_y_continuous(name="Percent Contribution (%)") +theme(axis.title.y=element_text(face="bold", size=14))
p7<-p6+theme(strip.text.x=element_text(face="bold", size=12))+theme(strip.background=element_rect(size=1.2, color="black"))+theme(panel.border=element_rect(size=1.2, color="black"))
p8<-p7+theme(legend.title= element_text(size=12, face="bold"), legend.text = element_text(size=12))
## save to file
pdf("refsoil_v1.1_rast_T1_phyla_sort_by_proteo_w_databasebias_facet.pdf", width=10, height=12)
## invert legend display order to match with stacked bars
p8+guides(colour = guide_legend(ncol = 1, reverse=T), fill = guide_legend(ncol = 1, reverse=T))
dev.off()

