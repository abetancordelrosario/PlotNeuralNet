
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input( '../imgs/010001_ir.jpg' ),

    #Stem layer
    to_Conv( name='ccr_b1', s_filer=640, n_filer=32, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40  ),
    to_Conv( name='ccr_b2', s_filer=320, n_filer=64, offset="(0.5,0,0)", to="(ccr_b1-east)", width=3, height=35, depth=35  ),
    to_Conv( name='ccr_b3', s_filer=320, n_filer=64, offset="(,0,0)", to="(ccr_b2-east)", width=3, height=35, depth=35  ),
    to_connection( "ccr_b1", "ccr_b2"),
    to_connection( "ccr_b2", "ccr_b3"),


    #Stage layer 1
    to_Conv(name='ccr_b4', s_filer=160, n_filer=128, offset="(4,0,0)", to="(ccr_b3-east)", width=5, height=30, depth=30  ),
    # *block_elan( name='ccr_b5', botton='ccr_b4', top='ccr_b6', s_filer=160, n_filer=128, offset="(5,0,0)", size=(40,40,2.5), opacity=0.5 ),
    to_elan1( name='ccr_b5', s_filer=160, n_filer=64, offset="(1,0,0)", to="(ccr_b4-east)", width=3, height=30, depth=30  ),
    to_connection( "ccr_b3", "ccr_b4"),
    to_connection( "ccr_b4", "ccr_b5"),
    to_connection( "elan_c3", "elan_c4"),
    to_skip( of='ccr_b5', to='elan_c3', pos=1.25),
    to_Pool("pool1", offset="(0,0,0)", to="(elan_c4-east)", height=25, depth=25),


    #Stage layer 2
    to_stage2( name='s2_0', s_filer=80, n_filer=512, offset="(3,0,0)", to="(pool1-east)", width=5, height=25, depth=25  ),
    to_skip( of='s2_0', to='s2_1', pos=1.25),
    to_skip( of='s2_2', to='s2_4', pos=1.25),
    to_connection( "pool1", "s2_0"),
    to_connection( "s2_1", "s2_2"),
    to_connection( "s2_4", "s2_5"),
    to_Pool("pool2", offset="(0,0,0)", to="(s2_5-east)", height=20, depth=20),


    #Stage layer 3
    to_stage3( name='s3_0', s_filer=80, n_filer=512, offset="(3,0,0)", to="(pool2-east)", width=7, height=20, depth=20  ),
    to_skip( of='s3_0', to='s3_1', pos=1.25),
    to_skip( of='s3_2', to='s3_4', pos=1.25),
    to_connection( "pool2", "s3_0"),
    to_connection( "s3_1", "s3_2"),
    to_connection( "s3_4", "s3_5"),
    to_Pool("pool3", offset="(0,0,0)", to="(s3_5-east)", height=15, depth=15),

    #Stage layer 4
    to_stage4( name='s4_0', s_filer=40, n_filer=512, offset="(2,0,0)", to="(pool3-east)", width=7, height=15, depth=15  ),
    to_skip( of='s4_0', to='s4_1', pos=1.25),
    to_skip( of='s4_2', to='s4_4', pos=1.25),
    to_connection( "pool3", "s4_0"),
    to_connection( "s4_1", "s4_2"),
    to_connection( "s4_4", "s4_5"),
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
