for i in `ls` #for循环遍历store目录下的文件
do
   if [ -d $i ] ; then #如果当前变量的是目录
        cd $i #进入目录
		cat  << EOF >index.html
<html>
 <script>	
 window.location.replace("https://blog.shenmo.tech/post/${PWD##*/}/");
</script>
</html>

EOF


        cd ..
   fi

done
