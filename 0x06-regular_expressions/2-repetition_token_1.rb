#!/usr/bin/env ruby
#Bash script on repetitive token

puts ARGV[0].scan(/\bhtn\b/).join
puts ARGV[0].scan(/\bhbtn\b/).join

