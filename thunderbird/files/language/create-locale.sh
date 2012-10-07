#!/bin/bash

CHANNEL="release"
RELEASE_TAG="THUNDERBIRD_12_0_RELEASE"
VERSION="12.0"

# These are Pardus supported languages. This list may changed by time to time
LOCALES="ca da de es-AR es-ES fr hu it nl pl pt-BR ru sv-SE tr"

test ! -d l10n && mkdir l10n
for locale in $LOCALES
do
    hg clone http://hg.mozilla.org/releases/l10n/mozilla-$CHANNEL/$locale l10n/$locale
    [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
done

cp -r l10n/tr/browser/searchplugins l10n/tr/mail
