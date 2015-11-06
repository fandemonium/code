for i in pool_*
        do
        cd /mnt/data3/fan/pitfoaming/$i/assembled
        for j in *.fastq
                do mv $j "$i"_"$j"
	done
        cd /mnt/data3/fan/pitfoaming/
done
