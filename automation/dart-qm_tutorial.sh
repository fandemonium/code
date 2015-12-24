NAME="rplB"
## all pathways need to be in full path ##
OUT_DIR="/mnt/data3/fan/dart-qm/tutorial_stuff/test"
HMMER="/home/ubuntu/hmmer_3.1/binaries"
RDPTOOLS="/home/ubuntu/RDPTools"
CLUSTALO="/home/ubuntu/clustalo_1.2.0"

if [ $# == 3 ]; then
  echo "Using hmmer for alignment ..."
  ## $1 as protein hmm model, $2 as the protein sequence in fa
  $HMMER/hmmalign -o $OUT_DIR/$NAME.hmm_aln.aa.stk $1 $2  
  $HMMER/esl-reformat --informat stockholm afa $OUT_DIR/$NAME.hmm_aln.aa.stk > $OUT_DIR/$NAME.hmm_aln.aa.fa
  java -jar $RDPTOOLS/AlignmentTools.jar align-nucl-to-prot $OUT_DIR/$NAME.hmm_aln.aa.fa $3 $OUT_DIR/$NAME.hmm_aln.na.fa $OUT_DIR/$NAME.hmm_aln.na.stat
  exit
fi

if [ $# == 1 ]; then
  echo "Aligning nucleotide sequences using clustal omega ..."
  $CLUSTALO -i $1 > $OUT_DIR/$NAME.clo_aln.na.fa
  exit
fi


