syntax on
filetype on
set relativenumber

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
set termguicolors
nnoremap <C-S-tab> :tabp<CR>
nnoremap <C-tab>   :tabn<CR>
call plug#begin()

Plug 'tyru/open-browser.vim' " opens url in browser
Plug 'http://github.com/tpope/vim-surround' " Surrounding ysw)
Plug 'https://github.com/preservim/nerdtree', { 'on': 'NERDTreeToggle' }
Plug 'https://github.com/ap/vim-css-color' " CSS Color Preview
Plug 'https://github.com/tpope/vim-commentary' " For Commenting gcc & gc
Plug 'whatyouhide/vim-gotham'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'pappasam/coc-jedi', { 'do': 'yarn install --frozen-lockfile && yarn build', 'branch': 'main' }
Plug 'tpope/vim-fugitive'
Plug 'morhetz/gruvbox'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}  " We recommend updating the parsers on update
Plug 'nvim-telescope/telescope-fzy-native.nvim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }


call plug#end()

let NERDTreeShowHidden=1
colors gruvbox
set noshowmode
nnoremap <C-t> :Telescope file_browser<cr>
