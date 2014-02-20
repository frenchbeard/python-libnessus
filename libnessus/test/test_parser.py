#!/usr/bin/env python

from libnessus.parser import NessusParser
from libnessus.objects import NessusReport
from test_nessus import TestNessus


class TestParser(TestNessus):
    """Unit test of parser"""
    def test_return_class(self):
        """test_return_class : Check the returned object is NessusReport"""
        for testfile in self.flist:
            self.assertEqual(isinstance(testfile['report'],
                             NessusReport), True)

    def test_number_of_host_in_report(self):
        """test_number_of_host_in_report :
            Check the number of host in the repport"""
        for testfile in self.flist:
            self.assertEqual(len(testfile['report'].hosts), testfile['hosts'])

    def test_badfile_for_excepetion(self):
        """test_badfile_for_excepetion :
            Check to raise when wrong input file"""
        for testfile in self.badlist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            self.assertRaises(Exception, NessusParser.parse, s)

    def test_parse_host(self):
        """test_parse_host : check host parsing"""

    def test_parse_vulnerability(self):
        """test_parse_vulnerability : check vuln parsing"""
