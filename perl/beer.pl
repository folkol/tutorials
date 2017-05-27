#!/usr/bin/perl -w
use strict;

my $bottles = 99;
my $bottlestr = 'bottles';
while ( $bottles > 0 ) {
    print "$bottles $bottlestr of beer on the wall,\n";
    print "$bottles $bottlestr of beer,\n";
    print "Take one down, pass it around,\n";
    $bottles--;
    if ( $bottles == 1 ) {
        $bottlestr = 'bottle';
    } else {
        $bottlestr = 'bottles';
    }
    print "$bottles $bottlestr of beer on the wall.\n\n";
}

