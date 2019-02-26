#!/bin/sh
#update json
HOMEDIR=sampleSaleProject
cd ${HOMEDIR}
pwd
ls -la

python3 scrape.py

push() {
  echo 'entering setup'
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git checkout master
  git add pins.json
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
  git push -f -q https://jliang117:${GH_TOKEN}@github.com/jliang117/jliang117.github.io.git
  
}

push
