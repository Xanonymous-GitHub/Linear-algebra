import HW02 .*

% Question 1
disp("@ Question 1");
[ans1, ans2, ans3, ans4, ans5] = HW02.questionOne();
% a
fprintf("2-3x5: %.0f\n\n", ans1);
% b
fprintf("4.5/sqrt(2): %.3f\n\n", ans2);
% c
fprintf("7^20: %d\n\n", ans3);
% d
fprintf("cos(pi/3): %.2f\n\n", ans4);
% e
fprintf("ln 8: %.3f\n\n", ans5);

% Question 2
disp("@ Question 2");
[b1, b2, b3, c1, c2, f] = HW02.questionTwo();
[ans1, ans2, E, F, G, H] = HW02.DInQuestionTwo();
[a, b, c, i] = HW02.getMatrices();
% a
disp("(a)");
disp("A: ")
disp(a);
disp("B: ")
disp(b);
disp("C: ")
disp(c);
disp("I: ");
disp(i);
% b
disp("(b)");
items = ["A", "B", "C", "I"];

for i = 1:4
    disp("Size of "+ items(i) + " is " + b1(1, i * 1) + " by " + b1(1, i * 2));
end

disp("a31 is: ");
disp(b2(1));
disp("c21 is:");
disp(b2(2));
disp("The second row of B is: ");
disp(b3);
% c
disp("(c)");
disp("The row reduced echelon form A is: ");
disp(c1);
disp("The row reduced echelon form B is: ");
disp(c2);
% d
disp("(d)");
disp("A+2C");
disp(ans1);
disp("transpose A");
disp(ans2);
disp("E = A*B");
disp(E);
disp("F = B*A");
disp(F);
disp("G = transpose B * transpose A ");
disp(G);
disp("H = transpose (A*B)");
disp(H);
disp("Is E equal to F?")

if isequal(E, F)
    disp("Yes.");
else
    disp("No.");
end

disp("Is G equal to H?");

if isequal(G, H)
    disp("Yes.");
else
    disp("No.");
end

% e
disp("The inverses of E");

if max(max(abs(det(E) - 0))) < 1e-13
    disp("irreversible.");
else
    disp(inv(E));
end

disp("The inverses of F");

if max(max(abs(det(F) - 0))) < 1e-13
    disp("irreversible.");
else
    disp(inv(F));
end

% f
disp("(f)");
disp(f);

% Question 3
HW02.questionThree;
