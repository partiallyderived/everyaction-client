#!/bin/bash

if [[ $# != 1 ]]; then
  echo "Error: Expected exactly one argument, got $#" 1>&2
  exit 1
fi

VERSION_INC=$(tr '[:upper:]' '[:lower:]' <<< "$1")
VERSION_STR=$(sed -nE 's/^version = (.*)$/\1/p' setup.cfg)

IFS='.' read MAJOR MINOR PATCH <<< $VERSION_STR

case "$VERSION_INC" in
  major)
    ((MAJOR += 1))
    MINOR=0
    PATCH=0
    ;;
  minor)
    ((MINOR += 1))
    PATCH=0
    ;;
  patch)
    ((PATCH += 1))
    ;;
  *)
    echo "Error: Argument should be one of major, minor, or patch, not $1" 1>&2
    exit 1
    ;;
esac

NEW_VERSION=$MAJOR.$MINOR.$PATCH

sed -i.bak -E "s/^version = .*/version = $NEW_VERSION/" setup.cfg
rm setup.cfg.bak

echo "Version updated to $NEW_VERSION"
