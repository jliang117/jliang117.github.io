#!/bin/sh

setup_git() {
  git remote add origin https://${GH_TOKEN}github.com/jliang117/jliang117.github.io.git
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git checkout master
}

commit_website_files() {
  git add pins.json
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push --quiet --set-upstream origin master
}

setup_git
commit_website_files
upload_files
