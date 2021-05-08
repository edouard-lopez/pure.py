#!/usr/bin/env elvish

use epm
epm:install &silent-if-installed github.com/edouard-lopez/pure-x.git

echo 'use github.com/edouard-lopez/pure-x.git/config/prompt' >> $E:HOME/.elvish/rc.elv
