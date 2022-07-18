#!/usr/bin/python3
'''
# meta-framework
## a mf cool minimalist/modular tool
- meta-framing
- log tool w/cron  
- meta management (exif and json)
- misc tools

rewrite of another project i made on: github.com/rightthumb
'''

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, EyeForMeta.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

_testing_=' imp modules Settings-loader '
_testing_=''
if 'modules' in _testing_:
    from sys import modules as _modules
    _modules_scrub=list(_modules.keys())

def onExit():
    global _testing_
    if 'modules' in _testing_:
        global _modules_scrub
        _modules_=[]
        for ms in _modules:
            if not ms in _modules_scrub:
                _modules_.append(ms)
                print('module:',ms)

#--> app meta
_meta_= {
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
                        'python3 mf.py [ os.fi -r + test - { path:bk, fo:foo bar } -out meta ] [ db -save fi-meta.db ]',
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
        '__file__': __file__,
    },
    'switches': []
}
#--> end#> _meta_={}


#--> start#> mini sting tool
class Str:
    placeholder ='fd2cd36d7368'
    strings = {
                    'Alpha': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'alpha': 'abcdefghijklmnopqrstuvwxyz',
                    'ALPHA': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'int': '0123456789',
                    'float': '.0123456789',
                    'not-filename': '/\\?%*:|"<>',
                    'filename': ' .-_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'visible': '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
                    'printable': ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c',
    }
    strings['printable2'] = strings['printable'] + '🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷🛶🥕🍒🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🖕🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈🐳🦑🚀🙈🙊🙉🌮🥒🐅🐯🍉🚽🍅👅🎩🍷'
    def do( self, what,a=None,b=None,c=None,d=None):
        if what in '.sh sh bash linux 2linux fix script x +x'.split(' '): return Str.sh(string);
        if what == 'be': return Str.cleanBE(a,b)
        if what == 'dup':
            while b+b in a: a=a.replace(b+b,b)
            return a
        _str = imp.load('_mf.algs.str')
        return _str.Str.do(what,a,b,c,d)
    def sh( self, string ):
        try:
            if os.path.isfile(string): string=__.getText(string,raw=True);
        except Exception as e: pass;
        string=str(string)
        string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' ).replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
        while '\t' in string: string = string.replace( '\t', '    ' );
        while ' \n' in string: string = string.replace( ' \n', '\n' );
        string=Str.do('be',string,'\n')
        return string

    def trim( self, string ):
        # string=Str.sh(string)
        if not type(string) == str: return string
        string=string.replace('\r','')
        testing=list(' \t\n')
        # def _trim_true_(string,testing):
        #     r=False
        #     for test in testing:
        #         if (string.startswith(test)): r=True
        #         if (string.endswith(test)): r=True
        #     return r
        def trimmer( self, string, testing ):
            for test in testing: string=do('be',string,test);
        while string[0] in testing or string[-1] in testing: string=Str.trimmer(string,testing)
        # try:
        # except Exception as e:
        #     return string
        
        # while _trim_true_(string,testing): string=trimmer(string,testing);
        return string


    def cleanBE( self, string, rWhat ):
        if not len(rWhat): return string;
        if not rWhat in string:
            return string
        string = Str.cleanEnd(string,rWhat)
        string = Str.cleanFirst(string,rWhat)
        return string
        
    def cleanEnd( self, string, rWhat ):
        if not rWhat in string:
            return string
        string = str(string)
        rWhat = str(rWhat)
        # string = replaceDuplicate(string,rWhat)
        string +=  '*?*'
        string = string.replace(rWhat + '*?*', '')
        string = string.replace('*?*', '')
        if string.endswith(rWhat):
            string = Str.cleanEnd(string,rWhat)
        return string



    def cleanLast( self, string,rWhat ):
        if not len(rWhat): return string;
        if not rWhat in string:
            return string
        return Str.cleanEnd(string,rWhat)

    def cleanFirst( self, string, rWhat ):
        if not len(rWhat): return string;
        if not rWhat in string:
            return string
        string = str(string)
        rWhat = str(rWhat)
        # string = replaceDuplicate(string,rWhat)
        string = '*?*' + str(string)
        string = string.replace('*?*' + rWhat, '')
        string = string.replace('*?*', '')
        if string.startswith(rWhat):
            string = Str.cleanFirst(string,rWhat)
        return string


#--> end#> mini sting tool

#--> start#> settings manager
class Settings:
    'settings manager'
    def __init__(self):
        self.storage={}
        self.demand={}
    def fn( self, subject, value=Str.placeholder, default=None, demand=None, special=None ): return self._('fn',subject,value,default,demand,special)
    def var( self, subject, value=Str.placeholder, default=None, demand=None, special=None ): return self._('vars',subject,value,default,demand,special)
    def _( self, parent, subject, value=Str.placeholder, default=None, demand=None, special=None ):
        'master manager'
        global _testing_
        if not parent in self.demand: self.demand[parent] = {}
        if not parent in self.storage: self.storage[parent] = {}
        if not demand is None: self.demand[parent][subject] = demand; return None;


        
        if not value == Str.placeholder: self.storage[parent][subject] = value
        if value == Str.placeholder:
            if subject in self.storage[parent]: return self.storage[parent][subject]
            if not subject in self.demand[parent]: return default
            
            #--> start#> loading imports
            loader=''
            test=self.demand[parent][subject]
            for scrub in imp.scrub_fn():
                test = test.replace(scrub,'')
            for ch in test:
                if ch in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.': loader+=ch
                else:loader+=' '
            loader=Str.do('dup',loader,' ')
            if '.' in loader:
                for p in loader.split(' '):
                    if '.' in p and not p.startswith('fig.'):
                        par=p.split('.')
                        run=par[0]+'=imp.load("'+p+'")'
                        if 'Settings-loader' in _testing_: print('loaded:', run)
                        exec( run )
            #--> end#> loading imports

            if 'Settings-loader' in _testing_: print('running:',self.demand[parent][subject])
            self.storage[parent][subject] = eval(self.demand[parent][subject])

        if special and type(special) == dict:

        return self.storage[parent][subject]
fig=Settings()
#--> end#> settings manager

#--> start#> simple namespace manager
class dot:
    def __init__(self): pass
#--> end#> simple namespace manager




#--> start#> python module import manager
from importlib import import_module
class import_subscriptions:
    def __init__( self ):
        self.storage={}
        self.subscribers={}
        self._scrub_fn=None
        self.scrub_mods_is = {
                                'pathlib.Path.home': 'pathlib.Path',
        }
        self.scrub_mods_starts = {
                                # 'os.path.': 'os.path'
        }
    def aliases( self, subject ):
        subject=subject.replace(' ','').replace('\t','')
        if subject in self.scrub_mods_is: subject = self.scrub_mods_is[subject]
        for k in self.scrub_mods_starts:
            if subject.startswith(k): subject = self.scrub_mods_starts[k]
        if subject.startswith('.'): subject='_mf.mods'+subject
        if subject.startswith('mf.') and not '.mods.' in subject: '_mf.mods'+subject[len('mf.'):]
        if subject.startswith('_mf.') and not '.mods.' in subject: '_mf.mods'+subject[len('_mf.'):]
        if subject.startswith('fn.') and not '.mods.' in subject: '_mf.mods'+subject[len('_mf.'):]
        return subject

    def _( self, subject, subscriber='_mf_' ):
        subject=self.aliases(subject)
        tmp=self.load( subject, subscriber )
        sub=subject.split('.')
        sub[0]='tmp'
        return eval( '.'.join(sub) )

    def load( self, subject, subscriber='_mf_' ):
        subject=self.aliases(subject)
        if not subject in self.subscribers:
            self.subscribers[subject]=[]
        if not subscriber in self.subscribers[subject]:
            self.subscribers[subject].append(subscriber)
        return self.imp(subject)

    def imp( self, subject ):
        global _testing_
        subject=self.aliases(subject)
        # print(subject); sys.exit();
        if '.' in subject and not '_rightThumb' in subject: return self.dots(subject);
        if not subject in self.storage:
            try:
                self.storage[subject] = import_module(subject)
                if 'imp' in _testing_:
                    print( 'imp.DID' )
                return self.storage[subject]
            except Exception as e:
                if 'imp' in _testing_:
                    print( 'imp.NO' )
                return None
        if 'imp' in _testing_:
            print( 'imp.YES' )
        return self.storage[subject]
    def dots(self, path):
        def _dots_(pth):
            try: exec(pth); return True;
            except Exception as e: return False;
        rts=path.split('.'); exec('global '+rts[0]);
        if _dots_(path): return eval(rts[0])
        pre=[]; thp=[];
        for i,seg in enumerate(rts):
            pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
            if i == len(rts)-1:
                exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
                f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
            else: f='1=dot()'.replace('1',npath);
            if not _dots_(npath):
                exec(f)
                if i == len(rts)-1: return eval(rts[0]);


    def scrub_fn(self):
        if not self._scrub_fn is None: return self._scrub_fn
        data='append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort, clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values, capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill'
        self._scrub_fn=[]
        for x in data.split(','):
            x=x.replace(' ','').replace('\t','')
            if x: self._scrub_fn.append( '.'+x+'(')
        return self._scrub_fn
    #--> end#> python module import manager scrub fn imp.scrub_fn

imp=import_subscriptions()
os=imp.load('os.sep')
#--> end#> python module import manager


isWin_cache=None
def isWin():
    if fig.fn('isWin') is None:
        tmp=imp._('platform.system')()
        if 'windows' in tmp.lower(): fig.fn('isWin',True)
        else: fig.fn('isWin',False)
    return fig.fn('isWin')

def isLinux():
    if isWin(): return False
    else: return True

def path( p, ab=True, pop=False, file=False, slash=None, folder=None, fi=None, fo=None ):
    os=imp.load('os.sep')
    try: os=imp.load('os.path._getfinalpathname')
    except Exception as e: pass
    os=imp.load('os.path.abspath')
    os=imp.load('os.path.isfile')
    os=imp.load('os.getenv')
    if not fo is None: pop=True;
    if not folder is None: pop=True;
    if not fi is None: file=True;

    # os = vc.FIG.imp('os')
    # os = imp('os')
    if slash is None:
        slash = os.sep
    if not p:
        return p.replace(os.sep+os.sep,os.sep)
    # print(p)
    p = p.replace( chr(92), slash )
    p = p.replace( chr(47), slash )
    while slash+slash in p:
        p = p.replace(slash+slash,slash)
    if ab:
        p = os.path.abspath(p)
        # try:
        # except Exception as e:
        #     pass
    try:
        p = os.path._getfinalpathname(p).lstrip(r'\?')
    except Exception as e:
        pass
    if type(p) == str and p[1] == ':':
        p = p[0].upper() + p[1:]
    if type(p) == str and ( pop or file ):

        if type(pop) == int:
            i=0
            while not i == pop:
                i+=1
                p = path( p, pop=True, slash=slash )
                # print(p)
            if file:
                p = path( p, file=True, slash=slash )
            return p.replace(os.sep+os.sep,os.sep)
        parts = p.split(slash)
        parts.reverse()
        f = parts.pop(0)
        parts.reverse()
        p = str(slash).join(parts)
        if file:
            p = f
    return p.replace(os.sep+os.sep,os.sep)



#--> start#> variables
# from pathlib import Path
# pathlib=imp.load('pathlib.Path')
# os=imp.load('os.getenv')
# os=imp.load('os.sep')
# socket=imp.load('socket.gethostname')

fig.var( 'home', demand='str(pathlib.Path.home())' )
fig.var( 'userprofile', demand="fig.var('home')" )
fig.var( 'computername', demand='socket.gethostname()' )
fig.var( 'computername2', demand="fig.var('computername').replace(' ','_')" )
fig.var( 'user', demand='os.getlogin()' )
fig.var( 'downloads', demand="fig.var('home')+os.sep+'Downloads'" )


# # user = os.getlogin()
# print('userprofile',userprofile)
# downloads = 
# computername2 = computername.replace(' ','_')
# #--> end#> variables



def pr(*args,p=None,c=None,pad=3,g=None,end=None,pvs=None,pv=None,json=None):

    args=list(args)
    for i, arg in enumerate(args): args[i]=str(arg)
    string=' '.join(args)
    print(string)


#--> start#> namespace manager
_mf=dot()
_mf.cl=dot()
_mf.v=dot()
#--> end#> namespace manager

#--> start#> class Code
class Code:
    """docstring for Code"""
    # def __init__(self): pass
    def index(  code, i=0, esc='\\', n='', v=True,r=False,both=True, sort=True, isArg=False ):
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
                        s=Code.index(code,i+3,esc,n='"""',v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i=s
                    elif not n and c3 == "'''":
                        s=Code.index(code,i+3,esc,n="'''",v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                    elif not n and c == "'":
                        s=Code.index(code,i+1,esc,n="'",v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i=s
                    elif not n and c == '"':
                        s=Code.index(code,i+1,esc,n='"',v=0,isArg=isArg)
                        index[i] = s
                        if both:
                            index[s] = i
                        i = s
                    elif not n and c2 == '/*':
                        i = Code.index(code,i+2,esc,n='*/',v=0,isArg=isArg)
                    elif not n and c2 == '//':
                        i = Code.index(code,i+2,esc,n='\n',v=0,isArg=isArg)+1


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
# _mf.cl.code=Code()
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
        self.index=Code.index(self.cmd, isArg=True)
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

        index=Code.index(cmd, isArg=True)
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

fig.var('term-argv',' '.join(imp._('sys.argv')))
do=Terminal( fig.var('term-argv') ).top(0).ea
# do=Terminal(_mf.v.terminal).top(0).drill(0)
# do=Terminal('[ stuff ]').drill(do[0])
# pr(do)
for x in do:
    pr(x)


'''
class SW():
    """docstring for Switch"""
    def __init__(self, label, sw, trigger=None, children=None):
        # super(Switch, self).__init__()
        self.dic = {
                        'label': label,
                        'sw': sw,
                        'trigger': trigger,
                        'children': children,
        }
'''
# _fig_figs_={}
# def con( parent='blank', subject=None, value=None, default='2108bd86bc21', p=None, s=None, v=None, d=None  ):
#     global _fig_figs_
#     if not p is None: parent=p
#     if not s is None: subject=s
#     if not v is None: value=v
#     if not d is None: default=d

#     if subject is None: return _fig_figs_
#     if value is None and default == '2108bd86bc21': return _fig_figs_[parent][subject]
#     if value is None : return default
#     if not parent in _fig_figs_: _fig_figs_[parent] = {}
#     _fig_figs_[parent][subject]=value
#     return _fig_figs_[parent][subject]



class Switches:

    def add( label=None, sw=None, trigger=None, children=None, profile=None, settings=None,  t=None, c=None, p=None, s=None ):
        if not p is None: profile=p
        if not t is None: trigger=t
        if not c is None: children=c
        if not s is None: settings=s
        val = {
                            'label': label,
                            'sw': sw,
                            'trigger': trigger,
                            'settings': settings,
                            'children': children,
            }

        if not profile is None and type(profile) is dict:
            for k in profile: val[k]=profile[k]
        
            if not val['settings'] is None and not settings is None:
                for k in settings: val['settings'][k]=settings[k]

            if not label is None: val['label'] = label
            if not sw is None: val['sw'] = sw
            if not trigger is None: val['trigger'] = trigger
            
            if not val['children'] is None and not children is None: val['children'] = val['children']+children
            elif not children is None: val['children'] = children

        return val


#--> ########## ########## ########## ########## ########## ########## ##########
#--> start#> coding

def action():
    fig._(
        'switches',
        'Perpetual-01',
        Switches.add(
                'Perpetual',
                '--perpetual',
        )
    )

    fig._(
        'switches',
        'Plus',
        Switches.add(
                'Plus',
                '+',
        )
    )
    fig._(
        'switches',
        'Minus',
        Switches.add(
                'Minus',
                '-',
        )
    )
    fig._(
        'switches',
        'Files',
        Switches.add(
                'Minus',
                '-',
        )
    )

    _meta_['switches']=[
        Switches.add('Help', '?,-?,-??,??,-help,--help,/help'),
        Switches.add('Plus', '+'),
        Switches.add('Minus', '-'),
    ]
    # pr(_meta_['switches'])


# imp.load('.os.fi')



# print( fig.var( 'home') )
# print( fig.var( 'userprofile') )
# print( fig.var( 'computername') )
# print( fig.var( 'computername2') )
# print( fig.var( 'user') )
# print( fig.var( 'downloads') )

# print()
# print()
# print()
# print()

# print( imp._('uuid.uuid4')() )
# print( imp._('uuid.uuid4')() )
# print( imp._('uuid.uuid4')() )


# print()
# print()
# print()
# print()
print( fig.var('term-argv') )


# print( __path__ )
print( __file__ )
print( path(__file__,file=True) )
print( path(__file__) )

#--> end#> coding
#--> ########## ########## ########## ########## ########## ########## ##########

if __name__ == '__main__':
    action()
    onExit()
    # __.isExit()


# import sys
# # print( sys.modules )
# for x in sys.modules: print(x)



