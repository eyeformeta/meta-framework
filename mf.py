#!/usr/bin/python3

am= {
    'app': 'mf.py',
    'git': 'eyeformeta',
    'description': 'meta-framework',
    'categories': [
                        '',
                ],
    'aliases': [
                       'mf',
                       '~.mf',
                       '~.mf.py',
    ],
    'usage': [
                        # 'epy another',
                        # 'e nmap',
                        # '',
    ],
    'relatedapps': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'prerequisite': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'examples': [
                        'python3 mf.py [ fi -r + test - { path:bk, fo:foo bar } -out meta ] [ db -save fi-meta.db ]',
                        '',
    ],
    'columns': [
                       # { 'name': 'name', 'abbreviation': 'n' },
                       # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
    ],
    'aliases': [
                       # 'this',
                       # 'app',
    ],
    'notes': [
                       # {},
    ],
    'paths': {
        'git-base': 'https://raw.githubusercontent.com/eyeformeta/meta-framework/',
        'relative': 'mf.py',
    }
}
#--> end#> me={}

from sys import argv
def pr(*args,p=None,c=None,pad=3,g=None,end=None,pvs=None,pv=None,json=None):
    args=list(args)
    for i, arg in enumerate(args): args[i]=str(arg)
    string=' '.join(args)
    print(string)

#--> start#> python2 compatability
class dot:
    def __init__(self): pass
_mf=dot()
_mf.cl=dot()
_mf.v=dot()
#--> end#> python2 compatability

class Code:
    """docstring for Code"""
    def __init__(self): pass
    def index( self, code, i=0, esc='\\', n='', v=True,r=False,both=True, sort=True, isArg=False ):
        if isArg: a_='-+'
        else: a_=''
        def _sort(sort,dic):
            if not sort: return dic;
            ks=list(dic.keys()); ks.sort(); new={};
            for k in ks: new[k]=dic[k];
            return new

        if type(code)==list:
            code=''.join(code)
        at=i

            
        table={}
        
        table['brackets'] = {}
        table['brackets']['i']=0
        table['brackets']['open'] = {}

        table['braces'] = {}
        table['braces']['i']=0
        table['braces']['open'] = {}

        table['par'] = {}
        table['par']['i']=0
        table['par']['open'] = {}



        index={}

        i-=1
        while True:
            i+=1
            if i >= len(code):
                break
            c=code[i]
            try:
                c2=c+code[i+1]
            except Exception as e:
                c2=''
            try:
                c3=c2+code[i+2]
            except Exception as e:
                c3=''
            try:
                c4=c3+code[i+3]
            except Exception as e:
                c4=''
            try:
                c5=c4+code[i+4]
            except Exception as e:
                c5=''
            if len(esc) == 1 and c==esc:
                i+=1
            else:
                if len(esc) == 1 and c==esc:
                    i+=1
                if n=='\n' and r:
                    ii=i
                    c=code[i]
                    while not ii == 0 and c == '\n':
                        ii-=1
                        c=code[ii]
                        if ii == 0:
                            return 0
                        elif c == '\n':
                            return ii

                elif len(n) == 1 and c==n:
                    return i
                elif len(n) == 2 and c2==n:
                    return i+1
                elif len(n) == 3 and c3==n:
                    return i+2
                elif len(n):
                    pass
                else:
                    if not n and c in '0123456789.':
                        cx = c
                        ii=i-1
                        while cx in '0123456789.':
                            ii+=1
                            try:
                                cx=code[ii]
                            except Exception as e:
                                ii-=1
                                index[i] = ii
                                if both:
                                    index[ii] = i
                                break
                        index[i] = ii
                        if both:
                            index[ii] = i
                        i=ii
                    elif not n and c in a_+'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        cx = c
                        ii=i-1
                        while cx in a_+'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._':
                            ii+=1
                            try:
                                cx=code[ii]
                            except Exception as e:
                                ii-=1
                                index[i] = ii
                                if both:
                                    index[ii] = i
                                break

                        index[i] = ii
                        if both:
                            index[ii] = i
                        i=ii
                    elif not n and c3 == '"""':
                        s=self.index(code,i+3,esc,n='"""',v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i=s
                    elif not n and c3 == "'''":
                        s=self.index(code,i+3,esc,n="'''",v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                    elif not n and c == "'":
                        s=self.index(code,i+1,esc,n="'",v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i=s
                    elif not n and c == '"':
                        s=self.index(code,i+1,esc,n='"',v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i = s
                    elif not n and c2 == '/*':
                        i = self.index(code,i+2,esc,n='*/',v=0,isArg=isArg)
                    elif not n and c2 == '//':
                        i = self.index(code,i+2,esc,n='\n',v=0,isArg=isArg)+1


                    elif not n and c == '{':
                        table['brackets']['i']+=1
                        table['brackets']['open'][table['brackets']['i']]=i
                    elif not n and c == '}':
                        try:
                            s=table['brackets']['open'][table['brackets']['i']]
                        except Exception as e:
                            return _sort(sort,index)
                        index[ s ]=i
                        if both:
                            index[ i ]=s
                        table['brackets']['i']-=1
                        if s==at:
                            return _sort(sort,index)
                    elif not n and c == '[':
                        table['braces']['i']+=1
                        table['braces']['open'][table['braces']['i']]=i
                    elif not n and c == ']':
                        try:
                            s=table['braces']['open'][table['braces']['i']]
                        except Exception as e:
                            return _sort(sort,index)
                        index[ s ]=i
                        if both:
                            index[ i ]=s
                        table['braces']['i']-=1
                        if s==at:
                            return _sort(sort,index)
                    elif not n and c == '(':
                        table['par']['i']+=1
                        table['par']['open'][table['par']['i']]=i
                    elif not n and c == ')':
                        try:
                            s=table['par']['open'][table['par']['i']]
                        except Exception as e:
                            return _sort(sort,index)
                        index[ s ]=i
                        if both:
                            index[ i ]=s
                        table['par']['i']-=1
                        if s==at:
                            return _sort(sort,index)
        return _sort(sort,index)
#--> end#> class Code

#--> start#> python2 compatability
_mf.cl.code=Code()
#--> end#> python2 compatability

# class String:
#     def 

class Terminal:
    """docstring for Terminal"""
    def __init__(self, cmd):
        # super(Terminal, self).__init__()
        self.cmd = cmd
        self.ea = []
    def top(self,dump=False):
        if dump: pr(self.cmd)
        self.index=_mf.cl.code.index(self.cmd, isArg=True)
        if dump: pr(self.index)
        i=-1
        while True:
            i+=1
            if i < len(self.cmd):
                c=self.cmd[i]
                if c == '[':
                    sub=self.cmd[i:self.index[i]+1]
                    self.ea.append(sub)
                    i=self.index[i]+1
            else: break
        return self
    def drill(self,cmd):
        if type(cmd) == int:
            if cmd < len(self.ea): cmd=self.ea[cmd]
            else: return None
        pass
        am=''
        cmd = cmd.replace('\t','    ')
        while cmd.startswith(' '): cmd=cmd[1:]
        while cmd.endswith(' '): cmd=cmd[:-1]
        if cmd.startswith('{'): cmd=cmd[1:];am='{}';
        if cmd.endswith('}'): cmd=cmd[:-1]
        if cmd.startswith('['): cmd=cmd[1:];am='[]';
        if cmd.endswith(']'): cmd=cmd[:-1]
        while cmd.startswith(' '): cmd=cmd[1:]
        while cmd.endswith(' '): cmd=cmd[:-1]
        # if am == '{}':

        index=_mf.cl.code.index(cmd, isArg=True)
        # pr(index)
        ea=[]
        
        until=-1
        for i, c in enumerate(cmd):
            if until < i:
                if i < len(cmd):
                    if i in index:
                        sub=cmd[i:index[i]+1]
                        if sub:
                            ea.append(sub)
                        if cmd[i] == '{':
                            until=index[i]+1
                            pr(self.drill(cmd[i:until]))

        # i=-1
        # while True:
        #     print(i)
        #     i+=1
        #     # if i in spent: i+=1
        #     if i < len(cmd):
        #         if i in index:
        #             sub=cmd[i:index[i]+1]
        #             ea.append(sub)
        #             i=index[i]+1
        #     else: break
        return ea



#--> end#> class Terminal

class Modules:
    """docstring for Modules"""
    def __init__(self, cmd): pass
#--> end#> class Modules
_mf.v.terminal=' '.join(argv)
do=Terminal(_mf.v.terminal).top(0).ea
# do=Terminal(_mf.v.terminal).top(0).drill(0)
# do=Terminal('[ stuff ]').drill(do[0])
# pr(do)
for x in do:
    pr(x)

