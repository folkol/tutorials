#!/usr/bin/perl
use strict;
use warnings;

open(MYFILE, ">myfile.txt") or die "Can't open myfile $!\n";
my ($name, $salary);
format MYFILE =
Name: @>>>>>>>>>>>>>>>>>>>>@##########.##
$name, $salary
.

format MYFILE_TOP =
Employee Names and Salaries                         Page: @>>>>>>>>>>>>>>>>>>>>
$%
.

write MYFILE
