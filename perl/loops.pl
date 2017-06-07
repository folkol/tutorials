#!/usr/bin/perl -w
use strict;

#foreach my $lol (reverse ('Blastoff!', 1..10)) {
#    print "$lol\n";
#    sleep(1);
#}
my @price_list = (100, 66, 2);
foreach my $price (@price_list) {
    $price *= 0.8;   # All items 20% off!
}

print "@price_list\n";

my $k = 0;
print $k++ while $k < 10;
print "\n";
