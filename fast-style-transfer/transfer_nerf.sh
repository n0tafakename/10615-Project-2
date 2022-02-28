while read -r line
do
	for style in la_muse rain_princess scream udnie wave wreck
	do
		mkdir -p download/nerf_output/$style/$line
		python evaluate.py --checkpoint download/weights/$style.ckpt \
			--in-path download/nerf_synthetic/$line/train \
			--out-path download/nerf_output/$style/$line
	done
done < nerf.txt
