def start_menu():
    print("""
     _______      ___      .___  ___.  _______    .___________. __  .___________. __       _______ 
    /  _____|    /   \     |   \/   | |   ____|   |           ||  | |           ||  |     |   ____|
    |  |  __     /  ^  \    |  \  /  | |  |__      `---|  |----`|  | `---|  |----`|  |     |  |__   
    |  | |_ |   /  /_\  \   |  |\/|  | |   __|         |  |     |  |     |  |     |  |     |   __|  
    |  |__| |  /  _____  \  |  |  |  | |  |____        |  |     |  |     |  |     |  `----.|  |____ 
    \______| /__/     \__\ |__|  |__| |_______|       |__|     |__|     |__|     |_______||_______|
                                                                                                   
                                                                                                   """)
    print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0xol:,'..              ..',:lox0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMWMMMMMMMMMMMMMMMMWXOdc,..                              ..;cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMWWMMMMMMMMMMMMWXko;.                                     ..   .;oOXWMWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWWMMMMMMMMMMMWKx:.         ...                                      .:xKWMMMMMMMMMMMMMMMMMMMM
    MMMMMMWWMMMMMMMMMMXk:.             ...                                        .:kXWMMMMMMMMMMMMMMMMM
    MMMWWMMMMMMMMMMW0o'                     .cc;...     ...;cl'                      'oKWMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMNOc.                       lNMWXK0OOOOO0KNWMWd.                       .cOWMMMMMMMMMMMMM
    MMMMMMMMMMMW0c.                        ,0WMMMMMMMMMMMMMMMMK,                         .c0WMMMMMMMMMMM
    MMMMMMMMMWKl.                         .dWMMMMMMMMMMMMMMMMMWo                           .lKMMMMMMMMMM
    MMMMMMMMNx'                           ;KMMMMMMMMMMMMMMMMMMMO'                            'xNMMMMMMMM
    MMMMMMWKc.                           .xWMMMMMMMMMMMMMMMMMMMNc                             .cKMMMMMMM
    MMMMMWO,                             :XMMMMMMMMMMMMMMMMMMMMMk.                              ,OWMMMMM
    MMMMWk.                              'llllllllllllllllllllll:.                               'kWMMMM
    MMWWx.                             .............................                              .xWMMM
    MMWk.                           'ckKXXXXXXXXXXXXXXXXXXXXXXXXXXXKx;.                            .kWMM
    MWO'                         'lOXWMMMWWWWWWWWWWWWNNWWWWWWWWWWWMMMW0o'                           ,0MM
    MX:                         ':llcc::loooollc:;,,,'',;:cllllcc:ccccllc.                         ..:XM
    Wd.   ...                         .cx0KKXXXK0ko:;codO0KXXXK0ko,...                               .dW
    0,     ...                        cXMMMMMMMMMMMXKNMMMMMMMMMMMWO'....                              ,0
    o.                           .,'. :XMMMMMMMMMNO;'oOKWMMMMMMMMWk. .,:.                             .o
    ,                            lXo   c0NMMWNKOo;.    .:x0XWWMWXk'   :Xx.                             ;
    .                            cXx.   .,::;,.           ..;::;.    .dWK,                             .
                                .oKd.                               cXNl                               
                                 .oX0o,.                         .,xX0:                                
                                   :ONN0xl;'..           ...',:ld0NKl.                                 
                                  .,oXMWMMWNXKO:        'kXXNWWMMW0l,...                               
                              .;oOKNMMMWMMMMMMMXl.     ,OWMMMMMMMMWNNXK0xl,.                           
    .                        .l0WMMMMMMMMMMMMMMMMXl.   ,0MMMMMMMMMMMMMMMMMMN0o'                        .
    '                      .cKWMMMMMMMMMMMMMMMMMMMXl.;xKWMWNXXNWWMMMMMMMMMMMMMXo.                      '
    c                     .xNMMMMMMMMMMMMMMMMMMMMMMN0KWWKd:;;;;;cxKWMMMMMMMMMMMW0;                     c
    k.       .           'OWMMMMMMMMMMMMMMMMMMMMMMMMMXOl',oOKK0kl',xNMMWMMMMMMMMMK:                   .k
    Xc      .           .kWMMMMMMMMMMMMMMMMMMMMMMMMMXc..lXMMMMMMW0;.dWMMMMMMMMMMMMK;            ..    cN
    MO.                .oWMMMMMMMMMMMMMMMMMMMMMMMMMMO. ,KMMMMMMMMMk':XMMMMMMMMMMMMMk.           .... 'OM
    MWd.               ,KMMMMMMMMMMMMMMMMMMMMMMMMMMM0' 'OMMMMMMMWWd.cXMMMMMMMMMMMMMNl               .dWM
    MMNl.             .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMWd,.,kNWMMMWXo.'OMMMMMMMMMMMMMMMO.              lNMM
    MMMX:             '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXO:',:ool:.  ;0WMMMMMMMMMMMMMMX;             cXMMM
    MMMMXc            :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkollloo'  'xNMMMMMMMMMMMMMWl            cXMMMM
    MMMMMXl.          lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl.  :0WMMMMMMMMMMMWd          .lXMMMMM
    MMMMMMNd.         dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk,  .dNMMMMMMMMMMMd.        .dNMMMMMM
    MMMMMMMWO;       .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl.  :0WMMMMMMMMMd.       ;OWMMMMMMM
    MMMMMMMMMXd.     .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;  .kWMMMMMMMWd.     .dXMMMMMMMMM
    MMMMMMMMMMW0c.   .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXd:l0WMMMMMMMWl    .c0WMMMMMMMMMM
    MMMMMMMMMMMMWOc.  dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMNc  .cOWMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0l'oNWWWWWWWWWWWWWWNNNWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWW0;.l0WMMMMMMMMMWMMMM
    MMMMMMMMMMMMMMMMWKOxc;,,,,,,,,,,','',;;,'''''''''''''''''.'..''',''''''''''',,,cdkKWWMMMMMMMMMMWMMMM
    MMMMMMMMMMMMMMMMMMWN0o,.            ..                          ..          .,oONMMMMMMMMMMMWWMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMN0d:.                                     ....     .:o0NMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXko:'..                                   .':oOXWMMMMMMMMMMMMMWWMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkoc,..                        .';cox0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKOxl:,..            ..,:lxOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)
    input("Press any key to start:")
    
def coffee_ending():
    print("""
       ____   U  ___ u  _____   _____ U _____ uU _____ u    
    U /"___|   \/"_ \/ |" ___| |" ___|\| ___"|/\| ___"|/    
    \| | u     | | | |U| |_  uU| |_  u |  _|"   |  _|"      
     | |/__.-,_| |_| |\|  _|/ \|  _|/  | |___   | |___      
      \____|\_)-\___/  |_|     |_|     |_____|  |_____|     
     _// \\      \\    )(\\,-  )(\\,-  <<   >>  <<   >>     
    (__)(__)    (__)  (__)(_/ (__)(_/ (__) (__)(__) (__)    
    
    MMMMMMMMMMMMMMMWd.lXk,oNXOc;OWMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMXl'o0l'oXNO,;OWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMM0,,KK;'0MWx.lWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMW0:,x0l'oXNO;,OMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMNd,:Ok;;kKl''lKMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMO':X0,;KWo..oWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM0,,00;,OWd..lNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0coX0:lXNd;;xWMMMMMMMMMMMMMMMMMMMMM
    MMXdcccccccccccc:;:c;;:c::;;ccccccccccl0WMWNWWMMMM
    MMk. '::::::::::::::::::::::::::::::,. ,o:,'';oOWM
    MMO. oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0'   'loo;..cK
    MM0' lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. .lXMMMWk' ;
    MMX; ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. :XMMMMMWx. 
    MMWo .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc  lWMMMMMMO. 
    MMM0' cNMMMMMMMMMMMMMMMMMMMMMMMMMMMk.  ;KMMMMMWd..
    MMMWd..dWMMMMMMMMMMMMMMMMMMMMMMMMM0; .. :0WMWXo. c
    MMMMNl .dNMMMMMMMMMMMMMMMMMMMMMMM0; 'kO;..;c:..'dN
    MWWWWXl..lKWWWWWWWWWWWWWWMMWWMWNx. ,OWWNOoccclkXWM
    c;;;;;,.  .;;;;;;;;;;;;;;;;;;;;'   ';;;;;:dXMMMMMM
    ;.  ,clllllllllllllllllllllllllllllll:.  .dNMMMMMM
    Nk,..ckKNWMMMMMMMMMMMMMMMMMMMMMMWNKko,..lKWMMMMMMM
    MMNkc'..',:cllllllllllllllllllc:;'...;dKWMMMMMMMMM
    MMMMWXkl;..                     .,cxKWMMMMMMMMMMMM
    """)
    
def double_agent_ending():
    print("""
     _______  _______  _______  __    _  _______    ______   _______  _______  _______  _______  _______  _______  ______  
    |   _   ||       ||       ||  |  | ||       |  |      | |       ||       ||       ||   _   ||       ||       ||      | 
    |  |_|  ||    ___||    ___||   |_| ||_     _|  |  _    ||    ___||    ___||    ___||  |_|  ||_     _||    ___||  _    |
    |       ||   | __ |   |___ |       |  |   |    | | |   ||   |___ |   |___ |   |___ |       |  |   |  |   |___ | | |   |
    |       ||   ||  ||    ___||  _    |  |   |    | |_|   ||    ___||    ___||    ___||       |  |   |  |    ___|| |_|   |
    |   _   ||   |_| ||   |___ | | |   |  |   |    |       ||   |___ |   |    |   |___ |   _   |  |   |  |   |___ |       |
    |__| |__||_______||_______||_|  |__|  |___|    |______| |_______||___|    |_______||__| |__|  |___|  |_______||______| 
    """)
    print("""
    MMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMWN0xc,..   .:d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMNO::kXMMMMMMMMMMMMMMMMMWKxc,.           .cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMK;  .dNMMMMMMMMMMMMMMMWk'                .lOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMX:   cXMMMMMMMMMMMMMMW0;                   .;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMNo.  :KMMMMMMMMMMMMMMXl.                     :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWx.  ;KMMMMMMMMMMMMMWO'                      .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWO'  '0WMMMMMMMMMMMMWKc.                     .kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMK;  .kWMMMMMMMMMMMMMWk.                     .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWNx'   :0WMMMMMMMMMMMMWk.                      lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMNk;. 'c. 'oXMMMMMMMMMMMW0,                     .oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMM0,   'c. .dNMMMMMMMMMMMMNo.                    ;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMXc        ,xNMMMMMMMMMMMMNd.                 .;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMWk,         .xWMMMMMMMMMMMMWk'               .;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMO'           cXMMMMMMMMMMMMMX:               ,oOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMK:           .dNMMMMMMMMMMMMWo.              ,o0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMWO,           :KMMMMMMMMMMWNWXx:.          .;xKNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMWx.          :KMMMMMMWKkd:;dNMN0l'.     .ckNMMNklldx0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMNo.        .dNMWX0xl;.    .k0ddkOxo:;:oOKOxxOk;    ..,coxOXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMW0,       .lkxl;'.         :x,  .;:;,;;;. .:dd'          ..;ldOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWk.         .              .ll.           .oOo.               ..;lkKNMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMW0:        ';.              ,o;           ;xx:                     .;xXMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWNKx,   .ckXXc               :c..:odddxdc;ddc.                       .oNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMXoo0KkoxKWN0l.               .lkKWMMMMMMWNKl'.                        'OMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMXc..cONNKd;.                  ,0MMMMMMMMMMO,                           oWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMNd.  .;;.                     .oNMMMMMMMMNo.                          .dWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWx.                            'OWMMMMMMM0,           .,ldo'          'OMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWk.                             cKMMMMMMWd.         'cdk00Oo.         :KMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWO'                             .xWMMMMMK:          ........         .oNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMK;                              ;0MMMMWx.                           .kWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMNc                              .oNMMMK:                            ,0MMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMNd.                              ,OMMWx.                            ;KMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWk'                               cXMXc                             cXMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMW0,                               .xWO'                            .oWMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMXc                                :0l                             .kMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMNl.                  ...          .;.                             ;0MMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMNl.                 ,OX0l.                                        cXMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMNo.                 :KMWd.                                       .dNMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMWd.                 cKMNo.                                       .kWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMW0;                .lXMXc                                        '0MMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMWk'               .oNMX:                                        :KMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMW0:.             .dNMK;                                       .lXMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMXd.             :xOx'                                       .dWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMW0c.             ..                                        'kWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMNx,.                                                .,:lxONMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWXOxo'                                            .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMX:                                             cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMWO'                                             ,0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMWx.                                             .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMNl                                               ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)
    
def fired_ending():
    print("""
    ____    ____  ______    __    __   __.______       _______     _______  __  .______       _______  _______  
    \   \  /   / /  __  \  |  |  |  | (_ )   _  \     |   ____|   |   ____||  | |   _  \     |   ____||       \ 
     \   \/   / |  |  |  | |  |  |  |  |/|  |_)  |    |  |__      |  |__   |  | |  |_)  |    |  |__   |  .--.  |
      \_    _/  |  |  |  | |  |  |  |    |      /     |   __|     |   __|  |  | |      /     |   __|  |  |  |  |
        |  |    |  `--'  | |  `--'  |    |  |\  \----.|  |____    |  |     |  | |  |\  \----.|  |____ |  '--'  |
        |__|     \______/   \______/     | _| `._____||_______|   |__|     |__| | _| `._____||_______||_______/ 
                                                                                                                
                                                                                                                """)
    
    print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl:,'...           ...,:cok0XWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWKkollodxkOKXNNWWMMMMMMMMMMMMWKkl;'.         ...........        ..;lxKNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMXd;.         ...,;:clodkO0XNXOl,.     ..,:codxxkOO00000OOkkxol:,..     .,lkXWMMMMMMMMMMMMMMMMMM
    MMMWO,    .,;,'...            ..'.     .;ldO0KXXXXXXXXXXXXXXXXXXXXXXK0Oxl;..    .ckXWMMMMMMMMMMMMMMM
    MMMO'   'd0KXKK0OOkxdoc:;,'...      .lx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0kl;.    'l0WMMMMMMMMMMMMM
    MMNl   'kXXXXXXXXXXXXXXXXXKK0Oxc.   :0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOo;.   .:ONMMMMMMMMMMM
    MMNc   ,OXXXXXXXXXXXXXXXXXXXXXX0:   ,OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKkc.   .:OWMMMMMMMMM
    MWK;   .dXXXXXXXXOl:::ccllodddo:.   cKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOl.   .lKWMMMMMMM
    WO,   .:OXXXXXXXKl.                 ;x0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOl.   'xNMMMMMM
    0,   ,xKXXXXXXXXXOdc::;;,''.....      ;xKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk;   .lXMMMMM
    o   .xXXXXXXXXXXXXXXXXXXKKK00OOkxdc.   .dXKOoccokKXXXXXXXXXXXXXXXXXXKkoclokKXXXXXXXXXXXX0l.   :KMMMM
    c   ,OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk,   ;kl.    .:dOXXXXXXXXXXXXXXX0c.    .c0XXXXXXXXXXXXKd.   ;0MMM
    d.  .dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk,   ;o.      .'oKXXXXXXXXXXXXXXd.      .dXXXXXXXXXXXXXXx'   ;KMM
    K;   .dXXXXXXXXXKklcccllllooodddddc.   .dO;      'cxXXXXXXXXXXXXXXXk,      ,OXXXXXXXXXXXXXXXx.   cXM
    0,   .oKXXXXXXXXO,                    .oKX0d:,,;lOKXXXXXXXXXXXXXXXXXOo;,,;o0XXXXXXXXXXXXXXXXKo.  .dW
    :   .dKXXXXXXXXXKxc:;;,,,'''.....      .o0XXXKKXXXXXXXXXXXXXXXXXXXXXXXXKKXXXXXXXXXXXXXXXXXXXX0c   '0
    .  .oXXXXXXXXXXXXXXXXXXKKKKK0000Okdl,.   :0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk.   o
       .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKo.  .oKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc   ,
    .  .cKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk'   lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXd.  .
    o.  .:OXXXXXXXXK0kkkkOOO0000KKKKKKK0d,   .xXXXXXXXXKKOkxdoolloodxkO0KXXXXXXXXXXXXXXXXXXXXXXXXXXk.   
    Nl    :0XXXXXXKd.............''',,,.    'dKXXX0koc:;'..          ...,cok0XXXXXXXXXXXXXXXXXXXXXXO'   
    Nc   .dKXXXXXXKd,....                 .cOXKOo:..                       ..:oOKXXXXXXXXXXXXXXXXXXO,   
    O.  .lKXXXXXXXXX0OOkkkxxxddooollc:'    :kd;.            .........          .;d0XXXXXXXXXXXXXXXXk'   
    k.  .oXXXXXXXXXXXXXXXXXXXXXXXXXXXX0l.   .        ..':ldkO000000Okdo:,.        'o0XXXXXXXXXXXXXXx.   
    K;   ;OXXXXXXXXXXXXXXXXXXXXXXXXXXXX0;         .:dO0KXXXXXXXXXXXXXXXXKOd:.       ,dKXXXXXXXXXXXKl.  .
    Wk.   'ok00KKKKKXXXXXXXXXXXXXXXXXXKd.       ,oOXXXXXXXXXXXXXXXXXXXXXXXXXOo,      .cOXXXXXXXXXXO,   :
    MWO:.   ...''',,,;;;:::ccccllloooc,.      'o0XXXXXXXXXXXXXXXXXXXXXXXXXXXXX0d'      ,kXXXXXXXXKo.  .k
    MMMNOc..                                .:OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO:.     ,kXXXXXXXk'   cX
    MMMMMWX0kko.    ':c:::;;;,,,'.         .l0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0l.     ;OXXXXX0:   '0M
    MMMMMMMMMMW0;   .l0XXXXXXXKK0;         c0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc.    .lKXXX0c   .xWM
    MMMMMMMMMMMMXl.   :OXXXXXXXXO'        ,OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO,     'kXX0:   .dWMM
    MMMMMMMMMMMMMNx.   :0XXXXXXXx.       .lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKl.    .dXk;   .xWMMM
    MMMMMMMMMMMMMMWd.  .xXXXXXXKl.       .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.    .co'   'kWMMMM
    MMMMMMMMMMMMMMMO.  .oXXXXXX0:   'lolld0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0dlllo:'.   :0WMMMMM
    MMMMMMMMMMMMMMMK,   cKXXXXX0:   ,OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOl.   .dXMMMMMMM
    MMMMMMMMMMMMMMWk.  .oKXXXXXXd.  .oKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKkc.   .c0WMMMMMMMM
    MMMMMMMMMMMMMMX:   ;OXXXXXXX0;   ,kKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0d;.   .cOWMMMMMMMMMM
    MMMMMMMMMMMMMMO'  .lXXXXXXXXKl    .:dOKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOd:.    .l0WMMMMMMMMMMMM
    MMMMMMMMMMMMMMx.  .xXXXXXXXXKl.      .,cdOKXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOxl;.    .;xKWMMMMMMMMMMMMMM
    MMMMMMMMMMMMMWd.  .kXXXXXXXXKl   .,.     .':ldkO0KKXXXXXXXXXXXXXK0Okdl:,.     .;d0WMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMWd.  .xXXXXXXXX0:   ;KXko;.       ..',,;:ccccccc::;,..       .;lkKWMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMk.  .dXXXXXXXXk'   oWMMMWXOdl:'..                     .';ldOXWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMK,   :0XXXXXX0c   '0MMMMMMMMMWNX0kxdollc:::;;::ccloxk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMWd.  .dKXXXXKo.  .dWMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMX:   .dKXXOc.   lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMK:   .,c:.   .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMXd'       .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWKl'   .;kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)
    
def camera_recorder():
    print("""
                                                    MMMMMMMMMWNXKKKXNWMMMMMMM
                                                  MMMMWWXK00Odc,'.',;cox0NMMMMM
                                            MMMMMWMMWX0kdlccccc::;,......:d0WMMM
                                        MMMMWNKOkkkkkxxdxdddodxkkkkdo:,....'lKWMMMM
                                      MMMWX0kdlccccllloooxkkOOOOkOOOOkko:'...cKMMMMM
                                  MMMMMWN0xdddoolllccllllodxkOOOkOOOOOOOkxl,.'OMMMMM
                               MMMMWNXK0OOOkkkkkkxddlcccclloxkOOkOOOOOOOOkkxclKMMMMM
                          MMMMMWNXKOkxxxxkkkOOkOOOkkkxddodxkkkOOOOOOOOOOOOOOkOXWMMMMM
                      MMMMWWNK0kxdolccccllloxkkOOOOkkOOOOkkkkkkkOOOOOOOOkkxxdoxKWMMMMM
                  MMMMWNXK00kxdollcclcclllodxkOOOOOOOOOOOOkkkkkkkOOkkkxddooooooxXMMMMM
             MMMMMWNXKK0OOOOkkkkxxddooodxkkOOOOOOOOOkkkkOOOOkkkkkxxdoooooooollookNMMMM
          MMMMWNNXK000OOOO0000OOOOOkkkkOOOkOOOOOOOOOOOOOOOkkkxddoollolooolcccccld0WMMM
        MMMWNXK0OkxdddoodddxxkOO00OOkkOOOOOOOkOOOOOOkkkkxxdooollllllcccccccllc:clxNMMM
      MMMWXK0kdoooolllloolooolooxkO0OOOOOOkkkkkOOkkxxdddooooooolcccllllccccoolclodKWWWWWWWWWWWWMMMMMMMMM
     MMWNK0xdollooooooooooooollooodxk00OOkkOOOkOkxoodxxkkkkkkkkkxkkkkkkkkxkkkkkkkk0KKKKKKKKKKKKKKNWMMMMM
    MMWXKOdollllccclllloolooollooooloxO0OOkOOOOOkddxkOOO000000000000000000000000000000000000XNNX0OKWMMMM
    MWNKkdooolc,...',clllllllllllllooodk00OOOOOOkddkkkOOOOOOOOOkOOOOkkkkkkkOOkkkkkkkkOOOOOkOOKXXKO0NMMMM
    MNKOdoool:.....,clldxxdlc:::ccllooook00OOOOOkodkOkkkOOOOOOOOOOOOkkkkkkkOOOkkkkkkOOOOOkkkOOOOK0OXMMMM
    WX0xolllc'....;cloxkkkdl:;;;;;:clooook00OOOxoclkOkkkOOOkkkOOOkkkOkkkkkOOOOOkkkOOOOkkkkkOOOOO00OXMMMM
    WX0xolll;....,cloxkkxoc;;;;,''',:looodO0OOOdc:cxOOOOOOOOOOOkOOOOOOkOOOOOOOOOkOOOkOkOOkkOOOkO00OXWMMM
    WXOxolll,....;lloxkxo:;;;;'''..',coolok00Okdc:cxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkOOOkOOOOOO00OKWMMM
    WX0xolll;....;clldxdl:;;;,''''..':oolox00Okdc:cdkkkOOKXKO0KX0OKNKO0XNNX0OO0XNNXKOOKXXXKOOOOO00kkKWMM
    MNKOdlllc'...':llllc:::;;;''''..,coolox00Okdc:cdkkkkOXMWXNMWK0NMN0KWWWWWKOXWWWNK0XWWNWWN0OOO00xokNMM
    MWX0kololc'...,cllllodoc;;;,'''';llllok0OOOxc:cdkkkkO0WMMMWXO0NMN0KWWXNMN0XMMWNK0NMNKXWWKOOO00xoxXMM
    MMWX0xooooc,...':clldxdc::::;;;:lllllxO0OkOxc::okkOkkOKWMWXOk0NMN00NMWWWKOXWMWNK0KWWWWWN0OOO00xoxXMM
     MMWX0kdooolc;,,;:clllllcccccclllllldO0OkkOxl::okOOOkkO0XKOkkOKXKOOKXXK0Ok0KXXK0OO0KXK0OOOOO00kdONMM
      MMWNKOxooooooolllllooooooolllllloxO0OOkxoc:::okkOOOOOOkkkkkkkkkkkOOkOOOOkkkkOOOOOOkkkkOOOO0KOOXMMM
       MMMWXKOxdoloooooooooooooooollodk00kdl:'..'::okOOkkOOkkkkkkkkkOOOOOOOkkOOkOkkkkOOOOkkkkOOO0KO0NMMM
        MMMMWKkkkxdoooooolloollooodxkOko:,......'::lxkOOOOOOOOkkkkOOOOOOOOOOOkOOOkkOOOOOOOOOOOOO0K0OXMMM
         MMMMKc;ldkkkkxdddddddxxkkkxl:,..........',cxOkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkOOOOOOO0K0OXMMM
          MMMNo...';cloddxxxxdooc:,...'............:xOOOOOOOOOOOOOOOkkkkOOOOOOOOOOkkOOkkkOOOOOOOOOOOXMMM
          MMMMO,......................'........':oOXNK0OOkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0XWMMM
           MMMNx;.....................'.....,cx0NMMMMWWWNXXXXXXNNNNXXNNNNNNNNNNNXXXXXXXXXXXXNNXXXNWMMMMM
             MMWNKOkxxdolcc:;,''......''';lkKWMMMMMMM
              MMMMMMMMMMMMWWNNXK0OkkxxkOKNWMMMMMMM
    
    """)

def envelope_note():
    print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkdoollllllllllodxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxolldkkOOOOOOOOOOkxolloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkocldkkkkOOkkOOkkkkkkOOkkdlcokXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdlcdkkkkkkkkkkkkkkkkkkkkkkkkkkocld0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMWWMMWKxlclxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxlclxKWMMMMMMMMMMMMWWMMMMMMMMMMMMMM
    MMMMMMMMMMMXxoxddddddddxddxdo:,:lllllllllllllllllllllllllllllllllllc:,:oddddddddddddddoxNMMMMMMMMMMM
    MMMMMMMMMMMKclkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkklcKMMMMMMMMMMM
    MMMMMMMMMMM0coOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOllKMMMMMMMMMMM
    MMMMMMMMMMMKcoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOllKMMMMMMMMMMM
    MMMMMMMMMMMKcoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOocKMMMMMMMMMMM
    MMMMMMMMMMM0coOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOolKMMMMMMMMMMM
    MMMMMMMMMWKo;oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo;oKWMMMMMMMMM
    MMMMMMMXkoc;,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,;cokXMMMMMMM
    MMMMN0dc:ldl;oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOl;ldl:cdONMMMM
    MWKxl:codddl;oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo;ldddoc:lxKWM
    klcclddddddl,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,lddddddoc:lk
    .':odddddddc,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,ldddddddo:'.
    cdl;;coddddc,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,cddddoc;;ldc
    oNWKxc;:lodc,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOl,cdol:;cxKWNo
    oNWMWN0dc;:;,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,::;cd0NWWWNo
    oNWWWWWWNOo;'ckOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkc';oONWWWWWWNo
    oNWWWWWWWWWXOdlldkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkdlldOXWWWWWWWWWNo
    oXWWWWWWWWWWWWXkolldOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOxllokKNWWWWWWWWWWWXo
    oXWWWWWWWWWWWWWWNKxollxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOxlloxKNWNNNNNWNNNNNNNXo
    lXWNNNNNNNNNNNNNNNNN0xoloxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOxollx0NNNNNNNNNNNNNNNNNNXo
    lXNNNNNNNNNNNNNNNNNNNNX0dllokOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkolldOXNNNNNNNNNNNNNNNNNNNNXl
    lXNNNNNNNNNNNNNNNNNNNNNNNXOdlldkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkdlloOXNNNNNNNNNNNNNNNNNNNNNNNXl
    lXNNNNNNNNNNNNNNNNNNNNNNNNNNKkolldkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkdllokKXNNNNNNNNNNNNNNNNNNNNNNNNNKl
    lKNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKxolldOOOOOOOOOOOOOOOOOOOOOOOOOOdlclx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXKl
    lKNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNX0xollxkkkkxxxxxxxxxxxxxxxxdlcld0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKl
    lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOc,cddddddddddddddddddddl;ckKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKl
    lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOdlld0NWWWWWWWWWWWWWWWWWWWWWXkoodOKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKl
    lKXXXXXXXXXXXXXXXXXXXXXXXXXXXX0dlcoONWWWWWWWWWWWWWWWWWWWWWWWWWWNKxoldOKXKKXKKXXXXKKKKKXXKKKKKKKKKX0l
    l0XXXXXXXXXXXXXXXXXXXXXXXXX0xlcokXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNOdllx0KKKKKKKKKKKKKKKKKKKKKKKKK0l
    l0XXXXXXKKKKKKXXKKXXKXXK0xlclxKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXkollx0KKKKKKKKKKKKKKKKKKKKKK0c
    l0KKKKKKKKKKKKKKKKKKK0xlccd0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKxlclx0KKKKKKKKKKKKKKKKKKK0c
    c0KKKKKKKKKKKKKKKK0koccoOXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0dlclx0KKKK0KKKKKKKKKKK0c
    c0KKKKKKKKKKKKK0koccokKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOoccok00000000000000Oc
    c0KKKKKKKKKK0Ooc:lxKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKkl:cok00000000000Oc
    cOKKKK0KK0Odc:cd0KXXXXXXXXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXXK0xc:cok00000000Oc
    cO00000Odc:cdOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOdc:cdk00000Oc
    cO00Odc::ok0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0ko:;cdOO0Oc
    ckxl::lx00K000000000000000000000000000000000000000000000000000000000000000000000000K00K000K0xl;;cdkc
    ',;:okOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOko:,,.
     .';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'  
     """)
    
def gun():
    print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0KWWMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMWWMWXXXNMMMM
    MMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMWMWWXo:;;lk0000KNWWWNNWWMMMMMMMMMMWWMMMMMMMMMMMMMWMMWXOdollccccOMMM
    MMMMMMMWWWMMMMMMMMMMMMMMMN0dlccoOXMMMO;;:,.,:c:::lllllc;:oddxdxxxkxddollollooooooolool;..';;:;,.:KMM
    MMMMMMWWMMMMMMMMMMMMMMMMNo.......;dKNO:',;looolollolloc',;;;;;;::::;;,,c:.,:::::::::cccccccccc:,,xWM
    MMMWWMMMMMMMMMMMMMMMMMMMWx::lo:....,:',loooc,,;'';c:::'';;;,;;,''';;;;::;'';,;;;;;;;;;;;;;:;,:c..,dN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l..'..cdol;.'ld;,dxxxd:';:;;::'. .clllclllllclllllllllllllllllc',,:X
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc...:ool'',,c:..cddxxdlcccccl,  .:::::::::::::::::::::::::::::.,,cN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOk:..;::;..:;,c...,odxxxxxxxxxx;..........................',,,,,..'dW
    MMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,...'';..:;'c;,o:.'ldddl::::::::.  .,,,,;.....''''''....;l;':cccl;.lXM
    MMMMMMMMMMMMMMMMMWWWX0kxxdoc'.',:l,'c''oc,:,,oo,;ddxo..cllllll'  .,,,,,.''..............',;;;;;';0MM
    MMMMMMMMMMMMMMMMMNOc,''',;:lloodool:;,,;,.,,,dl':xxxdc;;;;;::;.',';;;;;.',cO00000000000000000000XWMM
    MMMMMMMMMMMMMMMMNl..''''.',;cooooooddoool,..;c,''lxxdxxddddddo;cc;olllc'',xMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMNo.',,,,,,,,'.,cooooooooooo;..'.'.'c::cccccc:c:',,;oolo;',:0MMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMXl.';;,,,,,,,;;'.;looooooooc,..';;;;;;;;;;;;;;;;;..';,,,.,;oWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMWO;.','',,,,,,,;,,,.,looooooo,':.,llllllllc;,;clllo;.';;;'.;;kMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMNd'.........,,,,,,,,,.'coodddo,,o,,lollollo;...:olll;.,:;;,:;cKMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMXl.....''''...',,;;,,,,.'ldoc:;..,..'',,',,,;'.;llllo:,;::cc:;kWMMMMMMMMMMMMMMMMMMMMWWMMMM
    MMMMMMMMWXl....''....''..',,,,,,,;,',,,,.,oo,........oOOxc;:ll:ck0OOOOOKWMMMMMMMMMMMMMMMMMMMWWWMMMMM
    MMMMMMMMKc....''..,...''..,,,;;;;;;'.:o;,OMWNOc....,OWWMMWx,;;cKMWMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMM
    MMMMMMMXc....'''.....'''..,,..,;;'....:,cNMMMMO'..'xMMMMMMNl.,xWMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMM
    MMMMMMXc....'''''''''''....;ok0KKOxdxd;.cKWMMMK;...lNMMMMMK:.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMNo....'''''''''''....cXMWWWMMMMMWo',lKMMMW0:. .,xNWW0c',xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMWk'...'''''''''''....:KWMMMMMMMMMMXo,':dk0XNKxol:cxko,':kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMK;...''''''''''''..'.lWMMMMMMMMMMMMWOoc,'';;:::::;,';lxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMNl....''''''''''''..'.oWMMMMMMMMMMMMMMMNK0OkkxxxxkkO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMO'...'''''''''''',..'.lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMWl....'''''''''''''..'.cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMK;...''''''''''''''..'.;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMk....''''''''''''''...''xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MWl....'',;'..'..'''''..,.cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MX:...',;;;'..'..'''''..','dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    M0,...;,,,'''..''''''''..,',OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    Mk'...,,'''''''''''''''..',.cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    Mx.,'....................''.:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    Mk'...............''',;:cllxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MWKOkkkxkkkOOO000KKKXXNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)
    
def memory_stick():
    print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOdc,'............,;cdOXWMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkc'...,;:ccclccccc:;,'....;oONMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0d:...,:clllllllllllllllllll:;'..,dKWM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl,...,:llllllllllllllllllllllllllc;..'dN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKx:'..';cllllllllllllllllllllllllllllllll;..c
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOo;...,:cllllllllllllllllllllllllllllllllllll:..
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkc;'..';cllllllllllllllllllllllllllllllllllllllllc. 
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0d:...',:clllllllllllllllllllllllllllllllllllllllllloo' 
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl,...,cllllllllllllllllllllllllllllllllllllllllllllooodl. 
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKx:'..';clllllllllllllllllllllllllllllllllllllllllllloooooolc. 
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo;...,:lllllllllllllllllllllllllllllllllllllllllllllooooolllllc. 
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkc'..';cllllllllllllllooooollllllllllllllllllllllllloooooollllllllc. 
    MMMMMMMMMMMMMMMMMMMMMMMMMMN0d:...,:cllllooollllllllok00KKkollllllllllllllllllllloooooolllllllllll:. 
    MMMMMMMMMMMMMMMMMMMMMMWXOl,...,:lllllllx000OdllldxxkOOkOOxlllllllllllllllllloooooollllllllllllll:. :
    MMMMMMMMMMMMMMMMMMMWKxc'..';clllllllodkOOOOOxxxkOOOOOOxdolllllllllllllllloooooolllllllllllllc:,...oX
    MMMMMMMMMMMMMMMMN0o;...,:lllllllllldOOxoooxkkkxddO0KXXX0xollllllllllllooooollllllllllllllc;'..'cxXWM
    MMMMMMMMMMMMMMXo,..';clllllllllllloOKkdkO00Okxxxkkkxxxxdlllllllllloooooollllllllllllll:,...,lONMMMMM
    MMMMMMMMMMMMMWo .:clllllllllllllllxKKOkkkxxdddddolllllllllllllloooooolllllllllllllc:,...:d0NMMMMMMMM
    MMMMMMMMMMMMMNc 'oooollllllllok0000Oxollllllllllllllllllllloooooollllllllllllllc;'..'ckXWMMMMMMMMMMM
    MMMMMMMMMMMMNO, 'odxddooolllloxO00kdlllllllllllllllllllloooooollllllllllllll:,...;oONMMMMMMMMMMMMMMM
    MMMMMMMMWXkl,'':dkkkkxxdddoolllllllllllllllllllllllllooooollllllllllllllc;'..':xKWMMMMMMMMMMMMMMMMMM
    MMMMMN0d:'',cdkkkkkkkkkkxxxddoolllllllllllllllllooooooollllllllllllll:;...,lkXWMMMMMMMMMMMMMMMMMMMMM
    MWXkl;'':lxkkkkkddkkkkkOOkkkxxddooollllllllllooooooolllllllllllllc:,...:d0NMMMMMMMMMMMMMMMMMMMMMMMMM
    xc,',cdkkOkkkoc;,;okkkkOOkkOOkkxxxdddolllooddoolllllllllllllllc;'..'cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    ..cdkkkkkkkOxl:codxxoccoxOkkOkkkkkdodxxxxxddolllllllllllllc:,...;oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
     ':codkOkkOkkkkkkxl;,;coxkkkOkkdlc;;ldxxxddoollllllllllc;'..':xKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
     ',,;cxOOkkkkkkkkkxddkkOkkkxol:,,,,;ldxxxddoolllllllc;...,lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
     'cokO0kxxkOkkOkkkkkkOkkdoc;,,,,,,,;ldxxxddoollc:,....:d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
     'oOKKK0OOkxxkkkkOOkxdl:;,,,,,,,,,';ldxxxddoc;'..';cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    c'',cdO0KKK00Oxxkkxc;,,,,,,,,,,'....':lool;...;oONWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WXkl;'';ok0KKK00Oxl;',,,,,,'.....:oo;'....':xKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMN0d:'.,cxO0KK0d;,,,,'....,lkXWMMWX0OOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWXkc,'';okko;''....:d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMN0o:'.,,...,ckKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0l.  ,xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)