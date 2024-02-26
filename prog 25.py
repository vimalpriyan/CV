a=imread("C:/Users/farid/OneDrive/Pictures/dogyy.png");
Lap=[0, 1, 0, 1, -4, 1, 0, 1, 0];
a1=conv2(a,Lap,"C:/Users/farid/OneDrive/Pictures/dogyy.png");
a2=uint8(a1);
imtool(abs(a-a2),[])
lap=[-1 ,-1, -1, -1, 8, -1, -1, -1 ,-1];
a3=conv2(a,lap,"C:/Users/farid/OneDrive/Pictures/dogyy.png");
a4=uint8(a3);
imtool(abs(a+a4),[])
