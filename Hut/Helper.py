import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

class Helplot:
  """
  TensorFlow Model Training History Plot
  
  >>> history = model.fit(train, ...)
  >>> plot_hist = Helplot(history)
  >>> plot_hist.Relplot
  >>> plot_hist.Falplot
  """
  def __init__(self, history):
    self.history = history.history if hasattr(history, 'history') else history
    self.accuracy = self.history['accuracy']
    self.loop = [*range(1, len(self.accuracy) + 1)]
    self.loss = self.history['loss']
    self.validation = any(key.startswith('val_') for key in self.history.keys())

  @property
  def Relplot(self):
    """
    Result Plot
    """
    plt.figure()
    plt.plot(self.loop, self.accuracy, label='Train Accuracy')
    # Add Validation Plot if Available
    if self.validation:
      val_accuracy = self.history.get('val_accuracy')
      plt.plot(self.loop, val_accuracy, label='Val Accuracy')
    # Plot Settings
    plt.title("Accuracy Result")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    # Label on Conditional Situation
    if len(self.loop) <= 15:
      plt.xticks(self.loop)
    plt.legend()
    plt.show()

  @property
  def Falplot(self):
    """
    Fail Plot
    """
    plt.figure()
    plt.plot(self.loop, self.loss, label='Train Loss')
    # Add Validation Plot if Available
    if self.validation:
      val_loss = self.history.get('val_loss')
      plt.plot(self.loop, val_loss, label='Val Loss')
    # Plot Settings
    plt.title("Loss Result")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    # Label on Conditional Situation
    if len(self.loop) <= 15:
      plt.xticks(self.loop)
    plt.legend()
    plt.show()