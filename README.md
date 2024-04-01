# financify_data_processor
Python tools for getting data from the internet or PDFs into my financify_db

## Release Process

1. Create the release branch
    - Checkout the commit you want to base your release off of
    - Create a branch of the format `release/vMAJ.MIN.PATCH`, updating the appropriate section
2. Change the version number
    - Update the version number in `pyproject.toml`
    - Update the version number in `CHANGELOG.md` and add a new `Unreleased` section
    - Commit the version number changes
3. Push the release branch and create a PR
    - Push the release branch to the remote
    - Create a PR from the release branch to `main`
    - Add the `release` label to the PR
4. After the PR is merged, finalize the drafted release
    - Open the drafted release and change the target to "main"
    - Publish the release