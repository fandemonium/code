hmmalign -o rplB_1805_aligned.stk rplB.hmm fungene_8.1_rplB_1805_unaligned_protein_seqs.fa
esl-reformat --informat stockholm afa rplB_1805_aligned.stk > rplB_1805_aligned_aa.fa
java -jar ~/RDPTools/AlignmentTools.jar align-nucl-to-prot rplB_1805_aligned_na.fa fungene_8.1_rplB_1805_unaligned_nucleotide_seqs.fa rplB_1805_aligned_na.fa rplb_prot_to_nuc_aln.stat
