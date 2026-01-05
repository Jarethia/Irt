import pandas

def isTableNull(table : pandas.DataFrame) -> pandas.DataFrame:
  """
  Return Null Table w Desc Sort
  """
  # Calculate Nulls
  unfilter = table.isnull().sum()
  # Filter
  tabular = unfilter[unfilter > 0]
  # Sort Desc
  tabular = tabular.sort_values(ascending=False)
  # Return
  return tabular.to_frame(name="Total")