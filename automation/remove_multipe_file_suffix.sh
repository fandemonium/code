for i in a_*.txt; do mv -- "$i" "${i%%.txt}"; done
