set nocompatible              " be iMproved, required
filetype off                  " required

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
