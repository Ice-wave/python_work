import json
import getopt,sys
import os
def Begin_analyse(path):
    dirs = os.listdir(path)
    f2=open('data.json','w',encoding='utf-8')
    for fd in dirs:
        with open(path+'\\'+fd,encoding='utf-8') as f:
            for line in f:
                f2.write(line)
    return

def caculate(data,username,repo,event):
    count_event=0
    for i in data:
        if len(username)!=0:
            if username!=i['actor']['login']:
                continue
        if len(repo)!=0:
            if repo!=i['repo']['name']:
                continue
        if i['type']==event:
                count_event=count_event+1
    return count_event

if __name__ == '__main__':
    data=[]
    username=''
    repo=''
    event=''
    opt,arv= getopt.getopt(sys.argv[1:],'i:u:r:e:',['init=','user=','repo=','event='])
    if opt[0][0] == '-i' or opt[0][0] == '--init':
        Begin_analyse(opt[0][1])
        print(0)
        exit()
    else:
        with open('data.json',encoding='utf-8') as f:
            for line in f:
                data.extend(json.loads(line))
    for i in range(0,len(opt)):
        if '--user' == opt[i][0] or '-u' == opt[i][0]:
            username=opt[i][1]
            continue
        elif '--repo' == opt[i][0] or '-r' == opt[i][0]:
            repo=opt[i][1]
            continue
        elif '--event' == opt[i][0] or '-e' == opt[i][0]:
            event=opt[i][1]
            continue
    print(caculate(data,username,repo,event))