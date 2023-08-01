#!/usr/bin/env ruby
#Bash script on repetitive token

puts ARGV[0].scan(/hb(t{1,5})n/).join
