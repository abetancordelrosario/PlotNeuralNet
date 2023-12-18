import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #Stem layer
    # to_concatenation( name='ccr_b1', s_filer=80, n_filer=(512,512), offset="(0,0,0)", to="(0,0,0)", width=(5,5), height=25, depth=25  ),
    # to_concatenation( name='ccr_b1', s_filer=40, n_filer=(1024,1024), offset="(0,0,0)", to="(0,0,0)", width=(9,9), height=20, depth=20  ),
    to_concatenation( name='ccr_b1', s_filer=20, n_filer=(1024,1024), offset="(0,0,0)", to="(0,0,0)", width=(8,8), height=15, depth=15  ),
    
    to_Conv( name='ccr_b2', s_filer=20, n_filer=1024, offset="(2.5,0,0)", to="(ccr_b1-east)", width=8, height=15, depth=15, caption="`P3   P4    P5"  ),
    to_connection( "ccr_b1", "ccr_b2"),


    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
