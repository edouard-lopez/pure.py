import argparse
import os
import json

from pure import current_working_path, repository, prompt_symbol, virtual_env, colors


def layout():
    return "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def prompt(args):
    segments = {
        'current_working_path': current_working_path.segment(),
        'git_active_branch': repository.ActiveBranch(os.getcwd()).segment(),
        'git_is_dirty': repository.IsDirty(os.getcwd()).segment(),
        'virtual_env': virtual_env.segment(),
        'prompt_symbol': prompt_symbol.segment(args.last_command_status)
    }

    if args.json:
        [print(jsonify(segment)) for segment in segments.values()]
        return [jsonify(segment) for segment in segments.values()]
    else:
        segments_with_style = {}
        [segments_with_style.update({name: "{style}{text}".format(**segment)}) for name, segment in segments.items()]
        print(layout().format(**segments_with_style), end='')


def fetch(segment):
    return segment.get('style') + segment.get('text')


def jsonify(segment):
    return json.dumps(segment, sort_keys=True).replace('\\u00', '\\x')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('--last-command-status', dest='last_command_status', type=int,
                        help='last command\'s exit status')
    parser.add_argument('--json', action='store_true', help='return prompt as a JSON segments with colors')

    colors.load_theme()
    prompt(parser.parse_args())
