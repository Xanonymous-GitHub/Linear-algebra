% HW@

A=[1,4,0,2,-1;3,12,1,5,5;2,8,1,3,2;5,20,2,8,8];
B=[-2,1,3,1;-5,3,11,7;8,-5,-19,-13;0,1,7,5;-17,5,1,-3];
X=[1,5,1,0,3;4,22,2,1,0;3,13,1,1,1;7,36,3,2,0];
c=[-2;-1;0;-1];
d=[1;2;3;4;5];
clc;

% PROBLEM_1

fprintf("<PROBLEM_1>\n\n");

rref_A_c=rref([A,c]);
rref_B_d=rref([B,d]);

disp(rref_A_c);
disp("-->> No solution");
fprintf("\n");

disp(rref_B_d);
disp("-->> No solution");
fprintf("\n");

%PROBLEM_2

fprintf("<PROBLEM_2>\n\n");

disp("rank of A = "+rank(A));
disp("rank of transpose A = "+rank(A.'));
disp("rank of product of transpose A by A = "+rank(A.'*A));
disp("rank of B = "+rank(B));
disp("rank of transpose B = "+rank(B.'));
disp("rank of product of transpose B by B = "+rank(B.'*B));

fprintf("\n");

disp("nullity of A is "+size(null(A),2));
disp("nullity of transpose A is "+size(null(A.'),2));
disp("nullity of product of transpose A by A is "+size(null(A.'*A),2));
disp("nullity of B is "+size(null(B),2));
disp("nullity of transpose B is "+size(null(B.'),2));
disp("nullity of product of transpose B by B is "+size(null(B.'*B),2));

fprintf("\n");

%PROBLEM_3

fprintf("<PROBLEM_3>\n\n");

disp("the basis for the null space of A is ");
disp(null(sym(A)));
disp("the basis for the column space of A is ");
disp(colspace(sym(A)));
disp("the basis for the row space of A is ");
disp(colspace(sym(A).').');

fprintf("\n");

disp("the basis for the null space of B is ");
disp(null(sym(B)));
disp("the basis for the column space of B is ");
disp(colspace(sym(B)));
disp("the basis for the row space of B is ");
disp(colspace(sym(B).').');

fprintf("\n");

%PROBLEM_4

fprintf("<PROBLEM_4>\n\n");

disp("Do A and X have the same rank?");
if size(A)==size(X)
    if  rank(A)==rank(X)
        disp("Yes.");
    else
        disp("No");
    end
else
    disp("No");
end

disp("Do A and X have the same column space?");
if size(A)==size(X)
    if colspace(sym(A))==colspace(sym(X))
        disp("Yes.");
    else
        disp("No");
    end
else
    disp("No");
end

disp("Do A and X have the same null space?");
if size(A)==size(X)
    if null(sym(A))==null(sym(X))
        disp("Yes.");
    else
        disp("No");
    end
else
    disp("No");
end

disp("Do A and X have the same row space?");
if size(A)==size(X)
    if colspace(sym(A).')==colspace(sym(X).')
        disp("Yes.");
    else
        disp("No");
    end
else
    disp("No");
end
    






