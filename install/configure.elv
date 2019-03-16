#!/usr/bin/env elvish

mkdir --parents $E:HOME/.elvish/lib/
cp $E:HOME/.pure/config/prompt.elv $E:HOME/.elvish/lib/pure.elv
echo 'E:PURE_EXECUTABLE_PATH = $E:HOME/.pure/' >> $E:HOME/.elvish/rc.elv
echo 'use pure' >> $E:HOME/.elvish/rc.elv
