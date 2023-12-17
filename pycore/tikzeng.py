
import os

def to_head( projectpath ):
    pathlayers = os.path.join( projectpath, 'layers/' ).replace('\\', '/')
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{import}
\subimport{"""+ pathlayers + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image 
"""

def to_cor():
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
\def\SumColor{rgb:blue,5;green,15}
"""

def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""

# layers definition

def to_input( pathfile, to='(-3,0,0)', width=8, height=8, name="temp" ):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """+ to +""" {\includegraphics[width="""+ str(width)+"cm"+""",height="""+ str(height)+"cm"+"""]{"""+ pathfile +"""}};
"""

# Conv
def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Conv,Conv,relu
# Bottleneck
def to_ConvConvRelu( name, s_filer=256, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""" }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(width[0]) +""" , """+ str(width[1]) +""" },
        depth="""+ str(depth) +"""
        }
    };
"""

# \pic[shift={"""+ offset +"""}] at """+ to +"""  {Box={name=Bottleneck,caption=Stage Layer 4,%
# 		xlabel={{"","dummy"}},fill=,opacity=0.0,height=40,width=40,depth=40}};

def to_elan1( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    name2="elan_c2"
    name3="elan_c3"
    name4="elan_c4"
    return r"""


\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(3,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ name3 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(256) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(6) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(5,0,0)}] at """+ to +""" 
    {Box={
        name=""" + name4 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(256) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(6) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_stage2( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    s2_1 = "s2_1"
    s2_2 = "s2_2"
    s2_3 = "s2_3"
    s2_4 = "s2_4"
    s2_5 = "s2_5"
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(128) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };

\pic[shift={(5,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s2_1 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(256) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(6) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(7,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s2_2 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(128) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(9,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s2_4 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(512) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(7) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(11,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s2_5 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(512) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(7) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


def to_stage3( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    s3_1 = "s3_1"
    s3_2 = "s3_2"
    s3_3 = "s3_3"
    s3_4 = "s3_4"
    s3_5 = "s3_5"
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(256) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(6) +""",
        depth="""+ str(depth) +"""
        }
    };

\pic[shift={(5,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s3_1 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(256) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(7) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(7,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s3_2 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(6) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(9,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s3_4 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(1024) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(9) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(12,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s3_5 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(1024) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(9) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_stage4( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    s4_1 = "s4_1"
    s4_2 = "s4_2"
    s4_3 = "s4_3"
    s4_4 = "s4_4"
    s4_5 = "s4_5"
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(512) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };

\pic[shift={(4,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s4_1 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(1024) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(5) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(6,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s4_2 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(256) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(8,0,0)}] at """+ to +""" 
    {RightBandedBox={
        name="""+ s4_4 + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(1024) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(0.5) +""",
        height="""+ str(height) +""",
        width="""+ str(8) +""",
        depth="""+ str(depth) +"""
        }
    };
\pic[shift={(10,0,0)}] at """+ to +""" 
    {Box={
        name=""" + s4_5 +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(1024) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(8) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_6conv( name, s_filer=256, n_filer=(64,64,64,64,64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2,2,2,2,2), height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""", """+ str(n_filer[1]) +""", """+ str(n_filer[1]) +""", """+ str(n_filer[1]) +""", """+ str(n_filer[1]) +""" }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(width[0]) +""" , """+ str(width[1]) +""", """+ str(width[1]) +""", """+ str(width[1]) +""", """+ str(width[1]) +""", """+ str(width[1]) +""" },
        depth="""+ str(depth) +"""
        }
    };
"""

# def to_check_conv(name, s_filer=256, n_filer=(64, 64), offset="(0,0,0)", to="(0,0,0)", width=(2, 2), height=40, depth=40, caption=" "):
#     # Definición de la capa de convolución
#     convolution_layer = fr"""
# \pic[shift={offset}] at {to} 
#     {{RightBandedBox={{
#         name={name},
#         caption={caption},
#         xlabel={{ {n_filer[0]}, {n_filer[1]}, {n_filer[1]}, {n_filer[1]}, {n_filer[1]}, {n_filer[1]} }},
#         zlabel={s_filer},
#         fill=\ConvColor,
#         bandfill=\ConvReluColor,
#         height={height},
#         width={{ {width[0]} , {width[1]}, {width[1]}, {width[1]}, {width[1]}, {width[1]} }},
#         depth={depth}
#         }}
#     }};
# """
#     return convolution_layer
    # # Agregar conexiones en forma de parábola
    # connections = []
    # for i in range(5):
    #     connection_line = fr"\draw[->] ({name}.east) to[out=0,in=180] (c{i+1}.west);"
    #     connections.append(connection_line)

    # # Unir las líneas de conexión en un solo bloque de texto
    # connections_text = "\n".join(connections)

    # # Combinar la capa de convolución y las conexiones
    # result = convolution_layer + connections_text

    # return result

# Ejemplo de uso
output_code = to_6conv("conv1", caption="Conv1")  # Puedes ajustar los parámetros según tus necesidades
print(output_code)




# Pool
def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\PoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# unpool4, 
def to_UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +r""",
        caption="""+ caption +r""",
        fill=\UnpoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""



def to_ConvRes( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(n_filer) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


# ConvSoftMax
def to_ConvSoftMax( name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# SoftMax
def to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        xlabel={{" ","dummy"}},
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_Sum( name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Ball={
        name=""" + name +""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo=$+$
        }
    };
"""


def to_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
"""

def to_skip( of, to, pos=1.25):
    return r"""
\path ("""+ of +"""-southeast) -- ("""+ of +"""-northeast) coordinate[pos="""+ str(pos) +"""] ("""+ of +"""-top) ;
\path ("""+ to +"""-south)  -- ("""+ to +"""-north)  coordinate[pos="""+ str(pos) +"""] ("""+ to +"""-top) ;
\draw [copyconnection]  ("""+of+"""-northeast)  
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""

def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate( arch, pathname="file.tex" ):
    with open(pathname, "w") as f: 
        for c in arch:
            print(c)
            f.write( c )
     


