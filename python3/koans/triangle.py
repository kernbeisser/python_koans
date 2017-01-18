#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if a < 1 or b < 1 or c < 1:
        raise TriangleError("0?")

    if not (a + b > c) or not (b + c > a) or not (a + c > b):
        raise TriangleError("0?")

    return ['equilateral', 'isosceles', 'scalene'][len(set([a, b, c]))-1]

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
