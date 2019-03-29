# Theme

## Default

I used [Base16 schemes][base16]
* [Tomorrow][tomorrow]
* [Tomorrow-night][tomorrow-night]

## Create your own

Copy `pure/theme/template.json` to your `mine.json` and update colors. 

Then edit your config to pass the name of your file to pure using something like `--theme monokai`.


    {
        'primary': 'base16: base0E',
        'info':    'base16: base0D',
        'mute':    'base16: base04',
        'success': 'base16: base0B',
        'normal':  'base16: base01',
        'danger':  'base16: base08',
        'light':   'base16: base07',
        'warning': 'base16: base0A',
        'dark':    'base16: base02' 
    }


[base16]: https://github.com/chriskempson/base16
[tomorrow]: https://github.com/chriskempson/base16-tomorrow-scheme/blob/master/tomorrow.yaml
[tomorrow-night]: https://github.com/chriskempson/base16-tomorrow-scheme/blob/master/tomorrow-night.yaml