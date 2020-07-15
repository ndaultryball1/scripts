alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

function pycharm() {
    command pycharm "$1" &>/dev/null &
}

export PATH=$PATH:~/.local/bin
