#{{{
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
# Move to directory of file
function cdf() {
    if [[ -d $1 ]] ; then
      builtin cd $1
    elif [[ -L $1 ]] ; then
      builtin cd "$(dirname $(readlink $1))"
    else
      builtin cd "$(dirname $1)"
    fi
}
#}}}

alias ls='ls -lt --color=auto'
alias lsa='ls -alt --color=auto'

alias du="du -sh"

function pycharm() {
    command pycharm "$1" &>/dev/null &
}

function idea() {
    command idea "$1" &>/dev/null &

export PATH=$PATH:~/.local/bin
