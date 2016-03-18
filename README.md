### Aprils Fools day prank

A simple script I wrote to splice a song or parts of a song into someones music library.

This modules is dependent on https://github.com/jiaaro/pydub which in turn depends on ffmpeg.

Currently it only supports mp3 files, but it would be very easy to change read the pydub api reference.

LibraryMangler randomly chooses a start point somewhere between 15s-60s.

Mode1: The pranksong will append and replace the rest of the song

Mode2: The pranksong will splice itself in the middle of the song

Theirs a single function MangleLibrary which takes 3 arguments and 1 optional

First agrument is the path to the music library or the directory that get's walked looking for mp3's

Second argument is the path to the destination library. It does not need to exist and should look the same as the source library
after LibraryMangler has run
Third argument is the path to the audio file that will be spiced/appended to into their library

Fourth optional argument is a tuple of start/stop points of the audio file that will be randomly inserted into the library

In this example pranksong.mp3 will be appended to every song in the Music directory tree and saved to the Out directory:

`LM.MangleLibrary("Music", "Out", "pranksong.mp3")`

In this example pranksong.mp3 will be spliced into every mp3:

`LM.MangleLibrary("Music", "Out", "pranksong.mp3", ((0:None)))`

In this example pranksong.mp3 will be split into 3 clips 5000ms-10000ms, 84000ms-91000ms, 106000ms-110000ms. A random clip will be inserted into each song in the library

`LM.MangleLibrary("Music", "Out", "pranksong.mp3", (
  (5000,10000),
  (84000,91000),
  (106000,110000),
  ))`
