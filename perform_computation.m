% データを読み込み
load("data.mat");

% 結果を格納するための変数を初期化
results = struct();

% 102回のループで各配列に対して計算を適用
for i = 1:102
    A = squeeze(data1(i, :, :));
    B = squeeze(data2(i, :, :));
    [U, V, X, C, S] = gsvd(A, B);
    results(i).U = U;
    results(i).V = V;
    results(i).X = X;
    results(i).C = C;
    results(i).S = S;
end

% 結果を保存
save("results.mat", "results");
