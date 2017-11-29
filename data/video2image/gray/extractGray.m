path1 = '/home/cpss/caffe/zhong/hmdb51/data/hmdb51/';
path2 = '/home/cpss/caffe/zhong/hmdb51/data/hmdb51_img_gray/';

folderlist = dir(path1);
foldername = {folderlist(:).name};
foldername = setdiff(foldername,{'.','..'});

for i = 1:length(folderlist)-2
    if ~exist([path2,foldername{i}],'dir')
        mkdir([path2,foldername{i}]);
    end
    filelist = dir([path1,foldername{i},'/*.avi']);

    for j = 1:length(filelist)
        if ~exist([path2,foldername{i},'/',filelist(j).name(1:end-4)],'dir')
            mkdir([path2,foldername{i},'/',filelist(j).name(1:end-4)]);
        end 
        file1 = [path1,foldername{i},'/',filelist(j).name];
	file4 = [path2,foldername{i},'/',filelist(j).name(1:end-4),'/','Gray'];
        cmd = sprintf('./Gray -f %s -i %s',file1,file2);
        system(cmd);
    end
end

