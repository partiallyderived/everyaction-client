#!/bin/bash

VERSION_STR=$(sed -nE 's/^version = (.*)$/\1/p' setup.cfg)

IFS='.' read MAJOR MINOR PATCH <<< $VERSION_STR
((PATCH += 1))

if [[ $PATCH == "7\r" ]]; then
  echo yes
fi

NEW_VERSION=$MAJOR.$MINOR.$PATCH

sed -i.bak -E "s/^version = .*/version = $NEW_VERSION/" setup.cfg

echo "Version updated to $NEW_VERSION"
