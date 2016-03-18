import random
import os
from pydub import AudioSegment
from pydub.utils import mediainfo

def MangleLibrary(src, dst, audio, splice=None):
	if os.path.splitext(audio)[1] != ".mp3":
		raise "Prank audio is not an mp3"
	prank = AudioSegment.from_mp3(audio)
	# Walk src
	for root, dirs, files in os.walk(src):
		# Loop through files in this dir
		for fn in files:
			# If file is an mp3
			if os.path.splitext(fn)[1] == ".mp3":
				# Import song
				fullsong = AudioSegment.from_mp3(root+"/"+fn)
				# Pick random location between 10s and end of song
				start = random.randint(15,60)
				print("Spliced {} after {} seconds".format(root+"/"+fn,start))
				# Splice in prank song
				if splice != None:
					r = random.randint(0,len(splice)-1)
					final = fullsong[:start*1000] + prank[splice[r][0]:splice[r][1]] + fullsong[start*1000:]
					# final = fullsong[:start*1000] + prank + fullsong[start*1000:]
				else:
					final = fullsong[:start*1000] + prank
				# Recreate directory structrue in dst
				if not os.path.exists(dst+"/"+root):
					os.makedirs(dst+"/"+root)
				# Export song with tags
				final.export(dst+"/"+root+"/"+fn, format="mp3", tags=mediainfo(root+"/"+fn).get('TAG', {}))
