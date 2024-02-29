# Words of Power Vault

This is a trivial Python 3.10+ FastAPI server with a singular purpose of
colleting user generated [Words of Power] / [TexnoMagic] content.

This software can be used to collect user drawings as a series of points through
a REST API and save them into CSV files for further processing.

See [woptrainer] for a Godot client implemention.


## Status: alpha

It seems to work fine :)


## Installation

This is a standard python package.

Install with `pip` or `pipx` in the repo root:

    pip install .


## Configuration

You can configure `wopvault` through `wopvault.yaml` config files.

Please use

    wopvault config

to see

- config paths for your system
- current effective configuration


## Usage

You can start `uvicorn` dev server using

    wopvault server

`wopvault.api` is based on FastAPI,
feel free to use `wopvault.api:app` as you need.

See [woptrainer] for a Godot client implementation.


[Words of Power]: https://texnoforge.dev/words-of-power/
[TexnoMagic]: https://texnoforge.github.io/texnomagic/
[woptrainer]: https://github.com/texnoforge/woptrainer/
