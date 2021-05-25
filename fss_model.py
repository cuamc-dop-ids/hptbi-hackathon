################################################################################
#
################################################################################
# FSS Model
#
# Args:
#
# Return:
#
import numpy as np
from sklearn import linear_model

def fss_model(data):
    ############################################################################
    # User code starts here
    xmat = data[["age", "female", "icpyn1"]]
    yvec = data[["fss_total"]]
    rtn = linear_model.LinearRegression()
    rtn.fit(xmat, yvec)
    # User code ends here
    ############################################################################
    return rtn


################################################################################
# Predict Hackathon Mortality Model
#
# Args:
#
# Return:
#   predicted FSS values, integers values inclusively between 6 and 30
#
def predict_fss(model, newdata):
    ############################################################################
    # user defined code starts here
    xmat = newdata[["age", "female", "icpyn1"]]
    return model.predict(xmat).astype(int)

################################################################################
#                                 End of File
################################################################################
