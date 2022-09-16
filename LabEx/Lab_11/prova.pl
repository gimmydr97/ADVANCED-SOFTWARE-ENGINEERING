secFog(Opa, A, D) :-
    app(A, L),
    deployment(Opa, L, D).

node(fog1, fogOp1). % node(id, operatorId)
node(fog2, fogOp2).
node(cloud1, cloudOp).


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

query(secFog(appOp, weatherApp, D)).