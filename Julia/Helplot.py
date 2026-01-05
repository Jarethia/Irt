import seaborn as sns

sns.set_style("whitegrid")

def barSinglePlot(tabel, data, **plotargs):
  """
  Bar Plot for Single Data Column
  """
  # Define Plot with Key
  plot = sns.countplot(x = data, data = tabel, **plotargs)
  # Labeler in Containers
  for container in plot.containers:
    # Single Bar Labels
    plot.bar_label(container);

def barRelationalPlot(tabel, x, y, **plotargs):
  """
  Bar Plot for Relational Data
  """
  # Default Plot Args
  plotargs.setdefault('errorbar', None)
  # Define Plot with Key
  plot = sns.barplot(x = x, y = y, data = tabel, **plotargs)
  # Labeler in Containers
  for container in plot.containers:
    # Single Bar Labels
    plot.bar_label(container);