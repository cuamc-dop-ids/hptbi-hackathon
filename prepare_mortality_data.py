################################################################################
# Prepare Mortality Data
#
# Define data procesing steps to apply to the data set used to train and test
# models for predicting mortality.
#
# Args:
#   training  (logicial) if the data set to read in is the training or testing
#             data set.
#
# Return:
#   A pandas data.frame with the defnined primary outcome and any user specific
#   elements needed for training and testing their model.
#

import pandas
import numpy as np
import pathlib
import re

def prepare_mortality_data(training = True):
    training_data = pathlib.Path("./csvs/training.csv")
    testing_data  = pathlib.Path("./csvs/testing.csv")

    if not training and testing_data.exists():
        hackathon_mortality_data = pandas.read_csv(testing_data)
    else:
        hackathon_mortality_data = pandas.read_csv(training_data)

    # Define the primary outcome -- do not edit this.  If you need the outocme
    # in a different format, e.g., integer or logical, create an additional
    # data.frame element in the user defined code section below.
    hackathon_mortality_data["mortality"] = hackathon_mortality_data["hospdisposition"] == "Mortality"
    hackathon_mortality_data["mortality"] = hackathon_mortality_data["mortality"].astype(int)

    # Omit some elements - FSS is omitted from this data set.  FSS could not be
    # assessed for patients who died.  To reduce confusion FSS related elements
    # are omitted as missing values for FSS are be highly correlated with
    # mortality.
    #for c in hackathon_mortality_data.filter(regex = "fss").columns:
    #    hackathon_mortality_data = hackathon_mortality_data.drop(columns = c)
    hackathon_mortality_data = hackathon_mortality_data.filter(regex = "^(?!.*fss.*)")

    ##############################################################################
    # User Defined Code starts here
    hackathon_mortality_data["gcs_use"] = np.where(hackathon_mortality_data["gcsed"].isnull(), hackathon_mortality_data["gcsicu"], hackathon_mortality_data["gcsed"])

    # if there is a missing icpyn1 value set to 0 if no type is reported.
    hackathon_mortality_data.loc[(hackathon_mortality_data["icpyn1"].isna() & hackathon_mortality_data["icptype1"].isna() & hackathon_mortality_data["icptype2"].isna() & hackathon_mortality_data["icptype3"].isna()), "icpyn1"] = 0

    # User Defined Code ends here
    ##############################################################################

    return hackathon_mortality_data

################################################################################
#                                 End of File
###############################################################################.
