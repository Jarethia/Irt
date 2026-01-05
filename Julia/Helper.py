import pandas

def isTableNull(table : pandas.DataFrame) -> pandas.DataFrame:
  """
  Return Null Table w Desc Sort
  """
  unfilter = table.isnull().sum()
  tabular = unfilter[unfilter > 0]
  tabular = tabular.sort_values(ascending=False)
  tabular = tabular.to_frame(name="Total")
  return tabular