## automation script for hmmalign, names have to match

out=(~/Documents/Fan/pfam_hmm/*/ref_aligned.stk)
hmm=(~/Documents/Fan/pfam_hmm/*/Peptidase_*.hmm)
seq=(~/Documents/Fan/pfam_hmm/*/ref_*_1e-5.faa)

for((i=0;i<=${#hmm[@]};i++))
do
   hmmalign -o "${out[i]}" "${hmm[i]}" "${seq[i]}"
done

