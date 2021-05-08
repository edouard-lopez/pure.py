use path
use str

E:PURE_EXECUTABLE_PATH = (path:dir (path:dir (src)[name]))
E:PYTHONPATH = (str:join ':' [$E:PYTHONPATH $E:PURE_EXECUTABLE_PATH])

edit:prompt = {
    python3 $E:PURE_EXECUTABLE_PATH/pure/prompt.py
}
edit:rprompt = { printf "" }
