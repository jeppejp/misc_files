set nocompatible              " be iMproved, required
filetype off                  " required
set shell=/bin/bash
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'


Plugin 'vim-airline/vim-airline'
Plugin 'bling/vim-bufferline'
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'vim-syntastic/syntastic'
call vundle#end()            " required
filetype plugin indent on    " required


colo murphy
set smartindent tabstop=4 shiftwidth=4 expandtab
map - :Explore<cr>
map q :bn<cr>
set laststatus=2
set number
syntax on
execute pathogen#infect()

" Default syntastic settings
" Open bottom window with :Error and close with :lclose
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Highlight all search results
set hlsearch
