#!/bin/sh
#update json
python3 scrape.py

setup_git() {
  echo 'entering setup'
  git remote add origin https://${GH_TOKEN}github.com/jliang117/jliang117.github.io.git
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git config --global push.default simple
  git checkout master
}

commit_website_files() {
  echo 'adding to commit'
  git add pins.json
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
  git status
}

upload_files() {
  echo 'pushing'
  git push --set-upstream origin master
}

setup_git
commit_website_files
upload_files
