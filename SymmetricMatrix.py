#!/usr/bin/env python
"""SymmetricMatrix: Guarantees a symmetric matrix."""
# I'm not just subclassing numpy.ndarray for a few reasons.
# * There are a bunch of tricky gotchas and I'm too lazy to deal with them.
# * I'm only going to use this in a specific way, so I can make a bunch of
#   assumptions and know they're safe.
# * I might totally reimplement this to only store the upper triangle in a
#   vector to save space, but only if I have space issues in practice.

import numpy

class SymmetricMatrix(object):
  """A Symmetric matrix."""

  def __init__(self, size, dtype=float):
    self.size = size
    self.matrix = numpy.zeros((size, size), dtype)

  def __getitem__(self, itemIndex):
    return self.matrix.__getitem__(itemIndex)

  def __setitem__(self, itemIndex, itemValue):
    """This is where we impose symmetry."""
    # As long as at least one of the index elements is just an integer, this'll
    # be really easy.
    if not isinstance(itemIndex, tuple) and length(itemIndex) != 2:
      raise IndexError("Index must be 2D")
    elif all([isinstance(i, slice) for i in itemIndex]):
      raise NotImplementedError("I can only deal with slices in 1D now")
    else:
      self.matrix.__setitem__(itemIndex, itemValue)
      self.matrix.__setitem__((itemIndex[1], itemIndex[0]), itemValue)

  def __str__(self):
    return self.matrix.__str__()

def main():
  testMat = SymmetricMatrix(4)
  testMat[1, 2] = 9
  testMat[3, :] = 22
  testMat[0, :] = 97
  print(testMat)

if __name__ == "__main__":
  main()

