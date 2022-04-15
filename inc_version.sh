#!/bin/bash

VERSION_STR=$(sed -nE 's/^version = (.*)$/\1/p' setup.cfg)

IFS='.' read MAJOR MINOR PATCH <<< $VERSION_STR
((PATCH += 1))

NEW_VERSION=$MAJOR.$MINOR.$PATCH

sed -i.bak -E "s/^version = .*/version = $NEW_VERSION/" setup.cfg
rm setup.cfg.bak

echo "Version updated to $NEW_VERSION"
