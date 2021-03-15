data = dlmread('output_day19.txt');
data(9:108,6:105) = 0.5*ones(100,100)
figure()
imshow(data,[0,1])