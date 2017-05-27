#!/usr/bin/perl -w
use strict;

my $v;
if ( $v ) { print 'abc'; }
$v = '0.0';
if ( $v ) { print 'def'; }
if ( $v + 0 ) { print 'ghi'; }
