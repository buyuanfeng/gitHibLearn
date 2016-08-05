$ mkdir learngit
$ cd learngit
$ pwd
#通过git init命令把这个目录变成Git可以管理的仓库
$ git init
#git status命令可以让我们时刻掌握仓库当前的状态
$ git status
#git diff能看看具体修改了什么内容
$ git diff readme.txt 
#提交修改和提交新文件是一样的两步，第一步是git add
$ git add readme.txt
#第二步git commit
$ git commit -m "add distributed"
#版本控制系统肯定有某个命令可以告诉我们历史记录，在Git中，我们用git log命令查看
$ git log
$ git log --pretty=oneline
#回退版本Git必须知道当前版本是哪个版本，用HEAD表示当前版本，上一个版本就是HEAD^，
#上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。
$ git reset --hard HEAD^
#回退到指定版本
$ git reset --hard 3628164
#Git提供了一个命令git reflog用来记录你的每一次命令
$git reflog
#命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销
#这里有两种情况：
#一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
#一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。
$ git checkout -- readme.txt
#用命令git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区
$ git reset HEAD readme.txt
#从版本库中删除该文件，那就用命令git rm删掉，并且git commit
$ git rm test.txt
#要关联一个远程库，使用命令
$ git push -ugit push -u origin master
#关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
$git push -u origin master