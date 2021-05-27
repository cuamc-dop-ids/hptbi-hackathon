################################################################################
#
################################################################################
# Mortality Model
#
# Args:
#
# Return:
#

import numpy as np
from sklearn import linear_model

def mortality_model(data):

    ymat = data.loc[:, "mortality"]

    ############################################################################
    # User code starts here
    xmat = data[["age", "female", "gcs_use", "icpyn1"]]
    rtn = linear_model.LogisticRegression()

    rtn.fit(xmat, ymat)

    # User code ends here
    ############################################################################
    return rtn

################################################################################
# Predict Hackathon Mortality Model
#
# Args:
#
# Return:
#
def predict_mortality(model, newdata):

    ############################################################################
    # User Defined data preparation code starts here
    xmat = newdata[["age", "female", "gcs_use", "icpyn1"]]
    p = model.predict_proba(xmat)
    return np.where(p[:, 1] > 0.25, "Mortality", "Alive")


################################################################################
#                                 End of File
################################################################################
