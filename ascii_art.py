def start_menu():
    print("""
         _______..______   ____    ____  __     _______.     _______   ______   .__   __.  _______    
    /       ||   _  \  \   \  /   / (_ )   /       |    /  _____| /  __  \  |  \ |  | |   ____|   
   |   (----`|  |_)  |  \   \/   /   |/   |   (----`   |  |  __  |  |  |  | |   \|  | |  |__      
    \   \    |   ___/    \_    _/          \   \       |  | |_ | |  |  |  | |  . `  | |   __|     
.----)   |   |  |          |  |        .----)   |      |  |__| | |  `--'  | |  |\   | |  |____    
|_______/    | _|          |__|        |_______/        \______|  \______/  |__| \__| |_______|   
                                                                                                  
                     .______        ______     _______  __    __   _______                        
                     |   _  \      /  __  \   /  _____||  |  |  | |   ____|                       
                     |  |_)  |    |  |  |  | |  |  __  |  |  |  | |  |__                          
                     |      /     |  |  |  | |  | |_ | |  |  |  | |   __|                         
                     |  |\  \----.|  `--'  | |  |__| | |  `--'  | |  |____                        
                     | _| `._____| \______/   \______|  \______/  |_______|                       
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
    recorder = """
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

    """
    return recorder


def envelope_note():
    envelope = """
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
     """
    return envelope


def gun():
    gun = """
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
    """
    return gun


def memory_stick():
    usb ="""
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
    """
    return usb

def key():
    key = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdl:;;;;;;;;;;;;;;;:ldOXWMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:,;:ldk0XNNNNNNNNXK0kxl:,,:oONWMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;':d0XNXKK00OOOOOO000KXNNWWXOo:',o0WMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl';o0NN0OkddddooooooooodkKNNNNNNWN0d;'c0WMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0d''dXNKOxdodddddddddddodOKNNNNNNNNNWNWXx,.oXWWMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..lKNXOdddddoddddddddddOXNWNNNX0kkOXNNNNNKl.'kWMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,.;dNNKxddooodddodddddddkXNNNN0l'.  ..ckNNNNNd..oNMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;.xXNN0xdodddoddoodooodddONNNWO'   .';,..xNNNNNd. cXM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.lNWNKxooodddddddddooooddONNNNo   ;ONWWd.:XWNNNNl  oN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.,0WNXkodoodddddddoooddoookXWNNk. .kWWW0;.oNNNNNW0, .k
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWl.lNNN0doddodddddddooddddoodOXNNNk;.'cc:',xXNO0NNNNl  ;
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:.xWNXOodooddddddddddddddddddx0XNWX0xoodOXNKOdkNNNWx. .
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,.OWXKkoddoddddddddddddddddooodxkO0KXXXKKOkddokXNNWk.  
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,.OWXKkoddoddddddddddddddddddooooddddddddoodookNNNWO.  
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX;.kWXKkodooddddddddddddddddddddooodddooddooood0NNNNx.  
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc.dWNXOddoodddddddddddddddddooodddoodoodddddokXNNNXl   
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.cNNN0doddodddddddddddddddddddddddoodddooddxKNNNNO'  .
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWW0''OWWKxoodddddddddddddddddddddddddodddoddoxKNNNNXc   l
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNO'.xNXOdodddddddddddddddddddddddddddooddodkXNNNWXl.  '0
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c.;kX0kxooodddddddddddddddddoooodddooooddx0XNNNNXl.  .xW
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMXo''xXN0xooododdoooooodddddddddoooooodddodk0XNNNNN0;   .xWM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd''oKNXkddooooooddooooooodddddddoodooodxkOKNNNNNNKo.   'kWMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNx,'l0NX0xdooddddooodxxkkkkkkkkkxxxxxxkkOKXNNNNNWN0o'   .:KMMWM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk;.c0NX0xddodddddodk0KXNNNNNNNNNNNNNNNNNNNNNNNWN0d:.   .;kNWMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:.;ONX0xddddodddoox0NNNNNNNNNWWWWWWNNNNWWWNXKkdc,.    .cONMWWMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc.,xXXOxdodooddddooxKNNNNN0l;:cloodddddoolc:;'.     .'cxKWMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo',dXXOxddddooddddxxOXNNNNKo.                    .';cd0NWMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,'oKX0xdoodddxkO00KNNNNNNXx'   .:xxdollcccccloodk0KNWMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMWWNk;'lKNKkdodddx0XXNNWNNNNNWNO;    ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWWNO;.:0NXOdoddodkXNNNWNNNNNNN0l.   'xNMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMWWWO:.;kNXOxoooooodONNNWKo;:cooc.   .lKMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMWWKl.,xNX0xoddodddodONNNWO'        .:0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMXo',dXNKkdodooddxkk0NNNNWk.  ;ddollkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMNx,'oKNKkdoodxO0KXXNNNWNNNNo   oWMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMWNk,.c0NKkdddodOXNNNNNNWWNNN0c.  .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMNO;.:0NXOxoooodxKNNNWKdlooddl.   .dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMW0c.;kNXOxoddooodd0NWNW0,        .c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMWKl',xXX0xdoodooooodONNNWK;  .ll::ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMXd''dXN0xdooddxkkkkOKXNNNWK;  ;XMWWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMNx,'oKNKkdoodk0KXNNNNNNNNNNO:.  ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMNk,.l0NKkdoodokXWNNNNNWWNWNKl.   .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMWO;.:ONXOdoddoookXWNWKl:cllol'   .cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    W0c.;kXXOxdddoddddONNNWO'        .;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    l.,xXNXkddddodddk0XNNNWO'  ,dolllkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    ..oXNNNNKK0000KXNNWNNNXd.  oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    Kc.;ONNNNNNNNNNNNNNNXx,    oWMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WNk,.ckkkkOOOOOOOOko,    ,dXMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMXd'                 ,xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMWWO'              .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return key

def ink():
    ink = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kkOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMNOo:,'''',;lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc,'';,,;;;:;'',:xKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOoc;'',:lo:.....,c::;,'';lkXWMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxc;'',;cl::::::;,,;..';;;;:;,',cxKWMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOo:'',:lc:::ldOK0xoc:cc;...',,;;;:;,'';oONWMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl;'';cl::codx0XNXXXWWXOdl:::;'..','..coc;'',cxKWWMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0d:,',:lc::ldkXNKKOOOkOXWWWWWWKxoc:::,..':loolll:,..dWMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl;'';cl::cox0NMWXXXKKKKKXNNNNNWWWMWXkdl::coollllolc;. :XMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMN0d:'',:lc::ldkXWMMWXxcok0K0NWNXXXK0OkxxkXWWNk:':llll:,.... :NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWXkl;'';ccc:clldKWWWMMWKdlxKKo;ok0KKNXxc::co0NKkol:clc;'....'::.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMN0d:'',:llc;:odoc,';lk0NMMWW0kOOoc0KdccOWNK00Oxdl::cl:,.....,cok0x.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMWXkl;''',;;;;cc;:ooooc,'..,cxOXWMWWWXOkxlxXWWWKkoc::lc;'....':ldOKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMWKx:,'',,,;;:lc;;;;:c:cloool:'...;ok0NMWMWWWMNOdl::clc,.....;cok0KK0KK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMK;.,cll;..,:cllllc:;,,:lc:cooolc;'..':lxXWKkoc::lc:'....':ldOKKK00KKKKKKx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMO' .';clc;'..';clc:,..,lc:cc::loool:cooool::cl:,'....,cok0KKKKKKKKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMO. ....';cll:,.....';;;;,;;;;;c::cooolc::cc;'....';lodlcd0KKKKKKKKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMO.'lc;.....':clc::lc..,cloolc,.'clc:cll:,.....,codoc;'. :0KKKKKKKK0KKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMNo';lddl:'....';cllc,...,:c;'..,clc;'......;lodl:,,;lxl.:0K0K00K0KKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMWXkl;,:odoc,.....,:llc;'..',:cc;'....',:lddc;',:okkkkl.;000KOO000KKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMNO; ';codo:'....';ccl::;'.....;codoc;,,;lxxdxkxxkl.;kOO0OkOO0KKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMl.cd:;;clodc;...........,clooc;;',coxxxkkxkOkkOl.;k000OxkO00KKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oKOkoc;,:codl:,'..':oodo:,,:lddkOkkxxkkxxkOkkc.:OOO00O0OOKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oK00KK0ko:,;cdkOkkOxl:'.;dkOOkkOkOOkOkkkOkkkOl.:0KKKKK0KKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oKKKKK0KKKOdc;;::::;:do;oOkkkkkkkkkkOkkkkkkkOl.:0KKKKKKKKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oK0KKKKKKK0KK0OxxO0KKKx;oOkkkkkkkkkkkkkOOkkkOl.:0KKKKKKKKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oKKxclk0KK0KKKKKKXXXKKx:oOkkkkkkkkkkkkkkOOOkOl.:0KKKKKKKKKKKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oK0c .',:dOKKKKKKXXXKKx:oOkkkkkkkkkkkkkkkOOkOl.:0KKKK0KKKKKKKKKx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMl.oKKc ;xl;,,;oOKKKXXXKKx:oOkkkkkkkkkkkkkkkkkkOl.:0K0KK00KK0KKK0Kx.:NMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMl.oKKc ,kOkko..dKKKXXXKKx:oOkkkkkkkkkkkkkkkkkkOl.:0KKKK000KKKKK0x:.lNMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMl.oK0c 'xOkOk,.dK0KXXXKKx:oOkkkkkkkkkkkkkkkkkkOl.:0KKKKK0KK0ko:;;ckNMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oK0c .xOkkk,.dKKKXXXKKx:oOkkkkkkkkkkkkkkkkkkOl.:0KKKKK0xl;;:oONMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl.oKKc .dOkkk,.dKKKXXXKKx:oOkkkkkkkkkkOkkkkkkkOl.:0KKOo:;;cxKWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMo.oKKc .oOkkk,.dKKKXXXKKx:oOkkkkkkkkkkOOOOkkkkOl.;xl;,:oONWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMo.:O0c .cOkOk,.dKKKXXXKKx:oOkkkkkkkkkOOkkOOOkxo,..;cxKWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMXd:,;.  ;xkkk,.dK0KXXXKKx:oOkkkkkOOkOOkkdl:;,;:cdONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMWKxc;:;,;cd,.dK0KXXKKKx;oOkkOOOkxoc:,;;:lxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMW0dc,..dK0KXXXKKx:okdl:;;,;:cokKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXc.;dOKXNXKOl.';;:ldxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:;:lol;;:lk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkdookKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWWMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMNKKKKKXXKKKKKKKKKKKKKK0KXKKKKKXWMWXKK000KKKKKKKKKNMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXXXXXNNXNXXNNNXNNNNNNXNNXNXNNNMMMNXNNXXNNNNNWNNXNMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return ink

def mug():
    mug = """
    MMMMMMMMMMMMMMMMWNX0kdoc:,'...                 ......',:coxO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMWX0kdoc:,''...........''',,,,,,,,,,,,,,'''''.......'';:ldOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMNKkoc,'....',,;;::cccccccccccccccccccccccccccccc::::::;;,,..   .,lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MW0o,....,;:ccccccccccccccccccccccccccccccccc::::::::::::::::::;,...   'oKMMMMMMMMMMMMMMMMMMMMMMMMMM
    0c...,:ccccccccccccccccccccccccccccccccccccc:::::::::::::::::::::::;'.   cXMMMMMMMMMMMMMMMMMMMMMMMMM
    ' .;cccccccccccccccccccccccccccccccccccccccc::::::::::::::::::::::::,.   .kWWNKKKKXNWMMMMMMMMMMMMMMM
       ..';:ccccccccccccccccccccccccccccccccccc::::::::::::::::::::;;,'...',. .:;''...',:cokXWMMMMMMMMMM
           ..,;;::ccccccccccccccccccccccccccccc:::::::::::;;;,''......',;cc:. .',;:::;;,,....cONMMMMMMMM
    ..,..        .....'',,,;;;;;;:::::;;;;;;;;,,'''..............',;:cccccc:. .,,'......';;;'..,dXWMMMMM
    ,.;:;;,'..............................              ..,;::ccccccccccc::;.              ..,'. 'xNMMMM
    :.,::::::::;;;;:::::::::::::::::::::;;,'....''',,;;;:cccccccccccccc::::;. .cdkOOOkxl,.    .'' .oNMMM
    o.':::::::::::::::::::::::::::::::cccccccccccccccccccccccccccccc:::::::,..kWMMMMMMMMNx,...  .'..cXMM
    k..::::::::::::::::::::::::::::::::::::::::::::ccccccccccccc:::::::::::, '0MMMMMMMMMMMKc.''. .'. cXM
    0,.;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' ,KMMMMMMMMMMMMXc.',. .'..oW
    X:.,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' ;XMMMMMMMMMMMMMK;.,,. .. 'O
    Wo.':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. :XMMMMMMMMMMMMMWx..;.  .. l
    Mk..;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. cNMMMMMMMMMMMMMMK;.;,. .. '
    MK,.;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;. lWMMMMMMMMMMMMMMNc.,;'.....
    MNc.,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;..dWMMMMMMMMMMMMMMWo.':;;;,..
    MWd..:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;..xMMMMMMMMMMMMMMMWo.'::::;. 
    MMO'.;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,..kMMMMMMMMMMMMMMMNc.,::::;. 
    MMX;.,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::, .OMMMMMMMMMMMMMMMK,.;::::, .
    MMWl.'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::, '0MMMMMMMMMMMMMMWx..;::::. '
    MMMk..;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' ,KMMMMMMMMMMMMMMK;.,::::;. l
    MMMK,.;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' ;XMMMMMMMMMMMMMNl.':::::. .O
    MMMNc.,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. :XMMMMMMMMMMMMNl..;::::'  lN
    MMMWd.':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. cNMMMMMMMMMMWKc..;::::'  ;KM
    MMMMO'.;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. lWMMMMMMMMMXd'..:::::'  ,0MM
    MMMMX;.,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;..oWMMMMMMN0o'..,::::;.  ;0MMM
    MMMMWo.':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;..lKKK0kdc,...,:::::,. .cKMMMM
    MMMMMk..;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;. .'''....',:ccccc;.  'xNMMMMM
    MMMMMK,.;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,..,::::cccccccc:,.  .oKMMMMMMM
    MMMMMNl.,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,..:llccccc:;,'.. .;dXWMMMMMMMM
    MMMMMMx.'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,. ........   .':d0NMMMMMMMMMMM
    MMMMMM0'.;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' .;::::::clxOKNWMMMMMMMMMMMMMM
    MMMMMMX:.,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. :XMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMWo.'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,..xWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMM0,.;::::::::::::::::::::::::::::::::::::::::::::::::::::::::,. lNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWd.';::::::::::::::::::::::::::::::::::::::::::::::::::::::'. cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMNo..;:::::::::::::::::::::::::::::::::::::::::::::::::::,. .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMNx'.';::::::::::::::::::::::::::::::::::::::::::::::,.. .;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMWKl'.';::::::::::::::::::::::::::::::::::::::::;,..  .cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMWKd;..';;:::::::::::::::::::::::::::::::;,'..   .;dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMN0d:,..',;;::::::::::::::::::::::;'..    .,cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWXOdl:;,'...''',,,,,,,,,'''......';cokKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWX0xl:,...       ....',coxOKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return mug

def power_lead():
    lead = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMW0xdx0WMMMMMMMMMWKxddONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMNo.   .dWMMMMMMMWk'   .cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMK,     ;XMMMMMMMNc     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMK,     ;KMMMMMMMNc     .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMK,     ;KMMMMMMMNc     .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMK,     ;KMMMMMMMNc     .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMWKxol:.     .:lccclllc.      ,lokKWMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMW0:.                               .;kWMMMMMMMMMMMMMMMWX0xoc:;,,;;cox0NMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMO'                                   .xWMMMMMMMMMMMWKd:.             .,lONMMMMMMMMMMMMMMMMMMMMMMMM
    MWl                                     :XMMMMMMMMMWOc.                   .;kNMMMMMMMMMMMMMMMMMMMMMM
    MNc                                     ,KMMMMMMMKkl.      .':ldddol:.      .:0WMMMMMMMMMMMMMMMMMMMM
    MNc                                     ,KMMMMMWO'       'o0NWMMMMMMWXkc.     .xWMMMMMMMMMMMMMMMMMMM
    MNc                                     ,KMMMMWk.      .oXMMMMMMMMMMMMMWO,     .xWMMMMMMMMMMMMMMMMMM
    MNc                                     ;XMMMMK,      'kWMMMMMMMMMMMMMMMM0,     .OMMMMMMMMMMMMMMMMMM
    MWd.                                    oWMMMWo      .xWMMMMMMMMMMMMMMMMMWx.     lNMMMMMMMMMMMMMMMMM
    MM0,                                   'OMMMMX:      ;KMMMMMMMMMMMMMMMMMMM0'     :NMMMMMMMMMMMMMMMMM
    MMWx.                                 .dWMMMMX;      ;XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMNd.                               .lNMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMWk'                             .oNMMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMMMKl.                          ;OWMMMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMMMMW0l'                     .;kNMMMMMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMMMMMMWXk:.               .,o0NMMMMMMMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMWXOo:'        'cx0NMMMMMMMMMMMMMMX;      :XMMMMMMMMMMMMMMMMMMM0'     :XMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWNd.     ;KMMMMMMMMMMMMMMMMMMX;      :XMMMMMMMMMMMMMMWNKOxc.     'x0XWMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMMMMMMMMMN0d:'.           ..;lkXWMMMMMMMMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMMMMMMW0o,.      ..'''...      .cONMMMMMMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMMMMW0l.    .;lx0KNNNNNX0kd:.     ;kNMMMMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMMMNd.    ,dKWMMWXKKKKKKNWMWXk:.   .cKMMMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMMXc    'xNMMMMWx'......:KMMMMW0:.   ,OWMMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMMXc    cKMMMMMMX:       cXMMMMMMNd.   '0MMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMWd.   cXMMMMMMM0,      'OMMMMMMMMWd.   :XMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      :XMMK,   '0MMMMMMMMk.     .oWMMMMMMMMMNc   .xMM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMX;      ;XMMk.   lNMMMMMMMWd.     .;lloOWMMMMMMx.   lWM
    MMMMMMMMMMMMMMMMMM0'     cNMMMMMMMMMMMMMMMMMMK;      :XMMx.   oWMMMMMMMNl          .dNMMMMMMO.   cNM
    MMMMMMMMMMMMMMMMMMX:     ,0MMMMMMMMMMMMMMMMMMk.      oWMMk.   cNMMMMMMMNo...      ;OWMMMMMMMx.   lNM
    MMMMMMMMMMMMMMMMMMWd.     lNMMMMMMMMMMMMMMMM0;      .OMMMK;   'OMMMMMMMMNXKx.   .dNMMMMMMMMXc   .kMM
    MMMMMMMMMMMMMMMMMMMK;      cKWMMMMMMMMMMMMNx'       lNMMMWd.   :KMMMMMMMMMNc  .cKWMMMMMMMMNd.   :XMM
    MMMMMMMMMMMMMMMMMMMMO,      .lOXWMMMMMWN0d,       .cXMMMMMNl    ;0MMMMMMMWx. ,kWMMMMMMMMMXo.   ,0MMM
    MMMMMMMMMMMMMMMMMMMMW0:        .;clllc;'.       .o0XMMMMMMMXl.   .dXMMMMMO,.oXMMMMMMMMMNk;    ;0MMMM
    MMMMMMMMMMMMMMMMMMMMMMNx,                     .c0WMMMMMMMMMMNx'    'o0NMM0d0WMMMMMMMWKd;.   .lXMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMNOl,.              .;dKWMMMMMMMMMMMMMWKo.    .'cdk0KXXXXKOxl;.    .:OWMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMNKkoc;,''',;:ldOXWMMMMMMMMMMMMMMMMMMWKd;.      .......      .'o0WMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc,..          .':d0NMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kxdooodxk0XNMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return lead

def plate():
    plate = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNX0xoc;,'............',;cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl:,'........................',:ldk0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXOdc,......................................,cdOXWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMN0dc'..............................................'cd0NMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMN0o;......................................................;o0NMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWKd:..................';:lodxkkOOOOOOkkxdolc;'..................:dKWMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0l'...............;cdk0XNWMMMMMMMMMMMMMMMMMMWNX0kdc;...............'l0WMMMMMMMMMMMMMM
    MMMMMMMMMMMMWOc..............;lx0NWMMWXK0OkkxkKWMMMMMMMMMMMMMMMMMWNKxl;..............cOWMMMMMMMMMMMM
    MMMMMMMMMMW0l.............;oONMWN0koc:;;;;;::cOWMMMMMMMMMMMMMMMMMMMMMWN0o;.............l0WMMMMMMMMMM
    MMMMMMMMMXd'...........,lONWNKxc;,;coxOKXNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMWNOl,...........'dXMMMMMMMMM
    MMMMMMMWO;...........;xXWWKd:,;lx0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;...........;OWMMMMMMM
    MMMMMMNd'..........,xXMNOc,,lOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx,..........'dNMMMMMM
    MMMMMXl..........'oXWNk:':xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo'..........lXMMMMM
    MMMMKc..........:OWWO:':kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:..........cKMMMM
    MMMKc..........lXMXo',xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl..........cKMMM
    MMXl..........dNW0:.cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..........lXMM
    MNd..........dNWO,'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..........dNM
    MO,.........oNWO,'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.........,OM
    Xc.........cXM0;.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.........cX
    k'........,OMXc.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,........'k
    l.........oNWx.;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.........c
    ,........'OMK:.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO'........,
    .........:KMk',0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:.........
    .........lNWd.cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.........
    .........oWNo.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.........
    .........oWNo.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.........
    .........lNWd.cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.........
    .........:KMk',0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:.........
    ,........'OMK:.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO'........,
    c.........oNWd.;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.........c
    k'........,OMX:.oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,........'k
    Xc.........cXMO,'xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.........cX
    MO,.........oNWk',kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.........'OM
    MNd..........dNWx''xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..........dNM
    MMXl..........dNWk,'oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..........lXMM
    MMMKc..........lXW0c.:0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl..........cKMMM
    MMMMKc..........:OWXd,'oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:..........cKMMMM
    MMMMMXl..........'oXWKl',dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo'..........lXMMMMM
    MMMMMMNd'..........,xXW0l',o0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx,..........'dNMMMMMM
    MMMMMMMWO:...........;dXNKd;':d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXd;...........:OWMMMMMMM
    MMMMMMMMMXo'...........,oONNOo;,;lx0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl,...........'dXMMMMMMMMM
    MMMMMMMMMMW0l.............;d0XX0xc;,;:loxkOO0KNMMMMMMMMMMMMMMMMMMMMMMMN0d;.............l0WMMMMMMMMMM
    MMMMMMMMMMMMWOc..............;lxKNNKOxol::;;;:OWMMMMMMMMMMMMMMMMMWN0xl;..............cOWMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0l'...............;cdk0XNWNNNXNWMMMMMMMMMMMMWNX0kdc;...............'l0WMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWKx:..................';:lodxkkOOOOOOkkxdol:;'..................:dKWMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMN0o;......................................................;o0NMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMN0dc'..............................................'cd0NMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXOdc,......................................,cdOXWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl:,'........................',:ldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xoc;,'............',;cok0XNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return plate

def documents():
    document = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNkc;;::::cloxk0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMWXx;,lk00Okxolc::;::::lokNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMXd,,oOKKKKKKKKKKKKK0Okx;..dWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWo.c0Oc;::looxkO0KKKKKKKOd,'kWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMWWWNNXXXNWWWWWMMWMX;'kKl.:o;,;;;:::::clloxkOo,,:clldxO0XNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WMMMMWKOxxdooooddxxOXWMMMO',Ok',d;':clc:;;,,,,;;::::;,''...'',;:cclodkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMM
    WWMNOdodxkkOOOOOkxdoodONWd.c0c.l:.;;;;,,'',,;:ccc::;,,,',;;:::;,......',::ccloxkOKNWMMMMMMMMMMMMMMMM
    WNOoox0KKKKKKKKKKKKK0xooOc.dk',:...:kkdolc:ccc:;;,,,',;;:cccc:,,'',;;;::;,......';:cccldxO0XNWMMMMMM
    XdlkKXXXXXXXXXXXXXXXXX0xc.,kc.;'..;0NNNNNNNNXK0kdoolccccc::;,,,,,;:ccc:;;,,',;;;:;;'......';::ckWMMM
    xlOKXNNNNNNNNNNNNNNNNNNKk:cd'''..'ONNNNNNNNNNNNNNNNNNNXXKOkdolc::c::;;;,,,;;:ccc:;;,'',,;;;,...xWMMM
    lkKNWNNWNNNNNNNXXKKKKXXK0dc,... .xNNNNNNNNNNNNNXXXXXKKKKKKKKKKKKK0Okdolcc:::::;;;,,,;;:ccc:'  ,0WMMM
    o0KXNNNNNNNXXKKKKKKKKKKKKO:... .dXNNNNNNNXXXXKKKKK0KKKKKKKKKKKKKKKKKKKKKKK00Okdolc::::::;;;;,..dNMMM
    o0XKKKXXXKKKKXXXXXXXXXXXX0:    lXNNNNKOOO0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00Oxdocc:,,:::cd
    oONXXXXXXXXXXXXXXXXXXXXXXk,   :KNNNNX0dldkOkxxkK0O0O0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK000Oc.:
    xdKNNNNNNNNNNNNNNNNNNNNN0c.  ,0NNXXKKKkd0Odx0kdkxdxxdkKKKOkk0KK00KKKKKKKKKKKKKKKKKKKK00KK000K00Kk,,0
    Nxd0NNNNNNNNNNNNNNNNWNNO:.  .kNNKKKKK0dk0xx0K0dddx0Odx0Kxdkdxkxdxx00kxO0KK0KK000000KK0K000000000:.xW
    MNOdxKNWWWWWWWWWWWWWN0o'    cXXKKKKKKOd0Kxx00xddoxxxx0K0xoxkOxdOOOkdxxokkdxxk0OkkO0000000000000o.lNM
    MMWNOxxk0XNWWWWWNKOkl'      .:x0KKKKK000KOxxxxOxkKKKKK0kk0xoxdoxxkdx00Okdd0doxddddkkddxk000000x';KMM
    MMMMMWXOkkOOOOOkkkk0k;        .;x0K00KK0KKKK0K0O0000000koxdddoxO0kok0OOklodlxxldkO0OookO00000k,'OWMM
    MMMMMMMMMMWWNNNWWWMMM0,         .;x0K0000000000000000000OkOOOxdxkOdoddxddOxoxdoxxk0kok0O0000O:.dWMMM
    MMMMMMMMMMMMMMMMMMMMMO. ..        .;x00000000000000000000000000000OkxOOkk0kdxooxxO0ddO0O0OOOl.cNMMMM
    MMMMMMMMMMMMMMMMMMMMWd..lOo'        .;xO00000000000000000000000000O0000OO00OOkxdxOOxkOOOOkxo',KMMMMM
    MMMMMMMMMMMMMMMMMMMMWk:;:::;.         .;dO0O0000000000000000000OOOO00OO00OOOOOOOOOOOOOOkddo,.kWMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWNNK0Oxdo,.       .,lodxkOO00000000OOOOOOOOOOOOOOOOOOOOOOOOOOOkxdooo;.oWMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk;        'c:::;;;;;:clldxkkOOO0OOOOOOOOOOOOOOOOOkxxooooo:.:XMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk;    .lKMWNNK0Okxdolc:::;;;;::clodxkkkkkkxxxddoooooool.'0MWMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklcdKWWMWWWMMMMMMMMMWWNK0Oxdolc::;;,'',,;;:clllooooo,.xWMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0Okdolc:;;;,,,,;,.lNMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKOxl:,':0MMMMMMMMMM
    """
    return document

def tech():
    tech = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:....,lkKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:'lxxdlc::cldxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd,;ok0KKKK0Oxdlcc:ccldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:':ddxkdlodk00KKKK0OxolccccldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,,ldxxkxoc:;;;:codxO0KKKK0OxocccccldOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc':odxkkkkkkkkxol:;,,;;:ldkO0KKKK0Oxocc:ccodOKNWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,,lxkkkkkkkkkkkkkkkkkxdl:;,,,;cldk00KKKK0OxocccccodOKNWMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMKl';dkOOkkkkkkkkkkkkkkkkkkkkkkxoc:,,,,;coxO0KKKKK0Oxocc:cloxOKNWMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWk;'ckOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdl:;''',:ldkO0KKKK00kxocc:cloxOXNMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMXo';dO0Okkkkkkkkkdodxxkkkkkkkkkxxdddddddkkkxdoc;,''';:ldk00KKKK00kdocc:cloxK
    MMMMMMMMMMMMMMMMMMMMMMWO;':oOK00OOOkkkxolodxkOOOOOOOOOkkkkxddol::cdkkkkkkxdl:,'.'';coxO0KKKKK0Okdc,;
    MMMMMMMMMMMMMMMMMMMMMXd',dOdlc:cdOOkdc:lxOO0000K000000OOkkkkxddoc;,:dkkkkkkkkkxdoc;'..',;oOKKKKKOo' 
    MMMMMMMMMMMMMMMMMMMW0:'ckXNNXO;.lOxc';dOO0KKKKKKKKKKKKK0OOkkxddddo:''oOOkkkkkkkkkkkkxo;..cOKKKKOl.  
    MMMMMMMMMMMMMMMMMMNd',o0XNNNNk:oOx;.,dO00KKXXXKKKKKKKKKK0Okkkxdddolc.'x0OkkkkkkkkOOkd;..lOKKK0k:. ..
    MMMMMMMMMMMMMMMMMKc.:xKNNNNNKc:kkl..lkO0KKXNNNNXKKKKKKKK00Okkxddddol;.:00kkkkkkkO0d;. .o0KKK0d, .::.
    MMMMMMMMMMMMMMMWx,'lOKNNNNNNk,lOk; ,dO0KKXNNNNXKKKKKKKKK00Okkkxdddol;.,00Okkkkk0Oo.  .o0KKKOo. .c:.:
    MMMMMMMMMMMMMMKl.;d0XNNNNNNNk,lOx, ,dO0KKXNNNXKKKKKKKKKK00Okkxddddoc..oK0OkkkO0Oc.  .d0KK0k:. 'c;.oN
    MMMMMMMMMMMMWk,'cxKNNNNNNNNN0;;kk:.,ok0KKKKKKKKKKKKKKKKK0Okkkxdddol,.:0X0kkkO0k;   'x0KK0x,  ,c''xWM
    MMMMMMMMMMMXl.,oOKNNNNNNNNNNXl.cOd'.cxO00KK0KKKKKKKKKK00Okkkxdddoc,.:00kOOO00x,   ,x0K0Oo. .:c.;OWMM
    MMMMMMMMMWO;.:x0XNNNNNNNNKkl:,;d0Oo,'cxkO0000KKKK0000OOkkkxddddl:',oOd:::clxk,   ,k0K0kc. .c:.cKMMMM
    MMMMMMMMXo',lokKNNNNNKkoc::lx0XNNX0xc,;lxkOOOOOOOOOOkkxxxddooc;,:oOxloOX0x:co'  ;kKK0x,  'c,.oNMMMMM
    MMMMMMW0:.:dxxoooodolccox0XNNNNNNNXXKko::clodxxxxxxddddolc:;;coxkdllOXNNKx;';. :OK0Oo.  ,c''xWMMMMMM
    MMMMMNd''ldkKNNX0kxdkKXNNNNNNNNNNNNNNXKKOxolllc::::::::cllllooooox0XNNNKd,  ..cOK0kc. .::.;0WMMMMMMM
    MMMWKc.;odkKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXKK0OOOOOO00xclddxk0KNNNNNX0o'   .l0K0x;  .c;.cKMMMMMMMMM
    MMNx,.cddkXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXc.dXNNNNNNNNNXOl'   .o00Oo'  'c,.oNMMMMMMMMMM
    MKc.,oddkXWMWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXd.oXNNNNNNNNXkc.   .o00kc.  ;c''kWMMMMMMMMMMM
    k,.:dddkKWMMMMMMMMWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNO,cXNNNNNNNKx:.   .d00x;  .::.;0WMMMMMMMMMMMM
    .'lddddxOXNWMMMMMMMMMMMWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNK:;0NNNNNX0d;.   ;k0Oo'  .c;.cXMMMMMMMMMMMMMM
    .:xxdddddxxO0KXNWMMMMMMMMMMMWWWNNNNNNNNNNNNNNNNNNNNNNNNXl,ONNNNXOo;.  .oO0kc.  'c'.oNMMMMMMMMMMMMMMM
    ,'okOOkkxdddddxkO0KXNWMMMMMMMMMMMWWWWNNNNNNNNNNNNNNNNNNNx,lXNWWXx;   ;k00x;   ;c.'kWMMMMMMMMMMMMMMMM
    c.,;::ldkOOkxxdddddxkO0KXNWMMMMMMMMMMMMWWWNNNNNNNNNNNNNNKxoodxkXK; .oOKOd'  .::.;0WMMMMMMMMMMMMMMMMM
    d'cxdlc:;:coxOOOkxxdddddxkO0KXNWMMMMMMMMMMMMWWWWNNNNNNNNNNNX0o'l0c;kK0Ol.  .c,.cXMMMMMMMMMMMMMMMMMMM
    Kc,,,:oxxdl::::ldkOOOkxxdddddxkO0KXWWMMMMMMMMMMMMMWWWWNNNNNXk;.'k00K0k:.  'c'.dNMMMMMMMMMMMMMMMMMMMM
    MWXOdc;,,;coxxol:::coxkOOOkxddddddxkO0XNWWMMMMMMMMMMMMMMWWNO;.'d0KK0d,   ;:.'kWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMNKkoc;,,;ldxxoc:::coxO0OkkxdddddxxkO0XNWWMMMMMMMMMMWO:'lOKK0Ol.  .:;.;0WMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMWNKko:,,,:ldxdoc::cldkO0OkxxdddddxxkO0XNNWMMMMW0lck0KK0k:.  .c,.lXMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMWN0xl:,,,:oxxdlccccoxO0OOkxxdddddxxkkOKXX0dok0KK0d,   ,c'.dNMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMWXOxl:,,;coxxolcccldkO0OOkxdddddddxxxddxO0Oo.  .;:.'kWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXOdc;,,;cdxxolcccldO00OOkkxdddddddxx:.  .:;.;0MMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkoc;,,:ldxdolccloxkO00Okkxdxo,   .:,.lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKko:;,,:ldxdllcclldk0000o.  ,:..dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:;,;:odxxollllodc..;:.,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWNKko:;,;;:ldxdool::'.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNNNNNNKK0Oxlcc::l:. .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWWWMMWN0o,...;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    return tech
