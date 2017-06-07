#!/usr/bin/perl -w
use strict;

my %hash = (name => 'Matte',
            age => 37,
            occupation => 'computer programmer'
        );
print "$hash{name}, age $hash{age}, $hash{occupation}.\n";
print values(%hash);
print keys(%hash);
