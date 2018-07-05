for i in *.fna; do sed ':a; $!N; /^>/!s/\n\([^>]\)/\l/; ta; P; D' $i > ${i//.fna/.fa}; done
