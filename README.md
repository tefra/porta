# porta

I am here to serve you!

# Docker installation

This step requires to have docker installed.

```console
$ docker-compose up --build
```

Only include the `--build` on the first run or if we have made changes in the requirements.

# Virtualenv installation

This step requires to setup a virtual environment manually, personally I use [pyenv](https://github.com/pyenv/pyenv-installer)

```console
$ pyenv install 3.10-dev
$ pyenv virtualenv 3.10-dev porta
$ pyenv activate porta
```

If you use zsh and enable the pyenv plugin, you can auto activate the environment every time you enter the project by defining the env like this

```console
$ pyenv local porta
```

Install the app like this

```console
$ make sync-deps
$ make sync-dev-deps  # for local development
```

Start the app

```console
$ make start
```

# Verify installation

After you start the app in any way visit http://localhost:8002 you should get a welcome message.

# Running tests

```console
$ pytest tests/
```
