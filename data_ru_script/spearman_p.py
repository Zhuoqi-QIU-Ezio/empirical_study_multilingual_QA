import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

norm_dist = stats.norm()
dat1 = norm_dist.rvs(size=100)
exp_dist = stats.expon()
dat2 = exp_dist.rvs(size=100)
cor, pval = stats.pearsonr(dat1, dat2)
print( "Pearson correlation coefficient: " + str(cor))
cor, pval = stats.spearmanr(dat1, dat2)
print("Spearman's rank correlation coefficient: " + str(cor))