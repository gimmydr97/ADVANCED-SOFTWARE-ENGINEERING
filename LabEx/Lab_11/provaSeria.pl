% We assume application A is made from a list L of components. %
secFog(OpA, A, D) :-
    app(A, L),    
    deployment(OpA, L, D).

% *we can recursively define a deployment as the association of% 
%  each component C to a node N managed by OpN, i.e.d(C,N,OpN)%
% *redicate that checks if acomponent C meets its%
%  security requirements when deployed to an existing node N%
% *heck that the infrastructure operator OpN managing N --%
% towhich component C is deployed -- can be trusted according to the application operator OpA%

deployment(_,[],[]).
deployment(OpA,[C|Cs],[d(C,N,OpN)|D]) :-
    node(N,OpN),
    securityRequirements(C,N),
    trusts2(OpA, OpN), % line to be added
    deployment(OpA,Cs,D).

trusts(X,X).
trusts2(A,B) :-
    trusts(A,B).
trusts2(A,B) :- 
    trusts(A,C),
    trusts2(C,B).

app(weatherApp, [weatherMonitor]).
securityRequirements(weatherMonitor, N) :-
    (anti_tampering(N); access_control(N)),
    (wireless_security(N); iot_data_encryption(N)).

node(cloud, cloudOp).
0.99::anti_tampering(cloud).
0.99::access_control(cloud).
0.99::iot_data_encryption(cloud).

node(edge, edgeOp).
0.8::anti_tampering(edge).
0.9::wireless_security(edge).
0.9::iot_data_encryption(edge).



%%% trust relations declared by appOp
.9::trusts(appOp, edgeOp).  
.9::trusts(appOp, ispOp).
%%% trust relations declared by edgeOp
.7::trusts(edgeOp, cloudOp1).
.8::trusts(edgeOp, cloudOp2).
%%% trust relation declared by cloudOp1
.8::trusts(cloudOp1, cloudOp2).
%%% trust relation declared by cloudOp2
.2::trusts(cloudOp2, cloudOp).
%%% trust relations declared by ispOp  
.8::trusts(ispOp, cloudOp).
.6::trusts(ispOp, edgeOp).


query(secFog(appOp,weatherApp,D)).

