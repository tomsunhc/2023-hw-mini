# Troubleshooting

CMake uses environment variables to populate options including compile and link flags.
The configure step prints a few key variables.

If build errors occur, compare the messages with the printed flags to see if you have environment variables setting incompatible options for the cross compiler.

Example: on macOS, some may set `LDFLAGS=-Wl,-no-compact-unwind` but this is not acceptable to the cross compiler, resulting in link error:

```
Error: unable to disambiguate: -no_compact_unwind (did you mean --no_compact_unwind ?)
```

In this case, we set LDFLAGS to empty, reconfigure and build like:

```sh
LDFLAGS='' cmake -Bbuild --fresh
cmake --build build
```
