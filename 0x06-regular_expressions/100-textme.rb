#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=\[{1}from:|to:|flags:).*?(?=\])/).join(',')
