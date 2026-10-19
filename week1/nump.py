import numpy as np

socore = np.array([10,15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 100])


mean_score = np.mean(socore)
median_score = np.median(socore)
std_dev_score = np.std(socore)

print(f"mean : {mean_score :.2f} median : {median_score}  std : {std_dev_score}")