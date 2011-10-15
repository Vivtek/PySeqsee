from group import Group
from category import Category

from nose.tools import raises

class CategoryRepeated(Category):
  global_attributes = ('length', )
  
  @staticmethod
  def IsInstance(gp):
    if not isinstance(gp, Group):
      return False
    structures = [x.Structure() for x in gp.items]
    if len(structures) == 1:
      return { 'each': structures[0], 'length': len(structures)}
    for i in range(0, len(structures)-1):
      if structures[i] != structures[i+1]:
        return False
    return { 'each': structures[0], 'length': len(structures)}
  
@raises(Exception)
def test_cannot_init():
  CategoryRepeated()
  
def test_is_instance_in_isolation():
  g1 = Group.QuickCreate(5, 5, 5)
  g2 = Group.QuickCreate([5, 5], [5, 5], [5, 5])
  g3 = Group.QuickCreate([5], [5], [5])
  g4 = Group.QuickCreate([5, 5], [5, 5], [5, 6])
  
  assert not CategoryRepeated.IsInstance(g4)

  b = CategoryRepeated.IsInstance(g1)
  assert b
  assert 3 == b['length']
  assert 5 == b['each']

  b = CategoryRepeated.IsInstance(g2)
  assert b
  assert 3 == b['length']
  assert (5, 5) == b['each']

  b = CategoryRepeated.IsInstance(g3)
  assert b
  assert 3 == b['length']
  assert (5, ) == b['each']

def test_describe_as():
  g = Group.QuickCreate([5, 5], [5, 5], [5, 5])
  cm = g.cm
  
  assert not cm.IsKnownInstanceOf(CategoryRepeated)
  g.DescribeAs(CategoryRepeated)
  assert cm.IsKnownInstanceOf(CategoryRepeated)
  
  b = cm.GetBindings(CategoryRepeated)
  assert 3 == b['length']
  assert (5, 5) == b['each']

  b = cm.GetBindings()
  assert 3 == b['length']
  assert 'each' not in b
  
  g2 = Group.QuickCreate([5, 5], [5, 5], [5, 6])
  cm = g2.cm
  
  assert not cm.IsKnownInstanceOf(CategoryRepeated)
  g2.DescribeAs(CategoryRepeated)
  assert not cm.IsKnownInstanceOf(CategoryRepeated)
  assert cm.IsKnownNonInstanceOf(CategoryRepeated)