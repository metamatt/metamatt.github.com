#!/usr/bin/env python

import glob
import re

map = {}

for tumblr_dir in sorted(glob.glob('source/post/*')):
    tumblr_id = int(tumblr_dir.split('/')[2])
    assert tumblr_id > 0

    tumblr_post = 'http://blog.metamatt.com/post/%d' % tumblr_id

    redirect = open(tumblr_dir + '/index.html').read()
    match = re.search("url=(.*)'", redirect)
    assert match

    octo_post = 'http://blog.metamatt.com%s' % match.group(1)

    #print '%s, %s' % (tumblr_post, octo_post)
    map[tumblr_id] = '%s, %s' % (tumblr_post, octo_post)

for key in sorted(map.keys()):
    print map[key]
