import docker

client = docker.from_env()

prompt_output = b'\n\x1b[38;2;66;113;174m/home/pure/.pure \x1b[38;2;150;152;150m\x1b[38;2;150;152;150m\n\x1b[38;2;150;152;150m\x1b[38;2;137;89;168m\xe2\x9d\xaf '


def test_bash_render():
    client.images.build(path='./',
                        dockerfile='containers/bash.Dockerfile',
                        tag='pure-on-bash:integration-test',
                        rm=True)
    prompt = client.containers.run("pure-on-bash:integration-test", ["bash", "-c", "-i", "echo $PS1"])

    assert '/home/pure/.pure' in prompt.decode()
    assert '\n' in prompt.decode()
    assert '❯' in prompt.decode()

# # Todo: see https://stackoverflow.com/a/56229084/802365
# # def test_elvish_render():
# #     client.images.build(path='./',
# #                         dockerfile='containers/elvish.Dockerfile',
# #                         tag='pure-on-elvish:integration-test',
# #                         rm=True)
# #     prompt = client.containers.run("pure-on-elvish:integration-test", ["elvish", "-c", "'$edit:prompt | each $print~'"])
# #
# #     assert '/home/pure/.pure' in prompt.decode()
# #     assert '\n' in prompt.decode()
# #     assert '❯' in prompt.decode()


def test_fish_render():
    client.images.build(path='./',
                        dockerfile='containers/fish.Dockerfile',
                        tag='pure-on-fish:integration-test',
                        rm=True)
    prompt = client.containers.run("pure-on-fish:integration-test", ["fish", "-c", "'fish_prompt'"])
    prompt.join('')

    assert '/home/pure/.pure' in prompt.decode()
    assert '\n' in prompt.decode()
    assert '❯' in prompt.decode()


def test_zsh_render():
    client.images.build(path='./',
                        dockerfile='containers/zsh.Dockerfile',
                        tag='pure-on-zsh:integration-test',
                        rm=True)
    prompt = client.containers.run("pure-on-zsh:integration-test", ["zsh", "-c", "-i", "echo $PROMPT"])

    assert '/home/pure/.pure' in prompt.decode()
    assert '\n' in prompt.decode()
    assert '❯' in prompt.decode()
