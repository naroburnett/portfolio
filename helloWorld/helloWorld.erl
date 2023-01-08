% Deceleration of <helloWorld> Module 
-module(helloWorld).

% Call of <print_hello> function
-export([print_hello/0]).

% Deceleration of print_hello function.
print_hello()->
    io:format("Hello World!\n"). % Result: "Hello World!"