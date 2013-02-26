import glob
import subprocess

for i in glob.glob('source/post/*'):
	src = glob.glob('%s/*/index.html' % i)
	assert len(src) == 1
	src = src[0]
	dst = '%s/index.html' % i
	#print 'cp %s %s' % (src, dst)
	subprocess.call(['cp', src, dst])
