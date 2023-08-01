#!/usr/bin/env ruby
#Ruby script accepting one argument and pass to regular expression starts with h ends with n and single character in between

puts ARGV[0].scan(/\b(^h.n$)\b/)).join
