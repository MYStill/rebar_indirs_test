%%%-------------------------------------------------------------------
%% @doc rebar_inders_test public API
%% @end
%%%-------------------------------------------------------------------

-module(rebar_inders_test_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    rebar_inders_test_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
