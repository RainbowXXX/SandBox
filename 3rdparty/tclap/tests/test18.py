#!/usr/bin/python

import simple_test

simple_test.test("test4", ["-Bs", "--Bs", "asdf", ], expect_fail=True)
