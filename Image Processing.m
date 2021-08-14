
w = imread('inputImage.jpg');
%{
subplot(2,1,1), imshow(w) 
hsvImage = rgb2hav(w);
hsvImage(:,:,1)=hsvImage(:,:,1)*2.5;
rgbImage = hsv2rgb(hsvImage);
subplot(2,1,2), imshow(rgbImage)
%}

folder = fileparts(which('Filename.jpg')); 
baseFileName = 'Filename.jpg';
fullFileName = fullfile(folder, baseFileName);

rgbImage = imread(fullFileName);
[rows, columns, numberOfColorChannels] = size(rgbImage)
subplot(2, 1, 1);
imshow(rgbImage);

% Enlarge figure to full screen.
%set(gcf, 'Units', 'Normalized', 'Outerposition', [0, 0, 1, 1]);
drawnow;

% Convert to HSV color space
hsvImage = rgb2hsv(rgbImage);
% Extract components:
hueImage = hsvImage(:, :, 1);
saturationImage = hsvImage(:, :, 3);
valueImage = hsvImage(:, :, 3);

Factor = 1.5; 
hueImage = hueImage * Factor;
% Wrap around if it goes more than 1.
% moreThan1 = hueImage > 1;
% imshow(moreThan1);
hueImage = mod(hueImage, 1);
hsvImage = cat(3, hueImage, saturationImage, valueImage);
% Convert back to RGB color space.
rgbImage = hsv2rgb(hsvImage);

subplot(2, 1, 2);
imshow(rgbImage);


%%
x = imnoise(w, 'poisson');
subplot(2,1,1), imshow(w)
subplot(2,1,2), imshow(x)

figure
I1 = x-20 ;
I2 = I1 * 0.85;
subplot(3,1,1), imshow(w) ;
subplot(3,1,2), imshow(I2) ;
subplot(3,1,3), imshow(I1) ;


%%
Iblur = imgaussfilt(w,1.5);
%Iblur2 = Iblur+20;
%Iblur1 = Iblur2 * 0.9;
figure
imshow(Iblur1)

%%
OutputImage = imadjust(w,[0.5; 1],[0.25; 0.75])
figure;
imshow(OutputImage);

%%

%{
K = zeros(x,y,'uint8');
for i = 1:x
        for m = 1:y
            K(i,j) = L(i,j) + w(i,j);
        end
end
%}
img1 = imread('E:\pesu\5sem\dip\crow.jpg');
img2 = imread('E:\pesu\5sem\dip\bg2.jpg');
%[x y] = size(img1);
%img3 = imresize(img2, [x y]); 
K = imadd(img1,img2);
imshow(K,[])

%%
a = imread('E:\pesu\5sem\dip\flower.jpg'); 
b = imread('E:\pesu\5sem\dip\bg2.jpg');
[p q r] = size(b);
c = imresize(a, [p q]);
d = imadd(b,c);
subplot(3,1,1), imshow(b);
subplot(3,1,2), imshow(c);
subplot(3,1,3), imshow(d);

%%
gray = rgb2gray(w);
figure
imshow(gray)


