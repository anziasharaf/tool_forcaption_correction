from tempfile import NamedTemporaryFile
import shutil
import csv
filename="/home/user/Desktop/tool_for_caption_correction/out.csv"
tempfile = NamedTemporaryFile(mode='w', delete=False)
fields = ['image_id', 'caption_id','English_caption', 'Malayalam_caption']
with open(filename, 'r') as csvfile, tempfile:
	reader = csv.DictReader(csvfile, fieldnames=fields)
