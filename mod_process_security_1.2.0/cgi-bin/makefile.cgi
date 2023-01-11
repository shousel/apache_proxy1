#!/usr/bin/perl

@test = ("test");

open (OUT,"> test.txt");
print OUT @test;
close (OUT);

print "Content-type: text/html\n\n";
print "<META http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n";
print 'Complete';

exit;
