################################################################################
# Prepare FSS Data
#
# Define data procesing steps to apply to the data set used to train and test
# models for predicting total FSS.
#
# Args:
#   training  (logicial) if the data set to read in is the training or testing
#             data set.
#
# Return:
#   A data.frame with the defnined primary outcome and any user specific
#   elements needed for training and testing their model.
#
prepare_fss_data <- function(training = TRUE) {

  # import the data set
  if (!training & file.exists("./csvs/testing.csv")) {
    hackathon_fss_data <- read.csv(file = "./csvs/testing.csv")
  } else {
    hackathon_fss_data <- read.csv(file = "./csvs/training.csv")
  }

  # Define the primary outcome -- do not edit this.  If you need the outcome in
  # a different format, e.g., integer or logical, create an additional
  # data.frame element in user defined code section below.
  hackathon_fss_data$fss_total <-
    Reduce(function(x, y) {x + y},
           x = hackathon_fss_data[grep("^fss", names(hackathon_fss_data))])

  # subset to known FSS values
  hackathon_fss_data <-
    subset(hackathon_fss_data, hospdisposition != "Mortality")
  hackathon_fss_data <-
    subset(hackathon_fss_data, !is.na(fss_total))

  ##############################################################################
  # User Defined data preperation code starts here

  # deal with a possible missing value in icpyn1
  if (any(hackathon_fss_data$icpyn1)) {

    # if all information about type of monitor is missing then mark icpyn1 as 0
    flags <-
      as.integer(!(
                     hackathon_fss_data$icptype1 == "" | is.na(hackathon_fss_data$icptype1) &
                     hackathon_fss_data$icptype2 == "" | is.na(hackathon_fss_data$icptype2) &
                     hackathon_fss_data$icptype3 == "" | is.na(hackathon_fss_data$icptype3) 
                  ))

    idx <- which(is.na(hackathon_fss_data$icpyn1))
    hackathon_fss_data$icpyn1[idx] <- flags[idx]
  }

  # User Defined Code ends here
  ##############################################################################

  hackathon_fss_data
}

################################################################################
#                                 End of File
################################################################################
