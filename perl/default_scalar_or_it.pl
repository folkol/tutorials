#!/usr/bin/perl -w
use strict;

while ( <STDIN> ) {
    chomp;
    $_ = reverse;
    print;
}

