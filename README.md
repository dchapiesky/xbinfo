# xbinfo: Information about an xbstrap OS distribution

xbinfo is a utility to gather information from an OS distribution managed by xbstrap.

## xbstrap

xbstrap is a build system designed to build "distributions" consisting of multiple (usually many) packages.

See [xbstrap](https://github.com/managarm/xbstrap)

**Official xbstrap Discord server:** https://discord.gg/7WB6Ur3

## Installation

xbinfo is available from github

```
pip3 install xbinfo git+https://github.com/dchapiesky/xbinfo
```

or you may download the repo into a directory and run

```
pip3 install ./download-directory
```


## Basic usage

### Dependency Graphs

A full dependency graph of the xbstrap project can be created using:

```
xbinfo full-graph path-and-filename-without-extension-for-graph
```

The path and filename will be appended with ".png": the graph output file type

This command results in a graph much like this...

[Full Dependency Graph](./images/full.png)


A dependency graph of a specific package can be created using:

```
xbinfo pkg-graph package-name path-and-filename-without-extension-for-graph
```

possibly resulting in a graph like this...

[base Dependency Graph](./images/base.png)

You may append --dot to the graph commands...

```
xbinfo full-graph path-and-filename-without-extension-for-graph --dot
xbinfo pkg-graph package-name path-and-filename-without-extension-for-graph --dot
```

In addition to the png output file, a graphziv DOT file containing the raw data used to generate the graph will be created.


### Other Information

xbinfo can also tell you which packages are considered unstable by the OS Maintainers...

```
xbinfo show-unstable
```



