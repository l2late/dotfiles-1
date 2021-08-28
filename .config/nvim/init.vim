set clipboard+=unnamedplus
map <esc> :noh<CR>
autocmd BufEnter * lcd %:p:h
set number relativenumber
highlight LineNr ctermfg=grey
highlight CursorLineNr ctermfg=white

call plug#begin('~/.local/share/nvim/plugged')


" COLOR SCHEME

Plug 'morhetz/gruvbox'


" FILE MANAGER

Plug 'scrooloose/nerdtree'

map <F2> :NERDTreeToggle<CR>


" STATUSBAR

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

let g:airline_theme='gruvbox'
let g:airline#extensions#tabline#enabled = 1  
let g:airline#extensions#tabline#fnamemod = ':t'
 
let g:airline_powerline_fonts = 1
set noshowmode


" Indentation

Plug 'Yggdroot/indentLine'

let g:indentLine_fileTypeExclude = ['text', 'sh', 'help', 'terminal']
let g:indentLine_bufNameExclude = ['NERD_tree.*', 'term:.*']


" AUTOCOMPLETATIONS

Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'Shougo/neco-syntax'

let g:deoplete#enable_at_startup = 1
augroup deopleteCompleteDoneAu
  autocmd!
  autocmd CompleteDone * silent! pclose!
augroup END


Plug 'ervandew/supertab'

let g:SuperTabDefaultCompletionType = '<c-n>'


" SHOWS FUNCTION SYNTAX

Plug 'Shougo/echodoc.vim'

set noshowmode
let g:echodoc_enable_at_startup = 1


" SYNTAX ANALYZER

Plug 'neomake/neomake'


" SYNTAX HIGHLIGHTER

Plug 'sheerun/vim-polyglot'


" UNIX COMMANDS INTEGRATION

Plug 'tpope/vim-eunuch'


" () [] {}

Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-surround'


" BETTER COMMENTER

Plug 'scrooloose/nerdcommenter'

let g:NERDSpaceDelims = 1
let g:NERDTrimTrailingWhitespace = 1


" SHOWS CHANGES

Plug 'airblade/vim-gitgutter'

set updatetime=250


" RANGER INTEGRATION

Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}

let g:rnvimr_ex_enable = 1
nmap <space>r :RnvimrToggle<CR>
let g:rnvimr_ranger_cmd = 'ranger --cmd="set draw_borders both"'

" FILE SEARCHER 

Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

let g:fzf_commands_expect = 'alt-enter'
let g:fzf_history_dir = '~/.local/share/fzf-history'
nnoremap <C-p> :Files<CR>


" BETTER TABS

Plug 'kyazdani42/nvim-web-devicons'
Plug 'romgrk/barbar.nvim'

nnoremap <silent>    <A-1> :BufferGoto 1<CR>
nnoremap <silent>    <A-2> :BufferGoto 2<CR>
nnoremap <silent>    <A-3> :BufferGoto 3<CR>
nnoremap <silent>    <A-4> :BufferGoto 4<CR>
nnoremap <silent>    <A-5> :BufferGoto 5<CR>
nnoremap <silent>    <A-6> :BufferGoto 6<CR>
nnoremap <silent>    <A-7> :BufferGoto 7<CR>
nnoremap <silent>    <A-8> :BufferGoto 8<CR>
nnoremap <silent>    <A-9> :BufferLast<CR>

nnoremap <silent>    <A-,> :BufferPrevious<CR>
nnoremap <silent>    <A-.> :BufferNext<CR>

nnoremap <silent>    <A-<> :BufferMovePrevious<CR>
nnoremap <silent>    <A->> :BufferMoveNext<CR>

nnoremap <silent>    <A-p> :BufferPin<CR>

nnoremap <silent>    <A-c> :BufferClose<CR>


call plug#end()
