#!/usr/bin/perl -w
use strict;

my @things = ('peach', 2, 'apple', 3.1415927);
my @thing1 = @things;   # Evaluated in list context, which means copy of list
my $thing2 = @things;   # Evaluated in scalar context, which means length of list
my ($thing3, $thing4) = @things; # List context, deconstructuring assignment where tail is dropped
my ($head, @tail) = @things; # Mind @ in @tail

print "@thing1\n$thing2\n$thing3\n$thing4\n@tail\n";

