import numpy as np

def calculate(list):
  """
  Convert list into 3x3 numpy array and raise error if list length is not 9
  """
  # Custom error message
  if (len(list) - 9) != 0:
    raise ValueError("List must contain nine numbers.")

  # Convert into 3 x 3 matrix
  ex_nparray = np.reshape(list,((3, 3)))

  """
  Mean, var, std deviation, max, min, sum along both axes and flattened
  """
  ###############################################
  # Means by column
  mean_c1 = np.mean(ex_nparray[:,0])
  mean_c2 = np.mean(ex_nparray[:,1])
  mean_c3 = np.mean(ex_nparray[:,2])
  # Means by row
  mean_r1 = np.mean(ex_nparray[0])
  mean_r2 = np.mean(ex_nparray[1])
  mean_r3 = np.mean(ex_nparray[2])
  # Flattened mean
  mean_flat = np.mean(ex_nparray.flatten())
  ###############################################
  # Variances by column
  var_c1 = np.var(ex_nparray[:,0])
  var_c2 = np.var(ex_nparray[:,1])
  var_c3 = np.var(ex_nparray[:,2])
  # Variances by row
  var_r1 = np.var(ex_nparray[0])
  var_r2 = np.var(ex_nparray[1])
  var_r3 = np.var(ex_nparray[2])
  # Flattened variance
  var_flat = np.var(ex_nparray.flatten())
  ###############################################
  # Standard deviations by column
  std_c1 = np.std(ex_nparray[:,0])
  std_c2 = np.std(ex_nparray[:,1])
  std_c3 = np.std(ex_nparray[:,2])
  # Standard deviations by row
  std_r1 = np.std(ex_nparray[0])
  std_r2 = np.std(ex_nparray[1])
  std_r3 = np.std(ex_nparray[2])
  # Flattened standard deviation
  std_flat = np.std(ex_nparray.flatten())
  ###############################################
  # Max by column
  max_c1 = np.max(ex_nparray[:,0])
  max_c2 = np.max(ex_nparray[:,1])
  max_c3 = np.max(ex_nparray[:,2])
  # Max by row
  max_r1 = np.max(ex_nparray[0])
  max_r2 = np.max(ex_nparray[1])
  max_r3 = np.max(ex_nparray[2])
  # Flattened max
  max_flat = np.max(ex_nparray.flatten())
  ###############################################
  # Min by column
  min_c1 = np.min(ex_nparray[:,0])
  min_c2 = np.min(ex_nparray[:,1])
  min_c3 = np.min(ex_nparray[:,2])
  # Min by row
  min_r1 = np.min(ex_nparray[0])
  min_r2 = np.min(ex_nparray[1])
  min_r3 = np.min(ex_nparray[2])
  # Flattened min
  min_flat = np.min(ex_nparray.flatten())
  ###############################################
  # Sum by column
  sum_c1 = np.sum(ex_nparray[:,0])
  sum_c2 = np.sum(ex_nparray[:,1])
  sum_c3 = np.sum(ex_nparray[:,2])
  # Sum by row
  sum_r1 = np.sum(ex_nparray[0])
  sum_r2 = np.sum(ex_nparray[1])
  sum_r3 = np.sum(ex_nparray[2])
  # Flattened sum
  sum_flat = np.sum(ex_nparray.flatten())
  ###############################################
  calculations = {
      'mean': [[mean_c1, mean_c2, mean_c3], [mean_r1, mean_r2, mean_r3], mean_flat],
      'variance': [[var_c1, var_c2, var_c3], [var_r1, var_r2, var_r3], var_flat],
      'standard deviation': [[std_c1, std_c2, std_c3], [std_r1, std_r2, std_r3], std_flat],
      'max': [[max_c1, max_c2, max_c3], [max_r1, max_r2, max_r3], max_flat],
      'min': [[min_c1, min_c2, min_c3], [min_r1, min_r2, min_r3], min_flat],
      'sum': [[sum_c1, sum_c2, sum_c3], [sum_r1, sum_r2, sum_r3], sum_flat]
  }

  return calculations
