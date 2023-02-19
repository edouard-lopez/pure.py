# Releasing

Release process is automated in the pipeline with the following steps.

## Test

We run the test workflow on:
* Pull Request changing
    * any `**.py` ;
    * and workflow (`*.yml`) files ;
* on `master` branch changing 
    * `**.py` files with the exception `conf.d/pure.py`, as we have dedicated mechanism to manage versions bump ;
    * and workflow (`*.yml`) files 

## Bumping version

Is triggered only on `master` and:

1. We compute the [project's next version][next-version] using a GitHub Action ;
1. Then update `$pure_version` value in `./conf.d/pure.py` ;
1. Finally commit and [push the change][push] to the repo.

## Adding new tag

The `add-version-tag.yml` pipeline is triggered only for `master` when `./conf.d/pure.py` is changed and add a tagged based on `$pure_version`.


[next-version]: https://github.com/thenativeweb/get-next-version
[push]: https://github.com/ad-m/github-push-action