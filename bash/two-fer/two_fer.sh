#!/usr/bin/env bash

main () {
    if [[ -z "$1" ]]
    then
        name="you"
    else 
        name="$1"
    fi
    echo "One for $name, one for me."
}

# call main with all of the positional arguments
main "$@"
