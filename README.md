# Harmonized Pediatric Traumatic Brain Injury Hackathon

## Objectives for the Hackathon

Develop models for predicting

1. Hospital Mortality
2. Total Functional Status Score (FSS) at discharge

for pediatric patients with traumatic brain injuries.

This repository contains a training data set. Submitted models will be
evaluated against a hold out testing data set.

## What's in this Repository

### Data

A training data set is in `csvs/training.csv`. This is a 300 row data set, each row
representing the observations for one patient.  A data dictionary has been
provided in the file `data_dictionary.md`. Pay particular attention to the final two
columns where presence/absence of missing data is documented.

### Files Hackathon Users **Should** Edit

* `description.yaml` - a YAML file to document project metadata such as version,
  primary analysis language, author names and contact information, etc.
  Hackathon participants must provide author details and specify the language
  field, either R or py(thon).

* Language specific files - hackathon participants may remove the version of
  these files not pertaining to their preferred modeling language.  Within each
  file there are code blocks participants are expected to edit and code blocks
  participants are not expected to edit.

  * `prepare_mortality_data` defines a function for preparing the data set
    needed for supporting the model predicting mortality.

  * `prepare_fss_data` defines a function for preparing a data set to
    support the model predicting total FSS.

  * `mortality_model` defines two functions, one for training a model to predict
    mortality and a second function to return a vector of predicted
    Mortality/Alive status given the trained model and a data set.

  * `fss_model` defines two functions, one for training a model to predict
    total FSS at discharge and a second function to return a vector of predicted
    FSS values given the trained model and a data set.

  * `Dockerfile` - a template docker file has been provided to define an image
    used for training, testing, and evaluation of the models.

### Files Hackathon Users **Should Not** Edit

The files listed here should not be edited by hackathon participants.  These
files are provided so participants may test their submissions locally.  As will
be noted again in the submission section, modification of any of these files
will result in a rejected submission.

* `evaluate.R`
* `runme_py.sh`
* `runme_r.sh`
* `testing.py`
* `testing.R`
* `training.py`
* `training.r`
* `LICENSE`

## How To Train, Test, and Evaluate Your Models

After editing the files described above, you can train, test, and evaluate your
models in a Docker container. The result will be a new directory called
`output` with several files including `evaluation.txt` with modeling results.
The provided code base includes extremely simple models for mortality and total
FSS to serve as examples.  The following will build the images and run
the examples in a container.

```
# build the image for the language you want
docker build -t hackathon_r -f Dockerfile_r .
docker build -t hackathon_py -f Dockerfile_py .

# train, test, and evaluate the models in a container:
docker run -v $(PWD):/hackathon --rm hackathon_r /bin/bash runme_r.sh
docker run -v $(PWD):/hackathon --rm hackathon_py /bin/bash runme_py.sh
```

## System and Other Dependencies

At least one member of each team participating in the Hackathon needs to have an
active GitHub account.

_Local system dependencies are:_

* Docker
* git
* R or Python

_Other dependencies:_

* A github.com account

Hackathon participants are encouraged to use either R or python for model development.
Template files for both languages have been provided.  Evaluation of the models,
including training, testing, and evaluation of the testing, will be done using
Docker containers. Hackathon participants are encouraged to have Docker
installed for development and testing locally before submitting models.

## How to Participate in the Hackathon

The hackathon is open starting 6 July 2021 with final submissions to be comitted
and submitted before 11:59:59 PM (Mountain Daylight Time; UTC-6) on 1 August 2021.

1. REGISTER - complete and submit the [HPTBI Registration Form](https://docs.google.com/forms/d/e/1FAIpQLSdCV58GlVuoScxYkdPL1hV1CYgvvBxjgsBUAspjeH5UHatZRg/viewform)

2. Create your own github repo called <user-id>/hptbi-hackathon by using the ``Use
   this template'' button from the [base
   hptbi-hackathon](https://github.com/cuamc-dop-ids/hptbi-hackathon).  (Learn
   more about template repositories
   [here](https://docs.github.com/articles/creating-a-repository-from-a-template/))

3. Provide github users @dewittpe and @tdbennett with access to your repository by adding @dewittpe and @tdbennett as
   collaborators.  Instructions for adding a collaborator are found
   [here.](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)

4. Hackathon participants develop their models for mortality and total FSS

  a. Edit the `description.yaml` file to include hackathon participant(s) names
  and contact information and project data.

  b. Edit the `prepare_.*_data` scripts to generate the data sets needed for
  fitting the models.  The use of this function is needed to help make sure the
  same data steps are applied to the testing (holdout) data for evaluations.

  c. Edit the `mortality_model` and `fss_model` files to define the models and
  prediction functions.

  d. Local tests can be done via the `runme_*.sh` bash scripts, or within the
  docker container as noted above.

4. Submissions

  a. Commit changes to the edited files.  Any changes to the files listed in the
  'should not edit' section above will result in a rejected submission.

   * Make sure to update the version number within the `description.yaml` file.
      Version numbers should be of the form: `x.y` where `x` is either 0 or 1,
      and `y` is 1, 2, 3, 4, 5, ... Participants are allowed to submit "development"
      submissions to verify that the code runs and that predictions are created.
      These should be indexed as 0.1, 0.2, 0.3, and so on. Please note that you
      will not receive feedback about the accuracy of development submissions, only
      that the code runs. The final submission for the hackathon should be
      labelled `v1.0` in the `description.yaml` file.

   * Tag the commit with an annotated tag. Annotations should be of the form e.g.
      `v0.1`

  b. Push your changes and tag to your github repository.

  c. Complete the
  [submission](https://docs.google.com/forms/d/e/1FAIpQLSdjynOGDbpbNI6gLRsUx40Agu-ak8Cd45w7C4Ppd7u9GYhPKg/viewform)


5. When you notify us (step 4c above) about a submission, we will build the docker image
   and run the scripts in a container with both the training and testing data.
   We will update/create the file `output/evaluation.txt`, commit it, and push the
   evaluation to your repo on a new branch named `vx.y-eval` with the commit tagged with
   the annotation `vx.y-evaluation`

   The `output/evaluation.txt` file will have the same information which the
   participant can generate with additional lines for the testing set.

    a. Rejected - a submission will be rejected outright if test.sh,
    testing.(R|py), or training.(R|py) have been edited.

    b. Errored - the submission was evaluated but an error occurred in evaluating
    the submission.  Details on the error may or may not be provided, and the
    verboseness of the error(s) may be limited based on the number of submissions
    in the queue.

    c. Time out - evaluations will be done on a standard laptop with modest RAM and
    CPU capabilities, no GPU processing. A wall time limit of 24 hours will be enforced.

    c. Success - the code evaluated, predictions were generated for the testing
    (holdout) data set, and an evaluation score has been computed. Evaluation
    scores will only be provide for the final v1.0 submission.


## Assessment, Ranking, and Rewards for Participation

### Assessment

We will assess the entries using several model fit
statistics described in the `evaluate.R` script.

### Rewards

The first place entry will be rewarded $500, second place $250, third $150, and
fourth $100. Bonuses may be given to models that are deemed by the organiziers to be parsimonious,
interpretable, and feasible to implement in an electronic health record. Payment will
be by electronic gift card.

### Ranking
After the final submission date, results from v1.0 submitted projects will be
ranked as follows:

* Each of the metrics used to assess model fit will be ranked across entries on
  the testing data. Metrics from both models (mortality and FSS) will be counted in this assessment.
  In order to have the highest chance of winning, participants should submit
  models for both outcomes.

  * Ties will will be given the same integer value with the next entry skipping
    values.  For example, assume there is a tie for third on a metric between
    two entries.  The ranks would then be: 1, 2, 3, 3, 5, 6, ...  If the
    tie was between three entries the ranks would be: 1, 2, 3, 3, 3, 6, 7, ...

* The sum of all ranks for an entry will be the relative score for entry.  Low
  sums are preferable.  The lowest sum will be the winner.

* In the event of a tie in the scores between those in the top four entries the
  prize money for the tied placements will be pooled and equally divided.

## Rules and Acknowledgement of Participation

1. Participants agree to not attempt linkage attacks nor attempt to identify
   patients within the provide data set.

2. Participant agrees that the code and models used in this hackathon may be used
   by others after the hackathon, with appropriate citation of the participant's
   GitHub repository. This includes use by the organizers, other participants, or others.

3. Participant acknowledges that the organizers will submit the results of this hackathon
   as part of one or more abstracts and manuscripts submitted to conferences and
   peer-reviewed journal. Participants will be acknowledged as a group but not explicitly identified
   in the abstracts and manuscript.

## Funding for this Hackathon

This hackathon was supported by NIH/NICHD grant R03HD094912 and NIH/NICHD grant
number K23HD074620.

