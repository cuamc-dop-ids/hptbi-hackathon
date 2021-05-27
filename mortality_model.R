################################################################################
#
################################################################################
# Mortality Model
#
# Args:
#   data a data.frame resulting from a call to prepare_mortality_data()
#
# Return:
#   An R object.  This object will have the "hackathon_mortality_model" class
#   prepended to it such that a call to predict can be used to generate
#   predictions from the training and testing data sets.
#
mortality_model <- function(data) {

  ##############################################################################
  # User code starts here
  rtn <-
    glm(mortality ~ age + female + gcs_use + icpyn1,
        data = data,
        family = binomial())
  
  # User code ends here
  ##############################################################################

  class(rtn) <- c("hackathon_mortality_model", class(rtn))
  rtn
}

################################################################################
# Predict Hackathon Mortality Model
#
# An S3 function call for hackathon_mortality_model
#
# Args:
#   object  a hackathon_mortality_model object
#   newdata a data.frame
#   ...     additional arguments passed through.  Not expected to be used as
#           part of the hackathon.
#
# Return:
#   A character vector of length equal to the nrow(newdata) with values
#   "Mortality" and "Alive"
#
predict.hackathon_mortality_model <- function(object, newdata, ...) {
  
  ##############################################################################
  # User Defined data preparation code starts here

  p <- stats::predict.glm(object, newdata, type = "response", ...)
  ifelse(p > 0.25, "Mortality", "Alive")

}

################################################################################
#                                 End of File
################################################################################
