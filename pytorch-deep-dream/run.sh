for object in hotdog ship mic lego materials ficus
do
	mkdir -p outputs/nerf/$object
	ls images/nerf/$object > images/${object}.txt
	while read -r fname
	do
		python deep_dream.py --input_image images/nerf/$object/$fname --output_dir outputs/nerf/$object
	done < images/${object}.txt
done
