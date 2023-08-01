#!/usr/bin/env ruby
#Ruby script on repetitive token accepting one argument and pass to regular expression

puts ARGV[0].scan(/\bhbt*n\b/).join
