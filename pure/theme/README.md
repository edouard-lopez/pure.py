# Theme

## Default

I used [Base16 schemes][base16]
* [Tomorrow][tomorrow]
* [Tomorrow-night][tomorrow-night]

## Create your own

Copy `pure/theme/template.json` to your `mine.json` and update colors. 

Then edit your config to pass the name of your file to pure using something like `--theme monokai`.

```
{
    "primary": "#b294bb",
    "info":    "#81a2be",
    "mute":    "#b4b7b4",
    "success": "#b5bd68",
    "normal":  "#282a2e",
    "danger":  "#cc6666",
    "light":   "#ffffff",
    "warning": "#f0c674",
    "dark":    "#373b41" 
}
```

[base16]: https://github.com/chriskempson/base16
[tomorrow]: https://github.com/chriskempson/base16-tomorrow-scheme/blob/master/tomorrow.yaml
[tomorrow-night]: https://github.com/chriskempson/base16-tomorrow-scheme/blob/master/tomorrow-night.yaml