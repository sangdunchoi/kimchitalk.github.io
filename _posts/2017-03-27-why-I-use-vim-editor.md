---
layout: post
title: "Using vim editor is powerfull!"
date: 2017-04-03
tags: [tips]
comments: true
---



Vim editor is really powerful. I have to compare two files before pushing commits a repository. I use the [vim configuration for the modern pythonista](http://fisadev.github.io/fisa-vim-config/). Jumping lines in a file contains thousands of lines are hard but in vim this is much easier. I often use this commands and learned from stackoverflow answers.

    vimdiff -d file1 file2

    vimdiff -d scan_module/scan_op.py Downloads/Theano/theano/scan_module/scan_op.py


<img src="/images/vim-diff.png?raw=true" style="width: 800px;"/>

&nbsp;

#### Vimdiff commands

    Ctrl + w + >  - Switch to right side window
    Ctrl + w + <  - Switch to left side window

#### Substitute

    :%s/numpy/np/gc     - Substitute a pattern with confirmation
    :%s/numpy/np/g      - Substitute all patterns
    :%s/numpy\./np\./g  - Use \ if you want to search . eg; numpy. as numpy\.

#### Find a pattern

    /pattern or ?pattern  - [n - repeat in same direction, N - repeat in backward direction]
    :5s/foo/bar           - Replace foo to bar in the 5th line 

#### Remove a highlighted words 

    :noh

#### Show white spaces as a character

    :set list

#### Comment out lines 10 to 15

    :set number (this will show line numbers, you can add this in .vimrc file to show by default)

    :set relativenumber  (Show relative numbers from the current line)

    :10,15s/^/#  (comment lines 10 to 15)

    :10,15s/^#   (uncomment lines 10 to 15)


#### Add '*' to the end of all lines

    :%norm A*
    % = for every line 
    norm = type the following commands
    A* = append '*' to the end of current line 

#### Undo/redo

    u       - undo
    Ctrl +r - redo

#### Copy/paste

    y   - Copy marked text
    yy  - Copy a line
    12y - Copy 12 lines
    y$  - Copy to an end of the line
    p   - Paste after a cursor
    P   - Paste before cursor

#### Jump commands

    h     - Move cursor left
    j     - Move cursor down
    k     - Move cursor up
    l     - Move cursor right
    H     - Move to the top of the screen
    M     - Move to the middle of the screen
    L     - Move to the bottom of the screen
    w     - Jump forward to the start of a word
    e     - Jump forwards to the end of a word
    b     - Jump backward to the start of a word
    0     - Jump to the start of line
    $     - Jump to the end of line
    G     - Jump to the last line of the document
    1250G - Jump to the 1250th line
    J     - Join line below to the current one


#### Delete 

    dw        - delete a current word
    D or d$   - delete a line after the cursor position
    d^ or d0  - delete a line before the cursor position
    x         - delete a character
    dd        - delete a line
    c$        - delete end of the line with insert mode
    cw        - delete a current word and enter into insert mode
    r         - replace a single character
    

#### Quit the file 

    :q! (without saving changes, force quit)
    :wq (save and quit the file)
    :saveas file


#### Special commands

    *    - find the current cursor word
    .    - repeat the previous command

