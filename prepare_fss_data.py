################################################################################
# Prepare FSS Data
#
# Define data processing steps to apply to the data set used to train and test
# models for predicting FSS.
#
# Args:
#   training  (logical) if the data set to read in is the training or testing
#             data set.
#
# Return:
#   A pandas data.frame with the defined primary outcome and any user-specific
#   elements needed for training and testing their model.
#

import pandas
import numpy as np
import pathlib
import re

def prepare_fss_data(training = True):
    training_data = pathlib.Path("./csvs/training.csv")
    testing_data  = pathlib.Path("./csvs/testing.csv")

    if not training and testing_data.exists():
        hackathon_fss_data = pandas.read_csv(testing_data)
    else:
        hackathon_fss_data = pandas.read_csv(training_data)

    # Define the primary outcome -- do not edit this.  If you need the outcome in
    # a different format, e.g., integer or logical, create an additional
    # data.frame element in user defined code section below.
    hackathon_fss_data["fss_total"] = hackathon_fss_data["fssmental"] + hackathon_fss_data["fsssensory"] + hackathon_fss_data["fsscommun"] + hackathon_fss_data["fssmotor"] + hackathon_fss_data["fssfeeding"] + hackathon_fss_data["fssresp"]

    # subset to known FSS values
    hackathon_fss_data = hackathon_fss_data[(hackathon_fss_data["hospdisposition"] != "Mortality")]
    hackathon_fss_data = hackathon_fss_data[(hackathon_fss_data["fss_total"].notnull())]

    ##############################################################################
    # User Defined Code starts here
    hackathon_fss_data["gcs_use"] = np.where(hackathon_fss_data["gcsed"].isnull(), hackathon_fss_data["gcsicu"], hackathon_fss_data["gcsed"])

    # if there is a missing icpyn1 value set to 0 if no type is reported.
    hackathon_fss_data.loc[(hackathon_fss_data["icpyn1"].isna() & hackathon_fss_data["icptype1"].isna() & hackathon_fss_data["icptype2"].isna() & hackathon_fss_data["icptype3"].isna()), "icpyn1"] = 0

    # User Defined Code ends here
    ##############################################################################

    return hackathon_fss_data


################################################################################
#                                 End of File
###############################################################################.
