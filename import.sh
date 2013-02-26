#! /bin/sh
ruby -rubygems -e 'require "bundler/setup"; require "jekyll/migrators/tumblr"; Jekyll::Tumblr.process("http://blog.metamatt.com", "md")'
