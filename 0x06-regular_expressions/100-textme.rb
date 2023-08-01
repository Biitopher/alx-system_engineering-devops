#!/usr/bin/env ruby
#Ruby script that output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/[SENDER],[RECEIVER],[FLAGS]/).join
