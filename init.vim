syntax on
filetype on
set number
set showmatch
set incsearch
set hlsearch
set tabstop=4
set softtabstop=0 noexpandtab
set shiftwidth=4
filetype plugin indent on
augroup Shape autocmd! autocmd VimLeave * set guicursor=a:hor90 augroup END
set guicursor=
let $NVIM_TUI_ENABLE_CURSOR_SHAPE = 0
source $HOME/.config/nvim/vim-plug/plugins.vim
source $HOME/.config/nvim/themes/airline.vim
set termguicolors
color dracula
