from .models import Post, Comentario

# ........................... App Core | services ............................ 󰌠
# servicios de obtención de data



# ----------------------------------------------------------------- Post_Service
class Post_Service:
    '''
    Obtención de data | tabla Post
    Tabla contenedora de artículos y multimedia
    '''

    @staticmethod
    def post_order_by_date():
        '''
        Ordena artículos de tabla Post por fecha, 1° el más reciente
        '''
        return Post.objects.all().order_by("-fecha")                      # 🠶 01  
 

    @staticmethod
    def post_filter_by_title(titulo):
        '''
        Filtra artículos de tabla Post por el título del artículo
        '''
        return Post.objects.get(titulo = titulo)



# ----------------------------------------------------------- Comentario_Service
class Comentario_Service:
    '''
    Obtención de data | tabla Comentario
    Tabla contenedora de comentarios de los visitantes en cada artículo
    '''
    
    @staticmethod
    def comment_filter_by_art_title(titulo):
        '''
        Filtra comentarios de tabla Comentario por título del artículo
        '''
        return Comentario.objects.filter(art_relacionado = titulo) 
