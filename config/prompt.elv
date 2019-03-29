edit:prompt = { 
    python3 $E:PURE_EXECUTABLE_PATH/pure/prompt.py \
        --json \
        | from-json \
        | each [obj]{ styled $obj[text] $obj[style] }
}
edit:rprompt = { printf "" }
