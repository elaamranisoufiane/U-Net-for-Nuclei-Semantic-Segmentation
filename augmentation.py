import Augmentor


#p = Augmentor.Pipeline(source_directory="DSB/images", output_directory="./../DSB2/outputImages", ground_truth_output_directory= "./../DSB2/outputMasks", save_format="jpg")
p = Augmentor.Pipeline(source_directory="imagesToAugment/images", output_directory="outputImages", ground_truth_output_directory= "outputMasks", save_format="jpg")
p.ground_truth("imagesToAugment/groundTruthImages")

print("_______")
print(p.get_ground_truth_paths())

print("_______")

#DataFramePipeline(output_directory="output", save_format="jpg")



#add operations to the Pipeline object p as follows:
#p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.flip_left_right(probability=0.5)
#p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.flip_top_bottom(probability=0.5)
#p.crop_random(probability=1, percentage_area=0.5)
p.rotate180(probability=0.5)
p.rotate90(probability=0.5)
#p.rotate180(probability=0.5)
p.rotate270(probability=0.5)
#p.rotate45(probability=0.5)
p.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=10)
#create 10 samples
p.sample(4)
