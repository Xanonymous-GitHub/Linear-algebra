%%HW_02
classdef HW02

    properties (Access = private, Constant)
        A = [1, 2; -3, -4; 5, 6];
        B = [1, -2, -3; -4, 5, 6];
        C = [2, -1; pi, log10(2); -2, 6];
        I = eye(3);
    end

    methods (Static)

        function [a, b, c, i] = getMatrices()
            a = HW02.A;
            b = HW02.B;
            c = HW02.C;
            i = HW02.I;
        end

        function [ans1, ans2, E, F, G, H] = DInQuestionTwo()
            ans1 = HW02.A + 2 * HW02.C;
            ans2 = HW02.A.';
            E = HW02.A * HW02.B;
            F = HW02.B * HW02.A;
            G = HW02.B.' * HW02.A.';
            H = (HW02.A * HW02.B).';
        end

        function [ans1, ans2, ans3, ans4, ans5] = questionOne()
            ans1 = 2 - 3 * 5;
            ans2 = 4.5 / sqrt(2);
            ans3 = 7^20;
            ans4 = cos(pi / 3);
            ans5 = log(8);
        end

        function [b1, b2, b3, c1, c2, f] = questionTwo()
            b1 = [size(HW02.A), size(HW02.B), size(HW02.C), size(HW02.I)];
            b2 = [HW02.A(3, 1), HW02.C(2, 1)];
            b3 = HW02.B(2, :);
            c1 = rref(HW02.A);
            c2 = rref(HW02.B);
            f = zeros(4, 4);

            for i = 1:4
                f(i, i) = 3 * i - 2;
            end

        end

        function questionThree()
            x = linspace(-4, 4);
            y = 0.6 * x.^2 - 1;
            plot(x, y)
            xlim([-4 4])
        end

    end

end
