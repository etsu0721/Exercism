#!/usr/bin/env bash

print_two_fer_str () {
    echo "One for $1, one for me."
}

main () {
    if [[ -z "$1" ]]
    then
        print_two_fer_str "you"
    else 
        print_two_fer_str "$1"
    fi
}

# call main with all of the positional arguments
main "$@"
